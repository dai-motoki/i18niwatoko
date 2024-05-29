# Çok dilli çeviri i18niwatoko

i18niwatoko, her ana dilden dünyanın her ülkesinin diline toplu çeviri yapabilen bir AI aracıdır.
Ve burada bulunan tüm program dosyaları yalnızca kendi ana dillerinde yazılmış olup, hiçbir yüksek seviye dili yoktur, tamamen yeni bir program dosyasıdır.

![i18niwatoko](../readme_rich_progress.png)


## i18niwatoko'nun felsefesi

Dil engellerini aşarak, herkesin programlama yapmasının keyfini çıkarabileceği bir dünya için.

i18niwatoko, çok dilli çeviri sorunuyla mücadele etmek için doğmuş yenilikçi bir araçtır. Geleneksel çok dilli çeviri araçlarında, İngilizce tabanlı programlama dillerini kullanmak gerekiyordu ve bu, İngilizce konuşmayan insanlar için engel teşkil ediyordu.

Ancak i18niwatoko farklı. Doğal dille sistem çalıştırılabilen bir programlama dilidir ve herkes ana dilinde program yazabilir. Ayrıca i18niwatoko, Japonca mesaj dosyalarını toplu olarak birden fazla dile otomatik olarak çeviren bir işleve sahiptir. Bu sayede, elle çeviri yapmaya gerek kalmaz ve verimli bir şekilde çok dilli desteği sağlanabilir.

Programlama, özel yeteneklere sahip bir azınlığın işi değildir. Dil engellerini kaldırarak, dünyadaki herkesin programlamanın keyfini ve potansiyelini deneyimleyebilmesi. İşte i18niwatoko'nun yüce felsefesi budur.

i18niwatoko ile birlikte, dil çeşitliliğine saygı duyarak, programlama yoluyla dünyadaki herkesin yaratıcılığını ortaya çıkarıp, yeni fikirlerin doğmasını sağlayacak bir toplumu gerçekleştirmek için.

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
   
   # GCP Vertex AI ayarlarını yapın
   # GCP Vertex AI'dan proje kimliğini ve konumu alın. (Unuttuysan Motoki X'e başvur https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```
   
   <!-- Açıklama -->
   <!-- OpenAI, Anthropic ve GCP Vertex AI API anahtarlarını ve proje ayarlarını ortam değişkenlerine ayarlıyoruz. -->
   <!-- your_openai_api_key, your_anthropic_api_key, your_gcp_project_id değerlerini gerçek API ana