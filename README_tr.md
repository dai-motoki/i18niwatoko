# Çok Dilli Çeviri i18niwatoko

i18niwatoko, dünyanın her dilinden dünyanın her diline toplu çeviri yapabilen bir AI aracıdır.

## i18niwatoko'nun Felsefesi

Dil engellerini aşarak, herkesin programlama yapmasını sağlamak.

i18niwatoko, çok dilli çeviri sorunuyla mücadele etmek için doğmuş yenilikçi bir araçtır. Geleneksel çok dilli çeviri araçlarında, İngilizce tabanlı programlama dillerini kullanmak gerekiyordu ve bu, İngilizce konuşmayanlar için engel teşkil ediyordu.

Ancak i18niwatoko farklıdır. Doğal dilde sistem çalıştırılabilen bir programlama dilidir ve herkes ana dilinde program yazabilir. Ayrıca i18niwatoko, Japonca mesaj dosyalarını toplu olarak birden fazla dile otomatik olarak çeviren bir işleve sahiptir. Bu sayede, elle çeviri yapmaya gerek kalmaz ve çok dilli desteği verimli bir şekilde sağlanabilir.

Programlama, özel yeteneklere sahip bir azınlığın işi değildir. Dil engellerini kaldırarak, dünyadaki herkesin programlamanın keyfini ve potansiyelini deneyimlemesini sağlamak, i18niwatoko'nun yüce amacıdır.

i18niwatoko ile birlikte, dil çeşitliliğine saygı göstererek, teknolojinin gücüyle insanları birbirine bağlayalım. Programlama yoluyla, dünyadaki herkesin yaratıcılığını sergileyebileceği ve yeni fikirler üretebileceği bir toplumu gerçekleştirmek için.

## Gereksinimler

- Python 3.x
- niwatoko kütüphanesi
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Kurulum

1. niwatoko kütüphanesini yükleyin.

   ```
   pip install --upgrade niwatoko
   ```

2. OpenAI, Anthropic ve GCP Vertex AI ayarlarını yapın.

   ```
   # OpenAI API anahtarını ayarlayın
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Anthropic API anahtarını ayarlayın
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # GCP Vertex AI'ı ayarlayın
   # GCP Vertex AI'dan proje kimliğini ve konumu alın. (Unuttuysan Motoki X'e başvur https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## Kullanım

1. Çeviri tanım dosyası (`def_translation.md`) hazırlayın.

2. Aşağıdaki komutu çalıştırarak çeviriye başlayın. (gemini-1.5-flash kararlıdır.)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. Çeviri tamamlandığında, her dil için mesaj dosyaları oluşturulur.

4. def_translation.md, gereksinimleri tanımlar. Ayrıntı