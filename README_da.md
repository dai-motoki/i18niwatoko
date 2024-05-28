# Flersproglig oversættelse i18niwatoko

i18niwatoko er et AI-værktøj, der kan oversætte fra ethvert sprog til ethvert andet sprog.

## i18niwatokoens filosofi

At overskride sprogbarrierer og gøre programmering tilgængelig for alle.

i18niwatoko er et innovativt værktøj, der tager fat på udfordringerne ved flersproglig oversættelse. Tidligere flersproglige oversættelsesværktøjer krævede, at man arbejdede med programmeringssprog baseret på engelsk, hvilket udgjorde en barriere for ikke-engelsktalende.

Men i18niwatoko er anderledes. Det er et programmeringssprog, der kan køre på naturlige sprog, så alle kan programmere på deres modersmål. Derudover har i18niwatoko funktionalitet til at automatisk oversætte japanske beskedsfiler til flere sprog. Dette eliminerer behovet for manuel oversættelse og gør det muligt at implementere flersproget support på en effektiv måde.

Programmering er ikke forbeholdt en særlig talentfuld elite. Ved at fjerne sprogbarrierer kan vi lade mennesker over hele verden opleve glæden og mulighederne ved programmering. Det er i18niwatokoens noble vision.

Lad os sammen med i18niwatoko respektere sproglig mangfoldighed og bruge teknologiens kraft til at forbinde mennesker. Lad os realisere et samfund, hvor mennesker over hele verden kan udfolde deres kreativitet og skabe nye idéer gennem programmering.

## Forudsætninger

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

## Brug

1. Forbered en oversættelsesdefinitionsfil (`def_translation.md`).

2. Kør følgende kommando for at starte oversættelsen. (gemini-1.5-flash er stabil.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Når oversættelsen er færdig, genereres beskedsfiler for hvert sprog.

4. def_translation.md er kravspecifikationen. Rediger denne fil for at ændre oversættelseskravene.

## Oversatte sprog

Projektet oversætter til følgende sprog:

- Bengali (bn)
- Kinesisk (zh)
- Dansk (da)
- Tysk (de)
- Engelsk (en)
- Spansk (es)
- Persisk (fa)
- Finsk (fi)
- Fransk (fr)
- Hindi (hi)
- Italiensk (it)
- Koreansk (ko)
- Hollandsk (nl)
- Norsk (no)
- Polsk (pl)
- Portugisisk (pt)
- Russisk (ru)