# Prompt de sélection des modèles représentatifs

Copier le prompt ci-dessous dans le chatbot LLM utilisé pour examiner la liste. Fournir le CSV complet, en conservant les valeurs et identifiants d'origine.

```text
Tu es chargé d'identifier les variantes quantifiées et fine-tunées parmi des modèles MoE Hugging Face et de proposer une liste de modèles représentatifs pour une analyse de machine learning.

OBJECTIF
Pour chaque groupe de variantes d'un même modèle de base, garder le modèle de base s'il figure dans le tableau. Si le modèle de base n'y figure pas, proposer comme représentant le modèle disponible le plus similaire, en donnant un poids prioritaire à `total_params` et `activated_params`.

RÈGLES
1. Utilise uniquement les informations présentes dans le tableau. N'invente ni relation de parenté, ni nom de modèle, ni valeur numérique.
2. Repère les variantes quantifiées et fine-tunées à partir de `model_id`, des noms et métadonnées fournis, et des liens explicites de modèle de base. Distingue une vraie variante d'un modèle simplement similaire.
3. Pour comparer les tailles, utilise les valeurs numériques `total_params` et `activated_params`. Comme leurs échelles peuvent être très grandes, calcule pour chaque candidat disponible :
   - d_total = abs(log10(candidate.total_params) - log10(reference.total_params))
   - d_active = abs(log10(candidate.activated_params) - log10(reference.activated_params))
   - score = d_total + d_active
   Le score le plus faible indique la plus grande similarité sur ces deux critères. Les deux critères ont le même poids. Ne calcule pas le score si une valeur manque, est nulle ou invalide; indique alors « comparaison numérique impossible ».
4. Lorsque le modèle de base est présent, il reste le représentant, même si une variante a des nombres de paramètres très proches.
5. Lorsque le modèle de base est absent, classe les candidats disponibles par score. Utilise ensuite la proximité d'architecture (type, dimensions, nombre de couches et configuration MoE) comme critère secondaire en cas de scores égaux ou très proches. Ne présente pas une similarité numérique comme une preuve de parenté.
6. Si l'identité du groupe ou le meilleur candidat reste ambigu, ne tranche pas par invention : marque le cas « revue humaine requise » et donne les éléments qui manquent.
7. Produis une liste nettoyée où chaque `model_id` retenu apparaît une seule fois et garde exactement les valeurs d'origine. Ne modifie pas le CSV source.
8. Les substitutions par un modèle proche ne doivent pas être signalées par une colonne dans le dataset nettoyé. Elles doivent cependant apparaître dans le journal d'audit séparé.

SORTIE
A. `MODELES_RETENUS` : tableau contenant, pour chaque modèle retenu, son `model_id` exact et son statut (`modèle de base` ou `substitut proposé`).
B. `JOURNAL_AUDIT` : pour chaque groupe, liste les `model_id` examinés et leur statut (base, fine-tuné, quantifié, autre, incertain), le représentant proposé, la justification, les valeurs `total_params` et `activated_params` comparées, `d_total`, `d_active`, le score calculé, et un indicateur de revue humaine requise.
C. `A_VERIFIER` : liste les cas ambigus, les données manquantes/incohérentes, et les affirmations qui nécessiteraient une source externe.

Avant de terminer, vérifie que chaque ligne d'entrée est soit représentée dans un groupe du journal d'audit, soit explicitement classée comme modèle indépendant. Ne prétends pas avoir vérifié une information externe.

TABLEAU D'ENTRÉE :
[COLLER ICI LE CONTENU DU CSV]
```
