# Mehrsprachige Übersetzung i18niwatoko

i18niwatoko ist ein KI-Tool, das alle Sprachen der Welt aus jeder Muttersprache heraus übersetzt.
Und hier sind alle Programmdateien nur in ihrer jeweiligen Muttersprache geschrieben, es gibt keine einzige Hochsprache, es sind völlig neue Programmdateien.

![i18niwatoko](../readme_rich_progress.png)


## Die Philosophie von i18niwatoko

Mit dem Ziel, die Sprachbarrieren zu überwinden und eine Welt zu schaffen, in der jeder Programmieren genießen kann.

i18niwatoko ist ein innovatives Tool, das sich den Herausforderungen der mehrsprachigen Übersetzung stellt. Herkömmliche mehrsprachige Übersetzungstools erfordern den Umgang mit englischsprachigen Programmiersprachen, was für Nicht-Muttersprachler eine hohe Hürde darstellt.

Aber i18niwatoko ist anders. Es ist eine Programmiersprache, mit der man natürliche Sprachen verwenden kann, so dass jeder in seiner Muttersprache programmieren kann. Darüber hinaus verfügt i18niwatoko über eine Funktion, mit der japanische Nachrichtendateien automatisch in mehrere Sprachen übersetzt werden können. Dadurch wird manuelle Übersetzung überflüssig, und mehrsprachige Unterstützung kann effizient umgesetzt werden.

Programmieren ist nicht nur etwas für eine begabte Minderheit. Indem wir die Sprachbarrieren beseitigen, können Menschen auf der ganzen Welt die Freude und das Potenzial des Programmierens erleben. Das ist die erhabene Vision von i18niwatoko.

Gemeinsam mit i18niwatoko wollen wir eine Welt schaffen, in der die sprachliche Vielfalt respektiert wird und Menschen durch Programmierung ihre Kreativität entfalten und neue Ideen entwickeln können.

## Erforderliche Komponenten

- Python 3.x
- niwatoko-Bibliothek
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Einrichtung

1. Installieren Sie die niwatoko-Bibliothek.

   ```
   pip install --upgrade niwatoko
   ```

2. Konfigurieren Sie OpenAI, Anthropic und GCP Vertex AI.

   ```
   # Setzen Sie den OpenAI-API-Schlüssel
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Setzen Sie den Anthropic-API-Schlüssel
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Konfigurieren Sie GCP Vertex AI
   # Holen Sie sich die Projekt-ID und den Standort von GCP Vertex AI. (Wenn Sie sich nicht sicher sind, wenden Sie sich an Motoki X unter https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```
   
   <!-- Erklärung -->
   <!-- Legen Sie die API-Schlüssel und Projekteinstellungen für OpenAI, Anthropic und GCP Vertex AI als Umgebungsvariablen fest. -->
   <!-- Ersetzen Sie your_openai_api_key, your_anthropic_api_key und your_gcp_project_id durch Ihre tatsächlichen API-Schlüssel und Projekt-IDs. -->
   <!-- GEMINI_LOCATION gibt die GCP Vertex AI-Region an. Hier wird die Region Asien-