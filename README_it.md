# Traduzione multilingue i18niwatoko

i18niwatoko è uno strumento di intelligenza artificiale che traduce simultaneamente da qualsiasi lingua a qualsiasi altra lingua.


## La filosofia di i18niwatoko

Mirando a un mondo in cui chiunque possa divertirsi con la programmazione, superando le barriere linguistiche.

i18niwatoko è uno strumento innovativo nato per affrontare le sfide della traduzione multilingue. Gli strumenti di traduzione multilingue tradizionali richiedevano l'utilizzo di linguaggi di programmazione basati sull'inglese, ponendo un ostacolo per le persone di paesi non anglofoni.

Tuttavia, i18niwatoko è diverso. È un linguaggio di programmazione che consente di far funzionare i sistemi in linguaggio naturale, permettendo a chiunque di scrivere programmi nella propria lingua madre. Inoltre, i18niwatoko è dotato di una funzione che traduce automaticamente i file di messaggi in giapponese in più lingue. Ciò elimina la necessità di traduzione manuale, consentendo un'implementazione multilingue efficiente.

La programmazione non è appannaggio di pochi eletti con talenti speciali. Rimuovere le barriere linguistiche e permettere a tutti nel mondo di sperimentare il divertimento e il potenziale della programmazione. Questa è la nobile filosofia di i18niwatoko.

Insieme a i18niwatoko, rispettiamo la diversità linguistica e utilizziamo la forza della tecnologia per connettere le persone. Attraverso la programmazione, permettiamo a tutti nel mondo di esprimere la propria creatività e generare nuove idee, realizzando una società in cui tutti possano partecipare.

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
   # Ottieni l'ID del progetto GCP Vertex AI e la posizione (non ricordi? Contatta Motoki X https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Utilizzo

1. Prepara il file di definizione della traduzione (`def_translation.md`).

2. Esegui il seguente comando per avviare la traduzione. (gemini-1.5-flash è stabile)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Una volta completata la traduzione, verranno generati i file di messaggi per ciascuna lingua.

4. def_translation.md è il documento di specifica dei requisiti. Modifica questo file per i dettagli.

## Lingue di traduzione

Questo progetto traduce nelle seguenti lingue:

- Bengalese (bn)
- Cinese (zh)
- Danese (da)
- Tedesco (de)
- Inglese (en)
- Spagnolo (es)
- Persiano (fa)
- Finlandese (fi)
- Francese (fr)
- Hindi (hi)
- Italiano (it)