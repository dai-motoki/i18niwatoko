# Flerspråkig översättning i18niwatoko

i18niwatoko är ett AI-verktyg som översätter från alla språk till alla språk.

## Filosofin bakom i18niwatoko

Att överbrygga språkbarriärer och göra programmering tillgänglig för alla.

i18niwatoko är ett innovativt verktyg som tar sig an utmaningen med flerspråkig översättning. Tidigare flerspråkiga översättningsverktyg krävde att man hanterade programmeringsspråk baserade på engelska, vilket innebar en hög tröskel för icke-engelsktalande.

Men i18niwatoko är annorlunda. Det är ett programmeringsspråk som kan köras på naturliga språk, så att alla kan skriva program på sitt modersmål. Dessutom har i18niwatoko en funktion för att automatiskt översätta japanska meddelandefiler till flera språk. Detta eliminerar behovet av manuell översättning och gör det möjligt att effektivt hantera flerspråkig support.

Programmering är inte bara för en begränsad grupp med särskilda talanger. Genom att ta bort språkbarriärer kan vi låta människor över hela världen uppleva glädjen och möjligheterna med programmering. Det är den upphöjda visionen bakom i18niwatoko.

Tillsammans med i18niwatoko ska vi respektera språklig mångfald och använda teknikens kraft för att knyta människor samman. Genom programmering kan människor över hela världen uttrycka sin kreativitet och skapa nya idéer.

## Vad du behöver

- Python 3.x
- niwatoko-biblioteket
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Konfiguration

1. Installera niwatoko-biblioteket.

   ```
   pip install --upgrade niwatoko
   ```

2. Konfigurera OpenAI, Anthropic och GCP Vertex AI.

   ```
   # Ställ in OpenAI API-nyckel
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Ställ in Anthropic API-nyckel
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Konfigurera GCP Vertex AI
   # Hämta projekt-ID och plats från GCP Vertex AI (kontakta Motoki X om du är osäker https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Användning

1. Förbered översättningsdefinitionsfilen (`def_translation.md`).

2. Kör följande kommando för att starta översättningen. (gemini-1.5-flash är stabil.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. När översättningen är klar genereras meddelandefiler för varje språk.

4. def_translation.md är kravspecifikationen. Redigera den här filen för att ändra översättningskraven.

## Översättningsspråk

Projektet översätter till följande språk:

- Bengali (bn)
- Kinesiska (zh)
- Danska (da)
- Tyska (de)
- Engelska (en)
- Spanska (es)
- Persiska (fa)
- Finska (fi)
- Franska (fr)
- Hindi (hi)
- Italienska (it)
- Koreanska (ko)
- Nederländska (nl)
- Norska (no