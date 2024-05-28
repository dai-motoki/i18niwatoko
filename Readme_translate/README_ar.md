# متعدد اللغات الترجمة i18niwatoko

i18niwatoko هو أداة AI للترجمة الفورية من وإلى جميع لغات العالم.

## فلسفة i18niwatoko

نهدف إلى عالم حيث يستطيع الجميع الاستمتاع بالبرمجة بغض النظر عن اللغة.

ولد i18niwatoko لمواجهة تحديات الترجمة متعددة اللغات. كانت الأدوات التقليدية للترجمة متعددة اللغات تتطلب التعامل مع لغات البرمجة القائمة على اللغة الإنجليزية، مما يشكل عقبة كبيرة أمام غير الناطقين بالإنجليزية.

ولكن i18niwatoko مختلف. إنه لغة برمجة تعمل باللغات الطبيعية، مما يتيح لجميع الناس كتابة البرامج بلغتهم الأم. بالإضافة إلى ذلك، يتميز i18niwatoko بوظيفة الترجمة الآلية لملفات الرسائل باللغة اليابانية إلى العديد من اللغات الأخرى. وهذا يجعل من غير الضروري الترجمة اليدوية، مما يؤدي إلى دعم متعدد اللغات بكفاءة.

البرمجة ليست حكرًا على أصحاب المواهب الخاصة. إزالة حاجز اللغة وتمكين جميع الناس في جميع أنحاء العالم من تجربة متعة البرمجة وإمكاناتها. هذه هي الفلسفة السامية لـ i18niwatoko.

انضم إلينا في i18niwatoko لربط الناس من خلال قوة التكنولوجيا، مع احترام التنوع اللغوي. لتحقيق مجتمع يمكن فيه للجميع التعبير عن إبداعهم وإنشاء أفكار جديدة من خلال البرمجة.

## المتطلبات

- Python 3.x
- مكتبة niwatoko
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## الإعداد

1. قم بتثبيت مكتبة niwatoko.

   ```
   pip install --upgrade niwatoko
   ```

2. قم بتكوين OpenAI و Anthropic و GCP Vertex AI.

   ```
   # تعيين مفتاح API OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # تعيين مفتاح API Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # تكوين GCP Vertex AI
   # احصل على معرف المشروع وموقع GCP Vertex AI (إذا نسيت، اتصل بـ Motoki X https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## الاستخد