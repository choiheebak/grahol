import streamlit as st
import pandas as pd
import random
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar

def Crawler(yearc,countc,gubun):
    
    year = int(yearc)
    count = int(countc)

    if gubun == 's':
      
        st.subheader("축구 승무패") 
        st.markdown(str(year)+"년 "+str(count)+"회차")
  
        option = st.radio(
        "조합 선택하세요",
        ["다득표","1000원", "2000원", "3000원", "4000원", "6000원", "8000원", "9000원", "12000원", "16000원", "18000원", "24000원", 
        "27000원", "32000원", "36000원", "48000원", "54000원", "64000원", "72000원", "81000원", "96000원"],horizontal=True,
        )
 
        # option = st.selectbox(
        # "선택하세요", 
        # ("다득표","1000원", "2000원", "3000원", "4000원", "6000원", "8000원", "9000원", "12000원", "16000원", "18000원", "24000원", 
        # "27000원", "32000원", "36000원", "48000원", "54000원", "64000원", "72000원", "81000원", "96000원"), 
        # )

        # st.write(option) 
    
        # f = open('D:/datagithub/soccer/soccer_so5_johap.txt', 'r', encoding='UTF8')
        f = open('soccer_so5_johap.txt', 'r', encoding='UTF8')
      
        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            l = line
            l = l.replace("\n","")
            team_read.append(l)

        f.close

        home = []
        away = []
        win = []
        draw = []
        lose = []
        result = []
        big2 = []
        ai2 = []

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
                        big2.append(team_read[q][s:r])
                        s = r+1
                        ai2.append(team_read[q][s:])

        biga = []  
        for b in range(14):
            w = win[b].replace("%","")
            w = w.replace(" ","")
            d = draw[b].replace("%","")
            d = d.replace(" ","")
            l = lose[b].replace("%","")
            l = l.replace(" ","")
            wf = float(w)
            df = float(d)
            lf = float(l)

            h = [wf,df,lf]
            high = h.index(max(h))
            low = h.index(min(h))

            if high == 0 and low == 1:
                biga.append('승무')
            elif high == 0 and low == 2:
                biga.append('승패')
            elif high == 1 and low == 0:
                biga.append('무승')
            elif high == 1 and low == 2:
                biga.append('무패')
            elif high == 2 and low == 0:
                biga.append('패승')
            elif high == 2 and low == 1:
                biga.append('패무')
 
        bigai2 = [''] * len(big2)
        for i in range(len(big2)):
            bigai2[i] = big2[i] + ai2[i]

        bigai = [''] * len(big2)
        for i in range(len(big2)):
            if "승" in bigai2[i]:
                w = "승"
            else:
                w = ""
            if "무" in bigai2[i]:
                d = "무"
            else:
                d = ""
            if "패" in bigai2[i]:
                l = "패"
            else:
                l = ""
            bigai[i] = w+d+l

        big = []  
        if len(big2) == 0:
            big = biga
        else:
            for b in range(len(big2)):
                big.append(bigai[b])

        # print(biga)
        # print(big)
        
        johap = johap_def('s',option,biga,big)

        data = {"홈팀":[home[0],home[1],home[2],home[3],home[4],home[5],home[6],home[7],home[8],home[9],home[10],home[11],home[12],home[13]],
                "원정팀":[away[0],away[1],away[2],away[3],away[4],away[5],away[6],away[7],away[8],away[9],away[10],away[11],away[12],away[13]],
                "승":[win[0],win[1],win[2],win[3],win[4],win[5],win[6],win[7],win[8],win[9],win[10],win[11],win[12],win[13]],
                "무":[draw[0],draw[1],draw[2],draw[3],draw[4],draw[5],draw[6],draw[7],draw[8],draw[9],draw[10],draw[11],draw[12],draw[13]],
                "패":[lose[0],lose[1],lose[2],lose[3],lose[4],lose[5],lose[6],lose[7],lose[8],lose[9],lose[10],lose[11],lose[12],lose[13]],  
                # "결과":[result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13]],
                "조합":[johap[0],johap[1],johap[2],johap[3],johap[4],johap[5],johap[6],johap[7],johap[8],johap[9],johap[10],johap[11],johap[12],johap[13]]}
     
        df = pd.DataFrame(data, 

                index = ["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"],
                columns=["홈팀", "원정팀","승","무","패","조합"]) 

        st.table(df)
   
    elif gubun == 'b':
     
        st.subheader("야구 승1패")
        st.markdown(str(year)+"년 "+str(count)+"회차")
   
        option = st.radio(
        "조합 선택하세요",
        ["다득표","1000원", "2000원", "3000원", "4000원", "6000원", "8000원", "9000원", "12000원", "16000원", "18000원", "24000원", 
        "27000원", "32000원", "36000원", "48000원", "54000원", "64000원", "72000원", "81000원", "96000원"],horizontal=True,
        )
 
        # f = open('D:/datagithub/baseball/baseball_bb5_johap.txt', 'r', encoding='UTF8')
        f = open('baseball_bb5_johap.txt', 'r', encoding='UTF8')
      
        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            team_read.append(line)

        f.close

        home = []
        away = []
        win = []
        draw = []
        lose = []
        result = []
        big2 = []
        ai2 = []

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
                        big2.append(team_read[q][s:r])
                        s = r+1
                        ai2.append(team_read[q][s:])

        biga = []  
        for b in range(14):
            w = win[b].replace("%","")
            w = w.replace(" ","")
            d = draw[b].replace("%","")
            d = d.replace(" ","")
            l = lose[b].replace("%","")
            l = l.replace(" ","")
            wf = float(w)
            df = float(d)
            lf = float(l)

            h = [wf,df,lf]
            high = h.index(max(h))
            low = h.index(min(h))

            if high == 0 and low == 1:
                biga.append('승1')
            elif high == 0 and low == 2:
                biga.append('승패')
            elif high == 1 and low == 0:
                biga.append('1승')
            elif high == 1 and low == 2:
                biga.append('1패')
            elif high == 2 and low == 0:
                biga.append('패승')
            elif high == 2 and low == 1:
                biga.append('패1')
 
        bigai2 = [''] * len(big2)
        for i in range(len(big2)):
            bigai2[i] = big2[i] + ai2[i]

        bigai = [''] * len(big2)
        for i in range(len(big2)):
            if "승" in bigai2[i]:
                w = "승"
            else:
                w = ""
            if "1" in bigai2[i]:
                d = "1"
            else:
                d = ""
            if "패" in bigai2[i]:
                l = "패"
            else:
                l = ""
            bigai[i] = w+d+l

        big = []  
        if len(big2) == 0:
            big = biga
        else:
            for b in range(len(big2)):
                big.append(bigai[b])

        # print(biga)
        # print(big)

        johap = johap_def('b',option,biga,big)

        # print(johap)
      
        data = {"홈팀":[home[0],home[1],home[2],home[3],home[4],home[5],home[6],home[7],home[8],home[9],home[10],home[11],home[12],home[13]],
                "원정팀":[away[0],away[1],away[2],away[3],away[4],away[5],away[6],away[7],away[8],away[9],away[10],away[11],away[12],away[13]],
                "승":[win[0],win[1],win[2],win[3],win[4],win[5],win[6],win[7],win[8],win[9],win[10],win[11],win[12],win[13]],
                "①":[draw[0],draw[1],draw[2],draw[3],draw[4],draw[5],draw[6],draw[7],draw[8],draw[9],draw[10],draw[11],draw[12],draw[13]],
                "패":[lose[0],lose[1],lose[2],lose[3],lose[4],lose[5],lose[6],lose[7],lose[8],lose[9],lose[10],lose[11],lose[12],lose[13]],  
                # "결과":[result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13]],
                "조합":[johap[0],johap[1],johap[2],johap[3],johap[4],johap[5],johap[6],johap[7],johap[8],johap[9],johap[10],johap[11],johap[12],johap[13]]}
     
        df = pd.DataFrame(data, 

                index = ["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"],
                columns=["홈팀", "원정팀","승","①","패","조합"]) 

        st.table(df)
  
    elif gubun == 'k':
     
        st.subheader("농구 승5패")
        st.markdown(str(year)+"년 "+str(count)+"회차")
    
        option = st.radio(
        "조합 선택하세요",
        ["다득표","1000원", "2000원", "3000원", "4000원", "6000원", "8000원", "9000원", "12000원", "16000원", "18000원", "24000원", 
        "27000원", "32000원", "36000원", "48000원", "54000원", "64000원", "72000원", "81000원", "96000원"],horizontal=True,
        )
 
        # f = open('D:/datagithub/basketball/basketball_bk5_johap.txt', 'r', encoding='UTF8')
        f = open('basketball_bk5_johap.txt', 'r', encoding='UTF8')
      
        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            team_read.append(line)

        f.close

        home = []
        away = []
        win = []
        draw = []
        lose = []
        result = []
        big2 = []
        ai2 = []

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
                        big2.append(team_read[q][s:r])
                        s = r+1
                        ai2.append(team_read[q][s:])

        biga = []  
        for b in range(14):
            w = win[b].replace("%","")
            w = w.replace(" ","")
            d = draw[b].replace("%","")
            d = d.replace(" ","")
            l = lose[b].replace("%","")
            l = l.replace(" ","")
            wf = float(w)
            df = float(d)
            lf = float(l)

            h = [wf,df,lf]
            high = h.index(max(h))
            low = h.index(min(h))

            if high == 0 and low == 1:
                biga.append('승5')
            elif high == 0 and low == 2:
                biga.append('승패')
            elif high == 1 and low == 0:
                biga.append('5승')
            elif high == 1 and low == 2:
                biga.append('5패')
            elif high == 2 and low == 0:
                biga.append('패승')
            elif high == 2 and low == 1:
                biga.append('패5')
 
        bigai2 = [''] * len(big2)
        for i in range(len(big2)):
            bigai2[i] = big2[i] + ai2[i]

        bigai = [''] * len(big2)
        for i in range(len(big2)):
            if "승" in bigai2[i]:
                w = "승"
            else:
                w = ""
            if "5" in bigai2[i]:
                d = "5"
            else:
                d = ""
            if "패" in bigai2[i]:
                l = "패"
            else:
                l = ""
            bigai[i] = w+d+l

        big = []  
        if len(big2) == 0:
            big = biga
        else:
            for b in range(len(big2)):
                big.append(bigai[b])

        # print(biga)
        # print(big)

        johap = johap_def('k',option,biga,big)

        # print(johap)
 
        data = {"홈팀":[home[0],home[1],home[2],home[3],home[4],home[5],home[6],home[7],home[8],home[9],home[10],home[11],home[12],home[13]],
                "원정팀":[away[0],away[1],away[2],away[3],away[4],away[5],away[6],away[7],away[8],away[9],away[10],away[11],away[12],away[13]],
                "승":[win[0],win[1],win[2],win[3],win[4],win[5],win[6],win[7],win[8],win[9],win[10],win[11],win[12],win[13]],
                "5":[draw[0],draw[1],draw[2],draw[3],draw[4],draw[5],draw[6],draw[7],draw[8],draw[9],draw[10],draw[11],draw[12],draw[13]],
                "패":[lose[0],lose[1],lose[2],lose[3],lose[4],lose[5],lose[6],lose[7],lose[8],lose[9],lose[10],lose[11],lose[12],lose[13]],  
                # "결과":[result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13]],
                "조합":[johap[0],johap[1],johap[2],johap[3],johap[4],johap[5],johap[6],johap[7],johap[8],johap[9],johap[10],johap[11],johap[12],johap[13]]}
     
        df = pd.DataFrame(data, 

                index = ["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"],
                columns=["홈팀", "원정팀","승","5","패","조합"]) 

        st.table(df)
             
def johap_def(gubun, option, biga, big):
   
    list_johap = []

    if gubun == 's':
        k = ["승","무","패"]
    elif gubun == 'b':
        k = ["승","1","패"]
    elif gubun == 'k':
        k = ["승","5","패"]

    t = random.sample((0,1,2,3,4,5,6,7,8,9,10,11,12,13),6)
    # print(t)
     
    t1 = t[0]
    t2 = t[1]
    t3 = t[2]
    t4 = t[3]
    t5 = t[4]
    t6 = t[5]
   
    # print(t1, t2, t3, t4, t5, t6)

    if option == "다득표": 
        for i in range(14):
            a = biga[i][:1]   
                
            list_johap.append(a)

    elif option == "1000원": 
        for i in range(14):
            a = random.sample(big[i],1)
            # a = random.choice(big[i])
                
            list_johap.append(a)

    elif option == "2000원":  
        for i in range(14):
            if i == t1: 
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
              
            list_johap.append(a)

    elif option == "3000원": 
        for i in range(14):
            if i == t1: 
                a = k
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "4000원":
        for i in range(14):
            if i == t1: 
                a = random.sample(big[i],2)
            elif i == t2: 
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "6000원": 
        for i in range(14):
            if i == t1:  
                a = k
            elif i == t2:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "8000원":
        for i in range(14):
            if i == t1 or i == t2 or i == t3: 
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)
 
    elif option == "9000원": 
        for i in range(14):
            if i == t1 or i == t2: 
                a = k
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "12000원": 
        for i in range(14):
            if i == t1:  
                a = k
            elif i == t2 or i == t3:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "16000원":
        for i in range(14):
            if i == t1 or i == t2 or i == t3 or i == t4: 
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a) 

    elif option == "18000원": 
        for i in range(14):
            if i == t1 or i == t2:  
                a = k
            elif i == t3:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "24000원": 
        for i in range(14):
            if i == t1:  
                a = k
            elif i == t2 or i == t3 or i == t4:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "27000원": 
        for i in range(14):
            if i == t1 or i == t2 or i == t3:  
                a = k
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "32000원":
        for i in range(14):
            if i == t1 or i == t2 or i == t3 or i == t4 or i == t5: 
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a) 

    elif option == "36000원": 
        for i in range(14):
            if i == t1 or i == t2:  
                a = k
            elif i == t3 or i == t4:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "48000원": 
        for i in range(14):
            if i == t1:  
                a = k
            elif i == t2 or i == t3 or i == t4 or i == t5:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "54000원": 
        for i in range(14):
            if i == t1 or i == t2 or i == t3:  
                a = k
            elif i == t4:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "64000원":
        for i in range(14):
            if i == t1 or i == t2 or i == t3 or i == t4 or i == t5 or i == t6: 
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a) 

    elif option == "72000원": 
        for i in range(14):
            if i == t1 or i == t2:  
                a = k
            elif i == t3 or i == t4 or i == t5:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "81000원": 
        for i in range(14):
            if i == t1 or i == t2 or i == t3 or i == t4:  
                a = k
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    elif option == "96000원": 
        for i in range(14):
            if i == t1:  
                a = k
            elif i == t2 or i == t3 or i == t4 or i == t5 or i == t6:  
                a = random.sample(big[i],2)
            else:
                a = random.sample(big[i],1)
                
            list_johap.append(a)

    return list_johap

