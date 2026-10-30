# ygo-small-world-transit

## About

[遊戯王スモール・ワールド乗り換え検索](https://ygo-small-world-transit.streamlit.app)では、[遊戯王ニューロン](https://www.db.yugioh-card.com/yugiohdb/)の公開デッキURLを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。

## ライセンス

本プロジェクトのコードはMITライセンスで公開しています。詳細は[LICENSE.txt](LICENSE.txt)を参照してください。

## 使い方

YouTubeで[使い方動画](https://www.youtube.com/watch?v=VVvS8u706BM&t=6s)を公開しています。

1. 遊戯王ニューロンの公開デッキURLを入力する(デッキURLはデッキページ上部に表示されているものを使用する)
2. 「デッキ取得」ボタンを押す
3. サーチ元とするモンスターをリストから選択する
4. サーチ先とするモンスターをリストから選択する(任意。選択しない場合、読み込んだデッキ内で到達可能なサーチ先が全て表示される)
5. 「経路を検索」ボタンを押すと、経路数と、サーチ先ごとにまとめた経由候補が表示される。「経由でソート」に切り替えると、経由ごとのサーチ先候補を表示できる
6. 各グループの「一致理由を表示」を開くと、手札→経由→サーチ先の経路と、それぞれの一致項目を確認できる

ブックマークを使わない初回は「サンプルで試す」から、URLを入力せずにサンプルデッキを読み込むこともできます。

読み込み後はデッキ名と検索欄を表示します。別のデッキに切り替えるときや同じデッキを再読み込みするときは、「デッキを変更」からURL入力欄を開いてください。

デッキ取得後のページをブックマークすると、次回は同じデッキを自動で読み込みます。サーチ元・サーチ先の選択や検索結果は保存されません。

## 表示言語

ブラウザーの優先言語が英語（`en`、`en-US`、`en-GB` など）の場合は画面を英語で表示します。それ以外の言語や、言語を取得できない場合は日本語で表示します。

デッキURLの `request_locale` が未指定・空文字の場合、英語画面では英語、日本語画面では日本語のカード情報を取得します。入力URLやブックマークに言語が明示されている場合は、その指定を維持します。そのため、英語画面でも日本語指定のデッキURLから読み込むとカード名は日本語になります。サンプルデッキとカード説明リンクは画面の表示言語に合わせます。

画面の表示言語はブックマークには保存せず、アクセスしたブラウザーごとに判定します。デッキ名は登録された名前をそのまま表示します。手動の言語切り替えはありません。

## ローカルでの起動方法

起動にはPython 3.12以上が必要です。

1. このリポジトリをcloneし、プロジェクト直下に移動します。
2. 必要なパッケージをインストールします。

   ```bash
   python -m pip install -r requirements.txt
   ```

3. アプリを起動します。

   ```bash
   python -m streamlit run ./src/ui.py
   ```

他のPythonプロジェクトとのパッケージの干渉を避けたい場合は仮想環境を使用してください。

### トラブルシューティング

- `streamlit`コマンドが見つからない場合は、`python -m streamlit run ./src/ui.py`を実行してください。
- `No module named streamlit`と表示される場合は、起動に使うPythonで`python -m pip install -r requirements.txt`を実行してください。

## 開発

テストはプロジェクト直下で実行します。

```bash
python -m pytest
```

要件と設計は[設計書](docs/ygo-small-world-transit.md)を参照してください。

### 依存関係の管理

依存関係のバージョンは `requirements.in` で管理します。`requirements.txt` は間接依存までバージョンを固定した生成ファイルです。両方をGitに登録し、インストールには `requirements.txt` を使います。

生成には、`requirements-tools.txt` にバージョンを固定した [uv](https://docs.astral.sh/uv/pip/compile/) を使用します。

```bash
python -m pip install -r requirements-tools.txt
python -m uv pip compile requirements.in --output-file requirements.txt
```

依存関係を追加・変更するときは `requirements.in` を編集して再生成し、両ファイルを同じPRに含めてください。`requirements.txt` は直接編集しません。

`requirements.in` の指定範囲内で新しいバージョンに更新するには、生成コマンドの末尾に更新用のオプションを付けます。特定のパッケージだけを更新する場合は `--upgrade-package パッケージ名` 、すべてのパッケージを更新する場合は `--upgrade` を指定します。

```bash
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade-package streamlit
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade
```

CIでは再生成による差分がないことを確認してから、固定した依存関係でテストします。

### 依存関係の脆弱性スキャン

[Dependency security](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/dependency-security.yml) は、毎週土曜日と、main向けPRの作成・追加コミット・再オープン時に `requirements.txt` をTrivyで検査します。Actions画面から手動実行もできます。

除外設定を適用した後にHigh・Criticalが残っていると `dependency-security` チェックを失敗させます。修正版が未公開の脆弱性も対象です。DB取得失敗、レポートの欠落・破損、固定パッケージの解析漏れ、除外設定の不正も検査エラーとして失敗させます。

PRのチェック欄から実行結果を開くと、Summaryで検出・一時除外・判定対象の件数、判定対象のHigh・Critical一覧、一時除外した指摘の理由と期限を確認できます。詳細はログとArtifactsの `dependency-security-report` を確認してください。Artifactsには除外前・除外適用後のJSONレポート、Summary、検査した固定ファイル、使用した除外設定を14日間保存します。

特定の脆弱性を一時的に除外する場合は、リポジトリ直下の `.trivyignore` に除外する脆弱性IDを記載してください。修正版へ更新したら該当の除外を削除してください。 除外前の検出結果は詳細JSONに残ります。

## 公開アプリのスリープ対策

[Keep Streamlit app awake](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/keep_alive.yml)が、3時間ごとにPlaywrightのChromiumで公開アプリを開きます。監視ブラウザーの言語は `ja-JP` に固定します。スリープ画面の場合は解除ボタンを押し、タイトル・編集可能なデッキURL入力欄・有効な「デッキ取得」ボタンが表示されるまで待ちます。デッキの取得や検索は行いません。

フォークしたリポジトリでは、この定期アクセスは実行しません。

### 復帰確認と失敗時の対応

復帰確認は最大120秒待ち、一度再試行します（各試行のページ遷移待ちは別途最大30秒）。確認できなければワークフローを失敗させます。失敗時のスクリーンショットと各iframeのHTMLは、実行画面のArtifactsに7日間保存します。ログと合わせて、通信障害・Streamlit側の障害・画面やボタン名の変更を確認してください。UIの表示だけを確認するため、デッキ取得・検索機能の正常性までは保証しません。

[GitHubの定期実行](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)は遅延・欠落する場合があり、公開リポジトリに60日間活動がないと自動で無効になります。その場合はActions画面からワークフローを再び有効にしてください。[Streamlitのスリープ条件](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app#app-hibernation)や画面が変わる可能性もあるため、常時稼働を保証するものではありません。

### スリープ対策スクリプトのローカル検証

必要に応じて仮想環境に検証用の依存関係を追加してください。

```bash
python -m pip install playwright==1.63.0
python -m playwright install chromium
python scripts/keep_alive.py
python -m pytest test/keep_alive_test.py
```

`python scripts/keep_alive.py` は公開アプリに実際にアクセスして復帰を確認します。`python -m pytest test/keep_alive_test.py` はChromiumを使用し、通信先をローカルで再現します。Playwright未導入時はテストをスキップします。
