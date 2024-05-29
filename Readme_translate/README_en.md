# Multilingual Translation i18niwatoko

i18niwatoko is an AI tool that can simultaneously translate from any native language to all languages around the world.
And the program files here are all written only in their respective native languages, with no high-level languages at all, a completely new set of program files.

![i18niwatoko](../readme_rich_progress.png)


## The Philosophy of i18niwatoko

Aiming for a world where anyone can enjoy programming by overcoming language barriers.

i18niwatoko was born to tackle the challenge of multilingual translation. With conventional multilingual translation tools, there was a problem that they had to deal with programming languages based on English, which was a high hurdle for non-English speakers.

However, i18niwatoko is different. It is a programming language that can run systems in natural language, allowing anyone to write programs in their native language. Furthermore, i18niwatoko has the function to automatically translate Japanese message files into multiple languages. This eliminates the need for manual translation, allowing for efficient multilingual support.

Programming is not just for a select few with special talents. By removing language barriers, the goal of i18niwatoko is to enable people around the world to experience the joy and potential of programming.

Together with i18niwatoko, while respecting the diversity of languages, we aim to realize a society where people around the world can unleash their creativity and generate new ideas through programming.

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
   # Please obtain the project ID and location from GCP Vertex AI. (If you don't know, please contact Motoki X at https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

   <!-- Explanation -->
   <!-- Set the API keys and project settings for OpenAI, Anthropic, and GCP Vertex AI as environment variables. -->
   <!-- Replace your_openai_api_key, your_anthropic_api_key, and your_gcp_project_id with the actual API keys and project IDs. -->
   <!-- GEMINI_LOCATION specifies the GCP Vertex AI region. Here, we set it to the Asia Tokyo region (asia-northeast1). -->

## Usage

1. Prepare the translation definition file (`def_translation.md`).

2. Run the following command to start the translation.
* gemini-1.5-flash is stable, but natural language programs are generally unstable during the transitional period. Try running it about 3 times, and it should work reliably.
* Research on AI hallucination and natural language program grammar is also ongoing, so stability will gradually increase. If you want to run it, we recommend directly editing the intermediate Python file.

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Once the translation is complete, the message files for each language will be generated.

4. def_translation.md is the requirements definition file. Please modify this file for more details.

## Relationship with i18n
The above is a sample format for i18n.
 pip install i18nice[YAML].



## Translated Languages

This project translates to the following languages:

- Bengali (bn)
- Chinese (zh)
- Danish (da)
- German (de)
- English (en)
- English (en)
- Spanish (es)
- Persian (fa)
- Finnish (fi)
- French (