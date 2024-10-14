import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import m_subteam
import m_subbkgrass
import m_subbkgrai
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
import plotly.graph_objects as go
# 한글폰트
# from matplotlib import font_manager, rc
# font_path = "C:/Windows/Fonts/NanumBarunGothic.TTF"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

def Crawler(yearc,countc,gyungi):
    
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
    has = []
    aas = []
    hrebound = []
    arebound = []
    hduk = []
    aduk = []
    hpduk = []
    apduk = []
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
    win = []
    draw = []
    lose = []
    result = []
    fwin = []
    fdraw = []
    flose = []
    
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

    year = int(yearc)
    count = int(countc)
    i = int(gyungi)

    # print(year,count,i)

    ssh = str(year) + "년 " + str(count) + "회차"
    st.subheader(ssh)

    con = sqlite3.connect("c:/Users/iendo/basketball.db")
    cur = con.cursor()
    sql = "select 홈팀, 원정팀, 승, 무, 패, 결과, 해외승, 해외무, 해외패 from 승5패_일정결과 where 년도 = ? and 회차 = ? and 순번 = ?" 
    data = (year, count, i)
    cur.execute(sql,data)

    rows = cur.fetchall()
    for row in rows:
        p1 = row[0] 
        p2 = row[1]
        p3 = row[2]
        p4 = row[3]
        p5 = row[4]
        p6 = row[5]
        p7 = row[6]
        p8 = row[7]
        p9 = row[8]
        home.append(p1)
        away.append(p2)
        win.append(p3)
        draw.append(p4)
        lose.append(p5)
        result.append(p6)
        fwin.append(p7)
        fdraw.append(p8)
        flose.append(p9)

        # # print(home,away)
        l_gubun, l1_gubun, seq_team, tts_team, inq_team, seq1_team = m_subteam.inq_teamn("k", home[0])

        cur = con.cursor()     
        sql = "SELECT 순위,승률,경기수,승,패,승차,득점,어시스트,리바운드,스틸,블록,삼점슛,자유투,자유투성공,홈승,홈패,원정승,원정패, " \
                   "  디비전승,디비전패,연속,팀구분,디비전 FROM 팀순위 where 팀 = ?"    
        data = (seq_team,)
        cur.execute(sql,data)

        rows = cur.fetchall()
        for row in rows:
            p0 = int(row[0])
            p1 = float(row[1])
            p2 = int(row[2])
            p3 = int(row[3])
            p4 = int(row[4])
            p5 = float(row[5])
            p6 = float(row[6])
            p7 = row[7]
            p8 = row[8]
            p9 = row[9]
            p10 = row[10]
            p11 = row[11]
            p12 = row[12]
            p13 = row[13]
            p14 = row[14]
            p15 = row[15]
            p16 = row[16]
            p17 = row[17]
            p18 = row[18]
            p19 = row[19]
            p20 = row[20]
            p21 = row[21]
            p22 = row[22]
        
            hseq.append(p0)
            hsjum.append(p1)
            htotal.append(p2)
            hwin.append(p3)
            hdraw.append(0)
            hlose.append(p4)
            hcha.append(p5)
            hduk.append(p6)
            has.append(p7)
            hrebound.append(p8)
            hsteal.append(p9)
            hblock.append(p10)
            htsteal.append(p11)
            hfhrow.append(p12)
            hfhrows.append(p13)
            hhwin.append(p14)
            hhlose.append(p15)
            hawin.append(p16)
            halose.append(p17)
            hdwin.append(p18)
            hdlose.append(p19)
            hyeon.append(p20)
            htgubun.append(p21)
            hgigu.append(p22)
            hpduk.append(p6)

        cur = con.cursor()
        sql = "SELECT 순위, 선수, 득점, 어시스트, 리바운드, 경기수, 스틸, 블락슛, 야투, 삼점슛, 자유투, 야투성공, 삼점슛성공, 자유투성공 " \
               " FROM 개인순위 where 팀명 = ? order by 순위"    
        
        if l_gubun == 'N':            
            data = (seq_team,)
        else:
            data = (seq1_team,)
        cur.execute(sql,data)

        rows = cur.fetchall()
        for row in rows:
            p1 = row[0] 
            p2 = row[1]
            p3 = row[2]
            p4 = row[3]
            p5 = row[4]
            p6 = row[5]
            p7 = row[6]
            p8 = row[7]
            p9 = row[8]
            p10 = row[9]
            p11 = row[10]
            p12 = row[11]
            p13 = row[12]
            p14 = row[13]
            ghseq.append(p1)
            ghplay.append(p2)
            ghduk.append(p3)
            ghassist.append(p4) 
            ghrebound.append(p5)
            ghtotal.append(p6)
            ghsteal.append(p7)
            ghblock.append(p8) 
            ghyatoo.append(p9) 
            ghtpoint.append(p10)
            ghfthrow.append(p11)
            ghyatoos.append(p12)
            ghtpoints.append(p13)
            ghfthrows.append(p14)

        # print(ghplay,ghduk)

        l_gubun, l1_gubun, seq_team, tts_team, inq_team, seq1_team = m_subteam.inq_teamn("k", away[0])

        cur = con.cursor()   
        sql = "SELECT 순위,승률,경기수,승,패,승차,득점,어시스트,리바운드,스틸,블록,삼점슛,자유투,자유투성공,홈승,홈패,원정승,원정패, " \
                   "  디비전승,디비전패,연속,팀구분,디비전 FROM 팀순위 where 팀 = ?"    
        data = (seq_team,)
        cur.execute(sql,data)

        rows = cur.fetchall()
        for row in rows:
            p0 = int(row[0])
            p1 = float(row[1])
            p2 = int(row[2])
            p3 = int(row[3])
            p4 = int(row[4])
            p5 = float(row[5])
            p6 = float(row[6])
            p7 = row[7]
            p8 = row[8]
            p9 = row[9]
            p10 = row[10]
            p11 = row[11]
            p12 = row[12]
            p13 = row[13]
            p14 = row[14]
            p15 = row[15]
            p16 = row[16]
            p17 = row[17]
            p18 = row[18]
            p19 = row[19]
            p20 = row[20]
            p21 = row[21]
            p22 = row[22]
        
            aseq.append(p0)
            asjum.append(p1)
            atotal.append(p2)
            awin.append(p3)
            adraw.append(0)
            alose.append(p4)
            acha.append(p5)
            aduk.append(p6)
            aas.append(p7)
            arebound.append(p8)
            asteal.append(p9)
            ablock.append(p10)
            atsteal.append(p11)
            afhrow.append(p12)
            afhrows.append(p13)
            ahwin.append(p14)
            ahlose.append(p15)
            aawin.append(p16)
            aalose.append(p17)
            adwin.append(p18)
            adlose.append(p19)
            ayeon.append(p20)
            atgubun.append(p21)
            agigu.append(p22)
            apduk.append(p6)

        cur = con.cursor()
        sql = "SELECT 순위, 선수, 득점, 어시스트, 리바운드, 경기수, 스틸, 블락슛, 야투, 삼점슛, 자유투, 야투성공, 삼점슛성공, 자유투성공 " \
               " FROM 개인순위 where 팀명 = ? order by 순위"   
        if l_gubun == 'N':            
            data = (seq_team,)
        else:
            data = (seq1_team,)
        cur.execute(sql,data)

        rows = cur.fetchall()
        for row in rows:
            p1 = row[0] 
            p2 = row[1]
            p3 = row[2]
            p4 = row[3]
            p5 = row[4]
            p6 = row[5]
            p7 = row[6]
            p8 = row[7]
            p9 = row[8]
            p10 = row[9]
            p11 = row[10]
            p12 = row[11]
            p13 = row[12]
            p14 = row[13]
            gaseq.append(p1)
            gaplay.append(p2)
            gaduk.append(p3)
            gaassist.append(p4) 
            garebound.append(p5)
            gatotal.append(p6)
            gasteal.append(p7)
            gablock.append(p8) 
            gayatoo.append(p9) 
            gatpoint.append(p10)
            gafthrow.append(p11)
            gayatoos.append(p12)
            gatpoints.append(p13)
            gafthrows.append(p14)

        # print(gaplay,gaduk)

    con.close() 

    home[0] = '"'+home[0]
    away[0] = "'"+away[0]
    
    sh = str(i) + "경기"
    st.subheader(sh)
   
    df = pd.DataFrame(data=np.array([[home[0][1:],hseq[0],hsjum[0],htotal[0],hwin[0],hlose[0],hcha[0],hduk[0],has[0],hrebound[0],hsteal[0],
                                      hblock[0],htsteal[0],hfhrow[0],hfhrows[0],hhwin[0],hhlose[0],hawin[0],halose[0],hdwin[0],hdlose[0],hyeon[0],
                                      htgubun[0],hgigu[0]],
                                     [away[0][1:],aseq[0],asjum[0],atotal[0],awin[0],alose[0],acha[0],aduk[0],aas[0],arebound[0],asteal[0],
                                      ablock[0],atsteal[0],afhrow[0],afhrows[0],ahwin[0],ahlose[0],aawin[0],aalose[0],adwin[0],adlose[0],ayeon[0],
                                      atgubun[0],agigu[0]]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","순위","승률","경기수","승","패","승차","득점","AS","리바운드","스틸","블록","3점슛","자유투","자유투성공","홈승","홈패",
                     "원정승","원정패","디비전승","디비전패","연속","리그","디비전"]) 
 
    st.markdown("""
    <style>
    table {background-color: #f1f740;}
    </style>
    """, unsafe_allow_html=True)

    st.dataframe(df)

    colors = ['#FFA07A', '#F0E68C', '#87CEFA']
    labels = ['승','무','패']
    values = [hwin[0], hdraw[0], hlose[0]]

    figh = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figh.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    values = [awin[0], adraw[0], alose[0]]

    figa = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figa.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    tab1, tab2 = st.tabs(["홈팀 전적", "원정팀 전적"])
    with tab1:
        st.plotly_chart(figh, theme="streamlit")
    with tab2:
        st.plotly_chart(figa, theme="streamlit")

    st.markdown(":basketball: :blue[**투표 현황**]")
    df = pd.DataFrame(data=np.array([[home[0][1:],away[0][1:],win[0],draw[0],lose[0],fwin[0],fdraw[0],flose[0],result[0]]]), 

            index= ["현재"], 
            columns=["홈팀","원정팀","승","⑤","패","해외승","해외무","해외패","결과"]) 

    st.dataframe(df)

    win[0] = win[0].replace('%','')
    draw[0] = draw[0].replace('%','')
    lose[0] = lose[0].replace('%','')
    labels = ['승','⑤','패']
    values = [win[0], draw[0], lose[0]]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    st.plotly_chart(fig)

    # for m in range(3):
    #     if m == 0:
    #         st.markdown("**순위**"+"("+htgubun[0]+"-"+hgigu[0]+" "+str(hseq[0])+"위 : "+atgubun[0]+"-"+agigu[0]+" "+str(aseq[0])+"위)")
    #         df = pd.DataFrame(data=np.array([[hseq[0]],[aseq[0]]]), 
    #                 index= [home[0], away[0]], 
    #                 columns=["순위"]) 
            
    #         st.bar_chart(df, horizontal=True,use_container_width=True,color=["#C83F49"])
    #     elif m == 1:
    #         st.markdown("**승률**"+"("+str(hsjum[0])+" : "+str(asjum[0])+")")
    #         df = pd.DataFrame(data=np.array([[hsjum[0]],[asjum[0]]]),
    #                 index= [home[0], away[0]], 
    #                 columns=["승률"]) 

    #         st.bar_chart(df, horizontal=True,use_container_width=True,color=["#1E90FF"]) #dodger blue
    #     elif m == 2:
    #         st.markdown("**평균득점**"+"("+str(hpduk[0])+" : "+str(apduk[0])+")")
    #         df = pd.DataFrame(data=np.array([[hpduk[0]],[apduk[0]]]),
    #                 index= [home[0], away[0]], 
    #                 columns=["승점"]) 

    #         st.bar_chart(df, horizontal=True,use_container_width=True,color=["#12E193"])

    # 맞대결 전체
    game = 999
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subbkgrass.wdl_cnt(home[0][1:], away[0][1:], game) 

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    # # print(hwdl_list)
    def hwdl_def(gamesu):
        hwdl = [''] * gamesu
        cntw = 0
        cntd = 0
        cntl = 0
        for i in range(gamesu): 
            if hwdl_list[i] == 3:
                hwdl[i] = "승"
                cntw += 1
            elif hwdl_list[i] == 2 or hwdl_list[i] == 1:
                hwdl[i] = "⑤"
                cntd += 1
            elif hwdl_list[i] == 0:
                hwdl[i] = "패"
                cntl += 1

        wdlk = ''
        wdlk = str(cntw)+"승"+str(cntd)+"⑤"+str(cntl)+"패"

        return hwdl, wdlk, cntw, cntd, cntl    
    
    hwdl,wdlk, cntw, cntd, cntl = hwdl_def(len(hwdl_list))
     
    st.markdown(":basketball: :blue[**맞대결**]")
    st.markdown(" 전 체 : "+wdlk)     

    # 맞대결 7경기
    game = 7
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subbkgrass.wdl_cnt(home[0][1:], away[0][1:], game) 

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
        st.plotly_chart(fig1, theme="streamlit")
    with tab2:
        st.plotly_chart(fig2, theme="streamlit")

    # 최근 7경기
    game = 7
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subbkgrai.wdl_cnt(home[0][1:], game) 

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    hwdl,wdlk, cntwmh, cntdmh, cntlmh = hwdl_def(len(hwdl_list))
    
    st.markdown(":basketball: :blue[**최근7경기**]")
    st.markdown("홈팀 : "+home[0][1:]+"("+wdlk+")")

    df = pd.DataFrame(data=np.array([hil_list,ateam_list,jumsu_list,hwdl]),

        index= ["일자","상대","점수","결과"], 
        columns=["1","2","3","4","5","6","7"]) 
    
    st.dataframe(df) 

    game = 7
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subbkgrai.wdl_cnt(away[0][1:], game) 

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    hwdl,wdlk, cntwma, cntdma, cntlma = hwdl_def(len(hwdl_list))
    
    st.markdown("원정팀 : "+away[0][1:]+"("+wdlk+")")
    
    df = pd.DataFrame(data=np.array([hil_list,ateam_list,jumsu_list,hwdl]),

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
        st.plotly_chart(fig3, theme="streamlit")
    with tab2:
        st.plotly_chart(fig4, theme="streamlit")

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
    
    if len(ghplay) == 0:
        pass
    else:
        st.markdown(":basketball: :blue[**득점순위**]")
             
        st.markdown("홈팀 : "+home[0][1:]+"("+str(len(ghplay))+"명)")

        gaein_home(len(ghplay))

    def gaein_away(gamesu):

        if gamesu == 7:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4],gaseq[5],gaseq[6]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4],gaplay[5],gaplay[6]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4],gatotal[5],gatotal[6]],
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
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 6:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4],gaseq[5]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4],gaplay[5]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4],gatotal[5]],
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
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 5:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4]],
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
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)

        elif gamesu == 4:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2],gatotal[3]],
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
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2]],
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
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            data = {"순위":[gaseq[0],gaseq[1]],
                    "선수":[gaplay[0],gaplay[1]],
                    "경기수":[gatotal[0],gatotal[1]],
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
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            data = {"순위":[gaseq[0]],
                    "선수":[gaplay[0]],
                    "경기수":[gatotal[0]],
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
                    columns=["순위","선수","경기수","득점","어시스트","리바운드","스틸","블락슛","야투","삼점슛","자유투",
                             "야투성공","삼점슛성공","자유투성공"]) 
            st.dataframe(df)
             
    if len(gaplay) == 0:
        pass
    else:
        if len(ghplay) == 0:
            st.markdown(":basketball: :blue[**득점순위**]")
             
        st.markdown("원정팀 : "+away[0][1:]+"("+str(len(gaplay))+"명)")
        
        gaein_away(len(gaplay))
