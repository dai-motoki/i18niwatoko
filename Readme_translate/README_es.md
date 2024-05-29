# Traducción multilingüe i18niwatoko

i18niwatoko es una herramienta de IA que traduce simultáneamente de cualquier idioma nativo a todos los idiomas del mundo.
Y los archivos de programa que se encuentran aquí están escritos únicamente en sus respectivos idiomas nativos, sin ningún lenguaje de alto nivel, son archivos de programa completamente nuevos.

![i18niwatoko](../readme_rich_progress.png)


## La filosofía de i18niwatoko

Con el objetivo de crear un mundo donde todos puedan disfrutar de la programación, superando las barreras idiomáticas.

i18niwatoko nació para abordar el desafío de la traducción multilingüe. Las herramientas de traducción multilingüe tradicionales requieren trabajar con lenguajes de programación basados en inglés, lo que supone una barrera importante para las personas que no hablan inglés.

Pero i18niwatoko es diferente. Es un lenguaje de programación que permite ejecutar sistemas en lenguaje natural, lo que permite a cualquier persona escribir programas en su idioma nativo. Además, i18niwatoko cuenta con la función de traducir automáticamente archivos de mensajes en japonés a múltiples idiomas. Esto elimina la necesidad de traducción manual y permite una implementación multilingüe eficiente.

La programación no es solo para unos pocos con talentos especiales. Eliminar las barreras idiomáticas y permitir que las personas de todo el mundo experimenten la alegría y el potencial de la programación. Esa es la noble filosofía de i18niwatoko.

Junto con i18niwatoko, trabajaremos para crear una sociedad en la que se respete la diversidad lingüística y las personas de todo el mundo puedan desarrollar su creatividad y generar nuevas ideas a través de la programación.

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
   # Establecer la clave API de OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Establecer la clave API de Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Configurar GCP Vertex AI
   # Obtén el ID de proyecto y la ubicación de GCP Vertex AI. (Si no lo sabes, comunícate con Motoki X en https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Uso

1. Prepara el archivo de definición de traducción (`def_translation.md`).

2. Ejecuta el siguiente comando para iniciar la traducción.
   * gemini-1.5-flash es estable, pero los programas en lenguaje natural son en general inestables durante el período de transición. Probablemente funcione después de ejecutarlo 3 veces.
   * La alucinación de la IA y la investigación de la gramática de los programas en lenguaje natural también están en curso, por lo que la estabilidad irá aumentando gradualmente. Si quieres que funcione, te recomendamos que modifiques directamente el archivo Python intermedio.

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Una vez completada la traducción, se generarán los archivos de mensajes en cada idioma.

4. def_