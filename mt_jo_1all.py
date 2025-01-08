import streamlit as st
import pandas as pd
import numpy as np
import random
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar

def Crawler(yearc,countc,gubun):
    
    year = int(yearc)
    count = int(countc)

    def color_vowel(value):
        return f"background-color: pink;" if value in [*""] else None
        
    if gubun == 's':
      
        st.subheader("축구 승무패 "+ str(year)+"년 "+str(count)+"회차") 

        selection = ["다득표","1000원", "2000원", "3000원", "4000원", "6000원", "8000원", "9000원", "12000원", "16000원", "18000원", "24000원",  
        "27000원", "32000원", "36000원", "48000원", "54000원", "64000원", "72000원", "81000원", "96000원"]
        option = st.pills("조합 선택", selection, default="다득표")
        if option in selection:
            st.markdown(f"조합 : {option}")
        else:
            opt = "다득표"
            st.markdown(f"조합 : {opt}")
 
        if st.button("재조합"):            
            pass 

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
        fwin = []
        fdraw = []
        flose = []
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
                        fwin.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 7:
                        fdraw.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        flose.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
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
        if big2[0] == "":
            big = biga
        else:
            for b in range(len(big2)):
                big.append(bigai[b])

        johap = johap_def('s',option,biga,big)

        home = home
        away = away
        win = win
        draw = draw
        lose = lose
        fwin = fwin
        fdraw = fdraw
        flose = flose

        # index 생성
        index = [f"{i}경기" for i in range(1, 15)]

        # DataFrame 생성 (index 포함)
        df = pd.DataFrame({
            '홈팀': home,
            '원정팀': away,
            '승': win,
            '무': draw,
            '패': lose,
            '해외승': fwin,
            '해외무': fdraw,
            '해외패': flose
        }, index=index)
        
        # 스타일 적용 함수
        def highlight_cells(row):
            result = [''] * len(row)
            johap_item = johap[index.index(row.name)]
            highlight_style = 'background-color: #1565C0; color: white;'
            if '승' in johap_item:
                result[2] = highlight_style
            if '무' in johap_item:
                result[3] = highlight_style
            if '패' in johap_item:
                result[4] = highlight_style
            return result
        
        # DataFrame 표시        
        styled_df = df.style.set_properties(**{
            'text-align': 'center',
            'vertical-align': 'middle'
        }).set_table_styles([{
            'selector': 'th',
            'props': [('text-align', 'center'), ('background-color', '#E3F2FD')]
        }]).apply(highlight_cells, axis=1)

        st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

        st.text("* 발매일 이전 승무패 배당은 해외승무패 배당 기준 예측임")
        
    elif gubun == 'b':
     
        st.subheader("야구 승1패 "+ str(year)+"년 "+str(count)+"회차")
      
        selection = ["다득표","1000원", "2000원", "3000원", "4000원", "6000원", "8000원", "9000원", "12000원", "16000원", "18000원", "24000원",  
        "27000원", "32000원", "36000원", "48000원", "54000원", "64000원", "72000원", "81000원", "96000원"]
        option = st.pills("조합 선택", selection, default="다득표")
        if option in selection:
            st.markdown(f"조합 : {option}")
        else:
            opt = "다득표"
            st.markdown(f"조합 : {opt}")

        if st.button("재조합"):            
            pass 

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
        fwin = []
        fdraw = []
        flose = []
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
                        fwin.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 7:
                        fdraw.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        flose.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
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
        if big2[0] == "":
            big = biga
        else:
            for b in range(len(big2)):
                big.append(bigai[b])

        johap = johap_def('b',option,biga,big)
      
        home = home
        away = away
        win = win
        draw = draw
        lose = lose
        fwin = fwin
        flose = flose

        # index 생성
        index = [f"{i}경기" for i in range(1, 15)]

        # DataFrame 생성 (index 포함)
        df = pd.DataFrame({
            '홈팀': home,
            '원정팀': away,
            '승': win,
            '1': draw,
            '패': lose,
            '해외승': fwin,
            '해외패': flose
        }, index=index)
        
        # 스타일 적용 함수
        def highlight_cells(row):
            result = [''] * len(row)
            johap_item = johap[index.index(row.name)]
            highlight_style = 'background-color: #1565C0; color: white;'
            if '승' in johap_item:
                result[2] = highlight_style
            if '1' in johap_item:
                result[3] = highlight_style
            if '패' in johap_item:
                result[4] = highlight_style
            return result
        
        # DataFrame 표시       
        styled_df = df.style.set_properties(**{
            'text-align': 'center',
            'vertical-align': 'middle'
        }).set_table_styles([{
            'selector': 'th',
            'props': [('text-align', 'center'), ('background-color', '#E3F2FD')]
        }]).apply(highlight_cells, axis=1)

        st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

    elif gubun == 'k':
     
        st.subheader("농구 승5패 "+ str(year)+"년 "+str(count)+"회차")
    
        selection = ["다득표","1000원", "2000원", "3000원", "4000원", "6000원", "8000원", "9000원", "12000원", "16000원", "18000원", "24000원",  
        "27000원", "32000원", "36000원", "48000원", "54000원", "64000원", "72000원", "81000원", "96000원"]
        option = st.pills("조합 선택", selection, default="다득표")
        if option in selection:
            st.markdown(f"조합 : {option}")
        else:
            opt = "다득표"
            st.markdown(f"조합 : {opt}")
 
        if st.button("재조합"):            
            pass 
        
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
        fwin = []
        fdraw = []
        flose = []
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
                        fwin.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 7:
                        fdraw.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        flose.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
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
        if big2[0] == "":
            big = biga
        else:
            for b in range(len(big2)):
                big.append(bigai[b])

        johap = johap_def('k',option,biga,big)

        home = home
        away = away
        win = win
        draw = draw
        lose = lose
        fwin = fwin
        flose = flose

        # index 생성
        index = [f"{i}경기" for i in range(1, 15)]

        # DataFrame 생성 (index 포함)
        df = pd.DataFrame({
            '홈팀': home,
            '원정팀': away,
            '승': win,
            '5': draw,
            '패': lose,
            '해외승': fwin,
            '해외패': flose
        }, index=index)
        
        # 스타일 적용 함수
        def highlight_cells(row):
            result = [''] * len(row)
            johap_item = johap[index.index(row.name)]
            highlight_style = 'background-color: #1565C0; color: white;'
            if '승' in johap_item:
                result[2] = highlight_style
            if '5' in johap_item:
                result[3] = highlight_style
            if '패' in johap_item:
                result[4] = highlight_style
            return result
        
        # DataFrame 표시       
        styled_df = df.style.set_properties(**{
            'text-align': 'center',
            'vertical-align': 'middle'
        }).set_table_styles([{
            'selector': 'th',
            'props': [('text-align', 'center'), ('background-color', '#E3F2FD')]
        }]).apply(highlight_cells, axis=1)

        st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

        st.text("* 발매일 이전 승5패 배당은 데이터 기준 예측임")
        
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
   
    if option == "다득표": 
        for i in range(14):
            a = biga[i][:1]   
                
            list_johap.append(a)

    elif option == "1000원": 
        for i in range(14):
            a = random.sample(big[i],1)
                
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
                   
    else: 
        for i in range(14):
            a = biga[i][:1]   
                
            list_johap.append(a)

    list_j = [''.join(item) for item in list_johap]

    return list_j

