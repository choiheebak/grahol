import streamlit as st
import pandas as pd
import numpy as np
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

    ssh = str(year) + "년 축구 승무패 " + str(count) + "회차"
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
    hdraw = []
    hlose = []
    awin = []
    adraw = []
    alose = []
    hduk = []
    aduk = []
    hsil = []
    asil = []
    hcha = []
    acha = []
    hassist = []
    aassist = []
    hpduk = []
    apduk = []
    hpsil = []
    apsil = []
    htotal = []
    atotal = []
    hshooting = []
    ashooting = []
    hilja = []
    ailja = []
    hl_gubun = []
    al_gubun = []

    # print(year,count,i)
 
    def read_all_txt(g,k):
        if g == '11':
            f = open('soccer_so9_sseqhome.txt', 'r', encoding='UTF8')
        elif g == '12':
            f = open('soccer_so9_sseqaway.txt', 'r', encoding='UTF8')

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
                    hdraw.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    hlose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    hduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    hsil.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    hcha.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 11:
                    hpduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 12:
                    hpsil.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 13:
                    hshooting.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 14:
                    hilja.append(team_read[q][s:r])
                    s = r+1
                    hl_gubun.append(team_read[q][s:])

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
                    adraw.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    alose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    aduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    asil.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    acha.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 11:
                    apduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 12:
                    apsil.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 13:
                    ashooting.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 14:
                    ailja.append(team_read[q][s:r])
                    s = r+1
                    al_gubun.append(team_read[q][s:])

    def iljaseq_home(num_rows):
  
        # index = [f"{i}" for i in range(1, (num_rows+1))] 

        index = [hilja[i] for i in range(num_rows)]
        순위 = [int(hseq[i]) for i in range(num_rows)]
        경기수 = [htotal[i] for i in range(num_rows)]
        승점 = [hsjum[i] for i in range(num_rows)]
        승 = [hwin[i] for i in range(num_rows)]
        무 = [hdraw[i] for i in range(num_rows)]
        패 = [hlose[i] for i in range(num_rows)]
        득점 = [hduk[i] for i in range(num_rows)]
        실점 = [hsil[i] for i in range(num_rows)]
        득실차 = [hcha[i] for i in range(num_rows)]
        평균득점 = [hpduk[i] for i in range(num_rows)]
        평균실점 = [hpsil[i] for i in range(num_rows)]
        슈팅 = [hshooting[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            # "선수": 선수,
            "순위": 순위,
            "경기수": 경기수,
            "승점": 승점,
            "승": 승,
            "무": 무,
            "패": 패,
            "득점": 득점,
            "실점": 실점,
            "득실차": 득실차,
            "평균득점": 평균득점,
            "평균실점": 평균실점,
            "슈팅": 슈팅
        }

        # DataFrame 생성
        dfhs = pd.DataFrame(data, index=pd.Index(index, name="일자"))

        return dfhs

    def iljaseq_away(num_rows):
  
        # index = [f"{i}" for i in range(1, (num_rows+1))] 

        index = [ailja[i] for i in range(num_rows)]
        순위 = [int(aseq[i]) for i in range(num_rows)]
        경기수 = [atotal[i] for i in range(num_rows)]
        승점 = [asjum[i] for i in range(num_rows)]
        승 = [awin[i] for i in range(num_rows)]
        무 = [adraw[i] for i in range(num_rows)]
        패 = [alose[i] for i in range(num_rows)]
        득점 = [aduk[i] for i in range(num_rows)]
        실점 = [asil[i] for i in range(num_rows)]
        득실차 = [acha[i] for i in range(num_rows)]
        평균득점 = [apduk[i] for i in range(num_rows)]
        평균실점 = [apsil[i] for i in range(num_rows)]
        슈팅 = [ashooting[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            # "선수": 선수,
            "순위": 순위,
            "경기수": 경기수,
            "승점": 승점,
            "승": 승,
            "무": 무,
            "패": 패,
            "득점": 득점,
            "실점": 실점,
            "득실차": 득실차,
            "평균득점": 평균득점,
            "평균실점": 평균실점,
            "슈팅": 슈팅
        }

        # DataFrame 생성
        dfas = pd.DataFrame(data, index=pd.Index(index, name="일자"))

        return dfas


    st.markdown(":soccer: :blue[**일별 순위 추이**] (최대 10경기 기준)")
  
    # st.markdown("홈팀 : "+home[0])
   
    dfhs = iljaseq_home(len(hilja))

    # st.markdown("원정팀 : "+away[0])
    
    dfas = iljaseq_away(len(ailja))
   
    # plt.rcParams['font.family'] = 'NanumGothic'
    # plt.rcParams['axes.unicode_minus'] = False
    try: 
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
            plt.yticks(range(0, 21, 1))  # 1부터 10까지 1씩 증가
            plt.gca().invert_yaxis()  # 순위 축 반전 (1이 가장 위로)

            # 그리드 추가
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            st.pyplot(fig)

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
            plt.yticks(range(0, 21, 1))  # 1부터 10까지 1씩 증가
            plt.gca().invert_yaxis()  # 순위 축 반전 (1이 가장 위로)

            # 그리드 추가
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            st.pyplot(fig)

    except:
        # tab1, tab2 = st.tabs(["홈팀", "원정팀"])
        # with tab1:
        #     pass
        # with tab2:
        #     pass
        pass