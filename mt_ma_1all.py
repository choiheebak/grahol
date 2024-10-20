import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar

def Crawler(yearc,countc,gubun):
    
    ycount = []
    for i in range(len(yearc)):
        ycount.append(str(yearc[i])+"년 "+str(countc[i])+"회차")

    if gubun == 's':
      
        st.subheader("축구 승무패")

        option = st.selectbox(
        "",
        (ycount 
        )
        )

        sbox = option.replace("년 ","")
        sbox = sbox.replace("회차","")

        year = int(sbox[:4])
        count = int(sbox[4:])

        i = int(count)

        if i < 10:
            k = '0' + str(count)
        else:
            k = str(count)

        f = open('D:/datagithub/soccer/soccer_so0_master.txt', 'r', encoding='UTF8')
       
        rdr1 = f.readlines()    

        team_read = [] 
        for line in rdr1:
            if int(line[:4]) == int(year) and int(line[5:7]) == int(k):
                l = line[11:]
                l = l.replace("\n","")
                team_read.append(l)

        f.close

        home = []
        away = []
        win = []
        draw = []
        lose = []
        result = []
        fsu = []
        famt = []
        f2su = []
        f2amt = []
        f3su = []
        f3amt = []
        f4su = []
        f4amt = []
        bal = []

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        home.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        away.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 3:
                        win.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 4:
                        draw.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 5:
                        lose.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 6:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 7:
                        fsu.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        famt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        f2su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
                        f2amt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 11:
                        f3su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 12:
                        f3amt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 13:
                        f4su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 14:
                        f4amt.append(team_read[q][s:r])
                        s = r+1
                        bal.append(team_read[q][s:])


        if famt[0] == "":
            st.markdown(str(bal[0]))
        else:
            st.markdown(str(bal[0]))
            if fsu[0] == "":
                if famt[0][:1] == "-":
                    st.markdown("1등 : 0명")
                else:
                    st.markdown(famt[0])
            else:
                st.markdown("1등 : "+fsu[0]+"명 "+ famt[0]+"원")
            if f2su[0] == "":
                st.markdown("2등 : 0명")
            else:
                st.markdown("2등 : "+f2su[0]+"명 "+ f2amt[0]+"원")
            if f3su[0] == "":
                st.markdown("3등 : 0명")
            else:
                st.markdown("3등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
            st.markdown("4등 : "+f4su[0]+"명 "+ f4amt[0]+"원")
        

        data = {"홈팀":[home[0],home[1],home[2],home[3],home[4],home[5],home[6],home[7],home[8],home[9],home[10],home[11],home[12],home[13]],
                "원정팀":[away[0],away[1],away[2],away[3],away[4],away[5],away[6],away[7],away[8],away[9],away[10],away[11],away[12],away[13]],
                "승":[win[0],win[1],win[2],win[3],win[4],win[5],win[6],win[7],win[8],win[9],win[10],win[11],win[12],win[13]],
                "무":[draw[0],draw[1],draw[2],draw[3],draw[4],draw[5],draw[6],draw[7],draw[8],draw[9],draw[10],draw[11],draw[12],draw[13]],
                "패":[lose[0],lose[1],lose[2],lose[3],lose[4],lose[5],lose[6],lose[7],lose[8],lose[9],lose[10],lose[11],lose[12],lose[13]], 
                "결과":[result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13]]}
     
        df = pd.DataFrame(data, 

                index = ["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"],
                columns=["홈팀", "원정팀","승","무","패","결과"]) 

        st.table(df)
         
    elif gubun == 'b':
     
        st.subheader("야구 승1패")
   
        option = st.selectbox(
        "",
        (ycount),
        )

        sbox = option.replace("년 ","")
        sbox = sbox.replace("회차","")

        year = int(sbox[:4])
        count = int(sbox[4:])

        i = int(count)

        if i < 10:
            k = '0' + str(count)
        else:
            k = str(count)

        f = open('D:/datagithub/baseball/baseball_bb0_master.txt', 'r', encoding='UTF8')
       
        rdr1 = f.readlines()    

        team_read = [] 
        for line in rdr1:
            if int(line[:4]) == int(year) and int(line[5:7]) == int(k):
                l = line[11:]
                l = l.replace("\n","")
                team_read.append(l)

        f.close

        home = []
        away = []
        win = []
        draw = []
        lose = []
        result = []
        fsu = []
        famt = []
        f2su = []
        f2amt = []
        f3su = []
        f3amt = []
        f4su = []
        f4amt = []
        bal = []

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        home.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        away.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 3:
                        win.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 4:
                        draw.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 5:
                        lose.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 6:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 7:
                        fsu.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        famt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        f2su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
                        f2amt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 11:
                        f3su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 12:
                        f3amt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 13:
                        f4su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 14:
                        f4amt.append(team_read[q][s:r])
                        s = r+1
                        bal.append(team_read[q][s:])


        if famt[0] == "":
            st.markdown(str(bal[0]))
        else:
            st.markdown(str(bal[0]))
            if fsu[0] == "":
                if famt[0][:1] == "-":
                    st.markdown("1등 : 0명")
                else:
                    st.markdown(famt[0])
            else:
                st.markdown("1등 : "+fsu[0]+"명 "+ famt[0]+"원")
            if f2su[0] == "":
                st.markdown("2등 : 0명")
            else:
                st.markdown("2등 : "+f2su[0]+"명 "+ f2amt[0]+"원")
            if f3su[0] == "":
                st.markdown("3등 : 0명")
            else:
                st.markdown("3등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
            st.markdown("4등 : "+f4su[0]+"명 "+ f4amt[0]+"원")
          
        data = {"홈팀":[home[0],home[1],home[2],home[3],home[4],home[5],home[6],home[7],home[8],home[9],home[10],home[11],home[12],home[13]],
                "원정팀":[away[0],away[1],away[2],away[3],away[4],away[5],away[6],away[7],away[8],away[9],away[10],away[11],away[12],away[13]],
                "승":[win[0],win[1],win[2],win[3],win[4],win[5],win[6],win[7],win[8],win[9],win[10],win[11],win[12],win[13]],
                "①":[draw[0],draw[1],draw[2],draw[3],draw[4],draw[5],draw[6],draw[7],draw[8],draw[9],draw[10],draw[11],draw[12],draw[13]],
                "패":[lose[0],lose[1],lose[2],lose[3],lose[4],lose[5],lose[6],lose[7],lose[8],lose[9],lose[10],lose[11],lose[12],lose[13]], 
                "결과":[result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13]]}
     
        df = pd.DataFrame(data, 

                index = ["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"],
                columns=["홈팀", "원정팀","승","①","패","결과"]) 

        st.table(df)
         
    elif gubun == 'k':
     
        st.subheader("농구 승5패")
       
        option = st.selectbox(
        "",
        (ycount),
        )

        sbox = option.replace("년 ","")
        sbox = sbox.replace("회차","")

        year = int(sbox[:4])
        count = int(sbox[4:])

        i = int(count)

        if i < 10:
            k = '0' + str(count)
        else:
            k = str(count)

        f = open('D:/datagithub/basketball/basketball_bk0_master.txt', 'r', encoding='UTF8')
       
        rdr1 = f.readlines()    

        team_read = [] 
        for line in rdr1:
            if int(line[:4]) == int(year) and int(line[5:7]) == int(k):
                l = line[11:]
                l = l.replace("\n","")
                team_read.append(l)

        f.close

        home = []
        away = []
        win = []
        draw = []
        lose = []
        result = []
        fsu = []
        famt = []
        f2su = []
        f2amt = []
        f3su = []
        f3amt = []
        f4su = []
        f4amt = []
        bal = []

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        home.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        away.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 3:
                        win.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 4:
                        draw.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 5:
                        lose.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 6:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 7:
                        fsu.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        famt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        f2su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
                        f2amt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 11:
                        f3su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 12:
                        f3amt.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 13:
                        f4su.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 14:
                        f4amt.append(team_read[q][s:r])
                        s = r+1
                        bal.append(team_read[q][s:])


        if famt[0] == "":
            st.markdown(str(bal[0]))
        else:
            st.markdown(str(bal[0]))
            if fsu[0] == "":
                if famt[0][:1] == "-":
                    st.markdown("1등 : 0명")
                else:
                    st.markdown(famt[0])
            else:
                st.markdown("1등 : "+fsu[0]+"명 "+ famt[0]+"원")
            if f2su[0] == "":
                st.markdown("2등 : 0명")
            else:
                st.markdown("2등 : "+f2su[0]+"명 "+ f2amt[0]+"원")
            if f3su[0] == "":
                st.markdown("3등 : 0명")
            else:
                st.markdown("3등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
            st.markdown("4등 : "+f4su[0]+"명 "+ f4amt[0]+"원")
          
        data = {"홈팀":[home[0],home[1],home[2],home[3],home[4],home[5],home[6],home[7],home[8],home[9],home[10],home[11],home[12],home[13]],
                "원정팀":[away[0],away[1],away[2],away[3],away[4],away[5],away[6],away[7],away[8],away[9],away[10],away[11],away[12],away[13]],
                "승":[win[0],win[1],win[2],win[3],win[4],win[5],win[6],win[7],win[8],win[9],win[10],win[11],win[12],win[13]],
                "5":[draw[0],draw[1],draw[2],draw[3],draw[4],draw[5],draw[6],draw[7],draw[8],draw[9],draw[10],draw[11],draw[12],draw[13]],
                "패":[lose[0],lose[1],lose[2],lose[3],lose[4],lose[5],lose[6],lose[7],lose[8],lose[9],lose[10],lose[11],lose[12],lose[13]], 
                "결과":[result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13]]}
     
        df = pd.DataFrame(data, 

                index = ["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"],
                columns=["홈팀", "원정팀","승","5","패","결과"]) 

        st.table(df)


