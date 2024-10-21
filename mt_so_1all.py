import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
import plotly.graph_objects as go

def Crawler(yearc,countc,gyungi):
    
    home = ""
    away = ""
    hseq = ""
    aseq = ""
    hsjum = ""
    asjum = ""
    hwin = ""
    hdraw = ""
    hlose = ""
    awin = ""
    adraw = ""
    alose = ""
    hduk = ""
    aduk = ""
    hsil = ""
    asil = ""
    hcha = ""
    acha = ""
    hassist = ""
    aassist = ""
    hpduk = ""
    apduk = ""
    htotal = ""
    atotal = ""
    win = ""
    draw = ""
    lose = ""
    result = ""
    fwin = ""
    fdraw = ""
    flose = ""
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
    whseq = ""
    waseq = ""
    whsjum = ""
    wasjum = ""
    whwin = ""
    wawin = ""
    whdraw = ""
    wadraw = ""
    whlose = ""
    walose = ""
    whduk = ""
    waduk = ""
    whsil = ""
    wasil = ""
    whcha = ""
    wacha = ""
    whjo = ""
    wajo = ""
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

    # print(year,count,i)
 
    def read_txt(g,k):
        if g == '01':
            f = open('soccer_so1_teamhome.txt', 'r', encoding='UTF8')
        elif g == '02':
            f = open('soccer_so1_teamaway.txt', 'r', encoding='UTF8')
        elif g == '03':
            f = open('soccer_so1_onehome.txt', 'r', encoding='UTF8')
        elif g == '04':
            f = open('soccer_so1_oneaway.txt', 'r', encoding='UTF8')
        elif g == '05':
            f = open('soccer_so1_onetwohome.txt', 'r', encoding='UTF8')
        elif g == '06':
            f = open('soccer_so1_onetwoaway.txt', 'r', encoding='UTF8')
        elif g == '07':
            f = open('soccer_so1_hyunhwang.txt', 'r', encoding='UTF8')
        # if g == '01':
        #     f = open('D:/datagithub/soccer/soccer_so1_teamhome.txt', 'r', encoding='UTF8')
        # elif g == '02':
        #     f = open('D:/datagithub/soccer/soccer_so1_teamaway.txt', 'r', encoding='UTF8')
        # elif g == '03':
        #     f = open('D:/datagithub/soccer/soccer_so1_onehome.txt', 'r', encoding='UTF8')
        # elif g == '04':
        #     f = open('D:/datagithub/soccer/soccer_so1_oneaway.txt', 'r', encoding='UTF8')
        # elif g == '05':
        #     f = open('D:/datagithub/soccer/soccer_so1_onetwohome.txt', 'r', encoding='UTF8')
        # elif g == '06':
        #     f = open('D:/datagithub/soccer/soccer_so1_onetwoaway.txt', 'r', encoding='UTF8')
        # elif g == '07':
        #     f = open('D:/datagithub/soccer/soccer_so1_hyunhwang.txt', 'r', encoding='UTF8')

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
            f = open('soccer_so1_vstotal.txt', 'r', encoding='UTF8')
        elif g == '12':
            f = open('soccer_so1_vsseven.txt', 'r', encoding='UTF8')
        elif g == '13':
            f = open('soccer_so1_sevenhome.txt', 'r', encoding='UTF8')
        elif g == '14':
            f = open('soccer_so1_sevenaway.txt', 'r', encoding='UTF8')
        elif g == '15':
            f = open('soccer_so1_dukhome.txt', 'r', encoding='UTF8')
        elif g == '16':
            f = open('soccer_so1_dukaway.txt', 'r', encoding='UTF8')
        elif g == '17':
            f = open('soccer_so1_playerhome.txt', 'r', encoding='UTF8')
        elif g == '18':
            f = open('soccer_so1_playeraway.txt', 'r', encoding='UTF8')
        # if g == '11':
        #     f = open('D:/datagithub/soccer/soccer_so1_vstotal.txt', 'r', encoding='UTF8')
        # elif g == '12':
        #     f = open('D:/datagithub/soccer/soccer_so1_vsseven.txt', 'r', encoding='UTF8')
        # elif g == '13':
        #     f = open('D:/datagithub/soccer/soccer_so1_sevenhome.txt', 'r', encoding='UTF8')
        # elif g == '14':
        #     f = open('D:/datagithub/soccer/soccer_so1_sevenaway.txt', 'r', encoding='UTF8')
        # elif g == '15':
        #     f = open('D:/datagithub/soccer/soccer_so1_dukhome.txt', 'r', encoding='UTF8')
        # elif g == '16':
        #     f = open('D:/datagithub/soccer/soccer_so1_dukaway.txt', 'r', encoding='UTF8')
        # elif g == '17':
        #     f = open('D:/datagithub/soccer/soccer_so1_playerhome.txt', 'r', encoding='UTF8')
        # elif g == '18':
        #     f = open('D:/datagithub/soccer/soccer_so1_playeraway.txt', 'r', encoding='UTF8')

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
                hdraw = team_read[s:r]
                s = r+1
            elif rcnt == 7:
                hlose = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                hduk = team_read[s:r]
                s = r+1
            elif rcnt == 9:
                hsil = team_read[s:r]
                s = r+1
            elif rcnt == 10:
                hcha = team_read[s:r]
                s = r+1
                hpduk = team_read[s:]

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
                adraw = team_read[s:r]
                s = r+1
            elif rcnt == 7:
                alose = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                aduk = team_read[s:r]
                s = r+1
            elif rcnt == 9:
                asil = team_read[s:r]
                s = r+1
            elif rcnt == 10:
                acha = team_read[s:r]
                s = r+1
                apduk = team_read[s:]
    
    team_read = read_txt('05',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                home = team_read[:r]
                s = r+1
            elif rcnt == 2:
                whjo = team_read[s:r]
                s = r+1
            elif rcnt == 3:
                whseq = team_read[s:r]
                s = r+1
            elif rcnt == 4:
                whsjum = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                whwin = team_read[s:r]
                s = r+1
            elif rcnt == 6:
                whdraw = team_read[s:r]
                s = r+1
            elif rcnt == 7:
                whlose = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                whduk = team_read[s:r]
                s = r+1
            elif rcnt == 9:
                whsil = team_read[s:r]
                s = r+1
                whcha = team_read[s:]
                wgaw = "1"     
    
    team_read = read_txt('06',k)

    rcnt = 0
    for r in range(len(team_read)):
        if team_read[r] == ";":
            rcnt += 1
            if rcnt == 1:
                away = team_read[:r]
                s = r+1
            elif rcnt == 2:
                wajo = team_read[s:r]
                s = r+1
            elif rcnt == 3:
                waseq = team_read[s:r]
                s = r+1
            elif rcnt == 4:
                wasjum = team_read[s:r]
                s = r+1
            elif rcnt == 5:
                wawin = team_read[s:r]
                s = r+1
            elif rcnt == 6:
                wadraw = team_read[s:r]
                s = r+1
            elif rcnt == 7:
                walose = team_read[s:r]
                s = r+1
            elif rcnt == 8:
                waduk = team_read[s:r]
                s = r+1
            elif rcnt == 9:
                wasil = team_read[s:r]
                s = r+1
                wacha = team_read[s:]
                wgaw = "1"
    
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
   
    ssh = str(year) + "년 축구 승무패 " + str(count) + "회차"
    st.subheader(ssh)

    sh = str(i) + "경기"
    st.subheader(sh)

    df = pd.DataFrame(data=np.array([[home,hseq,hsjum,htotal,hwin,hdraw,hlose,hduk,hsil,hcha,hpduk],
                                     [away,aseq,asjum,atotal,awin,adraw,alose,aduk,asil,acha,apduk]]), 

            index= ["홈팀", "원정팀"], 
            columns=["팀명","순위","승점","경기수","승","무","패","득점","실점","득실차","평균득점"]) 

    st.dataframe(df)

    colors = ['#FFA07A', '#F0E68C', '#87CEFA']
    labels = ['승','무','패']
    values1 = [hwin, hdraw, hlose]

    figh = go.Figure(data=[go.Pie(labels=labels, values=values1)])
    figh.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    values2 = [awin, adraw, alose]

    figa = go.Figure(data=[go.Pie(labels=labels, values=values2)])
    figa.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
     
    if hwin == "" and hdraw == "" and hlose == "":
        pass
    else:
        tab1, tab2 = st.tabs(["홈팀 전적", "원정팀 전적"])
        with tab1:
            st.plotly_chart(figh)
        with tab2:
            try:
                st.plotly_chart(figa)
            except:
                st.plotly_chart(figa, theme=None)
     
    if l_hgubun == "A" or l_hgubun == "W":
        if wgaw == "1":
            df = pd.DataFrame(data=np.array([[home,whjo,whseq,whsjum,whwin,whdraw,whlose,whduk,whsil,whcha],
                                            [away,wajo,waseq,wasjum,wawin,wadraw,walose,waduk,wasil,wacha]]), 

                    index= ["홈팀", "원정팀"], 
                    columns=["팀명","조","순위","승점","승","무","패","득점","실점","득실차"]) 

            st.dataframe(df)

            values3 = [whwin, whdraw, whlose]

            figwh = go.Figure(data=[go.Pie(labels=labels, values=values3)])
            figwh.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

            values4 = [wawin, wadraw, walose]

            figwa = go.Figure(data=[go.Pie(labels=labels, values=values4)])
            figwa.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

            if whwin == "" and whdraw == "" and whlose == "":
                pass
            else:
                tab1, tab2 = st.tabs(["홈팀 전적", "원정팀 전적"])
                with tab1:
                    st.plotly_chart(figwh)
                with tab2:
                    try:
                        st.plotly_chart(figwa)
                    except:
                        st.plotly_chart(figwa, theme=None)

    st.markdown(":soccer: :blue[**투표 현황**]")
    df = pd.DataFrame(data=np.array([[home,away,win,draw,lose,fwin,fdraw,flose,result]]), 

            index= ["현재"], 
            columns=["홈팀","원정팀","승","무","패","해외승","해외무","해외패","결과"]) 

    st.dataframe(df)

    win = win.replace('%','')
    draw = draw.replace('%','')
    lose = lose.replace('%','')

    values5 = [win, draw, lose]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values5)])
    fig.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    try:
        st.plotly_chart(fig)
    except:
        st.plotly_chart(fig, theme=None)

    
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
            elif int(hwdl_list[i]) == 1:
                hwdl[i] = "무"
                cntd += 1
            elif int(hwdl_list[i]) == 0:
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
 
    gyungi_m(len(hwdl_list))

    values6 = [cntw, cntd, cntl]

    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
    fig1.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    values7 = [cntwm, cntdm, cntlm]

    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
    fig2.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    if cntw == 0 and cntd == 0 and cntl == 0:
        pass
    else:
        tab1, tab2 = st.tabs(["맞대결 전체", "맞대결 최근7경기"])
        with tab1:
            st.plotly_chart(fig1)
        with tab2:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)

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
    st.markdown("홈팀 : "+home+"("+wdlk+")")

    gyungi_c(len(hwdl_list))    
  
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
    
    gyungi_c(len(hwdl_list))

    values8 = [cntwmh, cntdmh, cntlmh]
    fig3 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
    fig3.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
  
    values9 = [cntwma, cntdma, cntlma]
    fig4 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
    fig4.update_traces(textfont_size=18,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    tab1, tab2 = st.tabs(["홈팀 최근7경기", "원정팀 최근7경기"])
    with tab1:
        st.plotly_chart(fig3)
    with tab2:
        try:
            st.plotly_chart(fig4)
        except:
            st.plotly_chart(fig4, theme=None)

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
        elif gamesu == 0:
            pass
     
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
                    ghduk.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    ghassist.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    ghpoint.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    ghtotal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    ghshoot.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    ghyshoot.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    ghyellow.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    ghred.append(team_read[q][s:r])
                    s = r+1
                    ghoffside.append(team_read[q][s:])

    if len(ghplay) == 0:
        pass
    else:
        st.markdown(":soccer: :blue[**득점순위**]")
           
        st.markdown("홈팀 : "+home+"("+str(len(ghplay))+"명)")
    
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
        elif gamesu == 0:
            pass
         
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
                    gaduk.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    gaassist.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    gapoint.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    gatotal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    gashoot.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    gayshoot.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    gayellow.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    gared.append(team_read[q][s:r])
                    s = r+1
                    gaoffside.append(team_read[q][s:])
   
    if len(gaplay) == 0:
        pass
    else:
        if len(ghplay) == 0:
            st.markdown(":soccer: :blue[**득점순위**]")
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
                    shduk.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    shassist.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    shpoint.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    shtotal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    shshoot.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    shyshoot.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    shyellow.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    shred.append(team_read[q][s:r])
                    s = r+1
                    shoffside.append(team_read[q][s:])

    team_read = read_all_txt('18',k)
    
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
                    saduk.append(team_read[q][s:r]) 
                    s = r+1
                elif rcnt == 4:
                    saassist.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 5:
                    sapoint.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 6:
                    satotal.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 7:
                    sashoot.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 8:
                    sayshoot.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 9:
                    sayellow.append(team_read[q][s:r])
                    s = r+1
                elif rcnt == 10:
                    sared.append(team_read[q][s:r])
                    s = r+1
                    saoffside.append(team_read[q][s:])

    # if len(shplay) == 0 & len(saplay) == 0:
    #     pass
    # else:
    st.markdown(":soccer: :blue[**선수**]")

    dataq = {"선수":[shplay],"포지션":[shpos],"득점":[shduk],"어시스트":[shassist],"공격포인트":[shpoint],"경기수":[shtotal],
            "슈팅":[shshoot],"유효슈팅":[shyshoot]}
    
    dfq = pd.DataFrame(dataq,
            columns=["선수","포지션","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅"]) 
    
    figq = go.Figure(data=[go.Table(
        header=dict(values=list(dfq.columns),
                    # fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[shplay,shpos,shduk,shassist,shpoint,shtotal,shshoot,shyshoot],
                #    fill_color='lavender',
                align='left'))])
    
    datar = {"선수":[saplay],"포지션":[sapos],"득점":[saduk],"어시스트":[saassist],"공격포인트":[sapoint],"경기수":[satotal],
            "슈팅":[sashoot],"유효슈팅":[sayshoot]}
    
    dfr = pd.DataFrame(datar,
            columns=["선수","포지션","득점","어시스트","공격포인트","경기수","슈팅","유효슈팅"]) 
    
    figr = go.Figure(data=[go.Table(
        header=dict(values=list(dfr.columns),
                    # fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[saplay,sapos,saduk,saassist,sapoint,satotal,sashoot,sayshoot],
                #    fill_color='lavender',
                align='left'))])

    figq.update_layout(height=500)
    figr.update_layout(height=500)
    
    
    if len(shplay) == 0 & len(saplay) == 0:
        tab1, tab2 = st.tabs(["홈팀", "원정팀"])
        with tab1:
            pass
        with tab2:
            pass
    else:
        tab1, tab2 = st.tabs(["홈팀", "원정팀"])
        with tab1:
            st.plotly_chart(figq, use_container_width=True)
        with tab2:
            st.plotly_chart(figr, use_container_width=True)

