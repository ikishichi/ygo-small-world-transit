# AGENTS.md

This file provides guidance to AI when working with code in this repository.

## プロジェクト概要

遊戯王の《スモール・ワールド》のサーチ経路を、遊戯王ニューロンの公開デッキURLから検索するStreamlitアプリ。本番は [ygo-small-world-transit.streamlit.app](https://ygo-small-world-transit.streamlit.app) にデプロイされている。

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

- `src/` 配下のモジュール同士は主に裸の import（例：`from deck import Deck`）を使っている。`deck_info.py` は相対 import と裸の import の両方に対応するが、`deck.py` や `ui.py` は対応していない。`streamlit run ./src/ui.py` やスクリプトを直接実行する `python src/deck.py` では `src/` が sys.path に追加される。一方、**プロジェクトルートから `python -m src.deck` のようにモジュールとして実行すると、裸の import を解決できず ImportError になる**。UI の起動には Streamlit のコマンドを使用する。
- 一方、`test/` 配下のテストは `from src.deck_info import DeckInfo` のように `src.` プレフィックス付きで import している。**pytest はプロジェクトルートから実行する必要がある**（`test/` に `cd` してから実行すると解決しない）。
- 実行経路とテスト経路で import 形式が非対称な点に注意すること。モジュール名の変更や新規モジュール追加時は両方の経路で確認する。

## アーキテクチャ

アプリは 6 モジュールで構成され、それぞれ単一責務を持つ。データの流れは基本的に一方向：

```
ui.py (Streamlit)
  ├─ url_resolver                       → URL構築・選択・取得前の検証とHTTPS化
  ├─ DeckInfo(url).fetch_html()          → 遊戯王ニューロンからHTML取得 (requests)
  ├─ Deck(html).parse_html()             → HtmlParser でモンスター情報を抽出し DataFrame 化
  │    └─ HtmlParser                     → BeautifulSoup(lxml) で detailtext_main を解析
  └─ SearchResult(df, origin, dest).get() → pandas ベースでサーチ経路を算出
```

- [src/ui.py](src/ui.py): Streamlit UI、クエリパラメータによるブックマーク対応、例外→画面エラー表示の責務。`session_state` に `MONSTERS_DF`・`SEARCH_RESULTS`・`DECK_NAME`・`LOADED_DECK_URL` を保持し、同じ取得済みURLの再実行では通信・解析を省く。明示的な取得操作は同じURLでも再取得する。取得成功後はURL入力フォームを閉じ、「デッキを変更」で再表示する。検索フォームは初期表示時から存在し、未取得時は無効。検索結果はサーチ先または経由ごとにまとめ、一致理由を展開表示する。
- [src/deck_info.py](src/deck_info.py): `normalize_deck_url()` で取得URLを検証・HTTPS化した後、接続5秒・読み取り15秒のタイムアウトでHTTP取得する。転送には追従せず、3xxは `ValueError`、4xx・5xxは `raise_for_status()` で例外化する。
- [src/deck.py](src/deck.py): HtmlParser の結果を pandas.DataFrame 化する薄いラッパー。
- [src/html_parser.py](src/html_parser.py): 遊戯王ニューロンの HTML 構造（`detailtext_main` → `t_body mlist_m` → `t_row c_normal`、`card_name` / `box_card_attribute` / `box_card_level_rank level` / `card_info_species_and_other_item` / `atk_power` / `def_power`）に強く依存している。**遊戯王ニューロンの HTML 構造変更がこのプロジェクトの最大の破壊要因**。構造や必須項目の欠落、未知のモンスター領域の内容、デッキ名の meta タグ・content 属性の欠落は `DeckStructureError`（`AttributeError` の派生）を送出する。モンスター領域が存在して空の場合は `NoMonsterError`（`ValueError` の派生）を送出する。UIは解析失敗とモンスター不在を区別して案内する。
- [src/search_result.py](src/search_result.py): 《スモール・ワールド》のロジックの本体。モンスター属性 6 項目（name, attribute, type, level, attack, defence）のうち**ちょうど 1 項目だけが一致する**組を「経由可能」と判定する二重ループ。origin → transit → dest の 2 ホップで全経路を列挙し DataFrame で返す。
- [src/url_resolver.py](src/url_resolver.py): デッキ識別用クエリパラメータの有無を判定し、遊戯王ニューロンのURLを構築する。デッキ取得ボタン押下時（「サンプルで試す」を含む）は入力URL、それ以外はクエリパラメータから構築したURLを選択する。`normalize_deck_url()` は取得先と必須パラメータを検証し、HTTPS化・取得時の言語補完・フラグメント除去を行う。

## 遊戯王ニューロンの URL 仕様

- UIは `url_resolver.py` から読み込んだ `VALID_PREFIX_HTTP` / `VALID_PREFIX_HTTPS` で入力URLのプレフィックスを検査する。取得直前には `normalize_deck_url()` が、スキームは `http` / `https`、ホストは `www.db.yugioh-card.com`、パスは `/yugiohdb/member_deck.action` であることを厳密に検証する。HTTP入力も実際の取得はHTTPSに統一する。
- クエリパラメータ `cgid` と `dno` でデッキを一意特定し、取得時には両方の空でない値が必要。`request_locale` は取得時に未指定・空文字なら `ja` を補完する。ブックマークからのURL構築では未指定時に `ja` を補完する。UI は明示的な取得操作での取得・解析成功後にこれら3項目を自身のURLにコピーして「ブックマーク共有」を実現している。サーチ元・サーチ先・検索結果はURLに保存しない。

## テストの方針

- 外部 HTTP は `pytest-mock` の `mocker.patch("requests.get", ...)` でモック。
- HtmlParser のテストはインラインの HTML 文字列をパラメタライズして渡す（実際の遊戯王ニューロンのフィクスチャは持たない）。新しい構造変更に追従する際はこのデータを更新する。
- UIは Streamlit の `AppTest` で、フォームの切り替え、取得済みデッキの再利用、取得失敗時の状態保持、検索結果のグループ表示などを検証する。`scripts/` の脆弱性レポートとスリープ対策にもテストがあり、スリープ対策のテストには追加のPlaywright・Chromiumが必要（導入方法はREADMEを参照）。

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
