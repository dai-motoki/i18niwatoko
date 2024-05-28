# Flerspråklig oversettelse i18niwatoko

i18niwatoko er et AI-verktøy som oversetter fra ethvert språk til ethvert språk.

## Filosofien bak i18niwatoko

Målet er å skape en verden der alle kan nyte programmering, uavhengig av språkbarrierer.

i18niwatoko er et innovativt verktøy som tar tak i utfordringene ved flerspråklig oversettelse. Tidligere flerspråklige oversettelsesverktøy krevde at man jobbet med programmeringsspråk basert på engelsk, noe som utgjorde en stor barriere for ikke-engelsktalende.

Men i18niwatoko er annerledes. Det er et programmeringsspråk som lar deg kjøre systemer på naturlige språk, slik at alle kan programmere på morsmålet sitt. I tillegg har i18niwatoko en funksjon for automatisk oversettelse av japanske meldingsfiler til flere språk. Dette eliminerer behovet for manuell oversettelse og gjør det mulig å effektivt støtte flere språk.

Programmering er ikke bare for de få med spesielle talenter. Ved å fjerne språkbarrierer kan vi la mennesker over hele verden oppleve gleden og mulighetene ved programmering. Det er den høye ambisjonen til i18niwatoko.

La oss sammen med i18niwatoko respektere språkmangfoldet og bruke teknologiens kraft til å knytte mennesker sammen. Gjennom programmering kan mennesker over hele verden utfolde sin kreativitet og skape nye ideer.

## Nødvendige komponenter

- Python 3.x
- niwatoko-biblioteket
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Oppsett

1. Installer niwatoko-biblioteket.

   ```
   pip install --upgrade niwatoko
   ```

2. Konfigurer OpenAI, Anthropic og GCP Vertex AI.

   ```
   # Sett OpenAI API-nøkkel
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Sett Anthropic API-nøkkel
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Konfigurer GCP Vertex AI
   # Hent prosjekt-ID og plassering fra GCP Vertex AI (kontakt Motoki X hvis du er usikker https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Bruk

1. Forbered oversettelsesdefinisjonsfilen (`def_translation.md`).

2. Kjør følgende kommando for å starte oversettelsen. (gemini-1.5-flash er stabil.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Når oversettelsen er ferdig, genereres meldingsfiler for hvert språk.

4. def_translation.md er kravspesifikasjonen. Endre denne filen for å justere kravene.

## Oversatte språk

Prosjektet oversetter til følgende språk:

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
- Nederlandsk (nl)
- Norsk (no)
- Polsk (pl)