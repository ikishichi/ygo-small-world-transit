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

```plantuml
@startuml
actor User as user
database 遊戯王DB as db
participant "スモワ乗り換え検索" as sw


@enduml
```

## クラス図

```plantuml
@startuml
test -> test2
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
