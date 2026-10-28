# ygo-small-world-transit

## About

[遊戯王スモール・ワールド乗り換え検索](https://ygo-small-world-transit.streamlit.app)では、[遊戯王ニューロン](https://www.db.yugioh-card.com/yugiohdb/)の公開デッキURLを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。

## ライセンス

ライセンスについては[LICENSE.txt](LICENSE.txt)を参照してください。

## 使い方

YouTubeで[使い方動画](https://www.youtube.com/watch?v=VVvS8u706BM&t=6s)を公開しています。

1. 遊戯王ニューロンの公開デッキURLを入力する(デッキURLはデッキページ上部に表示されているものを使用する)
2. 「デッキ取得」ボタンを押す
3. サーチ元とするモンスターをリストから選択する
4. サーチ先とするモンスターをリストから選択する(任意。選択しない場合、読み込んだデッキ内で到達可能なサーチ先が全て表示される)
5. 「経路を検索」ボタンを押すことで経由、サーチ先が表示される(結果は経由、サーチ先でソート可能)

読み込み後はデッキ名と検索欄を表示します。別のデッキに切り替えるときや同じデッキを再読み込みするときは、「デッキを変更」からURL入力欄を開いてください。

デッキ取得後のページをブックマークすると、次回は同じデッキを自動で読み込みます。サーチ元・サーチ先の選択や検索結果は保存されません。

## ローカルでの起動方法

事前にPython 3.12以上のインストールが必要です。

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

依存関係のバージョン範囲と脆弱性対応の固定値は `requirements.in` で管理します。`requirements.txt` は間接依存までバージョンを固定した生成ファイルです。両方をGitに登録し、インストールには `requirements.txt` を使います。

生成には、`requirements-tools.txt` にバージョンを固定した [uv](https://docs.astral.sh/uv/pip/compile/) を使用します。Python 3.12の仮想環境で次を実行してください。

```bash
python -m pip install -r requirements-tools.txt
python -m uv pip compile requirements.in --output-file requirements.txt
```

`uv.toml` でPython 3.12以上を対象とする `universal` 解決を設定しており、Windows限定の依存などは条件付きで記録します。通常の再生成では既存の固定バージョンを優先します。依存関係を追加・変更するときは `requirements.in` を編集して再生成し、両ファイルを同じPRに含めてください。`requirements.txt` は直接編集しません。

特定のパッケージを更新する場合は `--upgrade-package`、全体を更新する場合は `--upgrade` を追加します。

```bash
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade-package streamlit
python -m uv pip compile requirements.in --output-file requirements.txt --upgrade
```

`requirements.in` で `==` に固定した脆弱性対応のバージョンは、これらの更新操作でも変わりません。修正版を変更するときは、脆弱性情報を確認して `requirements.in` の固定値とコメントを更新してください。

更新後は、新しい仮想環境にインストールして整合性確認とテストを実行します。スリープ対策のテストも実行する場合は、後述のPlaywrightとChromiumもインストールしてください。

```bash
python -m pip install -r requirements.txt
python -m pip check
python -m pytest
```

CIでは再生成による差分がないことを確認してから、固定した依存関係でテストします。本番も同じコミットの `requirements.txt` を使い、PythonのバージョンをCIと揃えてください。既に稼働中の本番環境に反映するには再デプロイが必要です。

## 公開アプリのスリープ対策

[Keep Streamlit app awake](https://github.com/ikishichi/ygo-small-world-transit/actions/workflows/keep_alive.yml)が、3時間ごとにPlaywrightのChromiumで公開アプリを開きます。スリープ画面の場合は解除ボタンを押し、タイトル・編集可能なデッキURL入力欄・有効な「デッキ取得」ボタンが表示されるまで待ちます。デッキの取得や検索は行いません。

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

スリープ対策のテストはChromiumを使用し、通信先はローカルで再現します。Playwright未導入時はスキップします。
