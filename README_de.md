# Mehrsprachige Übersetzung i18niwatoko

i18niwatoko ist ein KI-Tool, das Übersetzungen von jeder Sprache in jede andere Sprache ermöglicht.

## Die Vision von i18niwatoko

Wir streben eine Welt an, in der jeder Programmieren genießen kann, indem wir Sprachbarrieren überwinden.

i18niwatoko ist ein innovatives Tool, das sich den Herausforderungen der mehrsprachigen Übersetzung stellt. Bisherige mehrsprachige Übersetzungstools erforderten den Umgang mit Programmiersprachen, die auf Englisch basieren, was für Nicht-Muttersprachler eine hohe Hürde darstellte.

Aber i18niwatoko ist anders. Es ist eine Programmiersprache, mit der man Systeme in natürlicher Sprache betreiben kann, sodass jeder in seiner Muttersprache programmieren kann. Darüber hinaus bietet i18niwatoko die Funktion, Japanisch-Sprachdateien automatisch in mehrere Sprachen zu übersetzen. Dadurch wird manuelle Übersetzung überflüssig, und mehrsprachige Unterstützung kann effizient umgesetzt werden.

Programmieren ist nicht nur etwas für eine begabte Minderheit. Indem wir Sprachbarrieren beseitigen, können Menschen auf der ganzen Welt die Freude und Möglichkeiten des Programmierens erleben. Das ist die erhabene Vision von i18niwatoko.

Lassen Sie uns gemeinsam mit i18niwatoko die sprachliche Vielfalt respektieren und die Kraft der Technologie nutzen, um Menschen miteinander zu verbinden. Durch Programmieren sollen Menschen auf der ganzen Welt ihre Kreativität entfalten und neue Ideen hervorbringen können.

## Erforderliche Komponenten

- Python 3.x
- niwatoko-Bibliothek
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Setup

1. Installieren Sie die niwatoko-Bibliothek.

   ```
   pip install --upgrade niwatoko
   ```

2. Konfigurieren Sie OpenAI, Anthropic und GCP Vertex AI.

   ```
   # OpenAI-API-Schlüssel setzen
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Anthropic-API-Schlüssel setzen
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # GCP Vertex AI konfigurieren
   # Holen Sie sich die Projekt-ID und den Standort von GCP Vertex AI. (Wenn Sie sich nicht sicher sind, kontaktieren Sie bitte Motoki X unter https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Verwendung

1. Erstellen Sie eine Übersetzungsdefinitionsdatei (`def_translation.md`).

2. Führen Sie den folgenden Befehl aus, um die Übersetzung zu starten. (gemini-1.5-flash ist stabil.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Nach Abschluss der Übersetzung werden die Sprachdateien für jede Sprache generiert.

4. Die Datei `def_translation.md` ist die Anforderungsspezifikation. Bitte passen Sie diese Datei an, um die Details anzupassen.

## Übersetzungssprachen

Dieses