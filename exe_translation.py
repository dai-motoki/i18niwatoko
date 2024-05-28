import anthropic
import os
from tqdm import tqdm

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

# 日本語ファイル
japanese_content = """
ja:
  cli_description: "抽象言語 パッケージマネージャー Grimo"
  subcommand_help: "利用可能なサブコマンド"
  search_help: "パッケージを検索する"
  query_help: "検索クエリ"
  language_help: "パッケージの言語"
  category_help: "パッケージのカテゴリ"
  tags_help: "パッケージのタグ"
  install_help: "パッケージをインストールする"
  package_help: "パッケージ名"
  version_help: "パッケージのバージョン"
  force_help: "強制的にインストールする"
  update_help: "パッケージをアップデートする"
  uninstall_help: "パッケージをアンインストールする"
  upload_help: "パッケージをアップロードする"
  package_path_help: "パッケージのパス"
  found_packages: "%{count}個のパッケージが見つかりました"
  no_packages_found: "パッケージが見つかりませんでした"
  install_success: "%{package}のインストールに成功しました"
  install_error: "インストールエラー: %{error}"
  update_success: "%{package}がバージョン%{version}にアップデートされました"
  update_error: "アップデートエラー: %{error}"
  already_up_to_date: "%{package}は既に最新です"
  uninstall_success: "%{package}のアンインストールに成功しました"
  uninstall_error: "アンインストールエラー: %{error}"
"""

# Claude API キー
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

# 翻訳モデル
model = "claude-3-haiku-20240307"

# 翻訳実行
for i, (language_code, language_name) in enumerate(tqdm(languages.items(), desc="翻訳中", unit="言語", bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]")):
    # 翻訳リクエスト
    messages = [
        {
            "role": "user",
            "content": f"{japanese_content}を{language_name}で翻訳"
        }
    ]
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        messages=messages
    )

    # 翻訳結果取得
    translated_text = message.content[0].text

    # 翻訳結果をファイルに出力
    with open(f"message.{language_code}.yml", "w", encoding="utf-8", errors="ignore") as f:
        f.write(translated_text)

    print(f"{language_name}翻訳完了")
