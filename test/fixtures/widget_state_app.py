"""実際のUIを固定デッキで動かすブラウザーテスト用エントリーポイント。"""

import runpy
import sys
from pathlib import Path
from unittest.mock import Mock, patch

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "src"))


def deck_response():
    from test.html_parser_test import ENGLISH_DECK_HTML

    return Mock(status_code=200, content=ENGLISH_DECK_HTML.encode("utf-8"))


with patch("requests.get", return_value=deck_response()):
    runpy.run_path(str(PROJECT_ROOT / "src" / "ui.py"), run_name="__main__")
