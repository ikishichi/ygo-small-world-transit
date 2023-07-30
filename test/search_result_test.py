import pytest
import pandas as pd
from src import search_result

def test_get():
    print("\nStart!!!")
    test_pd = pd.DataFrame(columns=['name', 'attribute', 'type', 'level', 'attack', 'defence'])
    test_pd = pd.DataFrame({'name':['テストマン','テストクリボー','LL-テスト・ダック'],
                            'attribute':['光','闇','風'],
                            'type':['サイバース族','悪魔族','鳥獣族'],
                            'level':['10','1','1'],
                            'attack':['100','0','50'],
                            'defence':['300','200','0']})
    print(test_pd)
    print()
    sr = search_result.SearchResult(test_pd,'LL-テスト・ダック')
    print('Go Test get Go')
    print(sr.get())
    assert True