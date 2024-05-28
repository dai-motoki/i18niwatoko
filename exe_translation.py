import os
import anthropic
from tqdm import tqdm

# 環境変数からAnthropic APIキーを取得
anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")

# Anthropic APIクライアントの初期化
client = anthropic.Anthropic(api_key=anthropic_api_key)

# 日本語ファイルの内容
japanese_content = """
# 多言語翻訳 i18niwatoko

i18niwatokoはあらゆる国の言語からあらゆる国の言語に一斉翻訳するAIツールです。


## i18niwatokoの理念

言語の壁を越えて、誰もがプログラミングを楽しめる世界を目指して。

i18niwatokoは、多言語翻訳の課題に立ち向かうために生まれた革新的なツールです。従来の多言語翻訳ツールでは、英語をベースとしたプログラミング言語を扱う必要があり、非英語圏の人々にとってハードルが高いという問題がありました。

しかし、i18niwatokoは違います。自然言語でシステムを動かすことができるプログラミング言語であり、誰もが母国語でプログラムを書くことができるのです。さらに、i18niwatokoは日本語のメッセージファイルを一括で複数の言語に自動翻訳する機能を備えています。これにより、手作業での翻訳が不要となり、効率的に多言語対応を行うことができます。

プログラミングは特別な才能を持った一部の人だけのものではありません。言語の壁を取り払い、世界中の人々がプログラミングの楽しさと可能性を体験できる。それがi18niwatokoの崇高な理念なのです。

i18niwatokoとともに、言語の多様性を尊重しながら、テクノロジーの力で人々をつなげていきましょう。プログラミングを通じて、世界中の人々が創造性を発揮し、新しいアイデアを生み出せる社会を実現するために。

## 必要なもの

- Python 3.x
- niwatoko ライブラリ
- GCP Vertex AI
- Anthropic Claude API
- OpenAI API

## セットアップ

1. niwatoko ライブラリをインストールします。

   