# Traducción multilingüe i18niwatoko

i18niwatoko es una herramienta de IA que traduce de cualquier idioma a cualquier idioma.

## Filosofía de i18niwatoko

Aspiramos a un mundo donde todos puedan disfrutar de la programación, superando las barreras lingüísticas.

i18niwatoko nació para abordar el desafío de la traducción multilingüe. Las herramientas de traducción multilingüe tradicionales requerían trabajar con lenguajes de programación basados en inglés, lo que suponía una barrera importante para las personas de países no angloparlantes.

Sin embargo, i18niwatoko es diferente. Es un lenguaje de programación que permite ejecutar sistemas en lenguaje natural, lo que permite a cualquiera escribir programas en su idioma materno. Además, i18niwatoko tiene la capacidad de traducir automáticamente archivos de mensajes en japonés a múltiples idiomas. Esto elimina la necesidad de traducción manual y permite una implementación eficiente de la compatibilidad multilingüe.

La programación no es solo para unos pocos con talentos especiales. Eliminando las barreras lingüísticas, queremos que las personas de todo el mundo puedan experimentar la alegría y el potencial de la programación. Esta es la noble filosofía de i18niwatoko.

Junto con i18niwatoko, respetemos la diversidad lingüística y utilicemos el poder de la tecnología para conectar a las personas. A través de la programación, permitamos que las personas de todo el mundo expresen su creatividad y generen nuevas ideas.

## Requisitos

- Python 3.x
- Biblioteca niwatoko
- GCP Vertex AI
- API de Anthropic Claude
- API de OpenAI

## Configuración

1. Instala la biblioteca niwatoko.

   ```
   pip install --upgrade niwatoko
   ```

2. Configura OpenAI, Anthropic y GCP Vertex AI.

   ```
   # Establecer la clave de API de OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Establecer la clave de API de Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Configurar GCP Vertex AI
   # Obtén el ID de proyecto y la ubicación de GCP Vertex AI. (Si no lo recuerdas, comunícate con Motoki X https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Uso

1. Prepara el archivo de definición de traducción (`def_translation.md`).

2. Ejecuta el siguiente comando para iniciar la traducción. (gemini-1.5-flash es estable).

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Una vez completada la traducción, se generarán los archivos de mensajes en cada idioma.

4. def_translation.md es el documento de especificación de requisitos. Modifícalo según sea necesario.

## Idiomas de traducción

Este proyecto traduce a los siguientes idiomas:

- Bengalí (bn)
- Chino (zh)
- Danés (da)
- Alemán (de)
- Inglés (en)
- Español (es)
- Persa (fa)
- Finlandés (fi)
- Francés (fr)
- Hindi (hi)
- Italiano (it)
- Coreano (ko)
- Holandés (nl)
- Noruego (no)
- Polaco (pl)
-