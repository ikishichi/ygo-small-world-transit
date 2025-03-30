# ygo-small-world-transit

## About

[遊戯王スモール・ワールド乗り換え検索](https://ygo-small-world-transit.streamlit.app)では、[遊戯王 オフィシャルカードゲーム デュエルモンスターズ - カードデータベース](https://www.db.yugioh-card.com/yugiohdb/)（以下、遊戯王DB）の公開デッキURLを読み込むことで、<<スモール・ワールド>>のサーチ経路を検索できます。

## ライセンス

ライセンスについてはLICENSE.txtを参照してください。

## 使い方

YouTubeで[使い方動画](https://www.youtube.com/watch?v=VVvS8u706BM&t=6s)を公開しています。

1. 遊戯王DBの公開デッキURLを入力する(デッキURLはデッキページ上部に表示されているものを使用する)
2. サーチ元とするモンスターをリストから選択する
3. サーチ先とするモンスターをリストから選択する(任意。選択しない場合、到達可能なサーチ先が全て表示される)
4. 検索ボタンを押すことで経由、サーチ先が表示される(結果は経由、サーチ先でソート可能)

## ローカルでの起動方法

事前にPythonのインストールが必要です。

1. このリポジトリを任意のディレクトリにcloneします。
2. プロジェクト直下に移動し`pip install -r requirements.txt`で必要なパッケージをインストールします。
3. `streamlit run .\src\ui.py`で起動します。

### トラブルシューティング
- streamlitコマンドが見つからない場合：ユーザのシステム環境変数Pathに以下を設定してください。
  - `C:\Users\＜ユーザ名＞\AppData\Roaming\Python\＜PythonXXX＞\Scripts`