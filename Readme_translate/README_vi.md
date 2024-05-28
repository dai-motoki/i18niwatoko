# Dịch đa ngôn ngữ i18niwatoko

i18niwatoko là một công cụ AI dịch tự động từ bất kỳ ngôn ngữ nào sang bất kỳ ngôn ngữ nào khác.

## Triết lý của i18niwatoko

Hướng tới một thế giới nơi mọi người đều có thể tận hưởng niềm vui lập trình, vượt qua rào cản ngôn ngữ.

i18niwatoko là một công cụ đột phá được tạo ra để giải quyết vấn đề dịch đa ngôn ngữ. Các công cụ dịch đa ngôn ngữ truyền thống yêu cầu sử dụng các ngôn ngữ lập trình dựa trên tiếng Anh, điều này tạo ra rào cản đối với những người không sử dụng tiếng Anh làm ngôn ngữ chính.

Tuy nhiên, i18niwatoko khác biệt. Đây là một ngôn ngữ lập trình cho phép chạy hệ thống bằng ngôn ngữ tự nhiên, cho phép mọi người viết chương trình bằng ngôn ngữ mẹ đẻ của họ. Hơn nữa, i18niwatoko còn có tính năng tự động dịch các tệp tin thông báo bằng tiếng Nhật sang nhiều ngôn ngữ khác. Điều này loại bỏ nhu cầu phải dịch thủ công, giúp triển khai đa ngôn ngữ một cách hiệu quả.

Lập trình không phải là đặc quyền của những người có tài năng đặc biệt. Loại bỏ rào cản ngôn ngữ, để mọi người trên thế giới có thể trải nghiệm niềm vui và tiềm năng của lập trình. Đó là triết lý cao cả của i18niwatoko.

Cùng với i18niwatoko, hãy tôn trọng sự đa dạng ngôn ngữ và sử dụng sức mạnh của công nghệ để kết nối mọi người. Thông qua lập trình, chúng ta có thể hiện thực hóa một xã hội nơi mọi người trên thế giới đều có thể phát huy sáng tạo và tạo ra những ý tưởng mới.

## Yêu cầu

- Python 3.x
- Thư viện niwatoko
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## Cài đặt

1. Cài đặt thư viện niwatoko.

   ```
   pip install --upgrade niwatoko
   ```

2. Thiết lập cấu hình cho OpenAI, Anthropic và GCP Vertex AI.

   ```
   # Thiết lập API key của OpenAI
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Thiết lập API key của Anthropic
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # Thiết lập GCP Vertex AI
   # Lấy project id và location từ GCP Vertex AI (nếu không nhớ, hãy liên hệ với Motoki X tại https://x.com