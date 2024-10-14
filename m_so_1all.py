import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import m_subteam
import m_subscgrass
import m_subscgrai
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
import plotly.graph_objects as go
# 한글폰트
# from matplotlib import font_manager, rc
# font_path = "C:/Windows/Fonts/NanumBarunGothic.TTF"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)
# @st.experimental_memo

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
    htotal = []
    atotal = []
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
    ghpoint = []
    gapoint = []
    ghtotal = []
    gatotal = []
    ghshoot = []
    gashoot = []
    ghyshoot = []
    gayshoot = []
    ghfoul = []
    gafoul = []
    ghyellow = []
    gayellow = []
    ghred = []
    gared = []
    ghoffside = []
    gaoffside = []
    shpos = []
    sapos = []
    shplay = []
    saplay = []
    shduk = []
    saduk = []
    shassist = []
    saassist = []
    shpoint = []
    sapoint = []
    shtotal = []
    satotal = []
    shshoot = []
    sashoot = []
    shyshoot = []
    sayshoot = []
    shyellow = []
    sayellow = []
    shred = []
    sared = []
    shoffside = []
    saoffside = []
    whseq = []
    waseq = []
    whsjum = []
    wasjum = []
    whwin = []
    wawin = []
    whdraw = []
    wadraw = []
    whlose = []
    walose = []
    whduk = []
    waduk = []
    whsil = []
    wasil = []
    whcha = []
    wacha = []
    whjo = []
    wajo = []
    wgaw = ''

    year = int(yearc)
    count = int(countc)
    i = int(gyungi)

    # print(year,count,i)

    ssh = str(year) + "년 " + str(count) + "회차"
    st.subheader(ssh)

    con = sqlite3.connect("c:/Users/iendo/soccer.db")
    cur = con.cursor()
    sql = "select 홈팀, 원정팀, 승, 무, 패, 결과, 해외승, 해외무, 해외패 from 승무패_일정결과 where 년도 = ? and 회차 = ? and 순번 = ?" 
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
        l_gubun, l1_gubun, seq_team, tts_team, inq_team, seq1_team = m_subteam.inq_teamn("s", home[0])

        cur = con.cursor()     
        if l_gubun == "A" or l_gubun == "W":
            sql = "SELECT 순위, 승점, 승, 무, 패, 득점, 실점, 득실차, 도움, 경기수 FROM 팀순위_UEFA where 팀 = ? and 팀구분 = ?"    
            data = (seq_team,"FIFA")
        else:
            sql = "SELECT 순위, 승점, 승, 무, 패, 득점, 실점, 득실차, 도움, 경기수 FROM 팀순위 where 팀 = ? and 팀구분 not in(?)"    
            data = (seq_team,"UEC")
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
            p7 = row[7]
            p8 = row[8]
            p9 = row[9]
            pa = row[5]
            if p9 == "":
                pass
            else:
                p9 = int(row[9])
            if pa == "":
                pass
            else:
                pa = int(row[5])
        
            hseq.append(p0)
            hsjum.append(p1)
            hwin.append(p2)
            hdraw.append(p3)
            hlose.append(p4)
            hduk.append(p5)
            hsil.append(p6)
            hcha.append(p7)
            hassist.append(p8)
            htotal.append(p9)
            if p9 == "" or pa == "":
                hpduk.append("")
            elif p9 == 0 or pa == 0:
                hpduk.append(0)
            else:
                j2 = 0
                j2 = round(pa/p9,2)
                hpduk.append(j2)

        if l_gubun == "A" or l_gubun == "W":
            cur = con.cursor()
            sql = "SELECT 순위, 승점, 승, 무, 패, 득점, 실점, 득실차, 조 FROM 팀순위_WCP where 팀 = ?"    
            data = (seq1_team,)
            cur.execute(sql,data)

            rows = cur.fetchall()
            for row in rows:
                p0 = int(row[0])
                p1 = int(row[1])
                p2 = row[2]
                p3 = row[3]
                p4 = row[4]
                p5 = row[5]
                p6 = row[6]
                p7 = row[7]
                p8 = row[8]
            
                whseq.append(p0)
                whsjum.append(p1)
                whwin.append(p2)
                whdraw.append(p3)
                whlose.append(p4)
                whduk.append(p5)
                whsil.append(p6)
                whcha.append(p7)
                whjo.append(p8)
                wgaw = '1'

        cur = con.cursor()
        sql = "SELECT 순위, 선수, 득점, 도움, 공격포인트, 경기수, 슈팅, 유효슈팅, 파울, 경고, 퇴장, 오프사이드 " \
               " FROM 개인순위 where 팀명 like ? order by 순위"    
        data = (inq_team,)
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
            ghseq.append(p1)
            ghplay.append(p2)
            ghduk.append(p3)
            ghassist.append(p4) 
            ghpoint.append(p5)
            ghtotal.append(p6)
            ghshoot.append(p7)
            ghyshoot.append(p8) 
            ghfoul.append(p9) 
            ghyellow.append(p10)
            ghred.append(p11)
            ghoffside.append(p12)

        # print(ghplay,ghduk)

        cur = con.cursor()
        sql = "SELECT 포지션, 선수, 득점, 도움, 공격포인트, 경기, 슈팅, 유효슈팅, 경고, 퇴장, 오프사이드 " \
               " FROM 선수 where 팀명 like ? order by 포지션, 득점 desc"    
        data = (inq_team,)
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
            shpos.append(p1)
            shplay.append(p2)
            shduk.append(p3)
            shassist.append(p4) 
            shpoint.append(p5)
            shtotal.append(p6)
            shshoot.append(p7)
            shyshoot.append(p8) 
            shyellow.append(p9)
            shred.append(p10)
            shoffside.append(p11)

        l_gubun, l1_gubun, seq_team, tts_team, inq_team, seq1_team = m_subteam.inq_teamn("s", away[0])

        cur = con.cursor()     
        if l_gubun == "A" or l_gubun == "W":
            sql = "SELECT 순위, 승점, 승, 무, 패, 득점, 실점, 득실차, 도움, 경기수 FROM 팀순위_UEFA where 팀 = ? and 팀구분 = ?"    
            data = (seq_team,"FIFA")
        else:
            sql = "SELECT 순위, 승점, 승, 무, 패, 득점, 실점, 득실차, 도움, 경기수 FROM 팀순위 where 팀 = ? and 팀구분 not in(?)"    
            data = (seq_team,"UEC")
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
            p7 = row[7]
            p8 = row[8]
            p9 = row[9]
            pa = row[5]
            if p9 == "":
                pass
            else:
                p9 = int(row[9])
            if pa == "":
                pass
            else:
                pa = int(row[5])
        
            aseq.append(p0)
            asjum.append(p1)
            awin.append(p2)
            adraw.append(p3)
            alose.append(p4)
            aduk.append(p5)
            asil.append(p6)
            acha.append(p7)
            aassist.append(p8)
            atotal.append(p9)
            if p9 == "" or pa == "":
                apduk.append("")
            elif p9 == 0 or pa == 0:
                apduk.append(0)
            else:
                j2 = 0
                j2 = round(pa/p9,2)
                apduk.append(j2)

        if l_gubun == "A" or l_gubun == "W":
            cur = con.cursor()
            sql = "SELECT 순위, 승점, 승, 무, 패, 득점, 실점, 득실차, 조 FROM 팀순위_WCP where 팀 = ?"    
            data = (seq1_team,)
            cur.execute(sql,data)

            rows = cur.fetchall()
            for row in rows:
                p0 = int(row[0])
                p1 = int(row[1])
                p2 = row[2]
                p3 = row[3]
                p4 = row[4]
                p5 = row[5]
                p6 = row[6]
                p7 = row[7]
                p8 = row[8]
            
                waseq.append(p0)
                wasjum.append(p1)
                wawin.append(p2)
                wadraw.append(p3)
                walose.append(p4)
                waduk.append(p5)
                wasil.append(p6)
                wacha.append(p7)
                wajo.append(p8)

        cur = con.cursor()
        sql = "SELECT 순위, 선수, 득점, 도움, 공격포인트, 경기수, 슈팅, 유효슈팅, 파울, 경고, 퇴장, 오프사이드 " \
               " FROM 개인순위 where 팀명 like ? order by 순위"    
        data = (inq_team,)
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
            gaseq.append(p1)
            gaplay.append(p2)
            gaduk.append(p3)
            gaassist.append(p4) 
            gapoint.append(p5)
            gatotal.append(p6)
            gashoot.append(p7)
            gayshoot.append(p8) 
            gafoul.append(p9) 
            gayellow.append(p10)
            gared.append(p11)
            gaoffside.append(p12)

        # print(gaplay,gaduk)

        cur = con.cursor()
        sql = "SELECT 포지션, 선수, 득점, 도움, 공격포인트, 경기, 슈팅, 유효슈팅, 경고, 퇴장, 오프사이드 " \
               " FROM 선수 where 팀명 like ? order by 포지션, 득점 desc"    
        data = (inq_team,)
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
            sapos.append(p1)
            saplay.append(p2)
            saduk.append(p3)
            saassist.append(p4) 
            sapoint.append(p5)
            satotal.append(p6)
            sashoot.append(p7)
            sayshoot.append(p8) 
            sayellow.append(p9)
            sared.append(p10)
            saoffside.append(p11)

    con.close() 

    home[0] = '"'+home[0]
    away[0] = "'"+away[0]
    
    sh = str(i) + "경기"
    st.subheader(sh)
    df = pd.DataFrame(data=np.array([[home[0][1:],hseq[0],hsjum[0],htotal[0],hwin[0],hdraw[0],hlose[0],hduk[0],hsil[0],hcha[0],hpduk[0]],
                                     [away[0][1:],aseq[0],asjum[0],atotal[0],awin[0],adraw[0],alose[0],aduk[0],asil[0],acha[0],apduk[0]]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","순위","승점","경기수","승","무","패","득점","실점","득실차","평균득점"]) 

    st.dataframe(df)

    colors = ['#FFA07A', '#F0E68C', '#87CEFA']
    labels = ['승','무','패']
    values = [hwin[0], hdraw[0], hlose[0]]

    figh = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figh.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    values = [awin[0], adraw[0], alose[0]]

    figa = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figa.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    if hwin[0] == "" and hdraw[0] == "" and hlose[0] == "":
        pass
    else:
        tab1, tab2 = st.tabs(["홈팀 전적", "원정팀 전적"])
        with tab1:
            st.plotly_chart(figh, theme="streamlit")
        with tab2:
            st.plotly_chart(figa, theme="streamlit")

    if l_gubun == "A" or l_gubun == "W":
        if wgaw == "1":
            df = pd.DataFrame(data=np.array([[home[0][1:],whjo[0],whseq[0],whsjum[0],whwin[0],whdraw[0],whlose[0],whduk[0],whsil[0],whcha[0]],
                                            [away[0][1:],wajo[0],waseq[0],wasjum[0],wawin[0],wadraw[0],walose[0],waduk[0],wasil[0],wacha[0]]]), 

                    index= ["홈팀", "원정팀"], 
                    columns=["팀명","조","순위","승점","승","무","패","득점","실점","득실차"]) 

            st.dataframe(df)

            values = [whwin[0], whdraw[0], whlose[0]]

            figwh = go.Figure(data=[go.Pie(labels=labels, values=values)])
            figwh.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

            values = [wawin[0], wadraw[0], walose[0]]

            figwa = go.Figure(data=[go.Pie(labels=labels, values=values)])
            figwa.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

            if whwin[0] == "" and whdraw[0] == "" and whlose[0] == "":
                pass
            else:
                tab1, tab2 = st.tabs(["홈팀 전적", "원정팀 전적"])
                with tab1:
                    st.plotly_chart(figwh, theme="streamlit")
                with tab2:
                    st.plotly_chart(figwa, theme="streamlit")

    st.markdown(":soccer: :blue[**투표 현황**]")
    df = pd.DataFrame(data=np.array([[home[0][1:],away[0][1:],win[0],draw[0],lose[0],fwin[0],fdraw[0],flose[0],result[0]]]), 

            index= ["현재"], 
            columns=["홈팀","원정팀","승","무","패","해외승","해외무","해외패","결과"]) 

    st.dataframe(df)

    win[0] = win[0].replace('%','')
    draw[0] = draw[0].replace('%','')
    lose[0] = lose[0].replace('%','')
    values = [win[0], draw[0], lose[0]]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    st.plotly_chart(fig)

    # for m in range(3):
    #     if m == 0:
    #         st.markdown("**순위**"+"("+str(hseq[0])+"위 : "+str(aseq[0])+"위)")
    #         df = pd.DataFrame(data=np.array([[hseq[0]],[aseq[0]]]), 
    #                 index= [home[0], away[0]], 
    #                 columns=["순위"]) 
            
    #         st.bar_chart(df, horizontal=True,use_container_width=True,color=["#C83F49"])
    #     elif m == 1:
    #         st.markdown("**승점**"+"("+str(hsjum[0])+" : "+str(asjum[0])+")")
    #         df = pd.DataFrame(data=np.array([[hsjum[0]],[asjum[0]]]),
    #                 index= [home[0], away[0]], 
    #                 columns=["승점"]) 

    #         st.bar_chart(df, horizontal=True,use_container_width=True,color=["#1E90FF"]) #dodger blue
    #     elif m == 2:
    #         st.markdown("**평균득점**"+"("+str(hpduk[0])+" : "+str(apduk[0])+")")
    #         df = pd.DataFrame(data=np.array([[hpduk[0]],[apduk[0]]]),
    #                 index= [home[0], away[0]], 
    #                 columns=["승점"]) 

    #         st.bar_chart(df, horizontal=True,use_container_width=True,color=["#12E193"])

    # 맞대결 전체
    game = 999
    gubun = ''
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subscgrass.wdl_cnt(home[0][1:], away[0][1:], l_gubun, game, gubun) 

    def hwdl_def(gamesu):

        hwdl = [''] * gamesu
        cntw = 0
        cntd = 0
        cntl = 0
        for i in range(gamesu): 
            if hwdl_list[i] == 3:
                hwdl[i] = "승"
                cntw += 1
            elif hwdl_list[i] == 1:
                hwdl[i] = "무"
                cntd += 1
            elif hwdl_list[i] == 0:
                hwdl[i] = "패"
                cntl += 1

        wdlk = ''
        wdlk = str(cntw)+"승"+str(cntd)+"무"+str(cntl)+"패"

        return hwdl, wdlk, cntw, cntd, cntl    
   
    def gyungi_m(gamesu):

        if gamesu == 7:
            df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

                    index= ["일자","점수","결과"], 
                    columns=["1","2","3","4","5","6","7"]) 
            st.dataframe(df)

        elif gamesu == 6:
            df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

                    index= ["일자","점수","결과"], 
                    columns=["1","2","3","4","5","6"]) 
            st.dataframe(df)

        elif gamesu == 5:
            df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

                    index= ["일자","점수","결과"], 
                    columns=["1","2","3","4","5"]) 
            st.dataframe(df)

        elif gamesu == 4:
            df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

                    index= ["일자","점수","결과"], 
                    columns=["1","2","3","4"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

                    index= ["일자","점수","결과"], 
                    columns=["1","2","3"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

                    index= ["일자","점수","결과"], 
                    columns=["1","2"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            df = pd.DataFrame(data=np.array([hil_list,jumsu_list,hwdl]),

                    index= ["일자","점수","결과"], 
                    columns=["1"]) 
            st.dataframe(df)
            
        elif gamesu == 0:
            st.markdown("")
   
    hwdl,wdlk, cntw, cntd, cntl = hwdl_def(len(hwdl_list))
     
    st.markdown(":soccer: :blue[**맞대결**]")
    st.markdown(" 전 체 : "+wdlk)
     
    # 맞대결 최근 7경기
    game = 7
    gubun = ''
    hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subscgrass.wdl_cnt(home[0][1:], away[0][1:], l_gubun, game, gubun) 

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))
  
    hwdl,wdlk, cntwm, cntdm, cntlm = hwdl_def(len(hwdl_list))
   
    st.markdown(" 최근7경기 : "+wdlk)
 
    gyungi_m(len(hwdl_list))

    values = [cntw, cntd, cntl]

    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    values = [cntwm, cntdm, cntlm]

    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    if cntw == 0 and cntd == 0 and cntl == 0:
        pass
    else:
        tab1, tab2 = st.tabs(["맞대결 전체", "맞대결 최근7경기"])
        with tab1:
            st.plotly_chart(fig1, theme="streamlit")
        with tab2:
            st.plotly_chart(fig2, theme="streamlit")

    # 최근 7경기
    game = 7
    gubun = ''
    hil_list, hteam_list, hateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subscgrai.wdl_cnt(home[0][1:], l_gubun, game, gubun)

    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    def gyungi_c(gamesu):

        if gamesu == 7:
            df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

                    index= ["일자","상대","점수","결과"], 
                    columns=["1","2","3","4","5","6","7"]) 
            st.dataframe(df)

        elif gamesu == 6:
            df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

                    index= ["일자","상대","점수","결과"], 
                    columns=["1","2","3","4","5","6"]) 
            st.dataframe(df)

        elif gamesu == 5:
            df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

                    index= ["일자","상대","점수","결과"], 
                    columns=["1","2","3","4","5"]) 
            st.dataframe(df)

        elif gamesu == 4:
            df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

                    index= ["일자","상대","점수","결과"], 
                    columns=["1","2","3","4"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

                    index= ["일자","상대","점수","결과"], 
                    columns=["1","2","3"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

                    index= ["일자","상대","점수","결과"], 
                    columns=["1","2"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            df = pd.DataFrame(data=np.array([hil_list,hateam_list,jumsu_list,hwdl]),

                    index= ["일자","상대","점수","결과"], 
                    columns=["1"]) 
            st.dataframe(df)
            
        elif gamesu == 0:
            st.markdown("")

    hwdl,wdlk, cntwmh, cntdmh, cntlmh = hwdl_def(len(hwdl_list))
   
    st.markdown(":soccer: :blue[**최근7경기**]")
    st.markdown("홈팀 : "+home[0][1:]+"("+wdlk+")")

    gyungi_c(len(hwdl_list))    

    game = 7
    gubun = ''
    hil_list, hteam_list, hateam_list, hjumsu1_list, hjumsu2_list, hwdl_list = m_subscgrai.wdl_cnt(away[0][1:], l_gubun, game, gubun)
   
    jumsu_list = []
    for i in range(len(hil_list)):
        jumsu_list.append(str(hjumsu1_list[i])+':'+str(hjumsu2_list[i]))

    hwdl,wdlk, cntwma, cntdma, cntlma = hwdl_def(len(hwdl_list))
    
    st.markdown("원정팀 : "+away[0][1:]+"("+wdlk+")")
    
    gyungi_c(len(hwdl_list))

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
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4],ghduk[5],ghduk[6]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2],ghassist[3],ghassist[4],ghassist[5],ghassist[6]],
                    "공격포인트":[ghpoint[0],ghpoint[1],ghpoint[2],ghpoint[3],ghpoint[4],ghpoint[5],ghpoint[6]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2],ghtotal[3],ghtotal[4],ghtotal[5],ghtotal[6]],
                    "슈팅":[ghshoot[0],ghshoot[1],ghshoot[2],ghshoot[3],ghshoot[4],ghshoot[5],ghshoot[6]],
                    "유효슈팅":[ghyshoot[0],ghyshoot[1],ghyshoot[2],ghyshoot[3],ghyshoot[4],ghyshoot[5],ghyshoot[6]],
                    "경고":[ghyellow[0],ghyellow[1],ghyellow[2],ghyellow[3],ghyellow[4],ghyellow[5],ghyellow[6]],
                    "퇴장":[ghred[0],ghred[1],ghred[2],ghred[3],ghred[4],ghred[5],ghred[6]],
                    "오프사이드":[ghoffside[0],ghoffside[1],ghoffside[2],ghoffside[3],ghoffside[4],ghoffside[5],ghoffside[6]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6","7"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)

        elif gamesu == 6:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3],ghseq[4],ghseq[5]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3],ghplay[4],ghplay[5]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4],ghduk[5]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2],ghassist[3],ghassist[4],ghassist[5]],
                    "공격포인트":[ghpoint[0],ghpoint[1],ghpoint[2],ghpoint[3],ghpoint[4],ghpoint[5]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2],ghtotal[3],ghtotal[4],ghtotal[5]],
                    "슈팅":[ghshoot[0],ghshoot[1],ghshoot[2],ghshoot[3],ghshoot[4],ghshoot[5]],
                    "유효슈팅":[ghyshoot[0],ghyshoot[1],ghyshoot[2],ghyshoot[3],ghyshoot[4],ghyshoot[5]],
                    "경고":[ghyellow[0],ghyellow[1],ghyellow[2],ghyellow[3],ghyellow[4],ghyellow[5]],
                    "퇴장":[ghred[0],ghred[1],ghred[2],ghred[3],ghred[4],ghred[5]],
                    "오프사이드":[ghoffside[0],ghoffside[1],ghoffside[2],ghoffside[3],ghoffside[4],ghoffside[5]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)

        elif gamesu == 5:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3],ghseq[4]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3],ghplay[4]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3],ghduk[4]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2],ghassist[3],ghassist[4]],
                    "공격포인트":[ghpoint[0],ghpoint[1],ghpoint[2],ghpoint[3],ghpoint[4]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2],ghtotal[3],ghtotal[4]],
                    "슈팅":[ghshoot[0],ghshoot[1],ghshoot[2],ghshoot[3],ghshoot[4]],
                    "유효슈팅":[ghyshoot[0],ghyshoot[1],ghyshoot[2],ghyshoot[3],ghyshoot[4]],
                    "경고":[ghyellow[0],ghyellow[1],ghyellow[2],ghyellow[3],ghyellow[4]],
                    "퇴장":[ghred[0],ghred[1],ghred[2],ghred[3],ghred[4]],
                    "오프사이드":[ghoffside[0],ghoffside[1],ghoffside[2],ghoffside[3],ghoffside[4]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)

        elif gamesu == 4:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2],ghseq[3]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2],ghplay[3]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2],ghduk[3]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2],ghassist[3]],
                    "공격포인트":[ghpoint[0],ghpoint[1],ghpoint[2],ghpoint[3]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2],ghtotal[3]],
                    "슈팅":[ghshoot[0],ghshoot[1],ghshoot[2],ghshoot[3]],
                    "유효슈팅":[ghyshoot[0],ghyshoot[1],ghyshoot[2],ghyshoot[3]],
                    "경고":[ghyellow[0],ghyellow[1],ghyellow[2],ghyellow[3]],
                    "퇴장":[ghred[0],ghred[1],ghred[2],ghred[3]],
                    "오프사이드":[ghoffside[0],ghoffside[1],ghoffside[2],ghoffside[3]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            data = {"순위":[ghseq[0],ghseq[1],ghseq[2]],
                    "선수":[ghplay[0],ghplay[1],ghplay[2]],
                    "득점":[ghduk[0],ghduk[1],ghduk[2]],
                    "어시스트":[ghassist[0],ghassist[1],ghassist[2]],
                    "공격포인트":[ghpoint[0],ghpoint[1],ghpoint[2]],
                    "경기수":[ghtotal[0],ghtotal[1],ghtotal[2]],
                    "슈팅":[ghshoot[0],ghshoot[1],ghshoot[2]],
                    "유효슈팅":[ghyshoot[0],ghyshoot[1],ghyshoot[2]],
                    "경고":[ghyellow[0],ghyellow[1],ghyellow[2]],
                    "퇴장":[ghred[0],ghred[1],ghred[2]],
                    "오프사이드":[ghoffside[0],ghoffside[1],ghoffside[2]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            data = {"순위":[ghseq[0],ghseq[1]],
                    "선수":[ghplay[0],ghplay[1]],
                    "득점":[ghduk[0],ghduk[1]],
                    "어시스트":[ghassist[0],ghassist[1]],
                    "공격포인트":[ghpoint[0],ghpoint[1]],
                    "경기수":[ghtotal[0],ghtotal[1]],
                    "슈팅":[ghshoot[0],ghshoot[1]],
                    "유효슈팅":[ghyshoot[0],ghyshoot[1]],
                    "경고":[ghyellow[0],ghyellow[1]],
                    "퇴장":[ghred[0],ghred[1]],
                    "오프사이드":[ghoffside[0],ghoffside[1]]}
            df = pd.DataFrame(data,

                    index= ["1","2"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            data = {"순위":[ghseq[0]],
                    "선수":[ghplay[0]],
                    "득점":[ghduk[0]],
                    "어시스트":[ghassist[0]],
                    "공격포인트":[ghpoint[0]],
                    "경기수":[ghtotal[0]],
                    "슈팅":[ghshoot[0]],
                    "유효슈팅":[ghyshoot[0]],
                    "경고":[ghyellow[0]],
                    "퇴장":[ghred[0]],
                    "오프사이드":[ghoffside[0]]}
            df = pd.DataFrame(data,

                    index= ["1"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)
    
    if len(ghplay) == 0:
        pass
    else:
        st.markdown(":soccer: :blue[**득점순위**]")
           
        st.markdown("홈팀 : "+home[0][1:]+"("+str(len(ghplay))+"명)")
    
        gaein_home(len(ghplay))

    def gaein_away(gamesu):

        if gamesu == 7:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4],gaseq[5],gaseq[6]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4],gaplay[5],gaplay[6]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4],gaduk[5],gaduk[6]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2],gaassist[3],gaassist[4],gaassist[5],gaassist[6]],
                    "공격포인트":[gapoint[0],gapoint[1],gapoint[2],gapoint[3],gapoint[4],gapoint[5],gapoint[6]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4],gatotal[5],gatotal[6]],
                    "슈팅":[gashoot[0],gashoot[1],gashoot[2],gashoot[3],gashoot[4],gashoot[5],gashoot[6]],
                    "유효슈팅":[gayshoot[0],gayshoot[1],gayshoot[2],gayshoot[3],gayshoot[4],gayshoot[5],gayshoot[6]],
                    "경고":[gayellow[0],gayellow[1],gayellow[2],gayellow[3],gayellow[4],gayellow[5],gayellow[6]],
                    "퇴장":[gared[0],gared[1],gared[2],gared[3],gared[4],gared[5],gared[6]],
                    "오프사이드":[gaoffside[0],gaoffside[1],gaoffside[2],gaoffside[3],gaoffside[4],gaoffside[5],gaoffside[6]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6","7"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)

        elif gamesu == 6:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4],gaseq[5]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4],gaplay[5]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4],gaduk[5]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2],gaassist[3],gaassist[4],gaassist[5]],
                    "공격포인트":[gapoint[0],gapoint[1],gapoint[2],gapoint[3],gapoint[4],gapoint[5]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4],gatotal[5]],
                    "슈팅":[gashoot[0],gashoot[1],gashoot[2],gashoot[3],gashoot[4],gashoot[5]],
                    "유효슈팅":[gayshoot[0],gayshoot[1],gayshoot[2],gayshoot[3],gayshoot[4],gayshoot[5]],
                    "경고":[gayellow[0],gayellow[1],gayellow[2],gayellow[3],gayellow[4],gayellow[5]],
                    "퇴장":[gared[0],gared[1],gared[2],gared[3],gared[4],gared[5]],
                    "오프사이드":[gaoffside[0],gaoffside[1],gaoffside[2],gaoffside[3],gaoffside[4],gaoffside[5]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5","6"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)

        elif gamesu == 5:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3],gaseq[4]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3],gaplay[4]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3],gaduk[4]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2],gaassist[3],gaassist[4]],
                    "공격포인트":[gapoint[0],gapoint[1],gapoint[2],gapoint[3],gapoint[4]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2],gatotal[3],gatotal[4]],
                    "슈팅":[gashoot[0],gashoot[1],gashoot[2],gashoot[3],gashoot[4]],
                    "유효슈팅":[gayshoot[0],gayshoot[1],gayshoot[2],gayshoot[3],gayshoot[4]],
                    "경고":[gayellow[0],gayellow[1],gayellow[2],gayellow[3],gayellow[4]],
                    "퇴장":[gared[0],gared[1],gared[2],gared[3],gared[4]],
                    "오프사이드":[gaoffside[0],gaoffside[1],gaoffside[2],gaoffside[3],gaoffside[4]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4","5"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)

        elif gamesu == 4:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2],gaseq[3]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2],gaplay[3]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2],gaduk[3]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2],gaassist[3]],
                    "공격포인트":[gapoint[0],gapoint[1],gapoint[2],gapoint[3]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2],gatotal[3]],
                    "슈팅":[gashoot[0],gashoot[1],gashoot[2],gashoot[3]],
                    "유효슈팅":[gayshoot[0],gayshoot[1],gayshoot[2],gayshoot[3]],
                    "경고":[gayellow[0],gayellow[1],gayellow[2],gayellow[3]],
                    "퇴장":[gared[0],gared[1],gared[2],gared[3]],
                    "오프사이드":[gaoffside[0],gaoffside[1],gaoffside[2],gaoffside[3]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3","4"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)
            
        elif gamesu == 3:
            data = {"순위":[gaseq[0],gaseq[1],gaseq[2]],
                    "선수":[gaplay[0],gaplay[1],gaplay[2]],
                    "득점":[gaduk[0],gaduk[1],gaduk[2]],
                    "어시스트":[gaassist[0],gaassist[1],gaassist[2]],
                    "공격포인트":[gapoint[0],gapoint[1],gapoint[2]],
                    "경기수":[gatotal[0],gatotal[1],gatotal[2]],
                    "슈팅":[gashoot[0],gashoot[1],gashoot[2]],
                    "유효슈팅":[gayshoot[0],gayshoot[1],gayshoot[2]],
                    "경고":[gayellow[0],gayellow[1],gayellow[2]],
                    "퇴장":[gared[0],gared[1],gared[2]],
                    "오프사이드":[gaoffside[0],gaoffside[1],gaoffside[2]]}
            df = pd.DataFrame(data,

                    index= ["1","2","3"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)
            
        elif gamesu == 2:
            data = {"순위":[gaseq[0],gaseq[1]],
                    "선수":[gaplay[0],gaplay[1]],
                    "득점":[gaduk[0],gaduk[1]],
                    "어시스트":[gaassist[0],gaassist[1]],
                    "공격포인트":[gapoint[0],gapoint[1]],
                    "경기수":[gatotal[0],gatotal[1]],
                    "슈팅":[gashoot[0],gashoot[1]],
                    "유효슈팅":[gayshoot[0],gayshoot[1]],
                    "경고":[gayellow[0],gayellow[1]],
                    "퇴장":[gared[0],gared[1]],
                    "오프사이드":[gaoffside[0],gaoffside[1]]}
            df = pd.DataFrame(data,

                    index= ["1","2"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)
            
        elif gamesu == 1:
            data = {"순위":[gaseq[0]],
                    "선수":[gaplay[0]],
                    "득점":[gaduk[0]],
                    "어시스트":[gaassist[0]],
                    "공격포인트":[gapoint[0]],
                    "경기수":[gatotal[0]],
                    "슈팅":[gashoot[0]],
                    "유효슈팅":[gayshoot[0]],
                    "경고":[gayellow[0]],
                    "퇴장":[gared[0]],
                    "오프사이드":[gaoffside[0]]}
            df = pd.DataFrame(data,

                    index= ["1"], 
                    columns=["순위","선수","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
            st.dataframe(df)
        
    if len(gaplay) == 0:
        pass
    else:
        if len(ghplay) == 0:
            st.markdown(":soccer: :blue[**득점순위**]")
        st.markdown("원정팀 : "+away[0][1:]+"("+str(len(gaplay))+"명)")
     
        gaein_away(len(gaplay))

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    
    if len(shplay) == 0:
        pass
    else:
        st.markdown(":soccer: :blue[**선수**]")
        # st.markdown("홈팀 : "+home[0][1:]+"("+str(len(shplay))+"명)")
        st.markdown("홈팀 : "+home[0][1:])

        data = {"선수":[shplay],"포지션":[shpos],"득점":[shduk],"어시스트":[shassist],"공격포인트":[shpoint],"경기수":[shtotal],
                "슈팅":[shshoot],"유효슈팅":[shyshoot],"경고":[shyellow],"퇴장":[shred],"오프사이드":[shoffside]}
        
        df = pd.DataFrame(data,
                columns=["선수","포지션","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
        
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        # fill_color='paleturquoise',
                        align='center'),
            cells=dict(values=[shplay,shpos,shduk,shassist,shpoint,shtotal,shshoot,shyshoot,shyellow,shred,shoffside],
                    #    fill_color='lavender',
                    align='center'))
        ])

        fig.update_layout(height=500)

        st.plotly_chart(fig)

    if len(saplay) == 0:
        pass
    else:
        if len(shplay) == 0:
            st.markdown(":soccer: :blue[**선수**]")
        # st.markdown("원정팀 : "+away[0][1:]+"("+str(len(saplay))+"명)")
        st.markdown("원정팀 : "+away[0][1:])
    
        data = {"선수":[saplay],"포지션":[sapos],"득점":[saduk],"어시스트":[saassist],"공격포인트":[sapoint],"경기수":[satotal],
                "슈팅":[sashoot],"유효슈팅":[sayshoot],"경고":[sayellow],"퇴장":[sared],"오프사이드":[saoffside]}
        
        df = pd.DataFrame(data,
                columns=["선수","포지션","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅","경고","퇴장","오프사이드"]) 
        
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        # fill_color='paleturquoise',
                        align='center'),
            cells=dict(values=[saplay,sapos,saduk,saassist,sapoint,satotal,sashoot,sayshoot,sayellow,sared,saoffside],
                    #    fill_color='lavender',
                    align='center'))
        ])

        fig.update_layout(height=500)

        st.plotly_chart(fig)

