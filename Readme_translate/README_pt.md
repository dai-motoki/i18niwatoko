# Tradução multilíngue i18niwatoko

i18niwatoko é uma ferramenta de IA que traduz de qualquer idioma para qualquer idioma.

## Filosofia do i18niwatoko

Visando um mundo onde todos possam desfrutar da programação, superando a barreira do idioma.

O i18niwatoko nasceu para enfrentar o desafio da tradução multilíngue. As ferramentas de tradução multilíngue existentes exigiam o uso de linguagens de programação baseadas no inglês, o que representava um obstáculo para as pessoas de países não anglófonos.

No entanto, o i18niwatoko é diferente. É uma linguagem de programação que permite operar sistemas em linguagem natural, permitindo que todos escrevam programas em seu idioma nativo. Além disso, o i18niwatoko possui a funcionalidade de traduzir automaticamente arquivos de mensagens em japonês para vários outros idiomas. Isso elimina a necessidade de tradução manual, tornando o suporte multilíngue mais eficiente.

A programação não é apenas para uma elite com talentos especiais. Ao remover as barreiras linguísticas, queremos que as pessoas do mundo todo possam experimentar a alegria e o potencial da programação. Essa é a nobre filosofia do i18niwatoko.

Juntos com o i18niwatoko, vamos respeitar a diversidade de idiomas e usar o poder da tecnologia para conectar as pessoas. Através da programação, vamos permitir que as pessoas de todo o mundo expressem sua criatividade e gerem novas ideias, realizando uma sociedade mais inclusiva.

## Requisitos

- Python 3.x
- Biblioteca niwatoko
- GCP Vertex AI
- API Anthropic Claude
- API OpenAI

## Configuração

1. Instale a biblioteca niwatoko.

   ```
   pip install --upgrade niwatoko
   ```

2. Configure a API OpenAI, Anthropic e GCP Vertex AI.

   ```
   # Definir a chave da API OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=sua_chave_api_openai
   
   # Definir a chave da API Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=sua_chave_api_anthropic
   
   # Configurar o GCP Vertex AI
   # Obtenha o ID do projeto e a localização do GCP Vertex AI (se não souber, entre em contato com o Motoki X em https://x.com/ai_syacho)
   export GEMINI_PROJECT=seu_id_projeto_gcp
   export GEMINI_LOCATION=asia-northeast1
   ```

## Uso

1. Prepare o arquivo de definição de tradução (`def_translation.md`).

2. Execute o seguinte comando para iniciar a tradução. (gemini-1.5-flash é a versão mais estável.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Quando a tradução for concluída, os arquivos de mensagem em cada idioma serão gerados.

4. O arquivo def_translation.md é o documento de especificação de requisitos. Modifique-o conforme necessário.

## Idiomas de tradução

Este projeto traduz para os seguintes idiomas:

- Bengali (bn)
- Chinês (zh)
- Dinamarquês (da)
- Alemão (de)
- Inglês (en)
- Espanhol (es)
- Persa (fa)
- Finlandês (fi)
- Francês (fr)
- Hindi (hi)
- Italiano (it)
- Coreano (ko)
- Holandês (nl)
- Norueguês (no)
-