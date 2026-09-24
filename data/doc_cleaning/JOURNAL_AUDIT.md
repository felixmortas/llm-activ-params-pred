# JOURNAL_AUDIT — Regroupement des variantes MoE Hugging Face

**Methodologie.** Les groupes ont ete constitues a partir (1) d'une signature d'architecture identique (model_type + dimensions structurelles : hidden_size, nb de couches, nb de tetes, nb d'experts, etc.) et (2) de liens explicites portes par le `model_id` (suffixes de quantification `-FP8/-GGUF/-NVFP4/-GPTQ/...`, de fine-tuning `-Instruct/-Chat/-Thinking/...`, ou balise `-Base`). Aucune relation de parente non visible dans le tableau n'a ete supposee. `score = d_total + d_active` avec `d_total = |log10(total_params_candidat) - log10(total_params_reference)|` (idem pour `d_active`), calcule par rapport au representant retenu pour la famille.

---

## DeepSeek-V3

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-V3` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-V3 | base | 684531386000 | 37561368018 | - | - | - | nom explicite, sans suffixe |
| deepseek-ai/DeepSeek-V3-0324 | fine-tune | 684531386000 | 37561368018 | 0.0 | 0.0 | 0.0 | checkpoint date, meme famille V3 |
| unsloth/DeepSeek-V3-0324-GGUF | quantifie | 704920158208 | 38680133632 | 0.0127 | 0.0127 | 0.0255 | GGUF de V3-0324, source=formula |

## DeepSeek-V3.1

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-V3.1-Base` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-V3.1-Base | base | 684531386000 | 37561368018 | - | - | - | suffixe -Base explicite |
| deepseek-ai/DeepSeek-V3.1 | fine-tune | 684531386000 | 37561368018 | 0.0 | 0.0 | 0.0 | variante chat de V3.1-Base |
| deepseek-ai/DeepSeek-V3.1-Terminus | fine-tune | 684531386000 | 37561368018 | 0.0 | 0.0 | 0.0 | mise a jour de V3.1 |

## DeepSeek-R1

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-R1` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-R1 | base | 684489845504 | 37559088622 | - | - | - | nom explicite, tete de ligne R1 |
| deepseek-ai/DeepSeek-R1-0528 | fine-tune | 684531386000 | 37561368018 | 0.0 | 0.0 | 0.0001 | checkpoint date de R1 |
| deepseek-ai/DeepSeek-R1-Zero | fine-tune | 684531386000 | 37561368018 | 0.0 | 0.0 | 0.0001 | variante RL-only de R1 |
| unsloth/DeepSeek-R1-GGUF | quantifie | 704920158208 | 38680133632 | 0.0128 | 0.0128 | 0.0255 | GGUF de R1 |
| unsloth/DeepSeek-R1-0528-GGUF | quantifie | 704920158208 | 38680133632 | 0.0128 | 0.0128 | 0.0255 | GGUF de R1-0528 |
| nvidia/DeepSeek-R1-NVFP4 | quantifie | 396767013632 | 21771261510 | 0.2368 | 0.2368 | 0.4737 | NVFP4 de R1 |
| microsoft/MAI-DS-R1 | fine-tune | 671026419200 | 36820328179 | 0.0086 | 0.0086 | 0.0173 | nom contient R1 explicitement |
| tngtech/DeepSeek-R1T-Chimera | autre | 684531386000 | 37561368018 | 0.0 | 0.0 | 0.0001 | merge explicite referencant R1 |
| tngtech/DeepSeek-TNG-R1T2-Chimera | autre | 684531386000 | 37561368018 | 0.0 | 0.0 | 0.0001 | merge explicite referencant R1 |
| unsloth/r1-1776-GGUF | quantifie | 704920158208 | 38680133632 | 0.0128 | 0.0128 | 0.0255 | GGUF + fine-tune '1776' de r1 (nom explicite 'r1') |

## DeepSeek-Prover-V2-671B

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `deepseek-ai/DeepSeek-Prover-V2-671B` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-Prover-V2-671B | incertain | 684531386000 | 37561368018 | - | - | - | meme architecture que V3/R1 mais nom sans lien explicite -> modele independant |

## DeepSeek-V4-Flash

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-V4-Flash` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-V4-Flash | base | 290944616402 | 20402835038 | - | - | - | nom explicite sans suffixe |
| deepseek-ai/DeepSeek-V4-Flash-0731 | fine-tune | 304180418494 | 21331011301 | 0.0193 | 0.0193 | 0.0386 | checkpoint date de V4-Flash |
| deepseek-ai/DeepSeek-V4-Flash-DSpark | incertain | 165265454782 | 11589435313 | 0.2456 | 0.2456 | 0.4913 | suffixe DSpark non documente (fine-tune/distillation probable) |
| nvidia/DeepSeek-V4-Flash-NVFP4 | quantifie | 166726476754 | 11691891205 | 0.2418 | 0.2418 | 0.4836 | NVFP4 de V4-Flash |
| Chunjiang-Intelligence/DeepSeek-v4-Fable | incertain | 149210695634 | 10463576355 | 0.29 | 0.29 | 0.58 | memes dims d'architecture mais total_params tres different (149G vs ~290-304G): incoherence a verifier |

## DeepSeek-V4-Pro

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-V4-Pro` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-V4-Pro | base | 1598839674782 | 87312401789 | - | - | - | nom explicite |
| deepseek-ai/DeepSeek-V4-Pro-0813 | fine-tune | 1650497936906 | 90133451960 | 0.0138 | 0.0138 | 0.0276 | checkpoint date |
| deepseek-ai/DeepSeek-V4-Pro-DSpark | incertain | 1650497936906 | 90133451960 | 0.0138 | 0.0138 | 0.0276 | suffixe non documente |

## DeepSeek-V3.2

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-V3.2` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-V3.2 | base | 685355329792 | 37606579175 | - | - | - | nom explicite |
| deepseek-ai/DeepSeek-V3.2-Exp | fine-tune | 685396921376 | 37608861374 | 0.0 | 0.0 | 0.0001 | variante experimentale de V3.2 |
| deepseek-ai/DeepSeek-V3.2-Speciale | fine-tune | 685396921376 | 37608861374 | 0.0 | 0.0 | 0.0001 | variante de V3.2 |

## DeepSeek-Math-V2

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `deepseek-ai/DeepSeek-Math-V2` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-Math-V2 | incertain | 685396921376 | 37608861374 | - | - | - | meme architecture que V3.2 mais nom sans lien explicite -> independant |

## DeepSeek-V2

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-V2` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-V2 | base | 235741434880 | 18637015110 | - | - | - | nom explicite |
| deepseek-ai/DeepSeek-V2-Chat | fine-tune | 235741434880 | 18637015110 | 0.0 | 0.0 | 0.0 | variante chat de V2 |
| deepseek-ai/DeepSeek-V2-Chat-0628 | fine-tune | 235741434880 | 18637015110 | 0.0 | 0.0 | 0.0 | checkpoint date |

## DeepSeek-V2.5 / DeepSeek-Coder-V2 (sans base explicite)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `deepseek-ai/DeepSeek-V2.5` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Pas de modele -Base pour V2.5 ni pour Coder-V2 dans le tableau; total_params/activated_params identiques pour tous les membres (score=0 partout), donc aucun departage numerique possible. Choix du representant necessiterait une source externe.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-V2.5 | incertain | 235741434880 | 18637015110 | - | - | - | aucune balise -Base; nom le plus simple du sous-groupe V2.5 |
| deepseek-ai/DeepSeek-V2.5-1210 | fine-tune | 235741434880 | 18637015110 | 0.0 | 0.0 | 0.0 | checkpoint date de V2.5 |
| deepseek-ai/DeepSeek-Coder-V2-Instruct | incertain | 235741434880 | 18637015110 | 0.0 | 0.0 | 0.0 | aucune balise -Base pour Coder-V2 dans le tableau |
| deepseek-ai/DeepSeek-Coder-V2-Instruct-0724 | fine-tune | 235741434880 | 18637015110 | 0.0 | 0.0 | 0.0 | checkpoint date de Coder-V2-Instruct |

## DeepSeek-V2-Lite

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-V2-Lite` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-V2-Lite | base | 15706484224 | 2645947730 | - | - | - | nom explicite |
| deepseek-ai/DeepSeek-V2-Lite-Chat | fine-tune | 15706484224 | 2645947730 | 0.0 | 0.0 | 0.0 | variante chat |

## DeepSeek-Coder-V2-Lite

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/DeepSeek-Coder-V2-Lite-Base` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/DeepSeek-Coder-V2-Lite-Base | base | 15706484224 | 2645947730 | - | - | - | suffixe -Base explicite |
| deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct | fine-tune | 15706484224 | 2645947730 | 0.0 | 0.0 | 0.0 | variante instruct |

## Kimi-K2

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `moonshotai/Kimi-K2-Base` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| moonshotai/Kimi-K2-Base | base | 1026470731056 | 38376638004 | - | - | - | suffixe -Base explicite |
| moonshotai/Kimi-K2-Instruct | fine-tune | 1026408235864 | 38374301497 | 0.0 | 0.0 | 0.0001 | variante instruct |
| moonshotai/Kimi-K2-Instruct-0905 | fine-tune | 1026470735448 | 38376638168 | 0.0 | 0.0 | 0.0 | checkpoint date |
| moonshotai/Kimi-K2-Thinking | fine-tune | 1026408240256 | 38374301662 | 0.0 | 0.0 | 0.0001 | variante reasoning |
| unsloth/Kimi-K2-Instruct-GGUF | quantifie | 1049337397248 | 39231553536 | 0.0096 | 0.0096 | 0.0191 | GGUF de Kimi-K2-Instruct; ATTENTION: model_type source indique 'deepseek_v3' au lieu de 'kimi_k2' (incoherence de metadonnees), lien etabli via le nom explicite |

## Moonlight-16B-A3B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `moonshotai/Moonlight-16B-A3B` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| moonshotai/Moonlight-16B-A3B | base | 15960111936 | 2890561333 | - | - | - | nom explicite |
| moonshotai/Moonlight-16B-A3B-Instruct | fine-tune | 15960111936 | 2890561333 | 0.0 | 0.0 | 0.0 | variante instruct |

## deepseek-moe-16b

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `deepseek-ai/deepseek-moe-16b-base` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| deepseek-ai/deepseek-moe-16b-base | base | 16375728128 | 2746157979 | - | - | - | suffixe -base explicite |
| deepseek-ai/deepseek-moe-16b-chat | fine-tune | 16375728128 | 2746157979 | 0.0 | 0.0 | 0.0 | variante chat |

## Qwen3-30B-A3B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `Qwen/Qwen3-30B-A3B` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| Qwen/Qwen3-30B-A3B | base | 30532122624 | 3352844924 | - | - | - | nom explicite sans suffixe |
| Qwen/Qwen3-30B-A3B-Instruct-2507 | fine-tune | 30532122624 | 3352844924 | 0.0 | 0.0 | 0.0 | variante instruct |
| Qwen/Qwen3-30B-A3B-Thinking-2507 | fine-tune | 30532122624 | 3352844924 | 0.0 | 0.0 | 0.0 | variante reasoning |
| Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 | quantifie | 30533947392 | 3353045309 | 0.0 | 0.0 | 0.0001 | FP8 de la variante instruct |
| unsloth/Qwen3-30B-A3B-GGUF | quantifie | 30531911680 | 3352821760 | 0.0 | 0.0 | 0.0 | GGUF du modele de base |
| Qwen/Qwen3-Coder-30B-A3B-Instruct | fine-tune | 30532122624 | 3352844924 | 0.0 | 0.0 | 0.0 | specialisation code, meme architecture |
| Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 | quantifie | 30533947392 | 3353045309 | 0.0 | 0.0 | 0.0001 | FP8 de Qwen3-Coder-30B-A3B-Instruct |
| Tongyi-Zhiwen/QwenLong-L1.5-30B-A3B | incertain | 30532122624 | 3352844924 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite avec Qwen3-30B-A3B, arch identique |
| NousResearch/nomos-1 | incertain | 30532122624 | 3352844924 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite, arch identique |
| miromind-ai/MiroThinker-v1.5-30B | incertain | 30532122624 | 3352844924 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite, arch identique |
| miromind-ai/MiroThinker-1.7-mini | incertain | 30532122624 | 3352844924 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite, arch identique |

## Qwen3-235B-A22B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `Qwen/Qwen3-235B-A22B` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| Qwen/Qwen3-235B-A22B | base | 235093634560 | 22190040653 | - | - | - | nom explicite |
| Qwen/Qwen3-235B-A22B-Instruct-2507 | fine-tune | 235093634560 | 22190040653 | 0.0 | 0.0 | 0.0 | variante instruct |
| Qwen/Qwen3-235B-A22B-Thinking-2507 | fine-tune | 235093634560 | 22190040653 | 0.0 | 0.0 | 0.0 | variante reasoning |
| Qwen/Qwen3-235B-A22B-Instruct-2507-FP8 | quantifie | 235107904512 | 22191387566 | 0.0 | 0.0 | 0.0001 | FP8 de la variante instruct |
| miromind-ai/MiroThinker-v1.5-235B | incertain | 235093634560 | 22190040653 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite |
| miromind-ai/MiroThinker-1.7 | incertain | 235093634560 | 22190040653 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite |
| baichuan-inc/Baichuan-M3-235B | incertain | 235093634560 | 22190040653 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite malgre architecture identique |

## Qwen3-Coder-480B-A35B-Instruct

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `Qwen/Qwen3-Coder-480B-A35B-Instruct` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| Qwen/Qwen3-Coder-480B-A35B-Instruct | incertain | 480154875392 | 35474039352 | - | - | - | seule variante non quantifiee disponible, pas de base pretrain publique dans le tableau |
| Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 | quantifie | 480184064000 | 35476195819 | 0.0 | 0.0 | 0.0001 | FP8 de la variante instruct |

## Qwen3-Next-80B-A3B (sans base non-finetunee)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `Qwen/Qwen3-Next-80B-A3B-Instruct` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Instruct et Thinking ont des total_params/activated_params strictement identiques (score=0) et la meme architecture: aucun departage possible sans information externe sur le veritable modele de base 'Qwen3-Next-80B-A3B'.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| Qwen/Qwen3-Next-80B-A3B-Instruct | incertain | 81324862720 | 3183985633 | - | - | - | aucune version 'base' de Qwen3-Next-80B-A3B dans le tableau |
| Qwen/Qwen3-Next-80B-A3B-Thinking | incertain | 81324862720 | 3183985633 | 0.0 | 0.0 | 0.0 | aucune version 'base' dans le tableau |
| unsloth/Qwen3-Next-80B-A3B-Instruct-GGUF | quantifie | 78888042496 | 3088580608 | 0.0132 | 0.0132 | 0.0264 | GGUF de la variante instruct |

## Qwen3-Coder-Next

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `Qwen/Qwen3-Coder-Next` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| Qwen/Qwen3-Coder-Next | base | 79674391296 | 3119367297 | - | - | - | nom explicite sans suffixe (seule version non quantifiee) |
| Qwen/Qwen3-Coder-Next-FP8 | quantifie | 79679212800 | 3119556066 | 0.0 | 0.0 | 0.0001 | FP8 de Qwen3-Coder-Next |

## Qwen3.8-2.4T-A95B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `Qwen/Qwen3.8-2.4T-A95B` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| Qwen/Qwen3.8-2.4T-A95B | base | 2446182725504 | 78431172082 | - | - | - | nom explicite |
| Qwen/Qwen3.8-2.4T-A95B-FP8 | quantifie | 2446182725504 | 78431172082 | 0.0 | 0.0 | 0.0 | FP8 |

## Qwen1.5-MoE-A2.7B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `Qwen/Qwen1.5-MoE-A2.7B` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| Qwen/Qwen1.5-MoE-A2.7B | base | 14315784192 | 1972894769 | - | - | - | nom explicite |
| Qwen/Qwen1.5-MoE-A2.7B-Chat | fine-tune | 14315784192 | 1972894769 | 0.0 | 0.0 | 0.0 | variante chat |

## GLM-5.2

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `zai-org/GLM-5.2` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| zai-org/GLM-5.2 | base | 753329940480 | 50152524869 | - | - | - | nom explicite |
| zai-org/GLM-5.2-FP8 | quantifie | 753329940480 | 50152524869 | 0.0 | 0.0 | 0.0 | FP8 |
| nvidia/GLM-5.2-NVFP4 | quantifie | 380989135104 | 25364141323 | 0.2961 | 0.2961 | 0.5921 | NVFP4 |
| mastouri/GLM-5.2-colibri-int4-g64-with-int8-mtp | quantifie | 782292221952 | 52080672768 | 0.0164 | 0.0164 | 0.0328 | quantification int4 personnalisee |

## GLM-5.3

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `zai-org/GLM-5.3` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| zai-org/GLM-5.3 | base | 753329940480 | 50152524869 | - | - | - | nom explicite |
| dealignai/GLM-5.3-CYBERSECURITY-FP8 | fine-tune+quantifie | 753329940480 | 50152524869 | 0.0 | 0.0 | 0.0 | fine-tune domaine cybersecurite + FP8 |

## GLM-5

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `zai-org/GLM-5` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| zai-org/GLM-5 | base | 753864139008 | 35773373370 | - | - | - | nom explicite |
| zai-org/GLM-5-FP8 | quantifie | 753910024032 | 35775550768 | 0.0 | 0.0 | 0.0001 | FP8 |

## GLM-5.1

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `zai-org/GLM-5.1` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| zai-org/GLM-5.1 | base | 753864139008 | 35773373370 | - | - | - | nom explicite |
| zai-org/GLM-5.1-FP8 | quantifie | 753910024032 | 35775550768 | 0.0 | 0.0 | 0.0001 | FP8 |

## GLM-4.5

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `zai-org/GLM-4.5` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| zai-org/GLM-4.5 | incertain | 358337791296 | 33212948328 | - | - | - | aucune variante associee dans le tableau (architecture 5120) |

## GLM-4.6

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `zai-org/GLM-4.6` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| zai-org/GLM-4.6 | base | 356785898816 | 33069109397 | - | - | - | nom explicite |
| ArliAI/GLM-4.6-Derestricted-v3 | fine-tune | 356785898816 | 33069109397 | 0.0 | 0.0 | 0.0 | fine-tune tiers (derestriction) |

## GLM-4.7

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `zai-org/GLM-4.7` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| zai-org/GLM-4.7 | base | 358337791296 | 33212948328 | - | - | - | nom explicite |
| zai-org/GLM-4.7-FP8 | quantifie | 358458391872 | 33224126330 | 0.0001 | 0.0001 | 0.0003 | FP8 |

## GLM-4.5-Air

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `zai-org/GLM-4.5-Air` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| zai-org/GLM-4.5-Air | base | 110468824832 | 13632377355 | - | - | - | nom explicite |
| ArliAI/GLM-4.5-Air-Derestricted | fine-tune | 110468824832 | 13632377355 | 0.0 | 0.0 | 0.0 | fine-tune tiers |
| PrimeIntellect/INTELLECT-3 | incertain | 106852251264 | 13186075010 | 0.0145 | 0.0145 | 0.0289 | pas de lien nominal explicite malgre architecture identique |
| cerebras/GLM-4.5-Air-REAP-82B-A12B | autre | 81932181504 | 13190383172 | 0.1298 | 0.0143 | 0.1441 | modele compresse/elague (REAP, nombre d'experts reduit): architecture differente (96 experts vs 128) mais nom explicitement lie a GLM-4.5-Air |

## MiniMax-M2

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `MiniMaxAI/MiniMax-M2` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| MiniMaxAI/MiniMax-M2 | base | 228689764864 | 11029749520 | - | - | - | nom explicite |
| MiniMaxAI/MiniMax-M2.1 | fine-tune | 228689764864 | 11029749520 | 0.0 | 0.0 | 0.0 | mise a jour de M2 |
| MiniMaxAI/MiniMax-M2.5 | fine-tune | 228703644928 | 11030418958 | 0.0 | 0.0 | 0.0001 | mise a jour de M2 |
| MiniMaxAI/MiniMax-M2.7 | fine-tune | 228689764864 | 11029749520 | 0.0 | 0.0 | 0.0 | mise a jour de M2 |

## MiniMax-M1 (variantes de contexte)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `MiniMaxAI/MiniMax-M1-80k` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Aucune balise -Base; total_params/activated_params identiques pour les deux variantes de contexte (score=0): aucun departage numerique possible.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| MiniMaxAI/MiniMax-M1-80k | incertain | 456089655296 | 39553278693 | - | - | - | variante de longueur de contexte, pas de balise base |
| MiniMaxAI/MiniMax-M1-40k | incertain | 456089655296 | 39553278693 | 0.0 | 0.0 | 0.0 | variante de longueur de contexte, pas de balise base |

## gpt-oss-20b

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `openai/gpt-oss-20b` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| openai/gpt-oss-20b | base | 20914757184 | 4187671602 | - | - | - | nom explicite |
| unsloth/gpt-oss-20b-GGUF | quantifie | 20907786240 | 4186275840 | 0.0001 | 0.0001 | 0.0003 | GGUF |
| openai/gpt-oss-safeguard-20b | fine-tune | 21511953984 | 4307245740 | 0.0122 | 0.0122 | 0.0245 | fine-tune officiel (garde-fous) |
| huihui-ai/Huihui-gpt-oss-20b-BF16-abliterated | fine-tune | 20914757184 | 4187671602 | 0.0 | 0.0 | 0.0 | fine-tune tiers (retrait de refus, 'abliterated') |
| p-e-w/gpt-oss-20b-heretic | fine-tune | 20914757184 | 4187671602 | 0.0 | 0.0 | 0.0 | fine-tune tiers |
| chromadb/context-1 | incertain | 20914757184 | 4187671602 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite malgre architecture identique |
| pat-jj/harness-1 | incertain | 20914757184 | 4187671602 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite |
| microsoft/OptiMind-SFT | incertain | 20914757184 | 4187671602 | 0.0 | 0.0 | 0.0 | pas de lien nominal explicite (SFT suggere un fine-tune, base non confirmee) |

## gpt-oss-120b

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `openai/gpt-oss-120b` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| openai/gpt-oss-120b | base | 116829156672 | 5712204907 | - | - | - | nom explicite |
| unsloth/gpt-oss-120b-GGUF | quantifie | 116788838400 | 5710233600 | 0.0001 | 0.0001 | 0.0003 | GGUF |
| openai/gpt-oss-safeguard-120b | fine-tune | 120412337472 | 5887399726 | 0.0131 | 0.0131 | 0.0262 | fine-tune officiel |

## NVIDIA-Nemotron-3-Nano-30B-A3B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16 | base | 31577937344 | 2279424392 | - | - | - | suffixe -Base explicite |
| nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 | fine-tune | 31577937344 | 2279424392 | 0.0 | 0.0 | 0.0 | variante post-entrainee BF16 |
| nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 | quantifie | 31577946256 | 2279425035 | 0.0 | 0.0 | 0.0 | FP8 |
| nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 | quantifie | 18237772608 | 1316476858 | 0.2384 | 0.2384 | 0.4768 | NVFP4 |

## NVIDIA-Nemotron-3.5-Lightning-30B-A3B

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Aucune version taguee -Base; BF16 propose comme reference par convention (precision native non quantifiee) mais ceci n'est pas garanti par le tableau seul.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16 | incertain | 31577937344 | 2279424392 | - | - | - | BF16 = precision native retenue comme reference, aucune balise -Base |
| nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4 | quantifie | 17820210764 | 1286335540 | 0.2485 | 0.2485 | 0.4969 | NVFP4 de la variante BF16 |

## Nemotron-Cascade-2-30B-A3B

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `nvidia/Nemotron-Cascade-2-30B-A3B` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| nvidia/Nemotron-Cascade-2-30B-A3B | incertain | 31577937344 | 2279424392 | - | - | - | architecture identique a Nemotron-3-Nano mais nom sans lien explicite -> independant |

## pipecat-ai/phonellm-alpha-1

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `pipecat-ai/phonellm-alpha-1` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| pipecat-ai/phonellm-alpha-1 | incertain | 31577937344 | 2279424392 | - | - | - | architecture identique a Nemotron-3-Nano mais nom sans lien explicite -> independant |

## nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16 | base | 63185902848 | 4561016340 | - | - | - | porte -Base dans son propre nom mais represente un modele independant (pas de variante associee dans le tableau) |

## NVIDIA-Nemotron-3-Super-120B-A12B

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Aucune balise -Base. FP8 partage exactement les memes total_params/activated_params que BF16 (suspect si FP8 est cense etre quantifie), et NVFP4 affiche un total_params ~2x plus faible sans changement d'architecture declare: incoherences de donnees a verifier avant de choisir un representant definitif.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 | incertain | 123611012096 | 5889045124 | - | - | - | BF16 retenu comme reference (precision native), aucune balise -Base |
| nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8 | incertain | 123611012096 | 5889045124 | 0.0 | 0.0 | 0.0 | valeurs total/activated identiques a BF16 (source possiblement dupliquee) |
| nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 | quantifie | 67228556288 | 3202886174 | 0.2645 | 0.2645 | 0.529 | NVFP4, total_params nettement inferieur (incoherence possible du champ total_params pour ce format) |

## Mixtral-8x7B (vocab 32002, fine-tunes communautaires)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `dphn/dolphin-2.5-mixtral-8x7b` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Le modele de base officiel 'Mixtral-8x7B-v0.1' (vocab 32002) n'apparait dans aucune ligne du tableau; seuls des fine-tunes tiers sont presents, avec des total_params/activated_params quasi identiques (ecarts <0.001%). Impossible de designer un representant sans connaitre les parametres du vrai modele de base.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| dphn/dolphin-2.5-mixtral-8x7b | fine-tune | 46702809088 | 12879748815 | - | - | - | fine-tune communautaire |
| dphn/dolphin-2.6-mixtral-8x7b | fine-tune | 46702542848 | 12879675392 | 0.0 | 0.0 | 0.0 | fine-tune communautaire |
| dphn/dolphin-2.7-mixtral-8x7b | fine-tune | 46702542848 | 12879675392 | 0.0 | 0.0 | 0.0 | fine-tune communautaire |
| NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO | fine-tune | 46702809088 | 12879748815 | 0.0 | 0.0 | 0.0 | fine-tune DPO |
| fireworks-ai/firefunction-v1 | incertain | 46702809088 | 12879748815 | 0.0 | 0.0 | 0.0 | fine-tune probable (function calling) mais pas de lien nominal explicite au nom Mixtral |
| TheBloke/dolphin-2.5-mixtral-8x7b-GPTQ | quantifie | 46711525376 | 12882152602 | 0.0001 | 0.0001 | 0.0002 | GPTQ de dolphin-2.5 |

## Mixtral-8x7B-v0.1 / Instruct (vocab 32000, GPTQ + fine-tune)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `TheBloke/Mixtral-8x7B-v0.1-GPTQ` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Ni 'Mixtral-8x7B-v0.1' ni 'Mixtral-8x7B-Instruct-v0.1' non quantifies ne figurent dans le tableau: seules des copies GPTQ et un fine-tune tiers sont disponibles. Impossible de proposer un representant fiable sans le modele de base.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| TheBloke/Mixtral-8x7B-v0.1-GPTQ | quantifie | 46711508992 | 12882136216 | - | - | - | GPTQ du modele de base officiel (non present en clair dans le tableau) |
| TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ | quantifie | 46711508992 | 12882136216 | 0.0 | 0.0 | 0.0 | GPTQ de la variante Instruct officielle (non presente en clair) |
| argilla/notux-8x7b-v1 | incertain | 46702792704 | 12879732431 | 0.0001 | 0.0001 | 0.0002 | fine-tune DPO probable, pas de lien nominal explicite |

## Mixtral-8x22B-v0.1

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `mistral-community/Mixtral-8x22B-v0.1` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| mistral-community/Mixtral-8x22B-v0.1 | base | 140620634112 | 39151530770 | - | - | - | nom explicite = modele de base officiel (miroir communautaire) |
| v2ray/Mixtral-8x22B-v0.1 | autre | 140620634112 | 39151530770 | 0.0 | 0.0 | 0.0 | miroir/duplication du meme modele de base (meme nom exact, meme valeurs) |
| alpindale/WizardLM-2-8x22B | incertain | 140620634112 | 39151530770 | 0.0 | 0.0 | 0.0 | fine-tune tiers connu mais pas de lien nominal explicite avec 'Mixtral' |
| HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1 | incertain | 140620634112 | 39151530770 | 0.0 | 0.0 | 0.0 | fine-tune ORPO probable (taille '141b-A35b' coherente avec 8x22B) mais pas de lien nominal explicite |

## inclusionAI/Ling-2.6-1T (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ling-2.6-1T` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ling-2.6-1T | incertain | 1025657871744 | 58551223250 | - | - | - | meme architecture (1T, bailing_hybrid); pas de nom partage explicite avec la ligne 'Ring' -> traite comme independant |

## inclusionAI/Ring-2.6-1T (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ring-2.6-1T` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ring-2.6-1T | incertain | 1025657871744 | 58551223250 | - | - | - | meme architecture (1T, bailing_hybrid); pas de nom partage explicite avec la ligne 'Ling' -> traite comme independant |

## inclusionAI/Ring-2.5-1T (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ring-2.5-1T` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ring-2.5-1T | incertain | 1012474606720 | 57798636725 | - | - | - | meme architecture (1T, bailing_hybrid); pas de nom partage explicite avec la ligne 'Ring' -> traite comme independant |

## inclusionAI/Ling-2.5-1T (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ling-2.5-1T` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ling-2.5-1T | incertain | 1012231160320 | 57784739220 | - | - | - | meme architecture (1T, bailing_hybrid); pas de nom partage explicite avec la ligne 'Ling' -> traite comme independant |

## inclusionAI/Ling-mini-2.0 (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ling-mini-2.0` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ling-mini-2.0 | incertain | 16255643392 | 1364977689 | - | - | - | meme architecture (mini-2.0, bailing_moe); pas de nom partage explicite avec la ligne 'Ring' -> traite comme independant |

## inclusionAI/Ring-mini-2.0 (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ring-mini-2.0` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ring-mini-2.0 | incertain | 16255643392 | 1364977689 | - | - | - | meme architecture (mini-2.0, bailing_moe); pas de nom partage explicite avec la ligne 'Ling' -> traite comme independant |

## inclusionAI/Ling-flash-2.0 (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ling-flash-2.0` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ling-flash-2.0 | incertain | 102889705216 | 5971877252 | - | - | - | meme architecture (flash-2.0, bailing_moe); pas de nom partage explicite avec la ligne 'Ring' -> traite comme independant |

## inclusionAI/Ring-flash-2.0 (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ring-flash-2.0` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ring-flash-2.0 | incertain | 102889705216 | 5971877252 | - | - | - | meme architecture (flash-2.0, bailing_moe); pas de nom partage explicite avec la ligne 'Ling' -> traite comme independant |

## inclusionAI/Ling-1T (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ling-1T` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ling-1T | incertain | 999705328640 | 48632240327 | - | - | - | meme architecture (1T, bailing_moe); pas de nom partage explicite avec la ligne 'Ring' -> traite comme independant |

## inclusionAI/Ring-1T (independant)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `inclusionAI/Ring-1T` — statut : **substitut propose**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ring-1T | incertain | 999705328640 | 48632240327 | - | - | - | meme architecture (1T, bailing_moe); pas de nom partage explicite avec la ligne 'Ling' -> traite comme independant |

## Ling-3.0-tiny

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `inclusionAI/Ling-3.0-tiny` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ling-3.0-tiny | base | 7893392800 | 1266992314 | - | - | - | nom explicite |
| bloomer010/Ling-3.0-tiny-GGUF | quantifie | 8093958144 | 1299185664 | 0.0109 | 0.0109 | 0.0218 | GGUF |

## Ling-3.0-flash

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `inclusionAI/Ling-3.0-flash` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| inclusionAI/Ling-3.0-flash | base | 127486405600 | 4768002133 | - | - | - | nom explicite |
| inclusionAI/Ling-3.0-flash-Fin | fine-tune | 127486405600 | 4768002133 | 0.0 | 0.0 | 0.0 | fine-tune domaine finance |

## Trinity-Large (Thinking/Preview)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `arcee-ai/Trinity-Large-Preview` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Aucune balise -Base; total_params/activated_params strictement identiques pour les deux variantes: aucun departage numerique possible.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| arcee-ai/Trinity-Large-Preview | incertain | 398635286016 | 11233734010 | - | - | - | aucune balise base; propose comme reference provisoire (preview = version anterieure) |
| arcee-ai/Trinity-Large-Thinking | fine-tune | 398635286016 | 11233734010 | 0.0 | 0.0 | 0.0 | variante reasoning, valeurs identiques a Preview |

## LongCat-Flash

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `meituan-longcat/LongCat-Flash-Chat` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Aucune balise -Base; total_params/activated_params identiques pour les trois variantes: aucun departage numerique possible.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| meituan-longcat/LongCat-Flash-Chat | incertain | 561862880256 | 14168336239 | - | - | - | aucune balise base; le plus 'like' des trois, propose comme reference provisoire |
| meituan-longcat/LongCat-Flash-Thinking | fine-tune | 561862880256 | 14168336239 | 0.0 | 0.0 | 0.0 | variante reasoning, valeurs identiques a Chat |
| meituan-longcat/LongCat-Flash-Thinking-2601 | fine-tune | 561862880256 | 14168336239 | 0.0 | 0.0 | 0.0 | checkpoint date de Thinking |

## Hy3

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `tencent/Hy3` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| tencent/Hy3 | base | 298786155776 | 20701051469 | - | - | - | nom explicite (version finale, sans suffixe) |
| tencent/Hy3-preview | autre | 298786155776 | 20701051469 | 0.0 | 0.0 | 0.0 | version anterieure (preview) du meme modele, valeurs identiques |

## Hymba-1.5B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `nvidia/Hymba-1.5B-Base` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| nvidia/Hymba-1.5B-Base | base | 1522797824 | 1522797824 | - | - | - | suffixe -Base explicite |
| nvidia/Hymba-1.5B-Instruct | fine-tune | 1522797824 | 1522797824 | 0.0 | 0.0 | 0.0 | variante instruct |

## Laguna-XS.2 / Laguna-XS-2.1 (doublon probable)

- **Modele de base present dans le tableau :** Non
- **Representant retenu :** `poolside/Laguna-XS-2.1` — statut : **substitut propose**
- **Revue humaine requise :** **OUI** — Les deux entrees partagent des valeurs total_params/activated_params rigoureusement identiques et un nom quasi identique: possible doublon de la meme fiche modele plutot qu'une reelle variante quantifiee/fine-tunee. A confirmer.

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| poolside/Laguna-XS-2.1 | incertain | 33442617088 | 2583994846 | - | - | - | nom au format standard, retenu comme representant |
| poolside/Laguna-XS.2 | autre | 33442617088 | 2583994846 | 0.0 | 0.0 | 0.0 | meme total_params/activated_params exacts que Laguna-XS-2.1: doublon probable du meme modele (variation orthographique du nom) |

## Laguna-S-2.1

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `poolside/Laguna-S-2.1` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| poolside/Laguna-S-2.1 | base | 117561977600 | 7226149534 | - | - | - | nom explicite |
| poolside/Laguna-S-2.1-NVFP4 | quantifie | 117561977600 | 7226149534 | 0.0 | 0.0 | 0.0 | NVFP4 |

## MiMo-V2.5-Pro

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `XiaomiMiMo/MiMo-V2.5-Pro` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| XiaomiMiMo/MiMo-V2.5-Pro | base | 1023244718976 | 44939650112 | - | - | - | nom explicite |
| XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash | quantifie | 554344371072 | 24346123284 | 0.2662 | 0.2662 | 0.5324 | FP4 |

## Solar-Open2-250B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `upstage/Solar-Open2-250B` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| upstage/Solar-Open2-250B | base | 250287810304 | 12221258355 | - | - | - | nom explicite |
| nota-ai/Solar-Open2-250B-Nota-NVFP4 | quantifie | 144591441664 | 7060229431 | 0.2383 | 0.2383 | 0.4766 | NVFP4 tiers |

## Xing4.0-29B-A4B

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `XingChen-AGI/Xing4.0-29B-A4B` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| XingChen-AGI/Xing4.0-29B-A4B | base | 31215031088 | 5137613459 | - | - | - | nom explicite |
| XingChen-AGI/Xing4.0-29B-A4B-FP8 | quantifie | 31215031088 | 5137613459 | 0.0 | 0.0 | 0.0 | FP8 |

## Step-3.5-Flash

- **Modele de base present dans le tableau :** Oui
- **Representant retenu :** `stepfun-ai/Step-3.5-Flash` — statut : **modele de base**
- **Revue humaine requise :** Non

| model_id | statut | total_params | activated_params | d_total | d_active | score | justification |
|---|---|---:|---:|---:|---:|---:|---|
| stepfun-ai/Step-3.5-Flash | base | 199384301376 | 12106308406 | - | - | - | nom explicite |
| stepfun-ai/Step-3.5-Flash-GGUF-Q4_K_S | quantifie | 210991972352 | 12811108352 | 0.0246 | 0.0246 | 0.0491 | GGUF Q4_K_S |
