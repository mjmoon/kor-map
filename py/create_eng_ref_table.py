# pylint: disable=E1101
import pandas as pd

PROVINCES = {
    '서울특별시': 'Seoul',
    '부산광역시': 'Busan',
    '대구광역시': 'Daegu',
    '인천광역시': 'Incheon',
    '광주광역시': 'Gwangju',
    '대전광역시': 'Daejeon',
    '울산광역시': 'Ulsan',
    '세종특별자치시': 'Sejong',
    '경기도': 'Gyeonggi',
    '북부출장소': 'Northern Branch',
    '강원도': 'Gangwon',
    '동해출장소': 'Eastern Branch',
    '충청북도': 'North Chungcheong',
    '충청남도': 'South Chungcheong',
    '전라북도': 'North Jeolla',
    '전라남도': 'South Jeolla',
    '경상북도': 'North Gyeongsang',
    '경상남도': 'South Gyeongsang',
    '제주특별자치도': 'Jeju'
}

DISTRICTS = {
    '종로구': 'Jongno District',
    '중구': 'Jung District',
    '용산구': 'Yongsan District',
    '성동구': 'Seongdong District',
    '광진구': 'Gwangjin District',
    '동대문구': 'Dongdaemun District',
    '중랑구': 'Jungnang District',
    '성북구': 'Seongbuk District',
    '강북구': 'Gangbuk District',
    '도봉구': 'Dobong District',
    '노원구': 'Nowon District',
    '은평구': 'Eunpyeong District',
    '서대문구': 'Seodaemun District',
    '마포구': 'Mapo District',
    '양천구': 'Yangcheon District',
    '강서구': 'Gangseo District',
    '구로구': 'Guro District',
    '금천구': 'Geumcheon District',
    '영등포구': 'Yeongdeungpo District',
    '동작구': 'Dongjak District',
    '관악구': 'Gwanak District',
    '서초구': 'Seocho District',
    '강남구': 'Gangnam District',
    '송파구': 'Songpa District',
    '강동구': 'Gangdong District',
    '서구': 'Seo District',
    '동구': 'Dong District',
    '영도구': 'Yeongdo District',
    '부산진구': 'Busanjin District',
    '동래구': 'Dongnae District',
    '남구': 'Nam District',
    '북구': 'Buk District',
    '해운대구': 'Haeundae District',
    '사하구': 'Saha District',
    '금정구': 'Geumjeong District',
    '연제구': 'Yeonje District',
    '수영구': 'Suyeong District',
    '사상구': 'Sasang District',
    '기장군': 'Gijang County',
    '수성구': 'Suseong District',
    '달서구': 'Dalseo District',
    '달성군': 'Dalseong County',
    '중구 영종출장소': 'Jung District Yeongjong Branch',
    '중구 용유출장소': 'Jung District Yongyu Branch',
    '연수구': 'Yeonsu District',
    '남동구': 'Namdong District',
    '부평구': 'Bupyeong District',
    '계양구': 'Gyeyang District',
    '서구 검단출장소': 'Seo District Geomdan Branch',
    '강화군': 'Ganghwa County',
    '옹진군': 'Ongjin County',
    '광산구': 'Gwangsan District',
    '유성구': 'Yuseong District',
    '대덕구': 'Daedeok District',
    '울주군': 'Ulju County',
    '수원시': 'Suwon',
    '수원시 장안구': 'Jangan District, Suwon',
    '수원시 권선구': 'Gwonseon District, Suwon',
    '수원시 팔달구': 'Paldal District, Suwon',
    '수원시 영통구': 'Yeongtong Disrict, Suwon',
    '성남시': 'Seongnam',
    '성남시 수정구': 'Sujeong District, Seongnam',
    '성남시 중원구': 'Jungwon District, Seongnam',
    '성남시 분당구': 'Bundang District, Seongnam',
    '의정부시': 'Uijeongbu',
    '안양시': 'Anyang',
    '안양시 만안구': 'Manan District, Anyang',
    '안양시 동안구': 'Dongan District, Anyang',
    '부천시': 'Bucheon',
    '광명시': 'Gwangmyeong',
    '평택시': 'Pyeongtaek',
    '송탄출장소': 'Songtan Branch',
    '안중출장소': 'Anjung Branch',
    '동두천시': 'Dongducheon',
    '안산시': 'Ansan',
    '안산시 상록구': 'Sangnok District, Ansan',
    '안산시 단원구': 'Danwon District, Ansan',
    '고양시': 'Goyang',
    '고양시 덕양구': 'Deokyang District, Goyang',
    '고양시 일산동구': 'Ilsandong District, Goyang',
    '고양시 일산서구': 'Ilsanseo District, Goyang',
    '과천시': 'Gwacheon',
    '구리시': 'Guri',
    '남양주시': 'Namyangju',
    '풍양출장소': 'Pungyang Branch',
    '오산시': 'Osan',
    '시흥시': ' Siheung',
    '군포시': 'Gunpo',
    '의왕시': 'Uiwang',
    '하남시': 'Hanam',
    '용인시': 'Yongin',
    '용인시 처인구': 'Cheoin District, Yongin',
    '용인시 기흥구': 'Giheung District, Yongin',
    '용인시 수지구': 'Suji District, Yongin',
    '파주시': 'Paju',
    '이천시': 'Icheon',
    '안성시': 'Anseong',
    '김포시': 'Gimpo',
    '화성시': 'Hwaseong',
    '화성시 동부출장소': 'East Branch, Hwaseong',
    '광주시': 'Gwangju',
    '양주시': 'Yangju',
    '포천시': 'Pocheon',
    '여주시': 'Yeoju',
    '연천군': 'Yeoncheon County',
    '가평군': 'Gapyeong County',
    '양평군': 'Yangpeyong County',
    '춘천시': 'Chuncheon',
    '원주시': 'Wonju',
    '강릉시': 'Gangneung',
    '동해시': 'Donghae',
    '태백시': 'Taebaek',
    '속초시': 'Sokcho',
    '삼척시': 'Samcheok',
    '홍천군': 'Hongcheon County',
    '횡성군': 'HoENseong County',
    '영월군': 'Yeongwol County',
    '평창군': 'Pyeongchang County',
    '정선군': 'Jeongseon County',
    '철원군': 'Cheorwon County',
    '화천군': 'Hwacheon County',
    '양구군': 'Yanggu County',
    '인제군': 'Inje County',
    '고성군': 'Goseong County',
    '양양군': 'Yangyang County',
    '청주시': 'Cheongju',
    '청주시 상당구': 'Sangdang District, Cheongju',
    '청주시 서원구': 'Seowon District, Cheongju',
    '청주시 흥덕구': 'Heungdeok District, Cheongju',
    '청주시 청원구': 'Cheongwon District, Cheongju',
    '충주시': 'Chungju',
    '제천시': 'Jecheon',
    '보은군': 'Boeun County',
    '옥천군': 'Okcheon County',
    '영동군': 'Yeongdong County',
    '증평군': 'Jeungpyeong County',
    '진천군': 'Jincheon County',
    '괴산군': 'Goesan County',
    '음성군': 'Eumseong County',
    '단양군': 'Danyang County',
    '천안시': 'Cheonan',
    '천안시 동남구': 'Dongnam District, Cheonan',
    '천안시 서북구': 'Seobuk District, Cheonan',
    '공주시': 'Gongju',
    '보령시': 'Boryeong',
    '아산시': 'Asan',
    '서산시': 'Seosan',
    '논산시': 'Nonsan',
    '계룡시': 'Gyeryong',
    '당진시': 'Dangjin',
    '금산군': 'Geumsan County',
    '부여군': 'Buyeo County',
    '서천군': 'Seocheon County',
    '청양군': 'Cheongyang County',
    '홍성군': 'Hongseong County',
    '예산군': 'Yesan County',
    '태안군': 'Taean County',
    '전주시': 'Jeonju',
    '전주시 완산구': 'Wansan District, Jeonju',
    '전주시 덕진구': 'Deokjin District, Jeonju',
    '전주시 효자출장소': 'Hyoja Branch, Jeonju',
    '군산시': 'Gunsan',
    '익산시': 'Iksan',
    '익산시 함열출장소': 'Hanyeol Branch, Iksan',
    '정읍시': 'Jeongeup',
    '남원시': 'Namwon',
    '김제시': 'Gimje',
    '완주군': 'Wanju County',
    '진안군': 'Jinan County',
    '무주군': 'Muju County',
    '장수군': 'Jangsu County',
    '임실군': 'Imsil County',
    '순창군': 'Sunchang County',
    '고창군': 'Gochang County',
    '부안군': 'Buan County',
    '목포시': 'Mokpo',
    '여수시': 'Yeosu',
    '순천시': 'Suncheon',
    '나주시': 'Naju',
    '광양시': 'Gwangyang',
    '담양군': 'Damyang County',
    '곡성군': 'Gokseong County',
    '구례군': 'Gurye County',
    '고흥군': 'Goheung County',
    '보성군': 'Boseong County',
    '화순군': 'Hwasun County',
    '장흥군': 'Jangheung County',
    '강진군': 'Gangjin County',
    '해남군': 'Haenam County',
    '영암군': 'Yeongam County',
    '무안군': 'Muan County',
    '함평군': 'Hampyeong County',
    '영광군': 'Yeonggwang County',
    '장성군': 'Jangseong County',
    '완도군': 'Wando County',
    '진도군': 'Jindo County',
    '신안군': 'Sinan County',
    '포항시': 'Pohang',
    '포항시 남구': 'Nam District, Pohang',
    '포항시 북구': 'Buk District, Pohang',
    '경주시': 'Gyeongju',
    '김천시': 'Gimcheon',
    '안동시': 'Andong',
    '구미시': 'Gumi',
    '영주시': 'Yeongju',
    '영천시': 'Yeongcheon',
    '상주시': 'Sangju',
    '문경시': 'Mungyeong',
    '경산시': 'Gyeongsan',
    '군위군': 'Gunwi County',
    '의성군': 'Uiseong County',
    '청송군': 'Cheongsong County',
    '영양군': 'Yeongyang County',
    '영덕군': 'Yeongdeok County',
    '청도군': 'Cheongdo County',
    '고령군': 'Goryeong County',
    '성주군': 'Seongju County',
    '칠곡군': 'Chilgok County',
    '예천군': 'Yecheon County',
    '봉화군': 'Bonghwa County',
    '울진군': 'Uljin County',
    '울릉군': 'Ulleung County',
    '창원시': 'Changwon',
    '창원시 의창구': 'Uichang District, Changwon',
    '창원시 성산구': 'Seongsan District, Changwon',
    '창원시 마산합포구': 'Masanhappo District, Changwon',
    '창원시 마산회원구': 'Masanhoewon District, Changwon',
    '창원시 진해구': 'Jinhae District, Changwon',
    '진주시': 'Jinju',
    '통영시': 'Tongyeong',
    '사천시': 'Sacheon',
    '사천 남양출장소': 'Namyang Branch, Sacheon',
    '김해시': 'Gimhae',
    '장유출장소': 'Jangyu Branch',
    '밀양시': 'Miryang',
    '거제시': 'Geoje',
    '양산시': 'Yangsan',
    '양산시 웅상출장소': 'Ungsang Branch, Yangsan',
    '의령군': 'Uiryeong County',
    '함안군': 'Haman County',
    '창녕군': 'Changnyeong County',
    '남해군': 'Namhae County',
    '하동군': 'Hadong County',
    '산청군': 'Sancheong County',
    '함양군': 'Hamyang County',
    '거창군': 'Cheochang County',
    '합천군': 'Hapcheon County',
    '제주시': 'Jeju',
    '서귀포시': 'Seogwipo'
}

ref = pd.read_csv('data/original/KIKmix.20180401.csv')
ref.columns = ['H_CD', 'LVL_1_KR', 'LVL_2_KR', 'LVL_3_KR', 'B_CD', 'LVL_4_KR', 'CREATED_DT', 'REMOVED_DT']

ref.loc[ref['LVL_2_KR'] == '중구영종출장소', 'LVL_2_KR'] = '중구 영종출장소'
ref.loc[ref['LVL_2_KR'] == '중구용유출장소', 'LVL_2_KR'] = '중구 용유출장소'
ref.loc[ref['LVL_2_KR'] == '서구검단출장', 'LVL_2_KR'] = '서구 검단출장소'
ref.loc[ref['LVL_2_KR'] == '화성시동부출장소', 'LVL_2_KR'] = '화성시 동부출장소'
ref.loc[ref['LVL_2_KR'] == '전주시효자출', 'LVL_2_KR'] = '전주시 효자출장소'
ref.loc[ref['LVL_2_KR'] == '익산시함열출', 'LVL_2_KR'] = '익산시 함열출장소'
ref.loc[ref['LVL_2_KR'] == '사천남양출장', 'LVL_2_KR'] = '사천 남양출장소'
ref.loc[ref['LVL_2_KR'] == '양산시웅상출장소', 'LVL_2_KR'] = '양산시 웅상출장소'

ref['LVL_1_EN'] = [PROVINCES[x] if x in PROVINCES else '' for x in ref['LVL_1_KR']]
ref['LVL_2_EN'] = [DISTRICTS[x] if x in DISTRICTS else '' for x in ref['LVL_2_KR'] ]

# drop 출장소 / branches
ref = ref[~ref.apply(lambda row: any(["Branch" in str(x) for x in row]), axis=1)].copy()

ref['LVL_3_CD'] = ref['B_CD'].apply(lambda x: str(x)[:8])
ref['LVL_3_CD'].head()
ref['LVL_2_CD'] = ref['B_CD'].apply(lambda x: str(x)[:5])
ref['LVL_2_CD'].head()
ref['LVL_1_CD'] = ref['B_CD'].apply(lambda x: str(x)[:2])

ref.drop(2969, inplace=True)  # 2969: LVL_2_CD='41171' has a duplicate
# save lvl 3 ref table
lvl3 = ref.loc[
        ref['LVL_3_CD'].apply(lambda x: int(x)%1000 > 0),
        ['LVL_3_CD', 'LVL_1_KR', 'LVL_1_EN', 'LVL_2_KR', 'LVL_2_EN', 'LVL_3_KR']
    ].drop_duplicates(['LVL_3_CD', 'LVL_1_KR', 'LVL_1_EN', 'LVL_2_KR', 'LVL_2_EN']).copy()
# lvl3[lvl3.duplicated('LVL_3_CD', keep=False)]
lvl3.to_csv(
    'data/interim/kor_admin_3_ref_w_en.csv', index=False
)

# save lvl 2 ref table
lvl2 = ref.loc[
        ref['LVL_2_CD'].apply(lambda x: int(x)%1000 > 0),
        ['LVL_2_CD', 'LVL_1_KR', 'LVL_1_EN', 'LVL_2_KR', 'LVL_2_EN']
    ].drop_duplicates().copy()
# lvl2[lvl2.duplicated('LVL_2_CD', keep=False)]
lvl2.to_csv(
    'data/interim/kor_admin_2_ref_w_en.csv', index=False
)

# save lvl 1 ref table
ref[
    ['LVL_1_CD', 'LVL_1_KR', 'LVL_1_EN']
].drop_duplicates().to_csv(
    'data/interim/kor_admin_1_ref_w_en.csv', index=False
)

any(
    ref[
        ['LVL_1_CD', 'LVL_1_KR', 'LVL_1_EN']
    ].drop_duplicates().duplicated('LVL_1_CD')
)
