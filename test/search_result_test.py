import pytest
import pandas as pd
from src import search_result

def test_get_no_destination():
    print("\ntest_get_no_destination...Start!!!")
    test_pd = pd.DataFrame(columns=['name', 'attribute', 'type', 'level', 'attack', 'defence'])
    test_pd = pd.DataFrame({'name':['テストマン','テストクリボー','LL-テスト・ダック','テストマンネオ','テストマンオリジン'],
                            'attribute':['光','闇','風','光','光'],
                            'type':['サイバース族','悪魔族','鳥獣族','サイバース族','サイバース族'],
                            'level':['10','1','1','10','10'],
                            'attack':['100','0','50','10000','10000'],
                            'defence':['200','200','0','200','0']})
    print(test_pd)
    print()
    sr = search_result.SearchResult(test_pd,'LL-テスト・ダック')
    print('Go Test get Go')
    print()
    print(sr.get())
    assert True

def test_get_set_destination():
    print("\ntest_get_set_destination...Start!!!")
    test_pd = pd.DataFrame(columns=['name', 'attribute', 'type', 'level', 'attack', 'defence'])
    test_pd = pd.DataFrame({'name':['テストマン','テストクリボー','LL-テスト・ダック','テストマンネオ','テストマンオリジン'],
                            'attribute':['光','闇','風','光','光'],
                            'type':['サイバース族','悪魔族','鳥獣族','サイバース族','サイバース族'],
                            'level':['10','1','1','10','10'],
                            'attack':['100','0','50','10000','10000'],
                            'defence':['200','200','0','200','0']})
    print(test_pd)
    print()
    sr = search_result.SearchResult(test_pd,'LL-テスト・ダック','テストマン')
    print('Go Test get Go')
    print()
    print(sr.get())
    assert True

def test_get_not_exist():
    print("\ntest_get_not_exist...Start!!!")
    test_pd = pd.DataFrame(columns=['name', 'attribute', 'type', 'level', 'attack', 'defence'])
    test_pd = pd.DataFrame({'name':['テストマン','テストクリボー','LL-テスト・ダック','テストマンネオ','テストマンオリジン'],
                            'attribute':['光','闇','風','光','光'],
                            'type':['サイバース族','悪魔族','鳥獣族','サイバース族','サイバース族'],
                            'level':['10','1','1','10','10'],
                            'attack':['100','0','50','10000','10000'],
                            'defence':['200','200','0','200','0']})
    print(test_pd)
    print()
    sr = search_result.SearchResult(test_pd,'BF-自動のテスト')
    print('Go Test get Go')
    print()
    print(sr.get())
    assert True