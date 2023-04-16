import pytest
import requests
from src import deckinfo

def test_success_true(mocker):
    test_response = requests.Response
    status_code_ydb = 200
    test_response.status_code = status_code_ydb
    mocker.patch("requests.get", return_value = test_response)
    #mocker.patch("src.deckinfo.DeckInfo.success", return_value = True)
    di = deckinfo.DeckInfo("https://www.db.yugioh-card.com/yugiohdb/testtesttest")
    assert True == di.success()

def test_success_false_url_isnot_ydb(mocker):
    test_response = requests.Response
    status_code_ydb = 200
    test_response.status_code = status_code_ydb
    mocker.patch("requests.get", return_value = test_response)
    #mocker.patch("src.deckinfo.DeckInfo.success", return_value = True)
    di = deckinfo.DeckInfo("https://github.com/ikishichi/ygo-small-world-transit")
    assert False == di.success()

def test_success_false_url_isnot_ydb(mocker):
    test_response = requests.Response
    status_code_ydb = 999
    test_response.status_code = status_code_ydb
    mocker.patch("requests.get", return_value = test_response)
    #mocker.patch("src.deckinfo.DeckInfo.success", return_value = True)
    di = deckinfo.DeckInfo("https://www.db.yugioh-card.com/yugiohdb/testtesttest")
    assert False == di.success()

def test_get():
    assert True
