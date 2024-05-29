# Traduction multilingue i18niwatoko

i18niwatoko est un outil d'IA qui traduit simultanément dans toutes les langues du monde à partir de la langue maternelle de chacun.
Et les fichiers de programme ici sont tous écrits uniquement dans leur langue maternelle respective, sans aucun langage de haut niveau, ce sont des fichiers de programme complètement nouveaux.

![i18niwatoko](../readme_rich_progress.png)


## La philosophie d'i18niwatoko

Viser un monde où tout le monde peut profiter du plaisir de la programmation, en franchissant la barrière des langues.

i18niwatoko est un outil innovant né pour relever le défi de la traduction multilingue. Les outils de traduction multilingue traditionnels nécessitent de travailler avec des langages de programmation basés sur l'anglais, ce qui représente un obstacle important pour les personnes non anglophones.

Mais i18niwatoko est différent. C'est un langage de programmation qui permet de faire fonctionner les systèmes dans des langues naturelles, permettant à chacun d'écrire des programmes dans sa langue maternelle. De plus, i18niwatoko dispose d'une fonction de traduction automatique de fichiers de messages japonais vers de multiples langues. Cela permet d'éviter les traductions manuelles et de réaliser efficacement une prise en charge multilingue.

La programmation n'est pas réservée à une élite douée. En éliminant les barrières linguistiques, nous permettons à tous les gens du monde d'expérimenter le plaisir et le potentiel de la programmation. Telle est la noble philosophie d'i18niwatoko.

Avec i18niwatoko, tout en respectant la diversité des langues, nous visons à réaliser une société où les gens du monde entier peuvent exprimer leur créativité et générer de nouvelles idées à travers la programmation.

## Prérequis

- Python 3.x
- Bibliothèque niwatoko
- GCP Vertex AI
- API Anthropic Claude
- API OpenAI

## Configuration

1. Installez la bibliothèque niwatoko.

   ```
   pip install --upgrade niwatoko
   ```

2. Configurez OpenAI, Anthropic et GCP Vertex AI.

   ```
   # Définition de la clé API OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Définition de la clé API Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Configuration de GCP Vertex AI
   # Récupérez l'ID de projet et l'emplacement de GCP Vertex AI. (Si vous ne savez plus, contactez Motoki X à https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Utilisation

1. Préparez le fichier de définition de traduction (`def_translation.md`).

2. Exécutez la commande suivante pour lancer la traduction.
   * gemini-1.5-flash est stable, mais les programmes en langage naturel sont en phase de transition et généralement instables. Essayez 3 fois et cela devrait fonctionner.
   * La recherche sur l'hallucination de l'IA et la grammaire des programmes en langage naturel est également en cours, donc la stabilité s'améliorera progressivement. Si vous voulez le faire fonctionner, nous vous recommandons de modifier directement le fichier Python intermédiaire.

   ```
   niwatoko def_translation.