# Dịch đa ngôn ngữ i18niwatoko

i18niwatoko là một công cụ AI dịch tự động từ ngôn ngữ mẹ đẻ của mỗi người sang tất cả các ngôn ngữ trên thế giới.
Và tất cả các tệp tin chương trình ở đây đều được viết bằng ngôn ngữ mẹ đẻ của mỗi người, không có bất kỳ ngôn ngữ lập trình cấp cao nào, đây là một tệp tin chương trình hoàn toàn mới.

![i18niwatoko](../readme_rich_progress.png)


## Triết lý của i18niwatoko

Hướng tới một thế giới nơi mọi người đều có thể tận hưởng niềm vui lập trình, vượt qua rào cản ngôn ngữ.

i18niwatoko là một công cụ đột phá được sinh ra để đối mặt với thách thức của dịch đa ngôn ngữ. Các công cụ dịch đa ngôn ngữ truyền thống đều dựa trên các ngôn ngữ lập trình dựa trên tiếng Anh, điều này tạo ra rào cản đối với những người không sử dụng tiếng Anh.

Tuy nhiên, i18niwatoko khác biệt. Đây là một ngôn ngữ lập trình cho phép vận hành hệ thống bằng ngôn ngữ tự nhiên, cho phép mọi người viết chương trình bằng ngôn ngữ mẹ đẻ của họ. Hơn nữa, i18niwatoko còn có tính năng tự động dịch các tệp tin thông báng bằng tiếng Nhật sang nhiều ngôn ngữ khác. Điều này giúp loại bỏ nhu cầu dịch thủ công, qua đó thực hiện hỗ trợ đa ngôn ngữ một cách hiệu quả.

Lập trình không phải là đặc quyền của những người có tài năng đặc biệt. Loại bỏ rào cản ngôn ngữ, để mọi người trên thế giới đều có thể trải nghiệm niềm vui và tiềm năng của lập trình. Đó chính là triết lý cao cả của i18niwatoko.

Cùng với i18niwatoko, chúng ta sẽ tôn trọng sự đa dạng ngôn ngữ và thực hiện một xã hội nơi mọi người có thể phát huy sáng tạo và tạo ra những ý tưởng mới thông qua lập trình.

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
   