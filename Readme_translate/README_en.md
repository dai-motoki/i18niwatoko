# Multilingual Translation i18niwatoko

i18niwatoko is an AI tool that can translate from any language to any language.

## The Philosophy of i18niwatoko

Aiming for a world where anyone can enjoy programming by overcoming language barriers.

i18niwatoko was born to tackle the challenges of multilingual translation. With traditional multilingual translation tools, there was a problem that users had to deal with programming languages based on English, which was a high hurdle for non-English speakers.

However, i18niwatoko is different. It is a programming language that can run systems in natural language, allowing anyone to write programs in their native language. Furthermore, i18niwatoko has the function to automatically translate Japanese message files into multiple languages. This eliminates the need for manual translation, allowing for efficient multilingual support.

Programming is not just for a select few with special talents. By removing language barriers, we can enable people around the world to experience the joy and potential of programming. This is the noble philosophy of i18niwatoko.

Together with i18niwatoko, let's connect people around the world while respecting linguistic diversity, using the power of technology. Through programming, let's realize a society where people can unleash their creativity and generate new ideas.

## Requirements

- Python 3.x
- niwatoko library
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Setup

1. Install the niwatoko library.

   ```
   pip install --upgrade niwatoko
   ```

2. Configure OpenAI, Anthropic, and GCP Vertex AI.

   ```
   # Set the OpenAI API key
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Set the Anthropic API key
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Configure GCP Vertex AI
   # Obtain the project ID and location from GCP Vertex AI. (If you don't know, please contact Motoki X at https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

   <!-- Explanation -->
   <!-- Set the API keys and project configurations for OpenAI, Anthropic, and GCP Vertex AI as environment variables. -->
   <!-- Replace your_openai_api_key, your_anthropic_api_key, and your_gcp_project_id with the actual API keys and project IDs. -->
   <!-- GEMINI_LOCATION specifies the GCP Vertex AI region. Here, we set it to the Asia-Northeast1 region. -->

## Usage

1. Prepare the translation definition file (`def_translation.md`).

2. Run the following command to start the translation. (gemini-1.5-flash is stable.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Once the translation is complete, the message files for each language will be generated.

4. def_translation.md is the requirements document. Please modify this file for more details.

## Supported Languages

This project supports translation to the following languages:

- Bengali (bn)
- Chinese (zh)
- Danish (da)
- German (de)
- English (en)
- Spanish (es)
- Persian (fa)
- Finnish (fi)
- French (fr)
- Hindi (hi)
- Italian (it)
- Korean (ko)
- Dutch (nl)
- Norwegian (no)
- Polish (pl)
- Portuguese (pt)
- Russian (ru)
- Swedish (sv)
- Thai (th)
- Turkish (tr)
- Ukrainian (uk)
- Vietnamese (vi)

## Cautions

- Translation may take some time.
- Be aware of API usage limits.
- The translation results may not be perfect, so manual corrections may be necessary.