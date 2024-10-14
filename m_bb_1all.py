import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import m_subteam
import m_subbbgrass
import m_subbbgrai
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
    hpitcher = []
    apitcher = []
    hpjachek = []
    apjachek = []
    hptotal = []
    aptotal = []
    hpwin = []
    apwin = []
    hplose = []
    aplose = []
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

    year = int(yearc)
    count = int(countc)
    i = int(gyungi)

    # # print(year,count,i)

    ssh = str(year) + "년 " + str(count) + "회차"
    st.subheader(ssh)

    con = sqlite3.connect("c:/Users/iendo/baseball.db")
    cur = con.cursor()
    sql = "select 홈팀, 원정팀, 승, 무, 패, 결과, 해외승, 해외무, 해외패 from 승1패_일정결과 where 년도 = ? and 회차 = ? and 순번 = ?" 
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
        l_gubun, l1_gubun, seq_team, tts_team, inq_team, seq1_team = m_subteam.inq_teamn("b", home[0])

        cur = con.cursor()     
        sql = "SELECT 순위,승률,승,무,패,게임차,연속,타율,평균자책,경기수,득점,홈런,안타,도루,탈삼진,실점,최근10경기,팀구분,지구 FROM 팀순위 where 팀 = ?"    
        data = (seq_team,)
        cur.execute(sql,data)

        rows = cur.fetchall()
        for row in rows:
            p0 = int(row[0])
            p1 = float(row[1])
            p2 = row[2]
            p3 = row[3]
            p4 = row[4]
            p5 = row[5]
            p6 = row[6]
            p7 = float(row[7])
            p8 = float(row[8])
            p9 = int(row[9])
            pa = int(row[10])
            p11 = row[11]
            p12 = row[12]
            p13 = row[13]
            p14 = row[14]
            p15 = row[15]
            p16 = row[16]
            p17 = row[17]
            p18 = row[18]
        
            hseq.append(p0)
            hsjum.append(p1)
            hwin.append(p2)
            hdraw.append(p3)
            hlose.append(p4)
            hcha.append(p5)
            hyeon.append(p6)
            htayul.append(p7)
            hjachek.append(p8)
            htotal.append(p9)
            if p9 == 0 or pa == 0:
                hpduk.append(0)
            else:
                j2 = 0
                j2 = round(pa/p9,2)
                hpduk.append(j2)
            hduk.append(pa)
            hhomerun.append(p11)
            hhit.append(p12)
            hrun.append(p13)
            htalsam.append(p14)
            hsil.append(p15)
            hrten.append(p16)
            htgubun.append(p17)
            hgigu.append(p18)

        cur = con.cursor()
        sql = "SELECT 순위, 선수, 득점, 도루, 타율, 경기수, 타수, 안타, 홈런, 타점, 볼넷, 삼진, 출루율, 장타율" \
               " FROM 개인순위 where 팀명 = ? order by 순위"    
        data = (seq_team,)
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
            ghdoru.append(p4) 
            ghtayul.append(p5)
            ghtotal.append(p6)
            ghtasu.append(p7)
            ghhit.append(p8) 
            ghhomerun.append(p9)
            ghtajum.append(p10)
            ghfball.append(p11)
            ghsamjin.append(p12)
            ghchulru.append(p13)
            ghjangta.append(p14)

        # print(ghplay,ghseq)

        cur = con.cursor()
        sql = "SELECT 포지션, 선수, 득점, 도루, 타율, 안타, CAST(홈런 as unsigned) as 홈런, 타점, 볼넷 " \
               " FROM 타자순위 where 팀 = ? order by 포지션, 홈런 desc"    
        data = (seq_team,)
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
            shpos.append(p1)
            shplay.append(p2)
            shduk.append(p3)
            shdoru.append(p4) 
            shtayul.append(p5)
            shhit.append(p6) 
            shhomerun.append(p7)
            shtajum.append(p8)
            shfball.append(p9)

        cur = con.cursor()
        sql = "SELECT 포지션, 선수, 평균자책, 승, 패, 세이브, 홀드, 이닝, 탈삼진 " \
               " FROM 투수순위 where 팀 = ? order by 포지션 desc, 승 desc"    
        data = (seq_team,)
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
            thpos.append(p1)
            thplay.append(p2)
            thjachek.append(p3)
            thwin.append(p4) 
            thlose.append(p5)
            thsave.append(p6) 
            thhold.append(p7)
            thinning.append(p8)
            thtalsam.append(p9)

        l_gubun, l1_gubun, seq_team, tts_team, inq_team, seq1_team = m_subteam.inq_teamn("b", away[0])

        cur = con.cursor()      
        sql = "SELECT 순위,승률,승,무,패,게임차,연속,타율,평균자책,경기수,득점,홈런,안타,도루,탈삼진,실점,최근10경기,팀구분,지구 FROM 팀순위 where 팀 = ?"    
        data = (seq_team,)
        cur.execute(sql,data)

        rows = cur.fetchall()
        for row in rows:
            p0 = int(row[0])
            p1 = float(row[1])
            p2 = row[2]
            p3 = row[3]
            p4 = row[4]
            p5 = row[5]
            p6 = row[6]
            p7 = float(row[7])
            p8 = float(row[8])
            p9 = int(row[9])
            pa = int(row[10])
            p11 = row[11]
            p12 = row[12]
            p13 = row[13]
            p14 = row[14]
            p15 = row[15]
            p16 = row[16]
            p17 = row[17]
            p18 = row[18]
        
            aseq.append(p0)
            asjum.append(p1)
            awin.append(p2)
            adraw.append(p3)
            alose.append(p4)
            acha.append(p5)
            ayeon.append(p6)
            atayul.append(p7)
            ajachek.append(p8)
            atotal.append(p9)
            if p9 == 0 or pa == 0:
                apduk.append(0)
            else:
                j2 = 0
                j2 = round(pa/p9,2)
                apduk.append(j2)
            aduk.append(pa)
            ahomerun.append(p11)
            ahit.append(p12)
            arun.append(p13)
            atalsam.append(p14)
            asil.append(p15)
            arten.append(p16)
            atgubun.append(p17)
            agigu.append(p18)
   
        cur = con.cursor()     
        sql = "SELECT 홈팀,홈선발,홈평균자책,홈경기수,홈승,홈패,원정팀,원정선발,원정평균자책,원정경기수,원정승,원정패 FROM 승1패_일정선발 " \
              "  where 년도 = ? and 회차 = ? and 순번 = ?"  
        data = (year, count, i)
        cur.execute(sql,data)

        rows = cur.fetchall()
        for row in rows:
            p0 = row[0]
            p1 = row[1]
            p2 = row[2]
            p3 = row[3]
            p4 = row[4]
            p5 = row[5]
            p6 = row[6]
            p7 = row[7]
            p8 = row[8]
            p9 = row[9]
            p10 = row[10]
            p11 = row[11]
        
            hpitcher.append(p1)
            hpjachek.append(p2)
            hptotal.append(p3)
            hpwin.append(p4)
            hplose.append(p5)
            apitcher.append(p7)
            apjachek.append(p8)
            aptotal.append(p9)
            apwin.append(p10)
            aplose.append(p11)

        cur = con.cursor()
        sql = "SELECT 순위, 선수, 득점, 도루, 타율, 경기수, 타수, 안타, 홈런, 타점, 볼넷, 삼진, 출루율, 장타율" \
               " FROM 개인순위 where 팀명 = ? order by 순위"    
        data = (seq_team,)
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
            gadoru.append(p4) 
            gatayul.append(p5)
            gatotal.append(p6)
            gatasu.append(p7)
            gahit.append(p8) 
            gahomerun.append(p9)
            gatajum.append(p10)
            gafball.append(p11)
            gasamjin.append(p12)
            gachulru.append(p13)
            gajangta.append(p14)

        # print(gaplay,gaseq)

        cur = con.cursor()
        sql = "SELECT 포지션, 선수, 득점, 도루, 타율, 안타, CAST(홈런 as unsigned) as 홈런, 타점, 볼넷 " \
               " FROM 타자순위 where 팀 = ? order by 포지션, 홈런 desc"    
        data = (seq_team,)
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
            sapos.append(p1)
            saplay.append(p2)
            saduk.append(p3)
            sadoru.append(p4) 
            satayul.append(p5)
            sahit.append(p6) 
            sahomerun.append(p7)
            satajum.append(p8)
            safball.append(p9)

        cur = con.cursor()
        sql = "SELECT 포지션, 선수, 평균자책, 승, 패, 세이브, 홀드, 이닝, 탈삼진 " \
               " FROM 투수순위 where 팀 = ? order by 포지션 desc, 승 desc"    
        data = (seq_team,)
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
            tapos.append(p1)
            taplay.append(p2)
            tajachek.append(p3)
            tawin.append(p4) 
            talose.append(p5)
            tasave.append(p6) 
            tahold.append(p7)
            tainning.append(p8)
            tatalsam.append(p9)

    con.close() 

    home[0] = '"'+home[0]
    away[0] = "'"+away[0]
    
    sh = str(i) + "경기"
    st.subheader(sh)
    
    df = pd.DataFrame(data=np.array([[home[0][1:],hseq[0],hsjum[0],htotal[0],hwin[0],hlose[0],hdraw[0],hcha[0],hyeon[0],htayul[0],
                                      hjachek[0],hduk[0],hpduk[0],hsil[0],hhomerun[0],hhit[0],hrun[0],htalsam[0],hrten[0],htgubun[0],hgigu[0]],
                                     [away[0][1:],aseq[0],asjum[0],atotal[0],awin[0],alose[0],adraw[0],acha[0],ayeon[0],atayul[0],
                                      ajachek[0],aduk[0],apduk[0],asil[0],ahomerun[0],ahit[0],arun[0],atalsam[0],arten[0],atgubun[0],agigu[0]]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","순위","승률","경기수","승","패","무","게임차","연속","타율","평균자책","득점","평균득점","실점","홈런","안타","도루",
                     "탈삼진","최근10경기","리그","지구"]) 

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

    st.markdown(":baseball: :blue[**투표 현황**]")
    df = pd.DataFrame(data=np.array([[home[0][1:],away[0][1:],win[0],draw[0],lose[0],fwin[0],fdraw[0],flose[0],result[0]]]), 

            index= ["현재"], 
            columns=["홈팀","원정팀","승","①","패","해외승","해외무","해외패","결과"]) 

    st.dataframe(df)

    win[0] = win[0].replace('%','')
    draw[0] = draw[0].replace('%','')
    lose[0] = lose[0].replace('%','')
    labels = ['승','①','패']
    values = [win[0], draw[0], lose[0]]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    st.plotly_chart(fig)

    # for m in range(3):
    #     if m == 0:
    #         st.markdown("**순위**"+"("+htgubun[0]+hgigu[0]+" "+str(hseq[0])+"위 : "+atgubun[0]+agigu[0]+" "+str(aseq[0])+"위)")
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
    
    st.markdown(":baseball: :blue[**선발투수**]") 

    df = pd.DataFrame(data=np.array([[home[0][1:],hpitcher[0],hpjachek[0],hptotal[0],hpwin[0],hplose[0]],
                                     [away[0][1:],apitcher[0],apjachek[0],aptotal[0],apwin[0],aplose[0]]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","선발투수","평균자책","이닝수","승","패"]) 

    st.dataframe(df)

    # 맞대결 전체
    game = 999
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subbbgrass.wdl_cnt(home[0][1:], away[0][1:], game) 

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
                hwdl[i] = "①"
                cntd += 1
            elif hwdl_list[i] == 0:
                hwdl[i] = "패"
                cntl += 1

        wdlk = ''
        wdlk = str(cntw)+"승"+str(cntd)+"①"+str(cntl)+"패"

        return hwdl, wdlk, cntw, cntd, cntl    
    
    hwdl,wdlk, cntw, cntd, cntl = hwdl_def(len(hwdl_list))
      
    st.markdown(":baseball: :blue[**맞대결**]") 
    st.markdown(" 전 체 : "+wdlk)     

    # 맞대결 최근 7경기
    game = 7
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subbbgrass.wdl_cnt(home[0][1:], away[0][1:], game) 

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    hwdl,wdlk, cntwm, cntdm, cntlm = hwdl_def(len(hwdl_list))
   
    st.markdown(" 최근7경기 : "+wdlk)
 
    df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

        index= ["일자","점수","결과"],
        columns=["1","2","3","4","5","6","7"]) 
        # columns=["1","2","3","4","5","6","7","8","9","10"]) 
    
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
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subbbgrai.wdl_cnt(home[0][1:], game) 

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    hwdl,wdlk, cntwmh, cntdmh, cntlmh = hwdl_def(len(hwdl_list))
      
    st.markdown(":baseball: :blue[**최근7경기**]") 
    st.markdown("홈팀 : "+home[0][1:]+"("+wdlk+")")

    df = pd.DataFrame(data=np.array([hil_list,ateam_list,jumsu_list,hwdl]),

        index= ["일자","상대","점수","결과"], 
        columns=["1","2","3","4","5","6","7"]) 
    
    st.dataframe(df) 

    game = 7
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subbbgrai.wdl_cnt(away[0][1:], game) 

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
                    "타율":[ghtayul[0],ghtayul[1],ghtayul[2],ghtayul[3],ghtayul[4],ghtayul[5],ghtayul[6]],
                    "홈런":[ghhomerun[0],ghhomerun[1],ghhomerun[2],ghhomerun[3],ghhomerun[4],ghhomerun[5],ghhomerun[6]],
                    "타점":[ghtajum[0],ghtajum[1],ghtajum[2],ghtajum[3],ghtajum[4],ghtajum[5],ghtajum[6]],
                    "안타":[ghhit[0],ghhit[1],ghhit[2],ghhit[3],ghhit[4],ghhit[5],ghhit[6]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4],ghduk[5],ghduk[6]],
                    "도루":[ghdoru[0],ghdoru[1],ghdoru[2],ghdoru[3],ghdoru[4],ghdoru[5],ghdoru[6]],
                    "볼넷":[ghfball[0],ghfball[1],ghfball[2],ghfball[3],ghfball[4],ghfball[5],ghfball[6]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6","7"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)

        elif gamesu == 6:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3],ghseq[4],ghseq[5]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3],ghplay[4],ghplay[5]],
                    "타율":[ghtayul[0],ghtayul[1],ghtayul[2],ghtayul[3],ghtayul[4],ghtayul[5]],
                    "홈런":[ghhomerun[0],ghhomerun[1],ghhomerun[2],ghhomerun[3],ghhomerun[4],ghhomerun[5]],
                    "타점":[ghtajum[0],ghtajum[1],ghtajum[2],ghtajum[3],ghtajum[4],ghtajum[5]],
                    "안타":[ghhit[0],ghhit[1],ghhit[2],ghhit[3],ghhit[4],ghhit[5]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4],ghduk[5]],
                    "도루":[ghdoru[0],ghdoru[1],ghdoru[2],ghdoru[3],ghdoru[4],ghdoru[5]],
                    "볼넷":[ghfball[0],ghfball[1],ghfball[2],ghfball[3],ghfball[4],ghfball[5]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)

        elif gamesu == 5:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3],ghseq[4]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3],ghplay[4]],
                    "타율":[ghtayul[0],ghtayul[1],ghtayul[2],ghtayul[3],ghtayul[4]],
                    "홈런":[ghhomerun[0],ghhomerun[1],ghhomerun[2],ghhomerun[3],ghhomerun[4]],
                    "타점":[ghtajum[0],ghtajum[1],ghtajum[2],ghtajum[3],ghtajum[4]],
                    "안타":[ghhit[0],ghhit[1],ghhit[2],ghhit[3],ghhit[4]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4]],
                    "도루":[ghdoru[0],ghdoru[1],ghdoru[2],ghdoru[3],ghdoru[4]],
                    "볼넷":[ghfball[0],ghfball[1],ghfball[2],ghfball[3],ghfball[4]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)

        elif gamesu == 4:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3]],
                    "타율":[ghtayul[0],ghtayul[1],ghtayul[2],ghtayul[3]],
                    "홈런":[ghhomerun[0],ghhomerun[1],ghhomerun[2],ghhomerun[3]],
                    "타점":[ghtajum[0],ghtajum[1],ghtajum[2],ghtajum[3]],
                    "안타":[ghhit[0],ghhit[1],ghhit[2],ghhit[3]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3]],
                    "도루":[ghdoru[0],ghdoru[1],ghdoru[2],ghdoru[3]],
                    "볼넷":[ghfball[0],ghfball[1],ghfball[2],ghfball[3]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2]],
                    "타율":[ghtayul[0],ghtayul[1],ghtayul[2]],
                    "홈런":[ghhomerun[0],ghhomerun[1],ghhomerun[2]],
                    "타점":[ghtajum[0],ghtajum[1],ghtajum[2]],
                    "안타":[ghhit[0],ghhit[1],ghhit[2]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2]],
                    "도루":[ghdoru[0],ghdoru[1],ghdoru[2]],
                    "볼넷":[ghfball[0],ghfball[1],ghfball[2]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            data = {"순위":[ghseq[0],ghseq[1]],
                    "선수":[ghplay[0],ghplay[1]],
                    "타율":[ghtayul[0],ghtayul[1]],
                    "홈런":[ghhomerun[0],ghhomerun[1]],
                    "타점":[ghtajum[0],ghtajum[1]],
                    "안타":[ghhit[0],ghhit[1]],
                    "득점":[ghduk[0],ghduk[1]],
                    "도루":[ghdoru[0],ghdoru[1]],
                    "볼넷":[ghfball[0],ghfball[1]]}
            df = pd.DataFrame(data,

                    index= ["1","2"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            data = {"순위":[ghseq[0]],
                    "선수":[ghplay[0]],
                    "타율":[ghtayul[0]],
                    "홈런":[ghhomerun[0]],
                    "타점":[ghtajum[0]],
                    "안타":[ghhit[0]],
                    "득점":[ghduk[0]],
                    "도루":[ghdoru[0]],
                    "볼넷":[ghfball[0]]}
            df = pd.DataFrame(data,

                    index= ["1"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)
    
    if len(ghplay) == 0:
        pass
    else:  
        st.markdown(":baseball: :blue[**타율순위**]")  
           
        st.markdown("홈팀 : "+home[0][1:]+"("+str(len(ghplay))+"명)")

        gaein_home(len(ghplay))
     
    def gaein_away(gamesu):

        if gamesu == 7:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4],gaseq[5],gaseq[6]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4],gaplay[5],gaplay[6]],
                    "타율":[gatayul[0],gatayul[1],gatayul[2],gatayul[3],gatayul[4],gatayul[5],gatayul[6]],
                    "홈런":[gahomerun[0],gahomerun[1],gahomerun[2],gahomerun[3],gahomerun[4],gahomerun[5],gahomerun[6]],
                    "타점":[gatajum[0],gatajum[1],gatajum[2],gatajum[3],gatajum[4],gatajum[5],gatajum[6]],
                    "안타":[gahit[0],gahit[1],gahit[2],gahit[3],gahit[4],gahit[5],gahit[6]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4],gaduk[5],gaduk[6]],
                    "도루":[gadoru[0],gadoru[1],gadoru[2],gadoru[3],gadoru[4],gadoru[5],gadoru[6]],
                    "볼넷":[gafball[0],gafball[1],gafball[2],gafball[3],gafball[4],gafball[5],gafball[6]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6","7"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)

        elif gamesu == 6:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4],gaseq[5]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4],gaplay[5]],
                    "타율":[gatayul[0],gatayul[1],gatayul[2],gatayul[3],gatayul[4],gatayul[5]],
                    "홈런":[gahomerun[0],gahomerun[1],gahomerun[2],gahomerun[3],gahomerun[4],gahomerun[5]],
                    "타점":[gatajum[0],gatajum[1],gatajum[2],gatajum[3],gatajum[4],gatajum[5]],
                    "안타":[gahit[0],gahit[1],gahit[2],gahit[3],gahit[4],gahit[5]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4],gaduk[5]],
                    "도루":[gadoru[0],gadoru[1],gadoru[2],gadoru[3],gadoru[4],gadoru[5]],
                    "볼넷":[gafball[0],gafball[1],gafball[2],gafball[3],gafball[4],gafball[5]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)

        elif gamesu == 5:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4]],
                    "타율":[gatayul[0],gatayul[1],gatayul[2],gatayul[3],gatayul[4]],
                    "홈런":[gahomerun[0],gahomerun[1],gahomerun[2],gahomerun[3],gahomerun[4]],
                    "타점":[gatajum[0],gatajum[1],gatajum[2],gatajum[3],gatajum[4]],
                    "안타":[gahit[0],gahit[1],gahit[2],gahit[3],gahit[4]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4]],
                    "도루":[gadoru[0],gadoru[1],gadoru[2],gadoru[3],gadoru[4]],
                    "볼넷":[gafball[0],gafball[1],gafball[2],gafball[3],gafball[4]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)

        elif gamesu == 4:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3]],
                    "타율":[gatayul[0],gatayul[1],gatayul[2],gatayul[3]],
                    "홈런":[gahomerun[0],gahomerun[1],gahomerun[2],gahomerun[3]],
                    "타점":[gatajum[0],gatajum[1],gatajum[2],gatajum[3]],
                    "안타":[gahit[0],gahit[1],gahit[2],gahit[3]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3]],
                    "도루":[gadoru[0],gadoru[1],gadoru[2],gadoru[3]],
                    "볼넷":[gafball[0],gafball[1],gafball[2],gafball[3]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2]],
                    "타율":[gatayul[0],gatayul[1],gatayul[2]],
                    "홈런":[gahomerun[0],gahomerun[1],gahomerun[2]],
                    "타점":[gatajum[0],gatajum[1],gatajum[2]],
                    "안타":[gahit[0],gahit[1],gahit[2]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2]],
                    "도루":[gadoru[0],gadoru[1],gadoru[2]],
                    "볼넷":[gafball[0],gafball[1],gafball[2]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            data = {"순위":[gaseq[0],gaseq[1]],
                    "선수":[gaplay[0],gaplay[1]],
                    "타율":[gatayul[0],gatayul[1]],
                    "홈런":[gahomerun[0],gahomerun[1]],
                    "타점":[gatajum[0],gatajum[1]],
                    "안타":[gahit[0],gahit[1]],
                    "득점":[gaduk[0],gaduk[1]],
                    "도루":[gadoru[0],gadoru[1]],
                    "볼넷":[gafball[0],gafball[1]]}
            df = pd.DataFrame(data,

                    index= ["1","2"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            data = {"순위":[gaseq[0]],
                    "선수":[gaplay[0]],
                    "타율":[gatayul[0]],
                    "홈런":[gahomerun[0]],
                    "타점":[gatajum[0]],
                    "안타":[gahit[0]],
                    "득점":[gaduk[0]],
                    "도루":[gadoru[0]],
                    "볼넷":[gafball[0]]}
            df = pd.DataFrame(data,

                    index= ["1"], 
                    columns=["순위","선수","타율","홈런","타점","안타","득점","도루","볼넷"]) 
            st.dataframe(df)
        
    if len(gaplay) == 0:
        pass
    else:
        if len(ghplay) == 0:
            st.markdown(":baseball: :blue[**타율순위**]")  
        st.markdown("원정팀 : "+away[0][1:]+"("+str(len(gaplay))+"명)")
     
        gaein_away(len(gaplay))

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    st.markdown(":baseball: :blue[**선수**]")  
    st.markdown("홈팀 : "+home[0][1:])
    
    data1 = {"선수":[shplay],"포지션":[shpos],"홈런":[shhomerun],"타율":[shtayul],"타점":[shtajum],
            "안타":[shhit],"득점":[shduk],"도루":[shdoru],"볼넷":[shfball]}
    
    df1 = pd.DataFrame(data1,
                columns=["선수","포지션","홈런","타율","타점","안타","득점","도루","볼넷"]) 
    
    fig1 = go.Figure(data=[go.Table(
        header=dict(values=list(df1.columns),
                    align='center'),
        cells=dict(values=[shplay,shpos,shhomerun,shtayul,shtajum,shhit,shduk,shdoru,shfball],
                align='center'))])
                
    data2 = {"선수":[thplay],"포지션":[thpos],"평균자책":[thjachek],"승":[thwin],"패":[thlose],
            "세이브":[thsave],"홀드":[thhold],"이닝":[thinning],"탈삼진":[thtalsam]}
    
    df2 = pd.DataFrame(data2,
                columns=["선수","포지션","평균자책","승","패","세이브","홀드","이닝","탈삼진"]) 
    
    fig2 = go.Figure(data=[go.Table(
        header=dict(values=list(df2.columns),
                    align='center'),
        cells=dict(values=[thplay,thpos,thjachek,thwin,thlose,thsave,thhold,thinning,thtalsam],
                align='center'))
    ])

    fig1.update_layout(height=500)
    fig2.update_layout(height=500)

    tab1, tab2 = st.tabs(["타자", "투수"])
    with tab1:
        st.plotly_chart(fig1, theme="streamlit")
    with tab2:
        st.plotly_chart(fig2, theme="streamlit")


    st.markdown("원정팀 : "+away[0][1:])
    
    data3 = {"선수":[saplay],"포지션":[sapos],"홈런":[sahomerun],"타율":[satayul],"타점":[satajum],
            "안타":[sahit],"득점":[saduk],"도루":[sadoru],"볼넷":[safball]}
    
    df3 = pd.DataFrame(data3,
                columns=["선수","포지션","홈런","타율","타점","안타","득점","도루","볼넷"]) 
    
    fig3 = go.Figure(data=[go.Table(
        header=dict(values=list(df3.columns),
                    align='center'),
        cells=dict(values=[saplay,sapos,sahomerun,satayul,satajum,sahit,saduk,sadoru,safball],
                align='center'))])

    data4 = {"선수":[taplay],"포지션":[tapos],"평균자책":[tajachek],"승":[tawin],"패":[talose],
            "세이브":[tasave],"홀드":[tahold],"이닝":[tainning],"탈삼진":[tatalsam]}
    
    df4 = pd.DataFrame(data4,
                columns=["선수","포지션","평균자책","승","패","세이브","홀드","이닝","탈삼진"]) 
    
    fig4 = go.Figure(data=[go.Table(
        header=dict(values=list(df4.columns),
                    align='center'),
        cells=dict(values=[taplay,tapos,tajachek,tawin,talose,tasave,tahold,tainning,tatalsam],
                align='center'))
    ])

    fig3.update_layout(height=500)
    fig4.update_layout(height=500)

    tab1, tab2 = st.tabs(["타자", "투수"])
    with tab1:
        st.plotly_chart(fig3, theme="streamlit")
    with tab2:
        st.plotly_chart(fig4, theme="streamlit")



    # st.markdown("**타자**"+" :  홈팀- "+home[0][1:]+"("+str(len(shplay))+"명)")
    
    # if len(shplay) == 0:
    #     pass
    # else:
    #     data = {"선수":[shplay],"포지션":[shpos],"홈런":[shhomerun],"타율":[shtayul],"타점":[shtajum],
    #             "안타":[shhit],"득점":[shduk],"도루":[shdoru],"볼넷":[shfball]}
        
    #     df = pd.DataFrame(data,
    #                 columns=["선수","포지션","홈런","타율","타점","안타","득점","도루","볼넷"]) 
        
    #     fig = go.Figure(data=[go.Table(
    #         header=dict(values=list(df.columns),
    #                     # fill_color='paleturquoise',
    #                     align='center'),
    #         cells=dict(values=[shplay,shpos,shhomerun,shtayul,shtajum,shhit,shduk,shdoru,shfball],
    #                 #    fill_color='lavender',
    #                 align='center'))
    #     ])

    #     fig.update_layout(height=500)

    #     st.plotly_chart(fig)

    # st.markdown("**타자**"+" :  원정팀- "+away[0][1:]+"("+str(len(saplay))+"명)")
    
    # if len(saplay) == 0:
    #     pass
    # else:
    #     data = {"선수":[saplay],"포지션":[sapos],"홈런":[sahomerun],"타율":[satayul],"타점":[satajum],
    #             "안타":[sahit],"득점":[saduk],"도루":[sadoru],"볼넷":[safball]}
        
    #     df = pd.DataFrame(data,
    #                 columns=["선수","포지션","홈런","타율","타점","안타","득점","도루","볼넷"]) 
        
    #     fig = go.Figure(data=[go.Table(
    #         header=dict(values=list(df.columns),
    #                     # fill_color='paleturquoise',
    #                     align='center'),
    #         cells=dict(values=[saplay,sapos,sahomerun,satayul,satajum,sahit,saduk,sadoru,safball],
    #                 #    fill_color='lavender',
    #                 align='center'))
    #     ])

    #     fig.update_layout(height=500)

    #     st.plotly_chart(fig)


    # st.markdown("**투수**"+" :  홈팀- "+home[0][1:]+"("+str(len(thplay))+"명)")
    
    # if len(thplay) == 0:
    #     pass
    # else:
    #     data = {"선수":[thplay],"포지션":[thpos],"평균자책":[thjachek],"승":[thwin],"패":[thlose],
    #             "세이브":[thsave],"홀드":[thhold],"이닝":[thinning],"탈삼진":[thtalsam]}
        
    #     df = pd.DataFrame(data,
    #                 columns=["선수","포지션","평균자책","승","패","세이브","홀드","이닝","탈삼진"]) 
        
    #     fig = go.Figure(data=[go.Table(
    #         header=dict(values=list(df.columns),
    #                     # fill_color='paleturquoise',
    #                     align='center'),
    #         cells=dict(values=[thplay,thpos,thjachek,thwin,thlose,thsave,thhold,thinning,thtalsam],
    #                 #    fill_color='lavender',
    #                 align='center'))
    #     ])

    #     fig.update_layout(height=500)

    #     st.plotly_chart(fig)

    # st.markdown("**투수**"+" :  원정팀- "+away[0][1:]+"("+str(len(taplay))+"명)")
    
    # if len(taplay) == 0:
    #     pass
    # else:
    #     data = {"선수":[taplay],"포지션":[tapos],"평균자책":[tajachek],"승":[tawin],"패":[talose],
    #             "세이브":[tasave],"홀드":[tahold],"이닝":[tainning],"탈삼진":[tatalsam]}
        
    #     df = pd.DataFrame(data,
    #                 columns=["선수","포지션","평균자책","승","패","세이브","홀드","이닝","탈삼진"]) 
        
    #     fig = go.Figure(data=[go.Table(
    #         header=dict(values=list(df.columns),
    #                     # fill_color='paleturquoise',
    #                     align='center'),
    #         cells=dict(values=[taplay,tapos,tajachek,tawin,talose,tasave,tahold,tainning,tatalsam],
    #                 #    fill_color='lavender',
    #                 align='center'))
    #     ])

    #     fig.update_layout(height=500)

    #     st.plotly_chart(fig)


