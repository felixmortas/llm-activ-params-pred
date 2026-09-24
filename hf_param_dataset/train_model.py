"""
Trains a regressor to predict `activated_params` from architecture features.

Two feature modes are offered (see FEATURE_MODE below):

- "full": uses every architecture field, including exact MoE routing
  numbers (num_local_experts, num_experts_per_tok...). This mostly
  re-learns our own analytical formula - useful if you want a model that
  can be applied even when you don't want to hand-code a new formula for
  a novel architecture family, but it isn't a hard learning problem.

- "restricted": deliberately hides the exact MoE routing numbers and only
  keeps total_params, model_type, hidden_size and num_hidden_layers. This
  forces the model to learn a *typical activation ratio per architecture
  family*, which is a genuinely harder and more interesting regression
  problem, and mirrors a realistic use case: "given a model I only know
  the size and family of, guess its likely active-parameter count".

We regress on log10(activated_params) because model sizes span several
orders of magnitude (from ~100M to >600B parameters).
"""
import argparse
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

FULL_NUMERIC_FEATURES = [
    "hidden_size", "num_hidden_layers", "num_attention_heads",
    "num_key_value_heads", "intermediate_size", "vocab_size",
    "is_moe", "num_local_experts", "num_experts_per_tok",
    "num_shared_experts", "moe_intermediate_size", "total_params",
]
RESTRICTED_NUMERIC_FEATURES = [
    "hidden_size", "num_hidden_layers", "total_params",
]
CATEGORICAL_FEATURES = ["model_type"]
TARGET = "activated_params"


def build_pipeline(numeric_features):
    preprocessor = ColumnTransformer([
        ("num", "passthrough", numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
    ])
    model = RandomForestRegressor(
        n_estimators=400,
        max_depth=None,
        min_samples_leaf=2,
        n_jobs=-1,
        random_state=42,
    )
    return Pipeline([("preprocess", preprocessor), ("model", model)])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", default="data/clean-hf_activated_params_dataset.csv")
    parser.add_argument("--feature-mode", choices=["full", "restricted"], default="restricted")
    parser.add_argument("--out", default="data/activated_params_model.joblib")
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    numeric_features = FULL_NUMERIC_FEATURES if args.feature_mode == "full" else RESTRICTED_NUMERIC_FEATURES

    df = df.dropna(subset=numeric_features + CATEGORICAL_FEATURES + [TARGET])
    X = df[numeric_features + CATEGORICAL_FEATURES]
    y = np.log10(df[TARGET].astype(float))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = build_pipeline(numeric_features)
    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)
    mae_log = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    # Also report error back in linear (parameter count) space, easier to interpret.
    mae_params = mean_absolute_error(10 ** y_test, 10 ** preds)

    print(f"Feature mode: {args.feature_mode}")
    print(f"R2 (log10 scale): {r2:.3f}")
    print(f"MAE (log10 scale): {mae_log:.3f}")
    print(f"MAE (raw param count): {mae_params:,.0f}")

    joblib.dump(pipeline, args.out)
    print(f"Model saved to {args.out}")


if __name__ == "__main__":
    main()
