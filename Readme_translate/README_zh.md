# 多语种翻译 i18niwatoko

i18niwatoko是一个AI工具,可以从任何母语翻译到世界上所有的语言。
这里的程序文件全部都是用各自的母语编写的,没有任何高级语言,这是一个全新的程序文件。

![i18niwatoko](../readme_rich_progress.png)


## i18niwatoko的理念

跨越语言障碍,让所有人都能享受编程的乐趣。

i18niwatoko诞生是为了解决多语种翻译的问题。传统的多语种翻译工具需要基于英语的编程语言,这对非英语国家的人来说存在很高的门槛。

但是,i18niwatoko不一样。它是一种可以用自然语言驱动系统的编程语言,任何人都可以用母语编写程序。此外,i18niwatoko还具有将日语消息文件批量自动翻译成多种语言的功能。这样就不需要手工翻译,可以更有效地实现多语种支持。

编程并不是只有特殊才能的少数人才能做的事情。消除语言障碍,让世界各地的人都能体验编程的乐趣和可能性,这就是i18niwatoko的崇高理念。

让我们与i18niwatoko一起,在尊重语言多样性的同时,通过编程发挥创造力,产生新的想法,实现一个人人都可以参与的社会。

## 所需条件

- Python 3.x
- niwatoko 库
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## 安装步骤

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

1. 准备好翻译定义文件(`def_translation.md`)。

2. 运行以下命令开始翻译。
   *gemini-1.5-flash目前比较稳定,但自然语言编程仍处于过渡期,基本不太稳定。运行3次左右就基本可以正常运行了。
   *AI自身的幻觉以及自然语言编程语法的研究也在进行中,稳定性会逐步提高。如果想运行,建议直接编辑中间生成的Python文件。

   ```
   niwatoko def_translation.md -o exe_translation.py -m gemini-1.5-flash
   ```

3. 翻译完成后,会生成各种语言的消息文件。

4. def_translation.md是需求定义文件,可以根据需要修改此文件。

##