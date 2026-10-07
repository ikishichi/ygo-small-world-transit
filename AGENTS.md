# AGENTS.md

This file provides guidance to AI when working with code in this repository.

## プロジェクト概要

遊戯王の《スモール・ワールド》のサーチ経路を、遊戯王DBの公開デッキURLから検索するStreamlitアプリ。本番は [ygo-small-world-transit.streamlit.app](https://ygo-small-world-transit.streamlit.app) にデプロイされている。

## よく使うコマンド

```bash
# 依存関係のインストール
pip install -r requirements.txt

# ローカル起動（プロジェクトルートで実行）
streamlit run ./src/ui.py

# テスト実行（プロジェクトルートで実行。src.* 形式で import しているため CWD 依存）
pytest

# 単一テストファイル / 単一テスト
pytest test/html_parser_test.py
pytest test/html_parser_test.py::TestHtmlParser::test_get_deck_name_normal
```

## 実行パス上の落とし穴

- `src/` 配下のモジュール同士は相対 import ではなく裸の import（例：`from deck import Deck`）を使っている。`streamlit run ./src/ui.py` やスクリプトを直接実行する `python src/deck.py` では `src/` が sys.path に追加される。一方、**プロジェクトルートから `python -m src.deck` のようにモジュールとして実行すると、裸の import を解決できず ImportError になる**。UI の起動には Streamlit のコマンドを使用する。
- 一方、`test/` 配下のテストは `from src.deck_info import DeckInfo` のように `src.` プレフィックス付きで import している。**pytest はプロジェクトルートから実行する必要がある**（`test/` に `cd` してから実行すると解決しない）。
- 実行経路とテスト経路で import 形式が非対称な点に注意すること。モジュール名の変更や新規モジュール追加時は両方の経路で確認する。

## アーキテクチャ

アプリは 6 モジュールで構成され、それぞれ単一責務を持つ。データの流れは基本的に一方向：

```
ui.py (Streamlit)
  ├─ url_resolver                       → クエリパラメータからURLを構築し、取得URLを選択
  ├─ DeckInfo(url).fetch_html()          → 遊戯王DBからHTML取得 (requests)
  ├─ Deck(html).parse_html()             → HtmlParser でモンスター情報を抽出し DataFrame 化
  │    └─ HtmlParser                     → BeautifulSoup(lxml) で detailtext_main を解析
  └─ SearchResult(df, origin, dest).get() → pandas ベースでサーチ経路を算出
```

- [src/ui.py](src/ui.py): Streamlit UI、クエリパラメータによるブックマーク対応、例外→画面エラー表示の責務。`session_state` に `MONSTERS_DF` と `SEARCH_RESULTS` を保持する。
- [src/deck_info.py](src/deck_info.py): HTTP 取得のみ。`raise_for_status()` で失敗を例外化。
- [src/deck.py](src/deck.py): HtmlParser の結果を pandas.DataFrame 化する薄いラッパー。
- [src/html_parser.py](src/html_parser.py): 遊戯王DB の HTML 構造（`detailtext_main` → `t_body mlist_m` → `t_row c_normal`、`card_name` / `box_card_attribute` / `box_card_level_rank level` / `card_info_species_and_other_item` / `atk_power` / `def_power`）に強く依存している。**遊戯王DBの HTML 構造変更がこのプロジェクトの最大の破壊要因**。`generate_monsters()` で発生した `AttributeError` は `AttributeError("デッキの読み込みに失敗しました")` に変換される。`get_deck_name()` で必要な meta タグや content 属性が見つからない場合は、デッキ名取得に失敗した旨の `AttributeError` をそのまま送出する。
- [src/search_result.py](src/search_result.py): 《スモール・ワールド》のロジックの本体。モンスター属性 6 項目（name, attribute, type, level, attack, defence）のうち**ちょうど 1 項目だけが一致する**組を「経由可能」と判定する二重ループ。origin → transit → dest の 2 ホップで全経路を列挙し DataFrame で返す。
- [src/url_resolver.py](src/url_resolver.py): デッキ識別用クエリパラメータの有無を判定し、遊戯王DBのURLを構築する。デッキ取得ボタン押下時は入力URL、それ以外はクエリパラメータから構築したURLを選択する。

## 遊戯王DB の URL 仕様

- 有効な URL プレフィックスは `http://www.db.yugioh-card.com/yugiohdb/member_deck.action` / `https://...` の 2 種のみ。[ui.py](src/ui.py) の `VALID_PREFIX_HTTP` / `VALID_PREFIX_HTTPS` で検査している。
- クエリパラメータ `cgid` と `dno` でデッキを一意特定。`request_locale` 未指定時は `ja` にフォールバック。UI はこのクエリパラメータを自身の URL にコピーして「ブックマーク共有」を実現している。

## テストの方針

- 外部 HTTP は `pytest-mock` の `mocker.patch("requests.get", ...)` でモック。
- HtmlParser のテストはインラインの HTML 文字列をパラメタライズして渡す（実際の遊戯王DB のフィクスチャは持たない）。新しい構造変更に追従する際はこのデータを更新する。

## コーディング規約

- Python 公式スタイルガイドに従う（docs/ygo-small-world-transit.md で明記）。
- ログは `logging` モジュールを使用（`print` は使わない）。

## レビュー

- 仕様・既存レビュースレッドを確認し、全変更ファイル・全差分と必要な関連コードを読む。
- 解決可能な既存レビュースレッドは解決済みにする。
- 正常系・異常系・境界値・既存動作への回帰、関連するセキュリティ・性能・保守性を確認する。
- 関連テストと必要なチェックを確認・実行し、変更箇所の静的解析警告を無視しない。
- 指摘は発生条件・影響・根拠・対象箇所・修正方向を示し、不具合・仕様の不明点・任意の改善案を区別する。確認範囲・未検証事項・検証結果も報告する。
- レビュー依頼だけでコード修正・コミット・マージ・PR承認を行わない。

### レビュー文面のフォーマット

- 各指摘は `[must|should|imo|nits] サマリー` で始める。
- 本文は「なぜ」（発生条件・根拠・影響）、「どのように」（修正方針と対象言語・形式のコードブロックによる最小限の修正案）、「メリット」（修正の効果）の順で改行して記載し、対象ファイル・最小限の行範囲を特定する。
- 仕様の質問・判断保留やレビュー全体の検証結果は、指摘とは別に報告する。
- GitHubへのレビュー本文には `レビュー実行モデル: モデル識別子` を記載し、単独コメントでは末尾に追記する。
