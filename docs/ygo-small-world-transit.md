# ygo-small-world-transit

## 要件定義

```plantuml
@startuml
left to right direction
:User: as user

package "スモワ乗り換え検索" {
    (検索) as uc1
    (デッキURL保存) as uc2
}
user --> uc1
user --> uc2

@enduml
```

1. スモールワールドのサーチ先が検索できる
1. 遊戯王DBからデッキレシピを読み込める
1. PC/スマートフォンでの表示に対応
1. デッキURLを保存できる

## データフロー図

```plantuml
@startuml
actor User as user
database 遊戯王DB as db
node "スモワ乗り換え検索" as sw

user --> db : デッキ登録
db --> user : デッキURL
user --> sw : デッキURL入力, 検索元, 検索先(任意)
sw --> user : 検索結果
sw --> db : デッキ情報要求
db --> sw : デッキ情報
@enduml
```

## シーケンス図

### 概略版

```plantuml
@startuml
actor User as user
participant "スモールワールド乗り換え検索" as sw
database 遊戯王DB as db

user --> sw : デッキURL
sw --> db : デッキ情報取得要求
db --> sw : デッキ情報(html)
sw --> user : 結果(OK/NG)
alt OK
    sw --> sw : デッキ情報解析(検索元、検索先表示用)
    sw --> sw : 検索用UI有効化
    user --> sw : 検索元、検索先(任意)入力(プルダウンメニュー)
    user --> sw : 検索ボタン
    sw --> sw : デッキ情報解析(検索)
    sw --> user : 検索結果
end

@enduml
```

### ソフトウェア詳細版

```plantuml
@startuml
actor User as user
box "スモールワールド乗り換え検索"
participant "UI表示" as ui
participant "DeckInfo" as di
participant "SearchResult" as sr
participant "Deck" as dc
participant "HtmlParser" as hp
end box
database 遊戯王DB as db

user --> ui : デッキURL
create di
ui --> di : デッキURL
di --> db : デッキ情報取得要求
db --> di : デッキ情報(html)
di --> ui : 結果(OK/NG)
di --> ui : デッキ情報(html)
create dc
ui --> dc : デッキ情報(html)
create hp
dc --> hp : デッキ情報(html)
hp --> dc : モンスター情報リスト
dc --> dc : モンスターリスト生成
dc --> hp : delete
destroy hp
dc --> ui : 結果(OK/NG)
alt OK
    ui --> dc : モンスターリスト要求
    dc --> ui : モンスターリスト
    ui --> user : 検索用UI有効化\n(検索元、検索先、検索ボタン)
    user --> ui : 検索元、検索先(任意)入力\n(プルダウンメニュー)
    user --> ui : 検索ボタン
    create sr
    ui --> sr : 検索要求\n(モンスターリスト、デッキ検索元、検索先)
    sr --> sr : 検索
    sr --> user : 検索結果
end

@enduml
```

## クラス図

```plantuml
@startuml
object "UI表示" as ui
note right
streamlit
を使用
endnote
class DeckInfo{
    - html
    + DeckInfo(url)
    + bool Success()
    + Get()
}
class SearchResult {
    - list SearchResult
    + SearchResult(MonsterList, origin, destination)
    + Get()
}
class Deck{
    - pandas.DataFrame MonsterList
    + Deck(html)
    + bool Exists()
    + list GetMonsterList()
    - void CreateMonsterList(html)
}
note right
pandas
を使用
endnote
class HtmlParser{
    - MonsterInfoList
    + HtmlParser(html)
    + GetMonsterInfoList()
}
note right
beautiful soup
を使用
endnote
ui "1"--"*" DeckInfo
ui "1"--"1" SearchResult

ui "1"--"*" Deck
Deck "1"--"1" HtmlParser
@enduml
```

## フローチャート

```plantuml
@startuml
test -> test2
@enduml
```

## 開発環境

* python
* github
* streamlit
* requests
* pandas
* beautiful soup

コーディング規約はPython公式に従う。

https://docs.python.org/ja/3/tutorial/controlflow.html#intermezzo-coding-style
