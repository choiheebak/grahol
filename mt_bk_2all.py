import streamlit as st
import pandas as pd
import numpy as np
import random
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

def Crawler(yearc,countc,gyungi):
    
    year = int(yearc)
    count = int(countc)
    i = int(gyungi)

    if i < 10:
        k = '0' + str(gyungi)
    else:
        k = str(gyungi)

    ssh = str(year) + "년 농구 승5패 " + str(count) + "회차"
    st.subheader(ssh)

    sh = str(i) + "경기"
    st.subheader(sh)
   

    home = []
    away = []
    hseq = []
    aseq = []
    hsjum = []
    asjum = []
    hwin = []
    hlose = []
    awin = []
    alose = []
    hcha = []
    acha = []
    hyeon = []
    ayeon = []
    has = []
    aas = []
    hrebound = []
    arebound = []
    hduk = []
    aduk = []
    htotal = []
    atotal = []
    hsteal = []
    asteal = []
    hblock = []
    ablock = []
    htsteal = []
    atsteal = []
    hfhrow = []
    afhrow = []
    hfhrows = []
    afhrows = []
    hhwin = []
    ahwin = []
    htgubun = []
    atgubun = []
    hgigu = []
    agigu = []
    hhlose = []
    ahlose = []
    hawin = []
    aawin = []
    halose = []
    aalose = []
    hdwin = []
    adwin = []
    hdlose = []
    adlose = []
    hilja = []
    ailja = []
    
    l_hgubun = ""
    l_agubun = ""
    l1_hgubun = ""
    l1_agubun = ""
    seq_hteam = ""
    seq_ateam = ""
    tts_hteam = ""
    tts_ateam = ""
    seq1_hteam = ""
    seq1_ateam = ""
    inq_hteam = ""
    inq_ateam = ""

    def read_all_txt(g,k):
        if g == '11':
            f = open('basketball_bk9_sseqhome.txt', 'r', encoding='UTF8')
        elif g == '12':
            f = open('basketball_bk9_sseqaway.txt', 'r', encoding='UTF8')

        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            if int(line[:2]) == int(k):
                l = line[3:]
                l = l.replace("\n","")
                team_read.append(l)
                
        f.close

        return team_read

    team_read = read_all_txt('11',k)

    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    home.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    hseq.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    hsjum.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    htotal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    hwin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    hlose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    hcha.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    hduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    has.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    hrebound.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 11:
                    hsteal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 12:
                    hblock.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 13:
                    htsteal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 14:
                    hfhrow.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 15:
                    hfhrows.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 16:
                    hhwin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 17:
                    hhlose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 18:
                    hawin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 19:
                    halose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 20:
                    hdwin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 21:
                    hdlose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 22:
                    hyeon.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 23:
                    htgubun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 24:
                    hgigu.append(team_read[q][s:r])
                    s = r+1
                    hilja.append(team_read[q][s:])

    team_read = read_all_txt('12',k)

    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    away.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    aseq.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    asjum.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    atotal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    awin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    alose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    acha.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    aduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    aas.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    arebound.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 11:
                    asteal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 12:
                    ablock.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 13:
                    atsteal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 14:
                    afhrow.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 15:
                    afhrows.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 16:
                    ahwin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 17:
                    ahlose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 18:
                    aawin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 19:
                    aalose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 20:
                    adwin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 21:
                    adlose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 22:
                    ayeon.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 23:
                    atgubun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 24:
                    agigu.append(team_read[q][s:r])
                    s = r+1
                    ailja.append(team_read[q][s:])
    
    def iljaseq_home(num_rows):
  
        # index = [f"{i}" for i in range(1, (num_rows+1))] 

        index = [hilja[i] for i in range(num_rows)]
        순위 = [int(hseq[i]) for i in range(num_rows)]
        경기수 = [htotal[i] for i in range(num_rows)]
        승률 = [hsjum[i] for i in range(num_rows)]
        승 = [hwin[i] for i in range(num_rows)]
        패 = [hlose[i] for i in range(num_rows)]
        승차 = [hcha[i] for i in range(num_rows)]
        득점 = [hduk[i] for i in range(num_rows)]
        AS = [has[i] for i in range(num_rows)]
        리바운드 = [hrebound[i] for i in range(num_rows)]
        스틸 = [hsteal[i] for i in range(num_rows)]
        블록 = [hblock[i] for i in range(num_rows)]
        삼점슛 = [htsteal[i] for i in range(num_rows)]
        자유투 = [hfhrow[i] for i in range(num_rows)]
        자유투성공 = [hfhrows[i] for i in range(num_rows)]
        홈승 = [hhwin[i] for i in range(num_rows)]
        홈패 = [hhlose[i] for i in range(num_rows)]
        원정승 = [hawin[i] for i in range(num_rows)]
        원정패 = [halose[i] for i in range(num_rows)]
        디비전승 = [hdwin[i] for i in range(num_rows)]
        디비전패 = [hdlose[i] for i in range(num_rows)]
        연속 = [hyeon[i] for i in range(num_rows)]
        리그 = [htgubun[i] for i in range(num_rows)]
        디비전 = [hgigu[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            # "선수": 선수,
            "순위": 순위,
            "경기수": 경기수,
            "승률": 승률,
            "승": 승,
            "패": 패,
            "승차": 승차,
            "득점": 득점,
            "AS": AS,
            "리바운드": 리바운드,
            "스틸": 스틸,
            "블록": 블록,
            "삼점슛": 삼점슛,
            "자유투": 자유투,
            "자유투성공": 자유투성공,
            "홈승": 홈승,
            "홈패": 홈패,
            "원정승": 원정승,
            "원정패": 원정패,
            "디비전승": 디비전승,
            "디비전패": 디비전패,
            "연속": 연속,
            "리그": 리그,
            "디비전": 디비전
        }

        # DataFrame 생성
        dfhs = pd.DataFrame(data, index=pd.Index(index, name="일자"))

        return dfhs

    def iljaseq_away(num_rows):
  
        # index = [f"{i}" for i in range(1, (num_rows+1))] 

        index = [ailja[i] for i in range(num_rows)]
        순위 = [int(aseq[i]) for i in range(num_rows)]
        경기수 = [atotal[i] for i in range(num_rows)]
        승률 = [asjum[i] for i in range(num_rows)]
        승 = [awin[i] for i in range(num_rows)]
        패 = [alose[i] for i in range(num_rows)]
        승차 = [acha[i] for i in range(num_rows)]
        득점 = [aduk[i] for i in range(num_rows)]
        AS = [aas[i] for i in range(num_rows)]
        리바운드 = [arebound[i] for i in range(num_rows)]
        스틸 = [asteal[i] for i in range(num_rows)]
        블록 = [ablock[i] for i in range(num_rows)]
        삼점슛 = [atsteal[i] for i in range(num_rows)]
        자유투 = [afhrow[i] for i in range(num_rows)]
        자유투성공 = [afhrows[i] for i in range(num_rows)]
        홈승 = [ahwin[i] for i in range(num_rows)]
        홈패 = [ahlose[i] for i in range(num_rows)]
        원정승 = [aawin[i] for i in range(num_rows)]
        원정패 = [aalose[i] for i in range(num_rows)]
        디비전승 = [adwin[i] for i in range(num_rows)]
        디비전패 = [adlose[i] for i in range(num_rows)]
        연속 = [ayeon[i] for i in range(num_rows)]
        리그 = [atgubun[i] for i in range(num_rows)]
        디비전 = [agigu[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            # "선수": 선수,
            "순위": 순위,
            "경기수": 경기수,
            "승률": 승률,
            "승": 승,
            "패": 패,
            "승차": 승차,
            "득점": 득점,
            "AS": AS,
            "리바운드": 리바운드,
            "스틸": 스틸,
            "블록": 블록,
            "삼점슛": 삼점슛,
            "자유투": 자유투,
            "자유투성공": 자유투성공,
            "홈승": 홈승,
            "홈패": 홈패,
            "원정승": 원정승,
            "원정패": 원정패,
            "디비전승": 디비전승,
            "디비전패": 디비전패,
            "연속": 연속,
            "리그": 리그,
            "디비전": 디비전
        }

        # DataFrame 생성
        dfas = pd.DataFrame(data, index=pd.Index(index, name="일자"))

        return dfas


    st.markdown(":basketball: :blue[**일별 순위 추이**]")
  
    # st.markdown("홈팀 : "+home[0])
   
    dfhs = iljaseq_home(len(hilja))

    # st.markdown("원정팀 : "+away[0])
    
    dfas = iljaseq_away(len(ailja))
   
    # plt.rcParams['font.family'] = 'NanumGothic'
    # plt.rcParams['axes.unicode_minus'] = False

    if len(hilja) == 0 and len(ailja) == 0:
        tab1, tab2 = st.tabs(["홈팀", "원정팀"])
        with tab1:
            pass
        with tab2:
            pass
    else:
        tab1, tab2 = st.tabs(["홈팀", "원정팀"])
        with tab1:
            st.text(home[0])
            st.dataframe(dfhs, use_container_width=True)   

            fig, ax = plt.subplots(figsize=(12, 6))
            sns.lineplot(x='일자', y='순위', data=dfhs, marker='o', color='red',linewidth=3, markersize=10)
            plt.title('', fontsize=20)
            plt.xlabel('DATE', fontsize=16)
            plt.ylabel('SEQ', fontsize=16, rotation=360)
            plt.xticks(rotation=45, fontsize=16)
            plt.yticks(fontsize=16)

            # y축 설정
            y_min = dfhs['순위'].min()
            y_max = dfhs['순위'].max()
            plt.yticks(range(0, 16, 1))  # 1부터 10까지 1씩 증가
            plt.gca().invert_yaxis()  # 순위 축 반전 (1이 가장 위로)

            # 그리드 추가
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            st.pyplot(fig)

            # # Streamlit의 내장 라인 차트 사용 (선택사항)
            # st.write("Streamlit 내장 라인 차트:")
            # st.line_chart(dfhs.set_index('일자'))    
        with tab2:
            st.text(away[0])
            st.dataframe(dfas, use_container_width=True)   

            fig, ax = plt.subplots(figsize=(12, 6))
            sns.lineplot(x='일자', y='순위', data=dfas, marker='o',color='blue',linewidth=3, markersize=10)
            plt.title('', fontsize=20)
            plt.xlabel('DATE', fontsize=16)
            plt.ylabel('SEQ', fontsize=16, rotation=360)
            plt.xticks(rotation=45, fontsize=16)
            plt.yticks(fontsize=16)

            # y축 설정
            y_min = dfas['순위'].min()
            y_max = dfas['순위'].max()
            # plt.yticks(range(y_min, y_max+1, 1))  # 1부터 10까지 1씩 증가
            plt.yticks(range(0, 16, 1))  # 1부터 10까지 1씩 증가
            plt.gca().invert_yaxis()  # 순위 축 반전 (1이 가장 위로)

            # 그리드 추가
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            st.pyplot(fig)
   