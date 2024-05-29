import os
from rich.progress import track
from rich.console import Console
from rich.panel import Panel
import anthropic

# Anthropic APIキーの設定
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

# 翻訳対象言語
languages = [
    "fr",
    "de",
    "en",
    "es",
    "it",
    "pt",
    "ru",
    "zh",
    "ko",
    "ar",
    "hi",
    "bn",
    "fa",
    "tr",
    "vi",
    "th",
    "uk",
    "pl",
    "nl",
    "sv",
    "no",
    "da",
    "fi",
]

# 日本語ファイルの読み込み
with open("./README.md", "r", encoding="utf-8") as f:
    japanese_content = f.read()

# Anthropic APIクライアントの初期化
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# 進捗バーの初期化
console = Console()
progress = track(
    range(len(languages)),
    description="翻訳中:",
    console=console,
    transient=True,
)

# 各言語への翻訳
for i, language in enumerate(languages):
    # 翻訳対象言語名を取得
    language_name = "フランス語"
    if language == "de":
        language_name = "ドイツ語"
    elif language == "en":
        language_name = "英語"
    elif language == "es":
        language_name = "スペイン語"
    elif language == "it":
        language_name = "イタリア語"
    elif language == "pt":
        language_name = "ポルトガル語"
    elif language == "ru":
        language_name = "ロシア語"
    elif language == "zh":
        language_name = "中国語"
    elif language == "ko":
        language_name = "韓国語"
    elif language == "ar":
        language_name = "アラビア語"
    elif language == "hi":
        language_name = "ヒンディー語"
    elif language == "bn":
        language_name = "ベンガル語"
    elif language == "fa":
        language_name = "ペルシャ語"
    elif language == "tr":
        language_name = "トルコ語"
    elif language == "vi":
        language_name = "ベトナム語"
    elif language == "th":
        language_name = "タイ語"
    elif language == "uk":
        language_name = "ウクライナ語"
    elif language == "pl":
        language_name = "ポーランド語"
    elif language == "nl":
        language_name = "オランダ語"
    elif language == "sv":
        language_name = "スウェーデン語"
    elif language == "no":
        language_name = "ノルウェー語"
    elif language == "da":
        language_name = "デンマーク語"
    elif language == "fi":
        language_name = "フィンランド語"

    # Claude3を用いて翻訳
    model = "claude-3-haiku-20240307"
    messages = [
        {
            "role": "user",
            "content": f"{japanese_content}を{language_name}で翻訳",
        }
    ]

    message = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        messages=messages,
    )
    translated_text = message.content[0].text

    # 翻訳結果をファイルに出力
    with open(f"Readme_translate/README_{language}.md", "w", encoding="utf-8") as f:
        f.write(translated_text)

    # 進捗バーの更新
    progress.update(i, description=f"翻訳中: {language_name}翻訳完了")
    progress.refresh()
