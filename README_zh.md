# 多语种翻译 i18niwatoko

i18niwatoko是一个AI工具,可以在各种语言之间进行全面翻译。

## i18niwatoko的理念

旨在跨越语言障碍,让所有人都能享受编程的乐趣。

i18niwatoko是为解决多语种翻译问题而诞生的创新性工具。传统的多语种翻译工具需要以英语为基础的编程语言,这对于非英语国家的人来说存在很高的门槛。

但是,i18niwatoko不同。它是一种可以用自然语言驱动系统的编程语言,任何人都可以用母语编写程序。此外,i18niwatoko还具有将日语消息文件批量自动翻译成多种语言的功能。这样就不需要手工翻译,可以更有效地实现多语种支持。

编程并不是只有少数有特殊才能的人才能做的事情。消除语言障碍,让世界各地的人都能体验编程的乐趣和可能性。这就是i18niwatoko崇高的理念。

让我们与i18niwatoko一起,在尊重语言多样性的同时,利用技术的力量来连接人们。通过编程,让世界各地的人都能发挥创造力,产生新的想法,实现一个更美好的社会。

## 所需条件

- Python 3.x
- niwatoko 库
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## 设置

1. 安装niwatoko库。

   ```
   pip install --upgrade niwatoko
   ```

2. 配置OpenAI、Anthropic和GCP Vertex AI。

   ```
   # 设置OpenAI API密钥
   # https://platform.openai.com/api-keys
   export OPENAI_API_KEY=your_openai_api_key
   
   # 设置Anthropic API密钥
   # https://console.anthropic.com/settings/keys
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   
   # 设置GCP Vertex AI
   # 从GCP Vertex AI获取project id和location。(如果忘记了,请联系元木X https://x.com/ai_syacho)
   export GEMINI_PROJECT=your_gcp_project_id
   export GEMINI_LOCATION=asia-northeast1
   ```

## 使用方法

1. 准备翻译定义文件(`def_translation.md`)。

2. 运行以下命令开始翻译。(gemini-1.5-flash版本比较稳定)

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. 翻译完成后,会生成各种语言的消息文件。

4. def_translation.md是需求定义文件,可以根据需要修改。

## 翻译语言

本项目支持以下语言的翻译:

- 孟加拉语(bn)
- 中文(zh)
- 丹麦语(da)
- 德语(de)
- 英语(en)
- 西班牙语(es)
- 波斯语(fa)
- 芬兰语(fi)
- 法语(fr)
- 印地语(hi)
- 意大利语(it)
- 韩语(ko)
- 荷兰语(nl)