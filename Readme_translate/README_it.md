# Traduzione multilingue i18niwatoko

i18niwatoko è uno strumento di intelligenza artificiale che traduce simultaneamente da qualsiasi lingua madre a tutte le lingue del mondo.
E qui i file di programma esistenti sono tutti scritti solo nella loro lingua madre, senza alcun linguaggio di alto livello, sono file di programma completamente nuovi.

![i18niwatoko](../readme_rich_progress.png)


## Filosofia di i18niwatoko

Mirando a un mondo in cui chiunque possa divertirsi con la programmazione, superando le barriere linguistiche.

i18niwatoko è uno strumento innovativo nato per affrontare la sfida della traduzione multilingue. Gli strumenti di traduzione multilingue tradizionali richiedono di utilizzare linguaggi di programmazione basati sull'inglese, il che rappresenta un ostacolo per le persone di paesi non anglofoni.

Ma i18niwatoko è diverso. È un linguaggio di programmazione che consente di far funzionare i sistemi con linguaggi naturali, permettendo a chiunque di scrivere programmi nella propria lingua madre. Inoltre, i18niwatoko è dotato di una funzione che traduce automaticamente i file di messaggi in giapponese in più lingue. Ciò elimina la necessità di traduzione manuale, consentendo un'implementazione multilingue efficiente.

La programmazione non è appannaggio di pochi talenti speciali. Rimuovere le barriere linguistiche e permettere a tutti nel mondo di sperimentare il divertimento e le possibilità della programmazione. Questa è la nobile filosofia di i18niwatoko.

Insieme a i18niwatoko, per realizzare una società in cui le persone di tutto il mondo possano esprimere la loro creatività e generare nuove idee attraverso la programmazione, rispettando la diversità linguistica.

## Requisiti

- Python 3.x
- Libreria niwatoko
- GCP Vertex AI
- API Anthropic Claude
- API OpenAI

## Configurazione

1. Installa la libreria niwatoko.

   ```
   pip install --upgrade niwatoko
   ```

2. Configura OpenAI, Anthropic e GCP Vertex AI.

   ```
   # Imposta la chiave API di OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Imposta la chiave API di Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Configura GCP Vertex AI
   # Ottieni l'ID del progetto e la posizione da GCP Vertex AI (se non lo ricordi, contatta Motoki X all'indirizzo https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Utilizzo

1. Prepara il file di definizione della traduzione (`def_translation.md`).

2. Esegui il seguente comando per avviare la traduzione.
   *gemini-1.5-flash è stabile, ma i programmi in linguaggio naturale sono in fase di transizione e fondamentalmente instabili. Provando 3 volte, dovrebbe funzionare quasi sicuramente.
   *Anche l'allucinazione dell'IA e la ricerca sulla grammatica dei programmi in linguaggio naturale sono in corso, quindi la stabilità migliorerà gradualmente. Se vuoi eseguirlo, ti consigliamo di modificare direttamente il file Python intermedio.

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Una volta completata la traduzione, verran