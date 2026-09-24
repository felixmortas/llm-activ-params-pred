---
title: 'Analyse exploratoire du dataset de paramètres activés'
type: 'feature'
created: '2026-09-24'
status: 'draft'
review_loop_iteration: 0
context:
  - '_bmad-output/specs/spec-activated-params-prediction/SPEC.md'
  - '_bmad-output/specs/spec-activated-params-prediction/data-science-workflow.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Le dépôt ne fournit pas encore d’analyse exploratoire reproductible qui établit la qualité, les distributions et les relations du dataset avant la modélisation.

**Approach:** Ajouter une commande Python qui lit le CSV nettoyé, vérifie ses colonnes et types, résume les valeurs manquantes et les distributions, explore les associations entre variables d’architecture et les comptes de paramètres, puis consigne les transformations et limites dans un rapport reproductible.

## Boundaries & Constraints

**Always:** Travailler sur `data/clean-hf_activated_params_dataset.csv` sans modifier les CSV d’entrée; inclure `total_params` et `activated_params`; conserver les valeurs manquantes visibles dans les diagnostics plutôt que les imputer silencieusement; distinguer les contrôles déterministes des observations statistiques; documenter provenance et transformations.

**Ask First:** Changer la source de données, corriger ou supprimer des lignes du dataset, ou choisir une stratégie d’imputation.

**Never:** Entraîner ou comparer des modèles, faire le split train/test, sélectionner un estimateur final, modifier le calculateur carbone ou prétendre qu’une corrélation démontre une causalité.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Dataset valide | CSV attendu avec colonnes requises | Rapport d’analyse et tableaux récapitulatifs reproductibles | Aucun |
| Fichier absent ou colonnes requises absentes | Chemin invalide ou schéma incomplet | Aucun résultat présenté comme valide | Message explicite indiquant le chemin ou les colonnes manquantes |
| Valeurs manquantes ou numériques invalides | CSV contenant des cellules vides, non finies ou incompatibles | Comptages et lignes concernées rapportés; aucune imputation implicite | L’analyse s’arrête si les champs indispensables ne peuvent pas être analysés |

</frozen-after-approval>

## Code Map

- `data/clean-hf_activated_params_dataset.csv` — entrée visée, 112 lignes et 20 colonnes observées; aucun manquant ou `model_id` dupliqué dans l’état inspecté. Les deux CSV présents ont le même contenu actuellement.
- `data/hf_activated_params_dataset.csv` — source brute existante; ne pas la modifier pendant cette analyse.
- `hf_param_dataset/architectures.py:27` — schéma d’architecture normalisé; `:50` et suivantes — alias et valeurs par défaut qui expliquent la provenance des champs.
- `hf_param_dataset/train_model.py:33` — inventaire des variables déjà considérées; `:68` — chargement pandas existant. Ne pas lancer ni étendre l’entraînement pour cette étape.
- `requirements.txt:1` — pandas est déjà une dépendance; aucun outil dédié à l’analyse exploratoire ni notebook n’existe.
- `_bmad-output/specs/spec-activated-params-prediction/data-science-workflow.md` — demande les contrôles, distributions, relations et transformations; la partie nettoyage des variantes et la modélisation restent hors de cette étape.
- `README.md` — décrit la collecte HF et les limites des comptes estimés par formule, à répercuter dans la documentation de provenance.

## Tasks & Acceptance

**Execution:**
- [ ] `hf_param_dataset/analyze_dataset.py` — créer une commande reproductible avec chemin d’entrée configurable; valider le schéma et les types; produire un rapport lisible sur les manquants, duplications, domaines, distributions et associations d’architecture avec `total_params` et `activated_params`.
- [ ] `data/analysis/` — écrire les résultats générés (rapport et tableaux de synthèse) dans un emplacement séparé des CSV d’entrée.
- [ ] `README.md` — documenter la commande, ses sorties, les transformations réellement appliquées (aucune modification du CSV) et les limites d’interprétation.

**Acceptance Criteria:**
- Étant donné le CSV nettoyé valide, lorsque la commande est lancée, alors elle produit les diagnostics et résumés de distributions et d’associations attendus sans modifier l’entrée.
- Étant donné un schéma invalide ou un fichier manquant, lorsque la commande est lancée, alors elle échoue avec un message explicite et ne présente pas de rapport incomplet comme résultat valide.
- Étant donné des valeurs manquantes ou invalides, lorsque l’analyse est produite, alors leur nombre et leur traitement sont explicitement rapportés sans imputation silencieuse.
- Étant donné les comptes de paramètres couvrant plusieurs ordres de grandeur, lorsque leurs distributions sont résumées, alors le rapport propose une lecture adaptée (échelle logarithmique ou quantiles) et précise que les associations ne sont pas causales.

## Spec Change Log

## Design Notes

Les comptes de paramètres s’étendent sur plusieurs ordres de grandeur. Présenter au minimum des quantiles et une vue logarithmique pour éviter que les grands modèles masquent la distribution; calculer les associations sur valeurs brutes et/ou logarithmiques en indiquant clairement l’échelle. Une transformation d’analyse ne doit jamais réécrire la source.

## Verification

**Manual checks (no tests requested):** Exécuter la commande documentée sur le CSV nettoyé; vérifier le rapport, les tableaux de synthèse et que le diff des deux CSV d’entrée est vide.
