# pylint: disable=E1101
import json
import pandas as pd

def check_unjoined(data):
    """Return original data( and unjoined data if any)."""
    obj = data['objects']
    geo = pd.DataFrame([x['properties'] for x in obj[list(obj)[0]]['geometries']])

    if 'unjoined' in list(obj):
        unjoined = data['objects']['unjoined']
        if len(unjoined['geometries']) > 0:
            print('Unjoined data found.')
            return (
                geo,
                pd.DataFrame([x['properties'] for x in unjoined['geometries']])
            )
    print('OK.')
    return (geo, True)

with open('data/plot/kor_admin_1.topojson', 'r') as f:
    geo1, test1 = check_unjoined(json.load(f))

with open('data/plot/kor_admin_2.topojson', 'r') as f:
    geo2, test2 = check_unjoined(json.load(f))

with open('data/plot/kor_admin_3.topojson', 'r') as f:
    geo3, test3 = check_unjoined(json.load(f))

test2 # 구 단위로 지도표기된 중견 도시들
geo2[geo2['LVL_2_KR'].apply(lambda x: any(t in x for t in test2['LVL_2_KR']))]
geo2[geo2['LVL_1_KR'] == '경기도']

test3 # 새솔동 new as of Jan 2018
geo3[geo3['LVL_2_KR'] == '화성시']
