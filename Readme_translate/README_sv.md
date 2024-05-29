# Flerspråkig översättning i18niwatoko

i18niwatoko är ett AI-verktyg som översätter från vilket modersmål som helst till alla världens språk.
Och här finns programfilerna som är skrivna enbart på respektive modersmål, det finns inga högre programmeringsspråk alls, helt nya programfilerna.

![i18niwatoko](../readme_rich_progress.png)


## i18niwatokos filosofi

Sträva efter en värld där alla kan njuta av programmering genom att överbrygga språkbarriärer.

i18niwatoko är ett banbrytande verktyg som tar sig an utmaningen med flerspråkig översättning. Tidigare flerspråkiga översättningsverktyg krävde att man hanterade programmeringsspråk baserade på engelska, vilket innebar en hög tröskel för icke-engelsktalande.

Men i18niwatoko är annorlunda. Det är ett programmeringsspråk som kan köra system på naturliga språk, så att alla kan skriva program på sitt modersmål. Dessutom har i18niwatoko en funktion för att automatiskt översätta japanska meddelandefiler till flera språk. Detta gör att manuell översättning blir onödig och att flerspråkig support kan utföras effektivt.

Programmering är inte bara för en begränsad grupp med särskilda talanger. Genom att ta bort språkbarriärer kan människor över hela världen uppleva glädjen och möjligheterna med programmering. Det är i18niwatokos upphöjda vision.

Tillsammans med i18niwatoko, för att förverkliga ett samhälle där människor över hela världen kan uttrycka sin kreativitet och skapa nya idéer genom programmering, samtidigt som vi respekterar språklig mångfald.

## Vad som behövs

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
   # Hämta projekt-ID och plats från GCP Vertex AI (om du glömmer, kontakta Motoki X på https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Användning

1. Förbered översättningsdefinitionsfilen (`def_translation.md`).

2. Kör följande kommando för att starta översättningen.
   *gemini-1.5-flash är stabil, men naturliga språkprogram är fortfarande i övergångsfasen och generellt instabila. Försök 3 gånger, då bör det fungera.
   *Forskning kring AI-hallucinationer och naturliga språkprogram pågår också, så stabiliteten kommer att öka med tiden. Om du vill köra det rekommenderar jag att du redigerar den mellanliggande Python-filen direkt.

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. När översättningen är klar genereras meddelan