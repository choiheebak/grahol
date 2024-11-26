import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
import plotly.graph_objects as go

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
   
    # st.markdown(":basketball: :red[**오디오 - 데이터 예측은 데이터에 따라 수시로 변경될 수 있고, 참고용입니다. 반드시 본인의 선택이 중요하고, 결과에 따른 책임은 본인의 몫입니다.**]")
    # # 오디오 출력
    # audio = 'kaudio_' + str(k) + '.mp3'
    # st.audio(audio, format="audio/mpeg", loop=True)

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
    has = ''
    aas = ''
    hrebound = ''
    arebound = ''
    hduk = ''
    aduk = ''
    hpduk = ''
    apduk = ''
    htotal = ''
    atotal = ''
    hsteal = ''
    asteal = ''
    hblock = ''
    ablock = ''
    htsteal = ''
    atsteal = ''
    hfhrow = ''
    afhrow = ''
    hfhrows = ''
    afhrows = ''
    hhwin = ''
    ahwin = ''
    htgubun = ''
    atgubun = ''
    hgigu = ''
    agigu = ''
    hhlose = ''
    ahlose = ''
    hawin = ''
    aawin = ''
    halose = ''
    aalose = ''
    hdwin = ''
    adwin = ''
    hdlose = ''
    adlose = ''
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
    ghassist = []
    gaassist = []
    ghrebound = []
    garebound = []
    ghtotal = []
    gatotal = []
    ghsteal = []
    gasteal = []
    ghblock = []
    gablock = []
    ghyatoo = []
    gayatoo = []
    ghtpoint = []
    gatpoint = []
    ghfthrow = []
    gafthrow = []
    ghyatoos = []
    gayatoos = []
    ghtpoints = []
    gatpoints = []
    ghfthrows = []
    gafthrows = []

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

    def read_txt(g,k):
        if g == '01':
            f = open('basketball_bk1_teamhome.txt', 'r', encoding='UTF8')
        elif g == '02':
            f = open('basketball_bk1_teamaway.txt', 'r', encoding='UTF8')
        elif g == '03':
            f = open('basketball_bk1_onehome.txt', 'r', encoding='UTF8')
        elif g == '04':
            f = open('basketball_bk1_oneaway.txt', 'r', encoding='UTF8')
        elif g == '05':
            f = open('basketball_bk1_hyunhwang.txt', 'r', encoding='UTF8')

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
            f = open('basketball_bk1_vstotal.txt', 'r', encoding='UTF8')
        elif g == '12':
            f = open('basketball_bk1_vsseven.txt', 'r', encoding='UTF8')
        elif g == '13':
            f = open('basketball_bk1_sevenhome.txt', 'r', encoding='UTF8')
        elif g == '14':
            f = open('basketball_bk1_sevenaway.txt', 'r', encoding='UTF8')
        elif g == '15':
            f = open('basketball_bk1_dukhome.txt', 'r', encoding='UTF8')
        elif g == '16':
            f = open('basketball_bk1_dukaway.txt', 'r', encoding='UTF8')

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
                hcha = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                hduk = team_read[s:r]
                s = r+1
            elif rcnt == 9:
                has = team_read[s:r]
                s = r+1
            elif rcnt == 10:
                hrebound = team_read[s:r]
                s = r+1
            elif rcnt == 11:
                hsteal = team_read[s:r]
                s = r+1
            elif rcnt == 12:
                hblock = team_read[s:r]
                s = r+1
            elif rcnt == 13:
                htsteal = team_read[s:r]
                s = r+1
            elif rcnt == 14:
                hfhrow = team_read[s:r]
                s = r+1
            elif rcnt == 15:
                hfhrows = team_read[s:r]
                s = r+1
            elif rcnt == 16:
                hhwin = team_read[s:r]
                s = r+1
            elif rcnt == 17:
                hhlose = team_read[s:r]
                s = r+1
            elif rcnt == 18:
                hawin = team_read[s:r]
                s = r+1
            elif rcnt == 19:
                halose = team_read[s:r]
                s = r+1
            elif rcnt == 20:
                hdwin = team_read[s:r]
                s = r+1
            elif rcnt == 21:
                hdlose = team_read[s:r]
                s = r+1
            elif rcnt == 22:
                hyeon = team_read[s:r]
                s = r+1
            elif rcnt == 23:
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
                acha = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                aduk = team_read[s:r]
                s = r+1
            elif rcnt == 9:
                aas = team_read[s:r]
                s = r+1
            elif rcnt == 10:
                arebound = team_read[s:r]
                s = r+1
            elif rcnt == 11:
                asteal = team_read[s:r]
                s = r+1
            elif rcnt == 12:
                ablock = team_read[s:r]
                s = r+1
            elif rcnt == 13:
                atsteal = team_read[s:r]
                s = r+1
            elif rcnt == 14:
                afhrow = team_read[s:r]
                s = r+1
            elif rcnt == 15:
                afhrows = team_read[s:r]
                s = r+1
            elif rcnt == 16:
                ahwin = team_read[s:r]
                s = r+1
            elif rcnt == 17:
                ahlose = team_read[s:r]
                s = r+1
            elif rcnt == 18:
                aawin = team_read[s:r]
                s = r+1
            elif rcnt == 19:
                aalose = team_read[s:r]
                s = r+1
            elif rcnt == 20:
                adwin = team_read[s:r]
                s = r+1
            elif rcnt == 21:
                adlose = team_read[s:r]
                s = r+1
            elif rcnt == 22:
                ayeon = team_read[s:r]
                s = r+1
            elif rcnt == 23:
                atgubun = team_read[s:r]
                s = r+1
                agigu = team_read[s:]

    team_read = read_txt('05',k)

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
  
    df = pd.DataFrame(data=np.array([[home,hseq,hsjum,htotal,hwin,hlose,hcha,hduk,has,hrebound,hsteal,
                                      hblock,htsteal,hfhrow,hfhrows,hhwin,hhlose,hawin,halose,hdwin,hdlose,hyeon,
                                      htgubun,hgigu],
                                     [away,aseq,asjum,atotal,awin,alose,acha,aduk,aas,arebound,asteal,
                                      ablock,atsteal,afhrow,afhrows,ahwin,ahlose,aawin,aalose,adwin,adlose,ayeon,
                                      atgubun,agigu]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","순위","승률","경기수","승","패","승차","득점","AS","리바운드","스틸","블록","3점슛","자유투","자유투성공","홈승","홈패",
                     "원정승","원정패","디비전승","디비전패","연속","리그","디비전"]) 
 
    st.dataframe(df, use_container_width=True)

    colors = ['#FFA07A', '#F0E68C', '#87CEFA']
    labels = ['승','무','패']
    values = [hwin, hdraw, hlose]

    figh = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figh.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    values = [awin, adraw, alose]

    figa = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figa.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    tab1, tab2 = st.tabs(["홈팀 전적", "원정팀 전적"])
    with tab1:
        st.plotly_chart(figh)
    with tab2:
        try:
            st.plotly_chart(figa)
        except:
            st.plotly_chart(figa, theme=None)
      
    def baedang():
  
        index = [home]
        원정팀 = [away]
        승 = [win]
        오 = [draw]
        패 = [lose]
        해외승 = [fwin]
        해외패 = [flose]
        결과 = [result]

        # 딕셔너리로 데이터 구성
        data = {
            "원정팀": 원정팀,
            "승": 승,
            "⑤": 오,
            "패": 패,
            "해외승": 해외승,
            "해외패": 해외패,
            "결과": 결과
        }

        # DataFrame 생성
        dfh = pd.DataFrame(data, index=pd.Index(index, name="홈팀"))
    
        return dfh

    st.markdown(":basketball: :blue[**투표 현황**] (* 발매일 이전 승5패 배당은 데이터 기준 예측임)")
    dfh = baedang()
   
    st.dataframe(dfh, use_container_width=True) 

    win = win.replace('%','')
    draw = draw.replace('%','')
    lose = lose.replace('%','')
    labels = ['승','⑤','패']
    values = [win, draw, lose]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    try:
        st.plotly_chart(fig)
    except:
        st.plotly_chart(fig, theme=None)

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
            if int(hwdl_list[i]) == 3:
                hwdl[i] = "승"
                cntw += 1
            elif int(hwdl_list[i]) == 2 or int(hwdl_list[i]) == 1:
                hwdl[i] = "⑤"
                cntd += 1
            elif int(hwdl_list[i]) == 0:
                hwdl[i] = "패"
                cntl += 1

        wdlk = ''
        wdlk = str(cntw)+"승"+str(cntd)+"⑤"+str(cntl)+"패"

        return hwdl, wdlk, cntw, cntd, cntl    
    
    hwdl,wdlk, cntw, cntd, cntl = hwdl_def(len(hwdl_list))
     
    st.markdown(":basketball: :blue[**맞대결**]")
    st.markdown(" 전 체 : "+wdlk)     

    # 맞대결 7경기
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
    
    st.markdown(":basketball: :blue[**최근7경기**]")
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

    def gaein_home(num_rows):
  
        index = [ghplay[i] for i in range(num_rows)]
        순위 = [ghseq[i] for i in range(num_rows)]
        출장시간 = [ghtotal[i] for i in range(num_rows)]
        득점 = [ghduk[i] for i in range(num_rows)]
        어시스트 = [ghassist[i] for i in range(num_rows)]
        리바운드 = [ghrebound[i] for i in range(num_rows)]
        스틸 = [ghsteal[i] for i in range(num_rows)]
        블락슛 = [ghblock[i] for i in range(num_rows)]
        야투 = [ghyatoo[i] for i in range(num_rows)]
        삼점슛 = [ghtpoint[i] for i in range(num_rows)]
        자유투 = [ghfthrow[i] for i in range(num_rows)]
        야투성공 = [ghyatoos[i] for i in range(num_rows)]
        삼점슛성공 = [ghtpoints[i] for i in range(num_rows)]
        자유투성공 = [ghfthrows[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            "순위": 순위,
            "출장시간": 출장시간,
            "득점": 득점,
            "어시스트": 어시스트,
            "리바운드": 리바운드,
            "스틸": 스틸,
            "블락슛": 블락슛,
            "야투": 야투,
            "삼점슛": 삼점슛,
            "자유투": 자유투,
            "야투성공": 야투성공,
            "삼점슛성공": 삼점슛성공,
            "자유투성공": 자유투성공
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
                    ghtotal.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    ghduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    ghassist.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    ghrebound.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    ghsteal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    ghblock.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    ghyatoo.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    ghtpoint.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 11:
                    ghfthrow.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 12:
                    ghyatoos.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 13:
                    ghtpoints.append(team_read[q][s:r])
                    s = r+1
                    ghfthrows.append(team_read[q][s:])

    if len(ghplay) == 0:
        pass
    else:
        st.markdown(":basketball: :blue[**득점순위**]")
             
        st.markdown("홈팀 : "+home+"("+str(len(ghplay))+"명)")

        gaein_home(len(ghplay))
 
    def gaein_away(num_rows):
  
        index = [gaplay[i] for i in range(num_rows)]
        순위 = [gaseq[i] for i in range(num_rows)]
        출장시간 = [gatotal[i] for i in range(num_rows)]
        득점 = [gaduk[i] for i in range(num_rows)]
        어시스트 = [gaassist[i] for i in range(num_rows)]
        리바운드 = [garebound[i] for i in range(num_rows)]
        스틸 = [gasteal[i] for i in range(num_rows)]
        블락슛 = [gablock[i] for i in range(num_rows)]
        야투 = [gayatoo[i] for i in range(num_rows)]
        삼점슛 = [gatpoint[i] for i in range(num_rows)]
        자유투 = [gafthrow[i] for i in range(num_rows)]
        야투성공 = [gayatoos[i] for i in range(num_rows)]
        삼점슛성공 = [gatpoints[i] for i in range(num_rows)]
        자유투성공 = [gafthrows[i] for i in range(num_rows)]

        # 딕셔너리로 데이터 구성
        data = {
            "순위": 순위,
            "출장시간": 출장시간,
            "득점": 득점,
            "어시스트": 어시스트,
            "리바운드": 리바운드,
            "스틸": 스틸,
            "블락슛": 블락슛,
            "야투": 야투,
            "삼점슛": 삼점슛,
            "자유투": 자유투,
            "야투성공": 야투성공,
            "삼점슛성공": 삼점슛성공,
            "자유투성공": 자유투성공
        }

        # DataFrame 생성
        df = pd.DataFrame(data, index=pd.Index(index, name="선수명"))
        # stremlit 출력
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
                    gatotal.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    gaduk.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    gaassist.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    garebound.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    gasteal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    gablock.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    gayatoo.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    gatpoint.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 11:
                    gafthrow.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 12:
                    gayatoos.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 13:
                    gatpoints.append(team_read[q][s:r])
                    s = r+1
                    gafthrows.append(team_read[q][s:])
        
    if len(gaplay) == 0:
        pass
    else:
        if len(ghplay) == 0:
            st.markdown(":basketball: :blue[**득점순위**]")
             
        st.markdown("원정팀 : "+away+"("+str(len(gaplay))+"명)")
        
        gaein_away(len(gaplay))
