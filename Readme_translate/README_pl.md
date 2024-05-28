# Wielojęzyczne tłumaczenie i18niwatoko

i18niwatoko to innowacyjne narzędzie AI, które umożliwia tłumaczenie z dowolnego języka na dowolny język.

## Filozofia i18niwatoko

Dążenie do świata, w którym każdy może cieszyć się programowaniem, pokonując bariery językowe.

i18niwatoko powstało, aby zmierzyć się z wyzwaniami związanymi z wielojęzycznym tłumaczeniem. Tradycyjne narzędzia do tłumaczenia wielojęzykowego wymagały korzystania z języków programowania opartych na angielskim, co stanowiło barierę dla osób spoza kręgu języka angielskiego.

Jednak i18niwatoko jest inne. Jest to język programowania, który pozwala na działanie systemów w językach naturalnych, umożliwiając każdemu pisanie programów w swoim ojczystym języku. Ponadto i18niwatoko posiada funkcję automatycznego tłumaczenia plików z komunikatami w języku japońskim na wiele innych języków. Dzięki temu nie ma potrzeby ręcznego tłumaczenia, co pozwala na efektywne wdrażanie wielojęzyczności.

Programowanie nie jest domeną tylko wyjątkowych talentów. Usuwając bariery językowe, chcemy umożliwić ludziom na całym świecie doświadczenie radości i możliwości, jakie niesie ze sobą programowanie. To wzniosła idea przyświecająca i18niwatoko.

Wraz z i18niwatoko, szanując różnorodność językową, łączmy ludzi za pomocą mocy technologii. Poprzez programowanie pozwólmy ludziom na całym świecie na wyrażanie kreatywności i generowanie nowych pomysłów, tworząc społeczeństwo, w którym wszyscy mogą się rozwijać.

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

2. Skonfiguruj ustawienia dla OpenAI, Anthropic i GCP Vertex AI.

   ```
   # Ustaw klucz API OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Ustaw klucz API Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Ustaw ustawienia GCP Vertex AI
   # Pobierz identyfikator projektu i lokalizację z GCP Vertex AI (jeśli nie pamiętasz, skontaktuj się z Motoki X https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Użycie

1. Przygotuj plik definicji tłumaczenia (`def_translation.md`).

2. Uruchom następujące polecenie, aby rozpocząć tłumaczenie. (gemini-1.5-flash jest stabilną wersją.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Po zakończeniu tłumaczenia zostaną wygenerowane pliki z komunikatami w różnych językach.

4. `def_translation.md` to plik specyfikacji wymagań. Możesz go edytować, aby dostosować szczegóły.

##