# Wielojęzyczne tłumaczenie i18niwatoko

i18niwatoko to narzędzie AI, które jednocześnie tłumaczy z każdego języka macierzystego na wszystkie inne języki na świecie.
A pliki programowe znajdujące się tutaj są napisane wyłącznie w ich własnych językach macierzystych, bez jakiegokolwiek wysokiego poziomu języka, to całkowicie nowe pliki programowe.

![i18niwatoko](../readme_rich_progress.png)


## Filozofia i18niwatoko

Dążąc do świata, w którym każdy może cieszyć się programowaniem, pokonując bariery językowe.

i18niwatoko to innowacyjne narzędzie, które powstało, aby stawić czoła wyzwaniom związanym z tłumaczeniem wielojęzycznym. Tradycyjne narzędzia do tłumaczenia wielojęzycznego wymagały korzystania z języków programowania opartych na angielskim, co stanowiło dużą barierę dla osób spoza kręgu języka angielskiego.

Ale i18niwatoko jest inny. Jest to język programowania, który pozwala na uruchamianie systemów w językach naturalnych, dzięki czemu każdy może pisać programy w swoim języku ojczystym. Ponadto i18niwatoko posiada funkcję automatycznego tłumaczenia plików komunikatów w języku japońskim na wiele innych języków. Eliminuje to konieczność ręcznego tłumaczenia, umożliwiając efektywne wdrażanie wielojęzyczności.

Programowanie nie jest domeną tylko wyjątkowych talentów. Usuwając bariery językowe, umożliwiamy ludziom na całym świecie doświadczenie radości i możliwości programowania. To wzniosła idea i18niwatoko.

Wraz z i18niwatoko, szanując różnorodność językową, dążymy do stworzenia społeczeństwa, w którym ludzie na całym świecie mogą wykorzystywać swoją kreatywność i generować nowe pomysły poprzez programowanie.

## Wymagania

- Python 3.x
- Biblioteka niwatoko
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Konfiguracja

1. Zainstaluj bibliotekę niwatoko.

   ```
   pip install --upgrade niwatoko
   ```

2. Skonfiguruj ustawienia OpenAI, Anthropic i GCP Vertex AI.

   ```
   # Ustawienie klucza API OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Ustawienie klucza API Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Ustawienia GCP Vertex AI
   # Pobierz identyfikator projektu i lokalizację z GCP Vertex AI (jeśli nie pamiętasz, skontaktuj się z Motoki X https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Użycie

1. Przygotuj plik definicji tłumaczenia (`def_translation.md`).

2. Uruchom następujące polecenie, aby rozpocząć tłumaczenie.
* Gemini-1.5-flash jest stabilny, ale w zasadzie programy w języku naturalnym są w okresie przejściowym i generalnie niestabilne. Jeśli uruchomisz to 3 razy, prawdopodobnie będzie to