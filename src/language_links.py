"""日英ページの切り替えリンクと、描画後のhead用メタデータ。"""

import json
from html import escape
from urllib.parse import urlencode


APP_URL = "https://ygo-small-world-transit.streamlit.app/"


def build_language_urls(query_params):
    """デッキ識別情報と取得言語を保持し、表示言語だけを切り替える。"""
    deck_params = {
        key: query_params[key]
        for key in ("cgid", "dno", "request_locale")
        if key in query_params
    }
    return {
        language: "?" + urlencode({"lang": language, **deck_params})
        for language in ("ja", "en")
    }


def language_navigation(query_params):
    """同じタブで開く通常のa要素を返す。URLの値はHTMLエスケープする。"""
    urls = build_language_urls(query_params)
    links = [
        f'<a href="{escape(urls[language], quote=True)}" '
        f'hreflang="{language}" lang="{language}" target="_self">{label}</a>'
        for language, label in (("ja", "日本語"), ("en", "English"))
    ]
    return " / ".join(links)


def language_metadata(language, query_params):
    """相互参照・自己参照のhreflangをheadに設定するスクリプトを返す。"""
    urls = {
        locale: APP_URL + query
        for locale, query in build_language_urls(query_params).items()
    }
    # URLはurlencode済みだが、script内のJSONもHTML終端を作れない形にする。
    payload = json.dumps({"language": language, "urls": urls}).replace("<", "\\u003c")
    return """
    <script>
    (() => {
        const metadata = PAYLOAD;
        document.documentElement.lang = metadata.language;
        document.head.querySelectorAll('link[data-small-world-language]')
            .forEach(link => link.remove());
        for (const [language, url] of Object.entries(metadata.urls)) {
            const link = document.createElement('link');
            link.rel = 'alternate';
            link.hreflang = language;
            link.href = url;
            link.dataset.smallWorldLanguage = language;
            document.head.appendChild(link);
        }
    })();
    </script>
    """.replace("PAYLOAD", payload)
