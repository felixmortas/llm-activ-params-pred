# Workflow data science

## Données et préparation

- Source d'entrée : `data/clean-hf_activated_params_dataset.csv`; cible : `activated_params`.
- Le fichier observé contient exactement 112 lignes et 20 colonnes; « environ 200 » était une approximation. Aucun `model_id` n'est répété.
- Repérer les quantifications, fine-tunings et doublons avant tout split. Privilégier le modèle de base. Si celui-ci est absent, retenir le modèle le plus proche; garder la décision dans un journal d'audit séparé, sans indicateur de substitution dans le dataset final.
- Utiliser `prompt-replacement-selection.md` pour assister le tri des 112 modèles avec un chatbot LLM. Vérifier les propositions avant d'appliquer le nettoyage; conserver le journal d'audit séparé.

## Analyse et modélisation

- Conduire le flux data science classique : contrôler types, valeurs manquantes et distributions; explorer les relations entre variables d'architecture, `total_params` et `activated_params`; documenter les transformations.
- Comparer plusieurs approches supervisées à une baseline univariée linéaire simple. Les variables d'architecture servent à l'analyse et à la comparaison; la fonction de livraison est contrainte à `total_params` seul.
- Faire le split aléatoire après le nettoyage. Les modèles d'une même famille peuvent être répartis entre partitions.
- Rapporter plusieurs indicateurs et analyser les erreurs et l'importance des features. Ne pas optimiser un indicateur unique; justifier à la conclusion le compromis le plus pertinent pour le calculateur carbone.

## Livraison

- Livrer le projet source documenté et reproductible, les résultats de comparaison et le journal d'audit du nettoyage.
- Extraire une fonction documentée `activated_params = f(total_params)` utilisable par le calculateur carbone existant.
- Décrire le domaine d'application, les limites et les incertitudes de généralisation de la fonction.
