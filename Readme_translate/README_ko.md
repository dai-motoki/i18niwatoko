# 다국어 번역 i18niwatoko

i18niwatoko는 모든 국가의 언어에서 모든 국가의 언어로 일괄 번역하는 AI 도구입니다.


## i18niwatoko의 이념

언어의 장벽을 넘어 누구나 프로그래밍을 즐길 수 있는 세상을 목표로 합니다.

i18niwatoko는 다국어 번역의 과제에 직면하여 탄생한 혁신적인 도구입니다. 기존의 다국어 번역 도구에서는 영어 기반의 프로그래밍 언어를 다루어야 했기 때문에, 영어권이 아닌 사람들에게는 진입 장벽이 높다는 문제가 있었습니다.

그러나 i18niwatoko는 다릅니다. 자연어로 시스템을 구동할 수 있는 프로그래밍 언어이며, 누구나 모국어로 프로그램을 작성할 수 있습니다. 또한 i18niwatoko는 일본어 메시지 파일을 일괄적으로 여러 언어로 자동 번역하는 기능을 갖추고 있습니다. 이를 통해 수작업 번역이 필요 없어지며, 효율적으로 다국어 대응을 할 수 있습니다.

프로그래밍은 특별한 재능을 가진 일부 사람들만의 것이 아닙니다. 언어의 장벽을 허물고, 전 세계 사람들이 프로그래밍의 즐거움과 가능성을 경험할 수 있게 하는 것. 이것이 i18niwatoko의 숭고한 이념입니다.

i18niwatoko와 함께 언어의 다양성을 존중하면서 기술의 힘으로 사람들을 연결해 나가겠습니다. 프로그래밍을 통해 전 세계 사람들이 창의성을 발휘하고 새로운 아이디어를 만들어낼 수 있는 사회를 실현하기 위해.

## 필요한 것

- Python 3.x
- niwatoko 라이브러리
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## 설치 및 설정

1. niwatoko 라이브러리를 설치합니다.

   ```
   pip install --upgrade niwatoko
   ```

2. OpenAI, Anthropic, GCP Vertex AI 설정을 수행합니다.

   ```
   # OpenAI API 키 설정
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # Anthropic API 키 설정
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # GCP Vertex AI 설정
   # GCP Vertex AI에서 project id와 location을 가져오세요. (모르겠다면 원목X에게 문의해주세요 https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```