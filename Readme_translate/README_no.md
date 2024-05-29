# Flerspråklig oversettelse i18niwatoko

i18niwatoko er et AI-verktøy som oversetter fra ethvert morsmål til alle verdens språk samtidig.
Og programfilene som finnes her er skrevet utelukkende på sine respektive morsmål, uten noe høynivåspråk i det hele tatt, en helt ny programfiltype.

![i18niwatoko](../readme_rich_progress.png)


## i18niwatokos filosofi

Med mål om en verden der alle kan nyte programmering uten språkbarrierer.

i18niwatoko er et innovativt verktøy som tar tak i utfordringene med flerspråklig oversettelse. Tradisjonelle flerspråklige oversettelsesverktøy krever at man håndterer programmeringsspråk basert på engelsk, noe som utgjør en stor barriere for ikke-engelsktalende.

Men i18niwatoko er annerledes. Det er et programmeringsspråk som lar deg kjøre systemer på naturlige språk, slik at alle kan skrive programmer på sitt morsmål. I tillegg har i18niwatoko en funksjon for automatisk oversettelse av japanske meldingsfiler til flere språk. Dette eliminerer behovet for manuell oversettelse og gjør det mulig å effektivt støtte flere språk.

Programmering er ikke bare for de få med spesielle talenter. Ved å fjerne språkbarrierer kan vi la mennesker over hele verden oppleve gleden og mulighetene ved programmering. Det er i18niwatokos høye ideal.

Sammen med i18niwatoko, la oss realisere et samfunn der mennesker over hele verden kan utfolde sin kreativitet og skape nye ideer gjennom programmering, samtidig som vi respekterer språkmangfoldet.

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
   # Hent prosjekt-ID og plassering fra GCP Vertex AI (hvis du glemmer det, kontakt Motoki X på https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Bruk

1. Klargjør oversettelsesdefinisjonsfilen (`def_translation.md`).

2. Kjør følgende kommando for å starte oversettelsen.
   *gemini-1.5-flash er stabil, men generelt sett er naturlige språkprogrammer i en overgangsperiode og grunnleggende ustabile. Prøv det 3 ganger, så bør det stort sett fungere.
   *Forskning på AI-hallusinasjoner og naturlige språkprogrammers grammatikk pågår også, så stabiliteten vil gradvis øke. Hvis du vil kjøre det, anbefaler vi at du redigerer den mellomliggende Python-filen direkte.

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Når overs