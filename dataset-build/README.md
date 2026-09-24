# HF Activated-Parameters Dataset & Model

Instructions données pour la construction d'un dataset de modèles HuggingFace (architecture + nombre de
paramètres activés).

Pour un modèle dense, `activated == total`. Pour un modèle Mixture-of-
Experts (Mixtral, Qwen-MoE, DeepSeek-V2/V3...), seule une fraction des
experts est routée par token, donc `activated < total`.

## Installation

```bash
pip install -r requirements.txt
```

## Construire le dataset

```bash
python -m dataset-build.src.build_dataset
```

Par défaut (`moe_only = True` dans `config.py`), ceci cible les **1000
modèles Mixture-of-Experts avec le plus de likes** (l'équivalent Hub des
"étoiles"), sans aucun filtre par mot-clé :

1. parcourt les modèles `text-generation` du Hub, strictement triés par
   nombre de likes décroissant ;
2. pour chacun, télécharge son `config.json` (pas les poids) et vérifie
   via `architectures.normalize_config().is_moe` s'il s'agit réellement
   d'un MoE ;
3. si oui : récupère le nombre de paramètres réel (métadonnées
   `safetensors` si disponibles) et **ajoute une ligne** au CSV de sortie
   immédiatement ;
4. si non (ou config illisible) : passe au suivant ;
5. dans tous les cas, **journalise** le modèle (`data/scrape_log.jsonl`) —
   c'est ce qui permet, en cas d'interruption, de relancer le script
   sans jamais revérifier un modèle déjà vu ;
6. s'arrête dès que 1000 modèles confirmés MoE ont été trouvés.

/!\ 1 000 modèles MoE était surestimé. En surveillant, je me suis arrêté quand les modèles passaient sous le seuil des 100 likes.
On a extrait 220 modèles MoE au total, probablement avec des doublons par rapport au modèle de base (modèles quantizés, distillé, fine-tuné). 

Le CSV (`data/hf_activated_params_dataset.csv`) et le log
(`data/scrape_log.jsonl`) sont écrits ligne par ligne au fil de l'eau :
tu peux interrompre le script (Ctrl+C, crash, coupure réseau) à tout
moment et le relancer, il reprendra exactement là où il s'était arrêté.

Passe `moe_only = False` dans `config.py` pour revenir à un mode
générique (tous types de modèles `text-generation`, sans confirmation
MoE ni reprise — voir `run_generic()` dans `build_dataset.py`).

## Limites connues

- La formule ignore les biais, les LayerNorm/RMSNorm, et les embeddings de
  position — leur poids est négligeable (<0.1%) sauf cas extrêmes.
- Les architectures à attention latente compressée (DeepSeek-V2/V3 MLA) ne
  sont pas modélisées avec précision.
- Le nombre total de paramètres "ground truth" (safetensors) n'est pas
  disponible sur tous les repos ; dans ce cas on retombe sur l'estimation
  par formule pour les deux quantités.
- `huggingface_hub` change fréquemment la signature de `list_models` /
  `model_info` entre versions. Pour la partie "lister/trier les modèles",
  on contourne complètement ce problème : `hub_rest.py` appelle directement
  l'API REST publique et stable `https://huggingface.co/api/models` (avec
  `requests`), en suivant la pagination standard par header `Link` — la
  même méthode que `huggingface_hub` utilise en interne. Seuls
  `hf_hub_download` (téléchargement du `config.json`) et `HfApi.model_info`
  (métadonnées safetensors) passent encore par `huggingface_hub`, car ces
  deux-là sont restés stables.

## Structure du projet

```
dataset-build/
  src/
    config.py          # cible (nb de MoE, tri par likes...)
    architectures.py   # normalisation des configs + formules total/activé
    hub_rest.py         # client REST direct et stable pour lister/trier les modèles
    fetch.py           # téléchargement config.json + métadonnées par modèle
    scrape_log.py       # log de reprise (JSONL append-only)
    build_dataset.py   # orchestration -> CSV, résumable
    train_model.py      # entraînement du modèle de régression
  tests/
    test_architectures.py  # validation des formules sur des modèles connus
data/                      # créé à l'exécution
  hf_activated_params_dataset.csv
  scrape_log.jsonl
```
