# Meertalige vertaling i18niwatoko

i18niwatoko is een AI-tool die automatisch vertaalt naar alle talen vanuit elke moedertaal.
En de programmabestanden die hier aanwezig zijn, zijn allemaal geschreven in slechts één moedertaal, zonder enige hogere programmeertaal. Het is een volledig nieuw programmabestand.

![i18niwatoko](../readme_rich_progress.png)


## Filosofie van i18niwatoko

Met als doel een wereld waarin iedereen kan genieten van programmeren, ongeacht de taalbarrière.

i18niwatoko is een innovatief hulpmiddel dat de uitdaging van meertalige vertaling aanpakt. Traditionele meertalige vertaalhulpmiddelen vereisen het gebruik van op Engels gebaseerde programmeertalen, wat een drempel vormt voor niet-Engelstaligen.

Maar i18niwatoko is anders. Het is een programmeertaal waarin natuurlijke taal kan worden gebruikt, zodat iedereen in zijn moedertaal kan programmeren. Bovendien heeft i18niwatoko de functie om Japanse berichtbestanden automatisch te vertalen naar meerdere talen. Hierdoor is handmatige vertaling niet meer nodig en kan meertalige ondersteuning efficiënt worden gerealiseerd.

Programmeren is niet alleen voor een select groepje met bijzondere talenten. Door taalbarrières weg te nemen, kunnen mensen over de hele wereld de vreugde en mogelijkheden van programmeren ervaren. Dat is de verheven filosofie van i18niwatoko.

Samen met i18niwatoko, met respect voor de diversiteit aan talen, willen we een samenleving realiseren waarin mensen over de hele wereld hun creativiteit kunnen ontplooien en nieuwe ideeën kunnen genereren via programmeren.

## Benodigdheden

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

2. Voer de volgende opdracht uit om de vertaling te starten.
* gemini-1.5-flash is stabiel, maar natuurlijke taal programma's zijn in een overgangsfase en over het algemeen instabiel. Als u het drie keer uitvoert, zal het vrijwel zeker werken.
* Onderzoek naar hallucinatie van AI en grammatica van natuurlijke taal programma's is ook gaande, dus de stabiliteit zal geleidelijk toenemen. Als u het wilt laten werken, raden we u aan om rechtstreeks te werken met het tussenliggende Python-bestand.

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Wann