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
 
    ssh = str(year) + "년 야구 승1패 " + str(count) + "회차"
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
    hcha = []
    acha = []
    hyeon = []
    ayeon = []
    htayul = []
    atayul = []
    hjachek = []
    ajachek = []
    hduk = []
    aduk = []
    hpduk = []
    apduk = []
    htotal = []
    atotal = []
    hhomerun = []
    ahomerun = []
    hhit = []
    ahit = []
    hrun = []
    arun = []
    htalsam = []
    atalsam = []
    hsil = []
    asil = []
    hrten = []
    arten = []
    htgubun = []
    atgubun = []
    hgigu = []
    agigu = []
    hilja = []
    ailja = []

    def read_all_txt(g,k):
        if g == '11':
            f = open('baseball_bb9_sseqhome.txt', 'r', encoding='UTF8')
        elif g == '12':
            f = open('baseball_bb9_sseqaway.txt', 'r', encoding='UTF8')

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
                    hdraw.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    hcha.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    hyeon.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    htayul.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 11:
                    hjachek.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 12:
                    hduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 13:
                    hpduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 14:
                    hsil.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 15:
                    hhomerun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 16:
                    hhit.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 17:
                    hrun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 18:
                    htalsam.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 19:
                    hrten.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 20:
                    htgubun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 21:
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
                    adraw.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    acha.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    ayeon.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    atayul.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 11:
                    ajachek.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 12:
                    aduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 13:
                    apduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 14:
                    asil.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 15:
                    ahomerun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 16:
                    ahit.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 17:
                    arun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 18:
                    atalsam.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 19:
                    arten.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 20:
                    atgubun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 21:
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
        무 = [hdraw[i] for i in range(num_rows)]
        승차 = [hcha[i] for i in range(num_rows)]
        득점 = [hduk[i] for i in range(num_rows)]
        실점 = [hsil[i] for i in range(num_rows)]
        평균득점 = [hpduk[i] for i in range(num_rows)]
        연속 = [hyeon[i] for i in range(num_rows)]
        타율 = [htayul[i] for i in range(num_rows)]
        자책 = [hjachek[i] for i in range(num_rows)]
        홈런 = [hhomerun[i] for i in range(num_rows)]
        안타 = [hhit[i] for i in range(num_rows)]
        도루 = [hrun[i] for i in range(num_rows)]
        탈삼진 = [htalsam[i] for i in range(num_rows)]
        최근10경기 = [hrten[i] for i in range(num_rows)]
        리그 = [htgubun[i] for i in range(num_rows)]
        지구 = [hgigu[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            # "선수": 선수,
            "순위": 순위,
            "경기수": 경기수,
            "승률": 승률,
            "승": 승,
            "패": 패,
            "무": 무,
            "승차": 승차,
            "득점": 득점,
            "실점": 실점,
            "평균득점": 평균득점,
            "연속": 연속,
            "타율": 타율,
            "자책": 자책,
            "홈런": 홈런,
            "안타": 안타,
            "도루": 도루,
            "탈삼진": 탈삼진,
            "최근10경기": 최근10경기,
            "리그": 리그,
            "지구": 지구
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
        무 = [adraw[i] for i in range(num_rows)]
        승차 = [acha[i] for i in range(num_rows)]
        득점 = [aduk[i] for i in range(num_rows)]
        평균득점 = [apduk[i] for i in range(num_rows)]
        실점 = [asil[i] for i in range(num_rows)]
        연속 = [ayeon[i] for i in range(num_rows)]
        타율 = [atayul[i] for i in range(num_rows)]
        자책 = [ajachek[i] for i in range(num_rows)]
        홈런 = [ahomerun[i] for i in range(num_rows)]
        안타 = [ahit[i] for i in range(num_rows)]
        도루 = [arun[i] for i in range(num_rows)]
        탈삼진 = [atalsam[i] for i in range(num_rows)]
        최근10경기 = [arten[i] for i in range(num_rows)]
        리그 = [atgubun[i] for i in range(num_rows)]
        지구 = [agigu[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            # "선수": 선수,
            "순위": 순위,
            "경기수": 경기수,
            "승률": 승률,
            "승": 승,
            "패": 패,
            "무": 무,
            "승차": 승차,
            "득점": 득점,
            "실점": 실점,
            "평균득점": 평균득점,
            "연속": 연속,
            "타율": 타율,
            "자책": 자책,
            "홈런": 홈런,
            "안타": 안타,
            "도루": 도루,
            "탈삼진": 탈삼진,
            "최근10경기": 최근10경기,
            "리그": 리그,
            "지구": 지구
        }

        # DataFrame 생성
        dfas = pd.DataFrame(data, index=pd.Index(index, name="일자"))

        return dfas


    st.markdown(":baseball: :blue[**일별 순위 추이**] (최대 10경기 기준)")
  
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
            plt.xlabel('DATE', fontsize=10)
            plt.ylabel('SEQ', fontsize=10, rotation=360)
            plt.xticks(rotation=45, fontsize=10)
            plt.yticks(fontsize=10)

            # y축 설정
            y_min = dfhs['순위'].min()
            y_max = dfhs['순위'].max()
            plt.yticks(range(0, 12, 1))  # 1부터 10까지 1씩 증가
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
            plt.xlabel('DATE', fontsize=10)
            plt.ylabel('SEQ', fontsize=10, rotation=360)
            plt.xticks(rotation=45, fontsize=10)
            plt.yticks(fontsize=10)

            # y축 설정
            y_min = dfas['순위'].min()
            y_max = dfas['순위'].max()
            # plt.yticks(range(y_min, y_max+1, 1))  # 1부터 10까지 1씩 증가
            plt.yticks(range(0, 12, 1))  # 1부터 10까지 1씩 증가
            plt.gca().invert_yaxis()  # 순위 축 반전 (1이 가장 위로)

            # 그리드 추가
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            st.pyplot(fig)
