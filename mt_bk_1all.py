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

    year = int(yearc)
    count = int(countc)
    i = int(gyungi)

    if i < 10:
        k = '0' + str(gyungi)
    else:
        k = str(gyungi)

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
   
    ssh = str(year) + "년 농구 승5패 " + str(count) + "회차"
    st.subheader(ssh)

    sh = str(i) + "경기"
    st.subheader(sh)
   
    df = pd.DataFrame(data=np.array([[home,hseq,hsjum,htotal,hwin,hlose,hcha,hduk,has,hrebound,hsteal,
                                      hblock,htsteal,hfhrow,hfhrows,hhwin,hhlose,hawin,halose,hdwin,hdlose,hyeon,
                                      htgubun,hgigu],
                                     [away,aseq,asjum,atotal,awin,alose,acha,aduk,aas,arebound,asteal,
                                      ablock,atsteal,afhrow,afhrows,ahwin,ahlose,aawin,aalose,adwin,adlose,ayeon,
                                      atgubun,agigu]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","순위","승률","경기수","승","패","승차","득점","AS","리바운드","스틸","블록","3점슛","자유투","자유투성공","홈승","홈패",
                     "원정승","원정패","디비전승","디비전패","연속","리그","디비전"]) 
 
    st.dataframe(df)

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
     
    st.markdown(":basketball: :blue[**투표 현황**]")
    df = pd.DataFrame(data=np.array([[home,away,win,draw,lose,fwin,fdraw,flose,result]]), 

            index= ["현재"], 
            columns=["홈팀","원정팀","승","⑤","패","해외승","해외무","해외패","결과"]) 

    st.dataframe(df)

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
    
    st.dataframe(df)
    
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
    
    st.dataframe(df) 

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
    
    st.dataframe(df) 

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

    def gaein_home(gamesu):

        if gamesu == 7:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3],ghseq[4],ghseq[5],ghseq[6]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3],ghplay[4],ghplay[5],ghplay[6]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2],ghtotal[3],ghtotal[4],ghtotal[5],ghtotal[6]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4],ghduk[5],ghduk[6]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2],ghassist[3],ghassist[4],ghassist[5],ghassist[6]],
                    "리바운드":[ghrebound[0],ghrebound[1],ghrebound[2],ghrebound[3],ghrebound[4],ghrebound[5],ghrebound[6]],
                    "스틸":[ghsteal[0],ghsteal[1],ghsteal[2],ghsteal[3],ghsteal[4],ghsteal[5],ghsteal[6]],
                    "블락슛":[ghblock[0],ghblock[1],ghblock[2],ghblock[3],ghblock[4],ghblock[5],ghblock[6]],
                    "야투":[ghyatoo[0],ghyatoo[1],ghyatoo[2],ghyatoo[3],ghyatoo[4],ghyatoo[5],ghyatoo[6]],
                    "삼점슛":[ghtpoint[0],ghtpoint[1],ghtpoint[2],ghtpoint[3],ghtpoint[4],ghtpoint[5],ghtpoint[6]],
                    "자유투":[ghfthrow[0],ghfthrow[1],ghfthrow[2],ghfthrow[3],ghfthrow[4],ghfthrow[5],ghfthrow[6]],
                    "야투성공":[ghyatoos[0],ghyatoos[1],ghyatoos[2],ghyatoos[3],ghyatoos[4],ghyatoos[5],ghyatoos[6]],
                    "삼점슛성공":[ghtpoints[0],ghtpoints[1],ghtpoints[2],ghtpoints[3],ghtpoints[4],ghtpoints[5],ghtpoints[6]],
                    "자유투성공":[ghfthrows[0],ghfthrows[1],ghfthrows[2],ghfthrows[3],ghfthrows[4],ghfthrows[5],ghfthrows[6]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6","7"], 
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 6:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3],ghseq[4],ghseq[5]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3],ghplay[4],ghplay[5]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2],ghtotal[3],ghtotal[4],ghtotal[5]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4],ghduk[5]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2],ghassist[3],ghassist[4],ghassist[5]],
                    "리바운드":[ghrebound[0],ghrebound[1],ghrebound[2],ghrebound[3],ghrebound[4],ghrebound[5]],
                    "스틸":[ghsteal[0],ghsteal[1],ghsteal[2],ghsteal[3],ghsteal[4],ghsteal[5]],
                    "블락슛":[ghblock[0],ghblock[1],ghblock[2],ghblock[3],ghblock[4],ghblock[5]],
                    "야투":[ghyatoo[0],ghyatoo[1],ghyatoo[2],ghyatoo[3],ghyatoo[4],ghyatoo[5]],
                    "삼점슛":[ghtpoint[0],ghtpoint[1],ghtpoint[2],ghtpoint[3],ghtpoint[4],ghtpoint[5]],
                    "자유투":[ghfthrow[0],ghfthrow[1],ghfthrow[2],ghfthrow[3],ghfthrow[4],ghfthrow[5]],
                    "야투성공":[ghyatoos[0],ghyatoos[1],ghyatoos[2],ghyatoos[3],ghyatoos[4],ghyatoos[5]],
                    "삼점슛성공":[ghtpoints[0],ghtpoints[1],ghtpoints[2],ghtpoints[3],ghtpoints[4],ghtpoints[5]],
                    "자유투성공":[ghfthrows[0],ghfthrows[1],ghfthrows[2],ghfthrows[3],ghfthrows[4],ghfthrows[5]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6"], 
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 5:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3],ghseq[4]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3],ghplay[4]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2],ghtotal[3],ghtotal[4]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2],ghassist[3],ghassist[4]],
                    "리바운드":[ghrebound[0],ghrebound[1],ghrebound[2],ghrebound[3],ghrebound[4]],
                    "스틸":[ghsteal[0],ghsteal[1],ghsteal[2],ghsteal[3],ghsteal[4]],
                    "블락슛":[ghblock[0],ghblock[1],ghblock[2],ghblock[3],ghblock[4]],
                    "야투":[ghyatoo[0],ghyatoo[1],ghyatoo[2],ghyatoo[3],ghyatoo[4]],
                    "삼점슛":[ghtpoint[0],ghtpoint[1],ghtpoint[2],ghtpoint[3],ghtpoint[4]],
                    "자유투":[ghfthrow[0],ghfthrow[1],ghfthrow[2],ghfthrow[3],ghfthrow[4]],
                    "야투성공":[ghyatoos[0],ghyatoos[1],ghyatoos[2],ghyatoos[3],ghyatoos[4]],
                    "삼점슛성공":[ghtpoints[0],ghtpoints[1],ghtpoints[2],ghtpoints[3],ghtpoints[4]],
                    "자유투성공":[ghfthrows[0],ghfthrows[1],ghfthrows[2],ghfthrows[3],ghfthrows[4]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5"], 
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 4:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2],ghtotal[3]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2],ghassist[3]],
                    "리바운드":[ghrebound[0],ghrebound[1],ghrebound[2],ghrebound[3]],
                    "스틸":[ghsteal[0],ghsteal[1],ghsteal[2],ghsteal[3]],
                    "블락슛":[ghblock[0],ghblock[1],ghblock[2],ghblock[3]],
                    "야투":[ghyatoo[0],ghyatoo[1],ghyatoo[2],ghyatoo[3]],
                    "삼점슛":[ghtpoint[0],ghtpoint[1],ghtpoint[2],ghtpoint[3]],
                    "자유투":[ghfthrow[0],ghfthrow[1],ghfthrow[2],ghfthrow[3]],
                    "야투성공":[ghyatoos[0],ghyatoos[1],ghyatoos[2],ghyatoos[3]],
                    "삼점슛성공":[ghtpoints[0],ghtpoints[1],ghtpoints[2],ghtpoints[3]],
                    "자유투성공":[ghfthrows[0],ghfthrows[1],ghfthrows[2],ghfthrows[3]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4"], 
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2]],
                    "리바운드":[ghrebound[0],ghrebound[1],ghrebound[2]],
                    "스틸":[ghsteal[0],ghsteal[1],ghsteal[2]],
                    "블락슛":[ghblock[0],ghblock[1],ghblock[2]],
                    "야투":[ghyatoo[0],ghyatoo[1],ghyatoo[2]],
                    "삼점슛":[ghtpoint[0],ghtpoint[1],ghtpoint[2]],
                    "자유투":[ghfthrow[0],ghfthrow[1],ghfthrow[2]],
                    "야투성공":[ghyatoos[0],ghyatoos[1],ghyatoos[2]],
                    "삼점슛성공":[ghtpoints[0],ghtpoints[1],ghtpoints[2]],
                    "자유투성공":[ghfthrows[0],ghfthrows[1],ghfthrows[2]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3"], 
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            data = {"순위":[ghseq[0],ghseq[1]],
                    "선수":[ghplay[0],ghplay[1]],
                    "경기수":[ghtotal[0],ghtotal[1]],
                    "득점":[ghduk[0],ghduk[1]],
                    "어시스트":[ghassist[0],ghassist[1]],
                    "리바운드":[ghrebound[0],ghrebound[1]],
                    "스틸":[ghsteal[0],ghsteal[1]],
                    "블락슛":[ghblock[0],ghblock[1]],
                    "야투":[ghyatoo[0],ghyatoo[1]],
                    "삼점슛":[ghtpoint[0],ghtpoint[1]],
                    "자유투":[ghfthrow[0],ghfthrow[1]],
                    "야투성공":[ghyatoos[0],ghyatoos[1]],
                    "삼점슛성공":[ghtpoints[0],ghtpoints[1]],
                    "자유투성공":[ghfthrows[0],ghfthrows[1]]}
            df = pd.DataFrame(data,

                    index= ["1","2"], 
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            data = {"순위":[ghseq[0]],
                    "선수":[ghplay[0]],
                    "경기수":[ghtotal[0]],
                    "득점":[ghduk[0]],
                    "어시스트":[ghassist[0]],
                    "리바운드":[ghrebound[0]],
                    "스틸":[ghsteal[0]],
                    "블락슛":[ghblock[0]],
                    "야투":[ghyatoo[0]],
                    "삼점슛":[ghtpoint[0]],
                    "자유투":[ghfthrow[0]],
                    "야투성공":[ghyatoos[0]],
                    "삼점슛성공":[ghtpoints[0]],
                    "자유투성공":[ghfthrows[0]]}
            df = pd.DataFrame(data,

                    index= ["1"], 
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
    
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

    def gaein_away(gamesu):

        if gamesu == 7:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4],gaseq[5],gaseq[6]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4],gaplay[5],gaplay[6]],
                    "춮장시간":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4],gatotal[5],gatotal[6]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4],gaduk[5],gaduk[6]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2],gaassist[3],gaassist[4],gaassist[5],gaassist[6]],
                    "리바운드":[garebound[0],garebound[1],garebound[2],garebound[3],garebound[4],garebound[5],garebound[6]],
                    "스틸":[gasteal[0],gasteal[1],gasteal[2],gasteal[3],gasteal[4],gasteal[5],gasteal[6]],
                    "블락슛":[gablock[0],gablock[1],gablock[2],gablock[3],gablock[4],gablock[5],gablock[6]],
                    "야투":[gayatoo[0],gayatoo[1],gayatoo[2],gayatoo[3],gayatoo[4],gayatoo[5],gayatoo[6]],
                    "삼점슛":[gatpoint[0],gatpoint[1],gatpoint[2],gatpoint[3],gatpoint[4],gatpoint[5],gatpoint[6]],
                    "자유투":[gafthrow[0],gafthrow[1],gafthrow[2],gafthrow[3],gafthrow[4],gafthrow[5],gafthrow[6]],
                    "야투성공":[gayatoos[0],gayatoos[1],gayatoos[2],gayatoos[3],gayatoos[4],gayatoos[5],gayatoos[6]],
                    "삼점슛성공":[gatpoints[0],gatpoints[1],gatpoints[2],gatpoints[3],gatpoints[4],gatpoints[5],gatpoints[6]],
                    "자유투성공":[gafthrows[0],gafthrows[1],gafthrows[2],gafthrows[3],gafthrows[4],gafthrows[5],gafthrows[6]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6","7"], 
                    columns=["순위","선수","춮장시간","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 6:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4],gaseq[5]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4],gaplay[5]],
                    "춮장시간":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4],gatotal[5]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4],gaduk[5]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2],gaassist[3],gaassist[4],gaassist[5]],
                    "리바운드":[garebound[0],garebound[1],garebound[2],garebound[3],garebound[4],garebound[5]],
                    "스틸":[gasteal[0],gasteal[1],gasteal[2],gasteal[3],gasteal[4],gasteal[5]],
                    "블락슛":[gablock[0],gablock[1],gablock[2],gablock[3],gablock[4],gablock[5]],
                    "야투":[gayatoo[0],gayatoo[1],gayatoo[2],gayatoo[3],gayatoo[4],gayatoo[5]],
                    "삼점슛":[gatpoint[0],gatpoint[1],gatpoint[2],gatpoint[3],gatpoint[4],gatpoint[5]],
                    "자유투":[gafthrow[0],gafthrow[1],gafthrow[2],gafthrow[3],gafthrow[4],gafthrow[5]],
                    "야투성공":[gayatoos[0],gayatoos[1],gayatoos[2],gayatoos[3],gayatoos[4],gayatoos[5]],
                    "삼점슛성공":[gatpoints[0],gatpoints[1],gatpoints[2],gatpoints[3],gatpoints[4],gatpoints[5]],
                    "자유투성공":[gafthrows[0],gafthrows[1],gafthrows[2],gafthrows[3],gafthrows[4],gafthrows[5]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6"], 
                    columns=["순위","선수","춮장시간","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 5:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4]],
                    "춮장시간":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2],gaassist[3],gaassist[4]],
                    "리바운드":[garebound[0],garebound[1],garebound[2],garebound[3],garebound[4]],
                    "스틸":[gasteal[0],gasteal[1],gasteal[2],gasteal[3],gasteal[4]],
                    "블락슛":[gablock[0],gablock[1],gablock[2],gablock[3],gablock[4]],
                    "야투":[gayatoo[0],gayatoo[1],gayatoo[2],gayatoo[3],gayatoo[4]],
                    "삼점슛":[gatpoint[0],gatpoint[1],gatpoint[2],gatpoint[3],gatpoint[4]],
                    "자유투":[gafthrow[0],gafthrow[1],gafthrow[2],gafthrow[3],gafthrow[4]],
                    "야투성공":[gayatoos[0],gayatoos[1],gayatoos[2],gayatoos[3],gayatoos[4]],
                    "삼점슛성공":[gatpoints[0],gatpoints[1],gatpoints[2],gatpoints[3],gatpoints[4]],
                    "자유투성공":[gafthrows[0],gafthrows[1],gafthrows[2],gafthrows[3],gafthrows[4]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5"], 
                    columns=["순위","선수","춮장시간","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 4:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3]],
                    "춮장시간":[gatotal[0],gatotal[1],gatotal[2],gatotal[3]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2],gaassist[3]],
                    "리바운드":[garebound[0],garebound[1],garebound[2],garebound[3]],
                    "스틸":[gasteal[0],gasteal[1],gasteal[2],gasteal[3]],
                    "블락슛":[gablock[0],gablock[1],gablock[2],gablock[3]],
                    "야투":[gayatoo[0],gayatoo[1],gayatoo[2],gayatoo[3]],
                    "삼점슛":[gatpoint[0],gatpoint[1],gatpoint[2],gatpoint[3]],
                    "자유투":[gafthrow[0],gafthrow[1],gafthrow[2],gafthrow[3]],
                    "야투성공":[gayatoos[0],gayatoos[1],gayatoos[2],gayatoos[3]],
                    "삼점슛성공":[gatpoints[0],gatpoints[1],gatpoints[2],gatpoints[3]],
                    "자유투성공":[gafthrows[0],gafthrows[1],gafthrows[2],gafthrows[3]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4"], 
                    columns=["순위","선수","춮장시간","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2]],
                    "춮장시간":[gatotal[0],gatotal[1],gatotal[2]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2]],
                    "리바운드":[garebound[0],garebound[1],garebound[2]],
                    "스틸":[gasteal[0],gasteal[1],gasteal[2]],
                    "블락슛":[gablock[0],gablock[1],gablock[2]],
                    "야투":[gayatoo[0],gayatoo[1],gayatoo[2]],
                    "삼점슛":[gatpoint[0],gatpoint[1],gatpoint[2]],
                    "자유투":[gafthrow[0],gafthrow[1],gafthrow[2]],
                    "야투성공":[gayatoos[0],gayatoos[1],gayatoos[2]],
                    "삼점슛성공":[gatpoints[0],gatpoints[1],gatpoints[2]],
                    "자유투성공":[gafthrows[0],gafthrows[1],gafthrows[2]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3"], 
                    columns=["순위","선수","춮장시간","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            data = {"순위":[gaseq[0],gaseq[1]],
                    "선수":[gaplay[0],gaplay[1]],
                    "춮장시간":[gatotal[0],gatotal[1]],
                    "득점":[gaduk[0],gaduk[1]],
                    "어시스트":[gaassist[0],gaassist[1]],
                    "리바운드":[garebound[0],garebound[1]],
                    "스틸":[gasteal[0],gasteal[1]],
                    "블락슛":[gablock[0],gablock[1]],
                    "야투":[gayatoo[0],gayatoo[1]],
                    "삼점슛":[gatpoint[0],gatpoint[1]],
                    "자유투":[gafthrow[0],gafthrow[1]],
                    "야투성공":[gayatoos[0],gayatoos[1]],
                    "삼점슛성공":[gatpoints[0],gatpoints[1]],
                    "자유투성공":[gafthrows[0],gafthrows[1]]}
            df = pd.DataFrame(data,

                    index= ["1","2"], 
                    columns=["순위","선수","춮장시간","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            data = {"순위":[gaseq[0]],
                    "선수":[gaplay[0]],
                    "춮장시간":[gatotal[0]],
                    "득점":[gaduk[0]],
                    "어시스트":[gaassist[0]],
                    "리바운드":[garebound[0]],
                    "스틸":[gasteal[0]],
                    "블락슛":[gablock[0]],
                    "야투":[gayatoo[0]],
                    "삼점슛":[gatpoint[0]],
                    "자유투":[gafthrow[0]],
                    "야투성공":[gayatoos[0]],
                    "삼점슛성공":[gatpoints[0]],
                    "자유투성공":[gafthrows[0]]}
            df = pd.DataFrame(data,

                    index= ["1"], 
                    columns=["순위","선수","춮장시간","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
     
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
