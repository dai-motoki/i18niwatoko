# Flersproglig oversættelse i18niwatoko

i18niwatoko er et AI-værktøj, der kan oversætte fra ethvert modersmål til alle verdens sprog.
Og her er programfiler, der udelukkende er skrevet på deres respektive modersmål, uden brug af noget højniveau-sprog - helt nye programfiler.

![i18niwatoko](../readme_rich_progress.png)


## i18niwatokos filosofi

At overskride sprogbarrierer og gøre programmering tilgængelig for alle.

i18niwatoko er et innovativt værktøj, der tager fat på udfordringerne ved flersproglig oversættelse. Traditionelle flersproglige oversættelsesværktøjer kræver, at man arbejder med programmeringssprog baseret på engelsk, hvilket kan være en stor barriere for ikke-engelsktalende.

Men i18niwatoko er anderledes. Det er et programmeringssprog, der kører på naturlige sprog, så alle kan skrive programmer på deres modersmål. Derudover har i18niwatoko funktioner til at automatisk oversætte japanske beskedsfiler til flere sprog. Dette eliminerer behovet for manuel oversættelse og gør det muligt at opnå flersproget support på en effektiv måde.

Programmering er ikke kun for en særlig talentfuld elite. Ved at fjerne sprogbarrierer kan vi lade hele verden opleve glæden og mulighederne ved programmering. Det er i18niwatokos ophøjede vision.

Sammen med i18niwatoko kan vi skabe et samfund, hvor sproglig mangfoldighed respekteres, og hvor mennesker over hele verden kan udfolde deres kreativitet og skabe nye idéer gennem programmering.

## Hvad du har brug for

- Python 3.x
- niwatoko-biblioteket
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Opsætning

1. Installer niwatoko-biblioteket.

   ```
   pip install --upgrade niwatoko
   ```

2. Konfigurer OpenAI, Anthropic og GCP Vertex AI.

   ```
   # Sæt OpenAI API-nøgle
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Sæt Anthropic API-nøgle
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Konfigurer GCP Vertex AI
   # Hent project-id og location fra GCP Vertex AI (kontakt Motoki X, hvis du er i tvivl https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Sådan bruges det

1. Forbered en oversættelsesdefinitionsfil (`def_translation.md`).

2. Kør følgende kommando for at starte oversættelsen.
*gemini-1.5-flash er stabil, men naturlige sprogprogrammer er generelt i en overgangsperiode og derfor grundlæggende ustabile. Prøv det 3 gange, så burde det næsten sikkert virke.
*Forskning i AI-hallucinationer og naturlige sprogprogrammer er også i gang, så stabiliteten vil gradvist forbedres. Hvis du gerne vil køre det, anbefaler vi, at du redigerer den mellemliggende Python-fil direkte.

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Når oversættelsen er færdig, genereres beskedsfiler for hvert sprog.

4. def_translation.md er kravspecifik