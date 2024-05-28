# Meertalige vertaling i18niwatoko

i18niwatoko is een AI-tool die in staat is om automatisch te vertalen tussen alle talen ter wereld.

## Filosofie van i18niwatoko

Met als doel een wereld waarin iedereen kan genieten van programmeren, ongeacht de taalbarrière.

i18niwatoko is een innovatieve tool die zich richt op de uitdaging van meertalige vertaling. Traditionele meertalige vertaaltools vereisen het gebruik van op Engels gebaseerde programmeertalen, wat een grote drempel vormt voor niet-Engelstaligen.

Maar i18niwatoko is anders. Het is een programmeertaal waarin natuurlijke taal kan worden gebruikt, waardoor iedereen in zijn of haar moedertaal kan programmeren. Bovendien heeft i18niwatoko de functie om Japanse berichtbestanden automatisch te vertalen naar meerdere talen. Hierdoor is handmatige vertaling niet meer nodig en kan meertalige ondersteuning efficiënt worden gerealiseerd.

Programmeren is niet alleen voor een select groepje met bijzonder talent. Door taalbarrières weg te nemen, kunnen mensen over de hele wereld de vreugde en mogelijkheden van programmeren ervaren. Dat is de verheven filosofie van i18niwatoko.

Samen met i18niwatoko zullen we de diversiteit van talen respecteren en de kracht van technologie gebruiken om mensen met elkaar te verbinden. Door middel van programmeren kunnen mensen over de hele wereld hun creativiteit uiten en nieuwe ideeën genereren.

## Vereisten

- Python 3.x
- niwatoko-bibliotheek
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Installatie

1. Installeer de niwatoko-bibliotheek.

   ```
   pip install --upgrade niwatoko
   ```

2. Configureer OpenAI, Anthropic en GCP Vertex AI.

   ```
   # Stel de OpenAI API-sleutel in
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Stel de Anthropic API-sleutel in
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Configureer GCP Vertex AI
   # Haal het project-ID en de locatie op uit GCP Vertex AI (neem contact op met Motoki X als u het niet meer weet https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Gebruik

1. Maak het vertaaldefinitiebestand (`def_translation.md`) klaar.

2. Voer de volgende opdracht uit om de vertaling te starten. (gemini-1.5-flash is stabiel.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Wanneer de vertaling is voltooid, worden de berichtbestanden voor elke taal gegenereerd.

4. def_translation.md is het vereistendocument. Pas deze file aan als u de details wilt wijzigen.

## Ondersteunde talen

Dit project ondersteunt vertaling naar de volgende talen:

- Bengaals (bn)
- Chinees (zh)
- Deens (da)
- Duits (de)
- Engels (en)
- Engels (en)
- Spaans (es)
- Perzisch (fa)
- Fins (fi)
- Frans (fr)
- Hindi (hi)
- Italiaans (it)
- Koreaans (ko)
- Nederlands (nl)
- Noors (no)