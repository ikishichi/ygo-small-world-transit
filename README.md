# ygo-small-world-transit

## About

[遊戯王スモール・ワールド乗り換え検索](https://ygo-small-world-transit.streamlit.app)では、[遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース](https://www.db.yugioh-card.com/yugiohdb/)（以下、遊戯王DB）の公開デッキURLを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。

## ライセンス

ライセンスについては[LICENSE.txt](LICENSE.txt)を参照してください。

## 使い方

YouTubeで[使い方動画](https://www.youtube.com/watch?v=VVvS8u706BM&t=6s)を公開しています。

1. 遊戯王DBの公開デッキURLを入力する(デッキURLはデッキページ上部に表示されているものを使用する)
2. 「デッキ取得」ボタンを押す
3. サーチ元とするモンスターをリストから選択する
4. サーチ先とするモンスターをリストから選択する(任意。選択しない場合、到達可能なサーチ先が全て表示される)
5. 検索ボタンを押すことで経由、サーチ先が表示される(結果は経由、サーチ先でソート可能)

## ローカルでの起動方法

事前にPythonのインストールが必要です。

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
