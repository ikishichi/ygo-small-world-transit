import pytest
import requests
from src import deckinfo

def test_success_true_http(mocker):
    test_response = requests.Response
    status_code_ydb = 200
    test_response.status_code = status_code_ydb
    mocker.patch("requests.get", return_value = test_response)
    #mocker.patch("src.deckinfo.DeckInfo.success", return_value = True)
    di = deckinfo.DeckInfo("http://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=testtesttest")
    assert True == di.success()

def test_success_true_https(mocker):
    test_response = requests.Response
    status_code_ydb = 200
    test_response.status_code = status_code_ydb
    mocker.patch("requests.get", return_value = test_response)
    #mocker.patch("src.deckinfo.DeckInfo.success", return_value = True)
    di = deckinfo.DeckInfo("https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=testtesttest")
    assert True == di.success()

def test_success_false_url_isnot_ydb(mocker):
    test_response = requests.Response
    status_code_ydb = 200
    test_response.status_code = status_code_ydb
    mocker.patch("requests.get", return_value = test_response)
    #mocker.patch("src.deckinfo.DeckInfo.success", return_value = True)
    di = deckinfo.DeckInfo("https://github.com/ikishichi/ygo-small-world-transit")
    assert False == di.success()

def test_success_false_requests_return_error(mocker):
    test_response = requests.Response
    status_code_ydb = 999
    test_response.status_code = status_code_ydb
    mocker.patch("requests.get", return_value = test_response)
    #mocker.patch("src.deckinfo.DeckInfo.success", return_value = True)
    di = deckinfo.DeckInfo("https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=testtesttest")
    assert False == di.success()

def test_get():
    di = deckinfo.DeckInfo("https://www.db.yugioh-card.com/yugiohdb/member_deck.action?cgid=7bfe490b6b4e019e9577b4d83d00ae69&dno=2&request_locale=ja")
    if di.success():
        #print(di.get())
        print('success yeah')
    assert True
