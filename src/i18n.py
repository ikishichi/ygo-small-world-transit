"""URL指定・ブラウザー言語の判定と画面に表示する日英文言。"""


def resolve_language(browser_locale: str | None, lang: str | None = None) -> str:
    """URLのja/en、ブラウザー言語、日本語の順に表示言語を決める。"""
    if lang in {"ja", "en"}:
        return lang
    language = (browser_locale or "").replace("_", "-").split("-")[0].lower()
    return "en" if language == "en" else "ja"


MESSAGES = {
    "ja": {
        "app_title": "遊戯王スモール・ワールド乗り換え検索",
        "intro": "[遊戯王ニューロン](https://www.db.yugioh-card.com/yugiohdb/?request_locale={locale})の公開デッキを読み込むことで、[<<スモール・ワールド>>](https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=16555&request_locale={locale})のサーチ経路を検索できます。",
        "deck_url_label": "遊戯王ニューロンの公開デッキURLを入力してください。",
        "url_placeholder": "URLを入力",
        "fetch_deck": "デッキ取得",
        "sample": "サンプルで試す",
        "loading": "デッキを読み込んでいます…",
        "unnamed_deck": "名前なしのデッキ",
        "loaded": ":green[✓ 読み込み済]　**{name}**",
        "change_deck": "デッキを変更",
        "bookmark_hint": "このページをブックマークすると、次回のデッキ入力を省略できます。",
        "origin_label": "手札から見せるモンスターを選択してください:red[（必須）]",
        "destination_label": "サーチ先とするモンスターを選択してください（任意）",
        "monster_placeholder": "モンスターを選択",
        "search": "経路を検索",
        "origin_required": "サーチ元のモンスターを選択してください。",
        "no_routes": "該当する経路はありません。サーチ元を変更するか、サーチ先の指定を外してお試しください。",
        "results": "検索結果",
        "route_count": "{count}経路",
        "route_count_one": "{count}経路",
        "sort": "並べ替え",
        "sort_transit": "経由でソート",
        "sort_destination": "サーチ先でソート",
        "destination": "サーチ先",
        "bridge": "経由",
        "unnamed_card": "カード名なし",
        "origin_summary": "**手札から見せるカード：** {name}",
        "group_summary": "**{label}：** {names}",
        "match_details": "一致理由を表示（{routes}）",
        "route": "**経路 {number}：** {origin} → {transit} → {destination}",
        "first_match": "手札→経由：{label}が一致（{value}）",
        "second_match": "経由→サーチ先：{label}が一致（{value}）",
        "first_match_missing": "手札→経由：一致項目を表示できません",
        "second_match_missing": "経由→サーチ先：一致項目を表示できません",
        "attribute": "属性",
        "type": "種族",
        "level": "レベル",
        "attack": "攻撃力",
        "defence": "守備力",
        "no_monsters": "メインデッキにモンスターが見つかりませんでした。",
        "monsters_hint": "モンスターを含む公開デッキのURLを指定してください。",
        "parse_error": "デッキ情報を解析できませんでした。時間を置いて再試行してください。",
        "public_hint": "デッキレシピが「公開」になっているか確認してください。",
        "network_error": "デッキ情報を取得できませんでした。通信状態を確認し、時間を置いて再試行してください。",
        "invalid_url": "無効なURLです。遊戯王ニューロンの公開デッキレシピのURLを入力してください。",
        "missing_deck_params": "デッキURLに必須情報（cgid、dno）がありません。公開デッキのURLを確認してください。",
        "redirect_error": "デッキ取得先から転送応答が返されました",
        "unexpected_error": "予期しないエラーが発生しました。時間を置いて再試行してください。",
        "footer": "[GitHub](https://github.com/ikishichi/ygo-small-world-transit) / お問い合わせ・バグ報告は[こちら](https://docs.google.com/forms/d/18bz8n0Iw7zcS1Js1EhHxuyQ_HwOyts9goOyytDGqOvI/edit?pli=1)",
    },
    "en": {
        "app_title": "Yu-Gi-Oh! Small World Route Finder",
        "intro": "Load a public deck from the [Yu-Gi-Oh! Card Database](https://www.db.yugioh-card.com/yugiohdb/?request_locale={locale}) to find search routes for [Small World](https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=16555&request_locale={locale}).",
        "deck_url_label": "Enter a public deck URL from the Yu-Gi-Oh! Card Database.",
        "url_placeholder": "Enter a URL",
        "fetch_deck": "Load deck",
        "sample": "Try a sample",
        "loading": "Loading deck…",
        "unnamed_deck": "Unnamed deck",
        "loaded": ":green[✓ Loaded] **{name}**",
        "change_deck": "Change deck",
        "bookmark_hint": "Bookmark this page to load the same deck next time.",
        "origin_label": "Select a monster to reveal from your hand :red[(required)]",
        "destination_label": "Select a monster to add to your hand (optional)",
        "monster_placeholder": "Select a monster",
        "search": "Find routes",
        "origin_required": "Select a monster to reveal from your hand.",
        "no_routes": "No routes found. Try a different starting monster or clear the destination selection.",
        "results": "Search results",
        "route_count": "{count} routes",
        "route_count_one": "{count} route",
        "sort": "Sort by",
        "sort_transit": "Sort by bridge",
        "sort_destination": "Sort by destination",
        "destination": "Destination",
        "bridge": "Bridge",
        "unnamed_card": "Unnamed card",
        "origin_summary": "**Card revealed from hand:** {name}",
        "group_summary": "**{label}:** {names}",
        "match_details": "Show matching properties ({routes})",
        "route": "**Route {number}:** {origin} → {transit} → {destination}",
        "first_match": "Hand → Bridge: matching {label} ({value})",
        "second_match": "Bridge → Destination: matching {label} ({value})",
        "first_match_missing": "Hand → Bridge: matching properties unavailable",
        "second_match_missing": "Bridge → Destination: matching properties unavailable",
        "attribute": "Attribute",
        "type": "Type",
        "level": "Level",
        "attack": "ATK",
        "defence": "DEF",
        "no_monsters": "No monsters were found in the Main Deck.",
        "monsters_hint": "Enter a public deck URL that contains monsters.",
        "parse_error": "Could not read the deck information. Please try again later.",
        "public_hint": "Check that the deck is set to public.",
        "network_error": "Could not load the deck. Check your connection and try again later.",
        "invalid_url": "Invalid URL. Enter a public deck URL from the Yu-Gi-Oh! Card Database.",
        "missing_deck_params": "The deck URL is missing required information (cgid, dno). Check the public deck URL.",
        "redirect_error": "The deck server returned a redirect. Check the public deck URL and try again.",
        "unexpected_error": "An unexpected error occurred. Please try again later.",
        "footer": "[GitHub](https://github.com/ikishichi/ygo-small-world-transit) / [Contact us or report a bug](https://docs.google.com/forms/d/18bz8n0Iw7zcS1Js1EhHxuyQ_HwOyts9goOyytDGqOvI/edit?pli=1)",
    },
}


def translate(key: str, language: str = "ja", **values) -> str:
    """画面文言を取得し、文章単位で変数を埋め込む。"""
    return MESSAGES.get(language, MESSAGES["ja"])[key].format(**values)


def route_count(count: int, language: str = "ja") -> str:
    """英語の経路数は単数・複数を区別する。"""
    key = "route_count_one" if count == 1 else "route_count"
    return translate(key, language, count=count)
