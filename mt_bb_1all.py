import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
import plotly.graph_objects as go

def Crawler(yearc,countc,gyungi):
    
    home = ''
    away = ''
    hseq = ''
    aseq = ''
    hsjum = ''
    asjum = ''
    hwin = ''
    hdraw = ''
    hlose = ''
    awin = ''
    adraw = ''
    alose = ''
    hcha = ''
    acha = ''
    hyeon = ''
    ayeon = ''
    htayul = ''
    atayul = ''
    hjachek = ''
    ajachek = ''
    hduk = ''
    aduk = ''
    hpduk = ''
    apduk = ''
    htotal = ''
    atotal = ''
    hhomerun = ''
    ahomerun = ''
    hhit = ''
    ahit = ''
    hrun = ''
    arun = ''
    htalsam = ''
    atalsam = ''
    hsil = ''
    asil = ''
    hrten = ''
    arten = ''
    htgubun = ''
    atgubun = ''
    hgigu = ''
    agigu = ''
    hpitcher = ''
    apitcher = ''
    hpjachek = ''
    apjachek = ''
    hptotal = ''
    aptotal = ''
    hpwin = ''
    apwin = ''
    hplose = ''
    aplose = ''
    win = ''
    draw = ''
    lose = ''
    result = ''
    fwin = ''
    fdraw = ''
    flose = ''

    ghseq = []
    gaseq = []
    ghplay = []
    gaplay = []
    ghduk = []
    gaduk = []
    ghdoru = []
    gadoru = []
    ghtayul = []
    gatayul = []
    ghtotal = []
    gatotal = []
    ghtasu = []
    gatasu = []
    ghhit = []
    gahit = []
    ghhomerun = []
    gahomerun = []
    ghtajum = []
    gatajum = []
    ghfball = []
    gafball = []
    ghsamjin = []
    gasamjin = []
    ghchulru = []
    gachulru = []
    ghjangta = []
    gajangta = []
    shpos = []
    sapos = []
    shplay = []
    saplay = []
    shduk = []
    saduk = []
    shdoru = []
    sadoru = []
    shtayul = []
    satayul = []
    shtasu = []
    satasu = []
    shhit = []
    sahit = []
    shhomerun = []
    sahomerun = []
    shtajum = []
    satajum = []
    shfball = []
    safball = []
    thpos = []
    tapos = []
    thplay = []
    taplay = []
    thjachek = []
    tajachek = []
    thwin = []
    tawin = []
    thlose = []
    talose = []
    thsave = []
    tasave = []
    thhold = []
    tahold = []
    thinning = []
    tainning = []
    thtalsam = []
    tatalsam = []

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

    year = int(yearc)
    count = int(countc)
    i = int(gyungi)

    if i < 10:
        k = '0' + str(gyungi)
    else:
        k = str(gyungi)

    def read_txt(g,k):
        if g == '01':
            f = open('baseball_bb1_teamhome.txt', 'r', encoding='UTF8')
        elif g == '02':
            f = open('baseball_bb1_teamaway.txt', 'r', encoding='UTF8')
        elif g == '03':
            f = open('baseball_bb1_onehome.txt', 'r', encoding='UTF8')
        elif g == '04':
            f = open('baseball_bb1_oneaway.txt', 'r', encoding='UTF8')
        elif g == '05':
            f = open('baseball_bb1_pitcherhome.txt', 'r', encoding='UTF8')
        elif g == '06':
            f = open('baseball_bb1_pitcheraway.txt', 'r', encoding='UTF8')
        elif g == '07':
            f = open('baseball_bb1_hyunhwang.txt', 'r', encoding='UTF8')

        rdr1 = f.readlines()    

        team_read = '' 
        for line in rdr1:
            if int(line[:2]) == int(k):
                team_read = line[3:]
                break

        f.close

        return team_read
    
    def read_all_txt(g,k):
        if g == '11':
            f = open('baseball_bb1_vstotal.txt', 'r', encoding='UTF8')
        elif g == '12':
            f = open('baseball_bb1_vsseven.txt', 'r', encoding='UTF8')
        elif g == '13':
            f = open('baseball_bb1_sevenhome.txt', 'r', encoding='UTF8')
        elif g == '14':
            f = open('baseball_bb1_sevenaway.txt', 'r', encoding='UTF8')
        elif g == '15':
            f = open('baseball_bb1_tayulhome.txt', 'r', encoding='UTF8')
        elif g == '16':
            f = open('baseball_bb1_tayulaway.txt', 'r', encoding='UTF8')
        elif g == '17':
            f = open('baseball_bb1_playerhhome.txt', 'r', encoding='UTF8')
        elif g == '18':
            f = open('baseball_bb1_playerphome.txt', 'r', encoding='UTF8')
        elif g == '19':
            f = open('baseball_bb1_playerhaway.txt', 'r', encoding='UTF8')
        elif g == '20':
            f = open('baseball_bb1_playerpaway.txt', 'r', encoding='UTF8')
        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            if int(line[:2]) == int(k):
                l = line[3:]
                l = l.replace("\n","")
                team_read.append(l)
                
        f.close

        return team_read

    team_read = read_txt('01',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                l_hgubun = team_read[:r] 
                s = r+1
            elif rcnt == 2:
                l1_hgubun = team_read[s:r] 
                s = r+1
            elif rcnt == 3:
                seq_hteam = team_read[s:r] 
                s = r+1
            elif rcnt == 4:
                tts_hteam = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                inq_hteam = team_read[s:r]
                s = r+1
                seq1_hteam = team_read[s:]

    team_read = read_txt('02',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                l_agubun = team_read[:r] 
                s = r+1
            elif rcnt == 2:
                l1_agubun = team_read[s:r] 
                s = r+1
            elif rcnt == 3:
                seq_ateam = team_read[s:r] 
                s = r+1
            elif rcnt == 4:
                tts_ateam = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                inq_ateam = team_read[s:r]
                s = r+1
                seq1_ateam = team_read[s:]

    team_read = read_txt('03',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                home = team_read[:r]
                s = r+1
            elif rcnt == 2:
                hseq = team_read[s:r]
                s = r+1
            elif rcnt == 3:
                hsjum = team_read[s:r]
                s = r+1
            elif rcnt == 4:
                htotal = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                hwin = team_read[s:r]
                s = r+1
            elif rcnt == 6:
                hlose = team_read[s:r]
                s = r+1
            elif rcnt == 7:
                hdraw = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                hcha = team_read[s:r]
                s = r+1
            elif rcnt == 9:
                hyeon = team_read[s:r]
                s = r+1
            elif rcnt == 10:
                htayul = team_read[s:r]
                s = r+1
            elif rcnt == 11:
                hjachek = team_read[s:r]
                s = r+1
            elif rcnt == 12:
                hduk = team_read[s:r]
                s = r+1
            elif rcnt == 13:
                hpduk = team_read[s:r]
                s = r+1
            elif rcnt == 14:
                hsil = team_read[s:r]
                s = r+1
            elif rcnt == 15:
                hhomerun = team_read[s:r]
                s = r+1
            elif rcnt == 16:
                hhit = team_read[s:r]
                s = r+1
            elif rcnt == 17:
                hrun = team_read[s:r]
                s = r+1
            elif rcnt == 18:
                htalsam = team_read[s:r]
                s = r+1
            elif rcnt == 19:
                hrten = team_read[s:r]
                s = r+1
            elif rcnt == 20:
                htgubun = team_read[s:r]
                s = r+1
                hgigu = team_read[s:]

    team_read = read_txt('04',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                away = team_read[:r]
                s = r+1
            elif rcnt == 2:
                aseq = team_read[s:r]
                s = r+1
            elif rcnt == 3:
                asjum = team_read[s:r]
                s = r+1
            elif rcnt == 4:
                atotal = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                awin = team_read[s:r]
                s = r+1
            elif rcnt == 6:
                alose = team_read[s:r]
                s = r+1
            elif rcnt == 7:
                adraw = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                acha = team_read[s:r]
                s = r+1
            elif rcnt == 9:
                ayeon = team_read[s:r]
                s = r+1
            elif rcnt == 10:
                atayul = team_read[s:r]
                s = r+1
            elif rcnt == 11:
                ajachek = team_read[s:r]
                s = r+1
            elif rcnt == 12:
                aduk = team_read[s:r]
                s = r+1
            elif rcnt == 13:
                apduk = team_read[s:r]
                s = r+1
            elif rcnt == 14:
                asil = team_read[s:r]
                s = r+1
            elif rcnt == 15:
                ahomerun = team_read[s:r]
                s = r+1
            elif rcnt == 16:
                ahit = team_read[s:r]
                s = r+1
            elif rcnt == 17:
                arun = team_read[s:r]
                s = r+1
            elif rcnt == 18:
                atalsam = team_read[s:r]
                s = r+1
            elif rcnt == 19:
                arten = team_read[s:r]
                s = r+1
            elif rcnt == 20:
                atgubun = team_read[s:r]
                s = r+1
                agigu = team_read[s:]
 
    team_read = read_txt('07',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                home = team_read[:r]
                s = r+1
            elif rcnt == 2:
                away = team_read[s:r]
                s = r+1
            elif rcnt == 3:
                win = team_read[s:r]
                s = r+1
            elif rcnt == 4:
                draw = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                lose = team_read[s:r]
                s = r+1
            elif rcnt == 6:
                fwin = team_read[s:r]
                s = r+1
            elif rcnt == 7:
                fdraw = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                flose = team_read[s:r]
                s = r+1
                result = team_read[s:]   
   
    team_read = read_txt('05',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                home = team_read[:r]
                s = r+1
            elif rcnt == 2:
                hpitcher = team_read[s:r]
                s = r+1
            elif rcnt == 3:
                hpjachek = team_read[s:r]
                s = r+1
            elif rcnt == 4:
                hptotal = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                hpwin = team_read[s:r]
                s = r+1
                hplose = team_read[s:]    
   
    team_read = read_txt('06',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                away = team_read[:r]
                s = r+1
            elif rcnt == 2:
                apitcher = team_read[s:r]
                s = r+1
            elif rcnt == 3:
                apjachek = team_read[s:r]
                s = r+1
            elif rcnt == 4:
                aptotal = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                apwin = team_read[s:r]
                s = r+1
                aplose = team_read[s:]
    
    ssh = str(year) + "년 야구 승1패 " + str(count) + "회차"
    st.subheader(ssh)

    sh = str(i) + "경기"
    st.subheader(sh)
    
    df = pd.DataFrame(data=np.array([[home,hseq,hsjum,htotal,hwin,hlose,hdraw,hcha,hyeon,htayul,
                                      hjachek,hduk,hpduk,hsil,hhomerun,hhit,hrun,htalsam,hrten,htgubun,hgigu],
                                     [away,aseq,asjum,atotal,awin,alose,adraw,acha,ayeon,atayul,
                                      ajachek,aduk,apduk,asil,ahomerun,ahit,arun,atalsam,arten,atgubun,agigu]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","순위","승률","경기수","승","패","무","게임차","연속","타율","평균자책","득점","평균득점","실점","홈런","안타","도루",
                     "탈삼진","최근10경기","리그","지구"]) 

    st.dataframe(df, use_container_width=True)

    colors = ['#FFA07A', '#F0E68C', '#87CEFA']
    labels = ['승','무','패']
    values = [hwin, hdraw, hlose]

    figh = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figh.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    values = [awin, adraw, alose]

    figa = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figa.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    if st.button("리그전적 그래프보기"):       
        tab1, tab2 = st.tabs(["홈팀 전적", "원정팀 전적"])
        with tab1:
            st.plotly_chart(figh)
        with tab2:
            try:
                st.plotly_chart(figa)
            except:
                st.plotly_chart(figa, theme=None)     
     
        if st.button("리그전적 그래프닫기"):  
            pass      
    
    def baedang():
  
        index = [home]
        원정팀 = [away]
        승 = [win]
        일 = [draw]
        패 = [lose]
        해외승 = [fwin]
        해외패 = [flose]
        결과 = [result]

        # 딕셔너리로 데이터 구성
        data = {
            "원정팀": 원정팀,
            "승": 승,
            "①": 일,
            "패": 패,
            "해외승": 해외승,
            "해외패": 해외패,
            "결과": 결과
        }

        # DataFrame 생성
        dfh = pd.DataFrame(data, index=pd.Index(index, name="홈팀"))
    
        return dfh

    st.markdown(":basketball: :blue[**투표 현황**]")
    dfh = baedang()
   
    st.dataframe(dfh, use_container_width=True) 

    win = win.replace('%','')
    draw = draw.replace('%','')
    lose = lose.replace('%','')
    labels = ['승','①','패']
    values = [win, draw, lose]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    if st.button("투표현황 그래프보기"):            
        try:
            st.plotly_chart(fig)
        except:
            st.plotly_chart(fig, theme=None)

        if st.button("투표현황 그래프닫기"): 
            pass           

    st.markdown(":baseball: :blue[**선발투수**]") 

    df = pd.DataFrame(data=np.array([[home,hpitcher,hpjachek,hptotal,hpwin,hplose],
                                     [away,apitcher,apjachek,aptotal,apwin,aplose]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","선발투수","평균자책","이닝수","승","패"]) 

    st.dataframe(df, use_container_width=True)

    # 맞대결 전체
    team_read = read_all_txt('11',k)

    hil_list = []
    hteam_list = []
    hateam_list = []
    hjumsu1_list = []
    hjumsu2_list = []
    hwdl_list = []
    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    hil_list.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    hteam_list.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    hateam_list.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    hjumsu1_list.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    hjumsu2_list.append(team_read[q][s:r])
                    s = r+1
                    hwdl_list.append(team_read[q][s:])

    def hwdl_def(gamesu):
        hwdl = [''] * gamesu
        cntw = 0
        cntd = 0
        cntl = 0
        for i in range(gamesu): 
            if float(hwdl_list[i]) == 3:
                hwdl[i] = "승"
                cntw += 1
            elif float(hwdl_list[i]) == 2 or float(hwdl_list[i]) == 1 or float(hwdl_list[i]) == 1.5:
                hwdl[i] = "①"
                cntd += 1
            elif float(hwdl_list[i]) == 0:
                hwdl[i] = "패"
                cntl += 1

        wdlk = ''
        wdlk = str(cntw)+"승"+str(cntd)+"①"+str(cntl)+"패"

        return hwdl, wdlk, cntw, cntd, cntl    
    
    hwdl,wdlk, cntw, cntd, cntl = hwdl_def(len(hwdl_list))
      
    st.markdown(":baseball: :blue[**맞대결**]") 
    st.markdown(" 전 체 : "+wdlk)     

    # 맞대결 최근 7경기 
    team_read = read_all_txt('12',k)

    hil_list = []
    hteam_list = []
    hateam_list = []
    hjumsu1_list = []
    hjumsu2_list = []
    hwdl_list = []

    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    hil_list.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    hteam_list.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    hateam_list.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    hjumsu1_list.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    hjumsu2_list.append(team_read[q][s:r])
                    s = r+1
                    hwdl_list.append(team_read[q][s:])

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    hwdl,wdlk, cntwm, cntdm, cntlm = hwdl_def(len(hwdl_list))
   
    st.markdown(" 최근7경기 : "+wdlk)
 
    df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

        index= ["일자","점수","결과"],
        columns=["1","2","3","4","5","6","7"]) 
    
    st.dataframe(df, use_container_width=True)
    
    values = [cntw, cntd, cntl]

    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    values = [cntwm, cntdm, cntlm]

    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    if st.button("맞대결 그래프보기"):         
        tab1, tab2 = st.tabs(["맞대결 전체", "맞대결 최근7경기"])    
        with tab1:
            try:
                st.plotly_chart(fig1)
            except:
                try:
                    st.plotly_chart(fig1, theme=None)
                except:
                    pass
        with tab2:
            try:
                st.plotly_chart(fig2)
            except:
                try:
                    st.plotly_chart(fig2, theme=None)
                except:
                    pass
                
        if st.button("맞대결 그래프닫기"): 
            pass     

    # 최근 7경기
    team_read = read_all_txt('13',k)
    
    hil_list = []
    hteam_list = []
    hateam_list = []
    hjumsu1_list = []
    hjumsu2_list = []
    hwdl_list = []

    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    hil_list.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    hteam_list.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    hateam_list.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    hjumsu1_list.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    hjumsu2_list.append(team_read[q][s:r])
                    s = r+1
                    hwdl_list.append(team_read[q][s:])

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    hwdl,wdlk, cntwmh, cntdmh, cntlmh = hwdl_def(len(hwdl_list))
      
    st.markdown(":baseball: :blue[**최근7경기**]") 
    st.markdown("홈팀 : "+home+"("+wdlk+")")

    df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

        index= ["일자","상대","점수","결과"], 
        columns=["1","2","3","4","5","6","7"]) 
    
    st.dataframe(df, use_container_width=True)   
  
    team_read = read_all_txt('14',k)
    
    hil_list = []
    hteam_list = []
    hateam_list = []
    hjumsu1_list = []
    hjumsu2_list = []
    hwdl_list = []

    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    hil_list.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    hteam_list.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    hateam_list.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    hjumsu1_list.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    hjumsu2_list.append(team_read[q][s:r])
                    s = r+1
                    hwdl_list.append(team_read[q][s:])

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    hwdl,wdlk, cntwma, cntdma, cntlma = hwdl_def(len(hwdl_list))
    
    st.markdown("원정팀 : "+away+"("+wdlk+")")
    
    df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

        index= ["일자","상대","점수","결과"], 
        columns=["1","2","3","4","5","6","7"]) 
    
    st.dataframe(df, use_container_width=True) 
 
    values = [cntwmh, cntdmh, cntlmh]
    fig3 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
  
    values = [cntwma, cntdma, cntlma]
    fig4 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    if st.button("최근7경기 그래프보기"):        
        tab1, tab2 = st.tabs(["홈팀 최근7경기", "원정팀 최근7경기"])
        with tab1:
            try:
                st.plotly_chart(fig3)
            except:
                try:
                    st.plotly_chart(fig3, theme=None)
                except:
                    pass
        with tab2:
            try:
                st.plotly_chart(fig4)
            except:
                try:
                    st.plotly_chart(fig4, theme=None)
                except:
                    pass
                
        if st.button("최근7경기 그래프닫기"):     
            pass  

    def gaein_home(num_rows):
  
        index = [ghplay[i] for i in range(num_rows)]
        순위 = [ghseq[i] for i in range(num_rows)]
        타율 = [ghtayul[i] for i in range(num_rows)]
        홈런 = [ghhomerun[i] for i in range(num_rows)]
        타점 = [ghtajum[i] for i in range(num_rows)]
        안타 = [ghhit[i] for i in range(num_rows)]
        득점 = [ghduk[i] for i in range(num_rows)]
        도루 = [ghdoru[i] for i in range(num_rows)]
        볼넷 = [ghfball[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            "순위": 순위,
            "타율": 타율,
            "홈런": 홈런,
            "타점": 타점,
            "안타": 안타,
            "득점": 득점,
            "도루": 도루,
            "볼넷": 볼넷
        }

        # DataFrame 생성
        df = pd.DataFrame(data, index=pd.Index(index, name="선수명"))
        st.dataframe(df, use_container_width=True)
            
    team_read = read_all_txt('15',k)
    
    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    ghseq.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    ghplay.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    ghtayul.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    ghhomerun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    ghtajum.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    ghhit.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    ghduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    ghdoru.append(team_read[q][s:r])
                    s = r+1
                    ghfball.append(team_read[q][s:])

    if len(ghplay) == 0:
        pass
    else:  
        st.markdown(":baseball: :blue[**타율순위**]")  
           
        st.markdown("홈팀 : "+home+"("+str(len(ghplay))+"명)")

        gaein_home(len(ghplay))
     
    def gaein_away(num_rows):
  
        index = [gaplay[i] for i in range(num_rows)]
        순위 = [gaseq[i] for i in range(num_rows)]
        타율 = [gatayul[i] for i in range(num_rows)]
        홈런 = [gahomerun[i] for i in range(num_rows)]
        타점 = [gatajum[i] for i in range(num_rows)]
        안타 = [gahit[i] for i in range(num_rows)]
        득점 = [gaduk[i] for i in range(num_rows)]
        도루 = [gadoru[i] for i in range(num_rows)]
        볼넷 = [gafball[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            "순위": 순위,
            "타율": 타율,
            "홈런": 홈런,
            "타점": 타점,
            "안타": 안타,
            "득점": 득점,
            "도루": 도루,
            "볼넷": 볼넷
        }

        # DataFrame 생성
        df = pd.DataFrame(data, index=pd.Index(index, name="선수명"))
        st.dataframe(df, use_container_width=True)
            
    team_read = read_all_txt('16',k)
    
    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    gaseq.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    gaplay.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    gatayul.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    gahomerun.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    gatajum.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    gahit.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    gaduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    gadoru.append(team_read[q][s:r])
                    s = r+1
                    gafball.append(team_read[q][s:])
  
    if len(gaplay) == 0:
        pass
    else:
        if len(ghplay) == 0:
            st.markdown(":baseball: :blue[**타율순위**]")  
        st.markdown("원정팀 : "+away+"("+str(len(gaplay))+"명)")
     
        gaein_away(len(gaplay))

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    team_read = read_all_txt('17',k)
    
    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    shplay.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    shpos.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    shhomerun.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    shtayul.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    shtajum.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    shhit.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    shduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    shdoru.append(team_read[q][s:r])
                    s = r+1
                    shfball.append(team_read[q][s:])

    team_read = read_all_txt('18',k)
    
    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    thplay.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    thpos.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    thjachek.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    thwin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    thlose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    thsave.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    thhold.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    thinning.append(team_read[q][s:r])
                    s = r+1
                    thtalsam.append(team_read[q][s:])

    st.markdown(":baseball: :blue[**선수**]")  
    st.markdown("홈팀 : "+home)
     
    def player_homep(num_rows):
  
        index = [thplay[i] for i in range(num_rows)]
        평균자책 = [thjachek[i] for i in range(num_rows)]
        승 = [thwin[i] for i in range(num_rows)]
        패 = [thlose[i] for i in range(num_rows)]
        세이브 = [thsave[i] for i in range(num_rows)]
        홀드 = [thhold[i] for i in range(num_rows)]
        이닝 = [thinning[i] for i in range(num_rows)]
        탈삼진 = [thtalsam[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            "평균자책": 평균자책,
            "승": 승,
            "패": 패,
            "세이브": 세이브,
            "홀드": 홀드,
            "이닝": 이닝,
            "탈삼진": 탈삼진
        }

        # DataFrame 생성
        dfhp = pd.DataFrame(data, index=pd.Index(index, name="투수명"))
    
        return dfhp   
     
    def player_homeh(num_rows):
  
        index = [shplay[i] for i in range(num_rows)]
        포지션 = [shpos[i] for i in range(num_rows)]
        홈런 = [shhomerun[i] for i in range(num_rows)]
        타율 = [shtayul[i] for i in range(num_rows)]
        타점 = [shtajum[i] for i in range(num_rows)]
        안타 = [shhit[i] for i in range(num_rows)]
        득점 = [shduk[i] for i in range(num_rows)]
        도루 = [shdoru[i] for i in range(num_rows)]
        볼넷 = [shfball[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            "포지션": 포지션,
            "홈런": 홈런,
            "타율": 타율,
            "타점": 타점,
            "안타": 안타,
            "득점": 득점,
            "도루": 도루,
            "볼넷": 볼넷
        }

        # DataFrame 생성
        dfhh = pd.DataFrame(data, index=pd.Index(index, name="타자명"))
    
        return dfhh   
    
    dfhp = player_homep(len(thplay))  
    dfhh = player_homeh(len(shplay))  
    
    tab1, tab2 = st.tabs(["투수", "타자"])
    with tab1:
        st.dataframe(dfhp, use_container_width=True, height=1000)      
    with tab2:
        st.dataframe(dfhh, use_container_width=True, height=1000)   

    team_read = read_all_txt('19',k)
    
    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    saplay.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    sapos.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    sahomerun.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    satayul.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    satajum.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    sahit.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    saduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    sadoru.append(team_read[q][s:r])
                    s = r+1
                    safball.append(team_read[q][s:])

    team_read = read_all_txt('20',k)
    
    for q in range(len(team_read)):
        rcnt = 0
        for r in range(len(team_read[q])):
            if team_read[q][r] == ";":
                rcnt += 1
                if rcnt == 1:
                    taplay.append(team_read[q][:r]) 
                    s = r+1
                elif rcnt == 2:
                    tapos.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 3:
                    tajachek.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    tawin.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    talose.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    tasave.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    tahold.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    tainning.append(team_read[q][s:r])
                    s = r+1
                    tatalsam.append(team_read[q][s:])

    st.markdown("원정팀 : "+away)
      
    def player_awayp(num_rows):
  
        index = [taplay[i] for i in range(num_rows)]
        평균자책 = [tajachek[i] for i in range(num_rows)]
        승 = [tawin[i] for i in range(num_rows)]
        패 = [talose[i] for i in range(num_rows)]
        세이브 = [tasave[i] for i in range(num_rows)]
        홀드 = [tahold[i] for i in range(num_rows)]
        이닝 = [tainning[i] for i in range(num_rows)]
        탈삼진 = [tatalsam[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            "평균자책": 평균자책,
            "승": 승,
            "패": 패,
            "세이브": 세이브,
            "홀드": 홀드,
            "이닝": 이닝,
            "탈삼진": 탈삼진
        }

        # DataFrame 생성
        dfap = pd.DataFrame(data, index=pd.Index(index, name="투수명"))
    
        return dfap    
    
    def player_awayh(num_rows):
  
        index = [saplay[i] for i in range(num_rows)]
        포지션 = [sapos[i] for i in range(num_rows)]
        홈런 = [sahomerun[i] for i in range(num_rows)]
        타율 = [satayul[i] for i in range(num_rows)]
        타점 = [satajum[i] for i in range(num_rows)]
        안타 = [sahit[i] for i in range(num_rows)]
        득점 = [saduk[i] for i in range(num_rows)]
        도루 = [sadoru[i] for i in range(num_rows)]
        볼넷 = [safball[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            "포지션": 포지션,
            "홈런": 홈런,
            "타율": 타율,
            "타점": 타점,
            "안타": 안타,
            "득점": 득점,
            "도루": 도루,
            "볼넷": 볼넷
        }

        # DataFrame 생성
        dfah = pd.DataFrame(data, index=pd.Index(index, name="타자명"))
    
        return dfah   
    
    dfap = player_awayp(len(taplay))  
    dfah = player_awayh(len(saplay))  
    
    tab1, tab2 = st.tabs(["투수", "타자"])
    with tab1:
        st.dataframe(dfap, use_container_width=True, height=1000)      
    with tab2:
        st.dataframe(dfah, use_container_width=True, height=1000)   
