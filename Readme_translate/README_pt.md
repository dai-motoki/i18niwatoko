# Tradução multilíngue i18niwatoko

i18niwatoko é uma ferramenta de IA que traduz simultaneamente de qualquer idioma nativo para todas as línguas do mundo.
E os arquivos de programa aqui existentes são todos escritos apenas em seus respectivos idiomas nativos, sem nenhuma linguagem de alto nível, sendo arquivos de programa completamente novos.

![i18niwatoko](../readme_rich_progress.png)


## Filosofia do i18niwatoko

Visando um mundo onde todos possam desfrutar da programação, superando a barreira do idioma.

O i18niwatoko nasceu para enfrentar o desafio da tradução multilíngue. As ferramentas de tradução multilíngue convencionais exigiam o uso de linguagens de programação baseadas no inglês, o que representava um obstáculo para as pessoas de países não anglófonos.

Mas o i18niwatoko é diferente. É uma linguagem de programação que permite operar sistemas em linguagem natural, onde qualquer pessoa pode escrever programas em seu idioma nativo. Além disso, o i18niwatoko possui a funcionalidade de traduzir automaticamente arquivos de mensagens em japonês para vários outros idiomas. Isso elimina a necessidade de tradução manual, permitindo uma abordagem eficiente para o suporte multilíngue.

A programação não é algo reservado apenas a uma elite com talentos especiais. Remover as barreiras linguísticas e permitir que pessoas de todo o mundo experimentem o prazer e o potencial da programação. Essa é a nobre filosofia do i18niwatoko.

Junto com o i18niwatoko, buscamos realizar uma sociedade onde a diversidade linguística é respeitada e as pessoas de todo o mundo possam expressar sua criatividade e gerar novas ideias por meio da programação.

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
   # Obtenha o ID do projeto e a localização do GCP Vertex AI. (Se você não souber, entre em contato com Motoki X https://x.com/ai_syacho)
   export GEMINI_PROJECT=seu_id_projeto_gcp
   export GEMINI_LOCATION=asia-northeast1
   ```

## Uso

1. Prepare o arquivo de definição de tradução (`def_translation.md`).

2. Execute o seguinte comando para iniciar a tradução.
   *gemini-1.5-flash é estável, mas os programas em linguagem natural são essencialmente instáveis durante o período de transição. Executá-lo cerca de 3 vezes deve fazê-lo funcionar com quase certeza.
   *A alucinação da IA e a pesquisa da gramática de programas em linguagem natural também estão em andamento, então a estabilidade deve melhorar gradualmente. Se você quiser executá-lo, recomendamos editar diretamente o arquivo Python intermediário.

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Quando a tradução for concluída, os arquivos de mensagem em cada idioma serão gerados.

4.