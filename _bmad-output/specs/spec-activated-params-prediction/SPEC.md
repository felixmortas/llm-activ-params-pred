---
id: SPEC-activated-params-prediction
companions:
  - data-science-workflow.md
  - prompt-replacement-selection.md
  - ../../../data/hf_activated_params_dataset.csv
sources: []
---

# Estimation des paramètres activés des modèles MoE

## Why

Le calculateur d'empreinte carbone par conversation existe déjà, mais il ne peut pas estimer les modèles propriétaires sans leur nombre de paramètres activés. Ce projet doit apprendre cette valeur à partir de modèles MoE publics, puis fournir une fonction utilisable à partir du nombre total de paramètres, avec un projet data science vérifiable et présentable en portfolio.

## Capabilities

- **CAP-1**
  - **intent:** Préparer un jeu de données MoE exploitable en identifiant les doublons quantifiés et fine-tunés et en privilégiant les modèles de base selon le prompt de sélection fourni.
  - **success:** Les exclusions et les substitutions par un modèle proche lorsque le modèle de base manque sont consignées dans un journal d'audit; le dataset final est prêt pour l'analyse.
- **CAP-2**
  - **intent:** Comparer des modèles supervisés fondés sur les variables d'architecture et rendre leur importance compréhensible.
  - **success:** Plusieurs indicateurs sont rapportés sur un split aléatoire tenu à l'écart, avec une comparaison à une baseline linéaire et une analyse de l'importance des variables.
- **CAP-3**
  - **intent:** Fournir une fonction qui estime `activated_params` à partir du seul `total_params` pour les modèles propriétaires.
  - **success:** La fonction et son domaine d'application sont documentés, et un modèle retenu après comparaison multi-indicateurs bat la baseline selon le critère justifié pour l'usage carbone.

## Constraints

- La fonction finale accepte uniquement `total_params` en entrée.
- Les variantes quantifiées et fine-tunées sont traitées avant la séparation des données; le modèle de base est privilégié.
- Le split principal est aléatoire. Des modèles d'une même famille peuvent se trouver dans les partitions d'entraînement et d'évaluation.
- Le modèle retenu doit battre une baseline de fonction linéaire naïve; le jugement repose sur plusieurs indicateurs et non sur un indicateur unique (principe de Goodhart).
- Le projet doit être documenté et reproductible pour être présenté en portfolio.

## Non-goals

- Implémenter ou modifier le calculateur carbone existant.

## Success signal

Le projet source permet de reproduire le nettoyage, l'analyse et la comparaison sur le CSV; il livre une fonction documentée fondée uniquement sur `total_params`. La conclusion compare plusieurs indicateurs au baseline, justifie le compromis retenu pour l'usage carbone et décrit les limites de généralisation.

## Assumptions

- Le prompt propose de comparer les écarts logarithmiques de `total_params` et `activated_params` à poids égal, puis d'utiliser la proximité d'architecture pour départager les candidats. Cette règle est une proposition à valider lors de son utilisation.

## Open Questions

- Quelles métriques et quelle règle de compromis permettront de décider si un modèle bat suffisamment la baseline pour l'usage carbone ?
- Le protocole de similarité proposé dans le prompt et le contrôle humain des rapprochements sont-ils adaptés après examen des résultats ?
