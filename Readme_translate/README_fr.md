# Traduction multilingue i18niwatoko

i18niwatoko est un outil d'IA qui permet de traduire simultanément d'une langue à toutes les autres langues.

## La philosophie d'i18niwatoko

Viser un monde où tout le monde peut profiter du plaisir de la programmation, en franchissant les barrières linguistiques.

i18niwatoko est un outil innovant né pour relever le défi de la traduction multilingue. Les outils de traduction multilingue traditionnels nécessitent de travailler avec des langages de programmation basés sur l'anglais, ce qui représente un obstacle important pour les personnes ne parlant pas anglais.

Mais i18niwatoko est différent. C'est un langage de programmation qui permet de faire fonctionner les systèmes dans des langues naturelles, permettant à chacun d'écrire des programmes dans sa langue maternelle. De plus, i18niwatoko dispose d'une fonctionnalité permettant de traduire automatiquement les fichiers de messages en japonais vers de multiples langues. Cela élimine le besoin de traduction manuelle et permet une prise en charge multilingue efficace.

La programmation n'est pas réservée à une élite douée. En éliminant les barrières linguistiques, nous voulons permettre à tous les gens du monde d'expérimenter le plaisir et le potentiel de la programmation. C'est la noble ambition d'i18niwatoko.

Avec i18niwatoko, respectons la diversité des langues et utilisons la puissance de la technologie pour connecter les gens. Permettons à tous d'exprimer leur créativité et de générer de nouvelles idées à travers la programmation, pour construire une société où chacun peut s'épanouir.

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
   # Définir la clé API OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Définir la clé API Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Configurer GCP Vertex AI
   # Récupérez l'ID de projet et l'emplacement de GCP Vertex AI. (Si vous ne savez plus, contactez Motoki X à https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Utilisation

1. Préparez le fichier de définition de traduction (`def_translation.md`).

2. Exécutez la commande suivante pour lancer la traduction. (gemini-1.5-flash est stable.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Une fois la traduction terminée, les fichiers de messages dans chaque langue seront générés.

4. Le fichier def_translation.md est le cahier des charges. Modifiez-le selon vos besoins.

## Langues traduites

Ce projet traduit dans les langues suivantes :

- Bengali (bn)
- Chinois (zh)
- Danois (da)
- Allemand (de)
- Anglais (en)
- Espagnol (es)
- Persan (fa)
- Finnois (fi)