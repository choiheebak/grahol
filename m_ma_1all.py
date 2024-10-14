import streamlit as st
import pandas as pd
import sqlite3
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
# 한글폰트
# from matplotlib import font_manager, rc
# font_path = "C:/Windows/Fonts/NanumBarunGothic.TTF"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

def Crawler(yearc,countc,gubun):
    
    # # print(yearc, len(yearc))
    # # print(countc, len(countc))

    ycount = []
    for i in range(len(yearc)):
        ycount.append(str(yearc[i])+"년 "+str(countc[i])+"회차")

    # # print(ycount, len(ycount))
    if gubun == 's':
      
        st.subheader("축구 승무패")

        option = st.selectbox(
        "",
        (ycount 
        )
        )

        sbox = option.replace("년 ","")
        sbox = sbox.replace("회차","")
        # # print("sbox", sbox)

        year = int(sbox[:4])
        count = int(sbox[4:])

        # print(year,count)

        con = sqlite3.connect("c:/Users/iendo/soccer.db")
        cur = con.cursor()
        sql = "select * from 승무패_일정결과 where 년도 = ? and 회차 = ?" 
        # sql = "select 홈팀, 원정팀, 승, 무, 패, 결과, 해외승, 해외무, 해외패 from 승무패_일정결과 where 년도 = ? and 회차 = ?" 
        data = (year, count)
        cur.execute(sql,data)

        home = []
        away = []
        win = []
        draw = []
        lose = []
        result = []
        fsu = []
        famt = []
        fwin = []
        fdraw = []
        flose = []
        f2su = []
        f2amt = []
        f3su = []
        f3amt = []
        f4su = []
        f4amt = []
        bal = []

        rows = cur.fetchall()
        for row in rows:
            p1 = row[14] 
            p2 = row[15]
            p3 = row[16]
            p4 = row[17]
            p5 = row[18]
            p6 = row[19]
            p7 = row[6]
            p8 = row[7]
            p9 = row[8]
            p10 = row[9]
            p11 = row[10]
            p12 = row[11]
            p13 = row[12]
            p14 = row[13]
            p15 = row[4]

            home.append(p1)
            away.append(p2)
            win.append(p3)
            draw.append(p4)
            lose.append(p5)
            result.append(p6)
            fsu.append(p7)
            famt.append(p8)
            f2su.append(p9)
            f2amt.append(p10)
            f3su.append(p11)
            f3amt.append(p12)
            f4su.append(p13)
            f4amt.append(p14)
            bal.append(p15)
            
        con.close() 
       
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
          
          
        # st.markdown(str(bal[0]))       
        # if famt[0] == "":
        #     pass
        # else:
        #     first = ''
        #     second = ''
        #     third = ''
        #     four = ''
        #     if fsu[0] == "":
        #         first = famt[0]
        #     else:
        #         first = fsu[0]+"명 "+ famt[0]+"원"
        #     second = f2su[0]+"명 "+ f2amt[0]+"원"
        #     third = f3su[0]+"명 "+ f3amt[0]+"원"
        #     four = f4su[0]+"명 "+ f4amt[0]+"원"
        
        #     data = {"1등":[first],
        #             "2등":[second],
        #             "3등":[third],
        #             "4등":[four]}
        
        #     df = pd.DataFrame(data, 

        #             index = ["적중"],
        #             columns=["1등", "2등","3등","4등"]) 
            
        #     st.table(df)
         
        # if famt[0] == "":
        #     st.markdown(str(bal[0]))
        #     # st.markdown(str(year)+"년 "+ str(count)+"회차"+" ("+str(bal[0])+")")
        # else:
        #     if famt[0][:1] == "-":
        #         if f2amt[0][:1] == "-":
        #             if f3amt[0][:1] == "-":
        #                 st.markdown(str(bal[0])+" - 4등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
        #                 # st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 4등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
        #             else:
        #                 st.markdown(str(bal[0])+" - 3등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
        #                 # st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 3등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
        #         else:
        #             st.markdown(str(bal[0])+" - 2등 : "+f2su[0]+"명 "+ f2amt[0]+"원")
        #             # st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 2등 : "+f2su[0]+"명 "+ f2amt[0]+"원")
        #     elif famt[0][:1] == "이":
        #         st.markdown(str(year)+"년 "+ str(count)+"회차 "+famt[0])
        #     else:
        #         st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 1등 : "+fsu[0]+"명 "+ famt[0]+"원")

        data = {"홈팀":[home[0],home[1],home[2],home[3],home[4],home[5],home[6],home[7],home[8],home[9],home[10],home[11],home[12],home[13]],
                "원정팀":[away[0],away[1],away[2],away[3],away[4],away[5],away[6],away[7],away[8],away[9],away[10],away[11],away[12],away[13]],
                "승":[win[0],win[1],win[2],win[3],win[4],win[5],win[6],win[7],win[8],win[9],win[10],win[11],win[12],win[13]],
                "무":[draw[0],draw[1],draw[2],draw[3],draw[4],draw[5],draw[6],draw[7],draw[8],draw[9],draw[10],draw[11],draw[12],draw[13]],
                "패":[lose[0],lose[1],lose[2],lose[3],lose[4],lose[5],lose[6],lose[7],lose[8],lose[9],lose[10],lose[11],lose[12],lose[13]], 
                "결과":[result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13]]}
     
        #         "해외승":[fwin[0],fwin[1],fwin[2],fwin[3],fwin[4],fwin[5],fwin[6],fwin[7],fwin[8],fwin[9],fwin[10],fwin[11],fwin[12],fwin[13]],
        #         "해외무":[fdraw[0],fdraw[1],fdraw[2],fdraw[3],fdraw[4],fdraw[5],fdraw[6],fdraw[7],fdraw[8],fdraw[9],fdraw[10],fdraw[11],fdraw[12],fdraw[13]],
        #         "해외패":[flose[0],flose[1],flose[2],flose[3],flose[4],flose[5],flose[6],flose[7],flose[8],flose[9],flose[10],flose[11],flose[12],flose[13]]}
        df = pd.DataFrame(data, 

                index = ["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"],
                columns=["홈팀", "원정팀","승","무","패","결과"]) 
                # columns=["홈팀", "원정팀","승","무","패","해외승","해외무","해외패"]) 

        st.table(df)
         
    elif gubun == 'b':
     
        st.subheader("야구 승1패")
   
        option = st.selectbox(
        "",
        (ycount),
        )
        # (ycount[0], ycount[1], ycount[2], ycount[3],ycount[4], ycount[5],ycount[6], ycount[7],ycount[8], ycount[9],
        #  ycount[10], ycount[11], ycount[12], ycount[13],ycount[14], ycount[15],ycount[16], ycount[17],ycount[18], ycount[19],
        #  ycount[20], ycount[21], ycount[22], ycount[23],ycount[24], ycount[25],ycount[26], ycount[27],ycount[28], ycount[29],
        #  ycount[30], ycount[31], ycount[32], ycount[33],ycount[34], ycount[35],ycount[36], ycount[37],ycount[38], ycount[39],
        #  ycount[40], ycount[41], ycount[42], ycount[43],ycount[44], ycount[45],ycount[46], ycount[47],ycount[48], ycount[49]),

        # )

        sbox = option.replace("년 ","")
        sbox = sbox.replace("회차","")

        year = int(sbox[:4])
        count = int(sbox[4:])

        # print(year,count)

        con = sqlite3.connect("c:/Users/iendo/baseball.db")
        cur = con.cursor()
        sql = "select * from 승1패_일정결과 where 년도 = ? and 회차 = ?" 
        data = (year, count)
        cur.execute(sql,data)

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

        rows = cur.fetchall()
        for row in rows:
            p1 = row[14] 
            p2 = row[15]
            p3 = row[16]
            p4 = row[17]
            p5 = row[18]
            p6 = row[19]
            p7 = row[6]
            p8 = row[7]
            p9 = row[8]
            p10 = row[9]
            p11 = row[10]
            p12 = row[11]
            p13 = row[12]
            p14 = row[13]
            p15 = row[4]

            home.append(p1)
            away.append(p2)
            win.append(p3)
            draw.append(p4)
            lose.append(p5)
            result.append(p6)
            fsu.append(p7)
            famt.append(p8)
            f2su.append(p9)
            f2amt.append(p10)
            f3su.append(p11)
            f3amt.append(p12)
            f4su.append(p13)
            f4amt.append(p14)
            bal.append(p15)
            
        con.close() 
        
        # if famt[0] == "":
        #     st.markdown(str(year)+"년 "+ str(count)+"회차")
        # else:
        #     if famt[0][:1] == "-":
        #         if f2amt[0][:1] == "-":
        #             if f3amt[0][:1] == "-":
        #                 st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 4등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
        #             else:
        #                 st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 3등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
        #         else:
        #             st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 2등 : "+f2su[0]+"명 "+ f2amt[0]+"원")
        #     elif famt[0][:1] == "이":
        #         st.markdown(str(year)+"년 "+ str(count)+"회차 "+famt[0])
        #     else:
        #         st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 1등 : "+fsu[0]+"명 "+ famt[0]+"원")

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

        # print(year,count)

        con = sqlite3.connect("c:/Users/iendo/basketball.db")
        cur = con.cursor()
        sql = "select * from 승5패_일정결과 where 년도 = ? and 회차 = ?" 
        data = (year, count)
        cur.execute(sql,data)

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

        rows = cur.fetchall()
        for row in rows:
            p1 = row[14] 
            p2 = row[15]
            p3 = row[16]
            p4 = row[17]
            p5 = row[18]
            p6 = row[19]
            p7 = row[6]
            p8 = row[7]
            p9 = row[8]
            p10 = row[9]
            p11 = row[10]
            p12 = row[11]
            p13 = row[12]
            p14 = row[13]
            p15 = row[4]

            home.append(p1)
            away.append(p2)
            win.append(p3)
            draw.append(p4)
            lose.append(p5)
            result.append(p6)
            fsu.append(p7)
            famt.append(p8)
            f2su.append(p9)
            f2amt.append(p10)
            f3su.append(p11)
            f3amt.append(p12)
            f4su.append(p13)
            f4amt.append(p14)
            bal.append(p15)
            
        con.close() 
    
        # if famt[0] == "":
        #     st.markdown(str(year)+"년 "+ str(count)+"회차")
        # else:
        #     if famt[0][:1] == "-":
        #         if f2amt[0][:1] == "-":
        #             if f3amt[0][:1] == "-":
        #                 st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 4등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
        #             else:
        #                 st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 3등 : "+f3su[0]+"명 "+ f3amt[0]+"원")
        #         else:
        #             st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 2등 : "+f2su[0]+"명 "+ f2amt[0]+"원")
        #     elif famt[0][:1] == "이":
        #         st.markdown(str(year)+"년 "+ str(count)+"회차 "+famt[0])
        #     else:
        #         st.markdown(str(year)+"년 "+ str(count)+"회차 "+" - 1등 : "+fsu[0]+"명 "+ famt[0]+"원")

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


