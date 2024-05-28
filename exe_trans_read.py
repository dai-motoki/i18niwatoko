import os
import anthropic
from tqdm import tqdm

# Anthropic APIキーを設定
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

# 翻訳言語集
languages = {
    "fr": "フランス語",
    "de": "ドイツ語",
    "en": "英語",
    "es": "スペイン語",
    "it": "イタリア語",
    "pt": "ポルトガル語",
    "ru": "ロシア語",
    "zh": "中国語",
    "ko": "韓国語",
    "ar": "アラビア語",
    "hi": "ヒンディー語",
    "bn": "ベンガル語",
    "fa": "ペルシャ語",
    "tr": "トルコ語",
    "vi": "ベトナム語",
    "th": "タイ語",
    "uk": "ウクライナ語",
    "pl": "ポーランド語",
    "nl": "オランダ語",
    "sv": "スウェーデン語",
    "no": "ノルウェー語",
    "da": "デンマーク語",
    "fi": "フィンランド語",
}

# 日本語ファイルを読み込む
with open("./README.md", "r", encoding="utf-8") as f:
    japanese_content = f.read()

# 翻訳開始
for i, (language_code, language_name) in enumerate(tqdm(languages.items(), desc="翻訳中: ", unit="言語")):
    # Claude3 実行
    model = "claude-3-haiku-20240307"  # モデル名を変更してください
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": f"{japanese_content}を{language_name}で翻訳"
            }
        ]
    )
    translated_text = message.content[0].text

    # 翻訳結果をファイルに出力
    output_filename = f"README_{language_code}.md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(translated_text)

    # プログレスバーの更新
    tqdm.write(f"{language_name}翻訳完了")
