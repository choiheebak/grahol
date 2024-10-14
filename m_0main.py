import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sqlite3
import pages as pg
import m_ma_1all
import m_so_1all
import m_bb_1all
import m_bk_1all
import m_dt_1all
import m_jo_1all
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
# 한글폰트
# from matplotlib import font_manager, rc
# font_path = "C:/Windows/Fonts/NanumBarunGothic.TTF"
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

# 1. as sidebar menu
with st.sidebar:
    choice = option_menu("그래홀", ["회차 조회","축구 승무패", '야구 승1패', "농구 승5패", "경기 통계", "조합기"], 
        menu_icon="cast", default_index=0,
        icons=['tablet', 'life-preserver', 'shadows','dribbble','graph-up-arrow','fan'], 
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "#A52A2A", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    }
    )    
    
if choice == "회차 조회":

    pagema = st.sidebar.radio("회차 조회", ["축구 승무패", "야구 승1패", "농구 승5패"])

    if pagema == "축구 승무패":

        con = sqlite3.connect("c:/Users/iendo/soccer.db")
        cur = con.cursor()
        cur.execute("SELECT 년도, 회차 FROM 승무패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

        year = []
        count = []
        rows = cur.fetchall()
        for row in rows:
            p1 = row[0] 
            p2 = row[1]
            year.append(p1)
            count.append(p2)

        con.close() 

        m_ma_1all.Crawler(year,count,'s') 

    elif pagema == "야구 승1패": 

        con = sqlite3.connect("c:/Users/iendo/baseball.db")
        cur = con.cursor()
        cur.execute("SELECT 년도, 회차 FROM 승1패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

        year = []
        count = []
        rows = cur.fetchall()
        for row in rows:
            p1 = row[0] 
            p2 = row[1]
            year.append(p1)
            count.append(p2)

        con.close()    
        m_ma_1all.Crawler(year,count,'b')

    elif pagema == "농구 승5패": 

        con = sqlite3.connect("c:/Users/iendo/basketball.db")
        cur = con.cursor()
        cur.execute("SELECT 년도, 회차 FROM 승5패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

        year = []
        count = []
        rows = cur.fetchall()
        for row in rows:
            p1 = row[0] 
            p2 = row[1]
            year.append(p1)
            count.append(p2)

        con.close()  

        m_ma_1all.Crawler(year,count,'k')

elif choice == "축구 승무패":

    con = sqlite3.connect("c:/Users/iendo/soccer.db")
    cur = con.cursor()
    cur.execute("SELECT 년도, 회차 FROM 승무패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

    row = cur.fetchone()
    year = row[0] 
    count = row[1]  
    # print(year, count)

    con.close() 

    pageso = st.sidebar.radio("축구 승무패", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])

    if pageso == "1경기":
        m_so_1all.Crawler(year,count,1) 
    elif pageso == "2경기":   
        m_so_1all.Crawler(year,count,2)
    elif pageso == "3경기": 
        m_so_1all.Crawler(year,count,3)
    elif pageso == "4경기": 
        m_so_1all.Crawler(year,count,4)
    elif pageso == "5경기": 
        m_so_1all.Crawler(year,count,5)
    elif pageso == "6경기": 
        m_so_1all.Crawler(year,count,6)
    elif pageso == "7경기": 
        m_so_1all.Crawler(year,count,7)
    elif pageso == "8경기": 
        m_so_1all.Crawler(year,count,8)
    elif pageso == "9경기": 
        m_so_1all.Crawler(year,count,9)
    elif pageso == "10경기": 
        m_so_1all.Crawler(year,count,10)
    elif pageso == "11경기": 
        m_so_1all.Crawler(year,count,11)
    elif pageso == "12경기": 
        m_so_1all.Crawler(year,count,12)
    elif pageso == "13경기": 
        m_so_1all.Crawler(year,count,13)
    elif pageso == "14경기": 
        m_so_1all.Crawler(year,count,14)

elif choice == "야구 승1패":

    pagebb = st.sidebar.radio("야구 승1패", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])
    
    con = sqlite3.connect("c:/Users/iendo/baseball.db")
    cur = con.cursor()
    cur.execute("SELECT 년도, 회차 FROM 승1패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

    row = cur.fetchone()
    year = row[0] 
    count = row[1]  
    # print(year, count)

    con.close()  

    if pagebb == "1경기":
        m_bb_1all.Crawler(year,count,1) 
    elif pagebb == "2경기":   
        m_bb_1all.Crawler(year,count,2)
    elif pagebb == "3경기": 
        m_bb_1all.Crawler(year,count,3)
    elif pagebb == "4경기": 
        m_bb_1all.Crawler(year,count,4)
    elif pagebb == "5경기": 
        m_bb_1all.Crawler(year,count,5)
    elif pagebb == "6경기": 
        m_bb_1all.Crawler(year,count,6)
    elif pagebb == "7경기": 
        m_bb_1all.Crawler(year,count,7)
    elif pagebb == "8경기": 
        m_bb_1all.Crawler(year,count,8)
    elif pagebb == "9경기": 
        m_bb_1all.Crawler(year,count,9)
    elif pagebb == "10경기": 
        m_bb_1all.Crawler(year,count,10)
    elif pagebb == "11경기": 
        m_bb_1all.Crawler(year,count,11)
    elif pagebb == "12경기": 
        m_bb_1all.Crawler(year,count,12)
    elif pagebb == "13경기": 
        m_bb_1all.Crawler(year,count,13)
    elif pagebb == "14경기": 
        m_bb_1all.Crawler(year,count,14)
        
elif choice == "농구 승5패":
    pagebk = st.sidebar.radio("농구 승5패", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])
    
    con = sqlite3.connect("c:/Users/iendo/basketball.db")
    cur = con.cursor()
    cur.execute("SELECT 년도, 회차 FROM 승5패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

    row = cur.fetchone()
    year = row[0] 
    count = row[1]  
    # print(year, count)

    con.close()  

    if pagebk == "1경기":
        m_bk_1all.Crawler(year,count,1) 
    elif pagebk == "2경기":   
        m_bk_1all.Crawler(year,count,2)
    elif pagebk == "3경기": 
        m_bk_1all.Crawler(year,count,3)
    elif pagebk == "4경기": 
        m_bk_1all.Crawler(year,count,4)
    elif pagebk == "5경기": 
        m_bk_1all.Crawler(year,count,5)
    elif pagebk == "6경기": 
        m_bk_1all.Crawler(year,count,6)
    elif pagebk == "7경기": 
        m_bk_1all.Crawler(year,count,7)
    elif pagebk == "8경기": 
        m_bk_1all.Crawler(year,count,8)
    elif pagebk == "9경기": 
        m_bk_1all.Crawler(year,count,9)
    elif pagebk == "10경기": 
        m_bk_1all.Crawler(year,count,10)
    elif pagebk == "11경기": 
        m_bk_1all.Crawler(year,count,11)
    elif pagebk == "12경기": 
        m_bk_1all.Crawler(year,count,12)
    elif pagebk == "13경기": 
        m_bk_1all.Crawler(year,count,13)
    elif pagebk == "14경기": 
        m_bk_1all.Crawler(year,count,14)
        
elif choice == "경기 통계":
    pagedt = st.sidebar.radio("경기통계", ["승무패 경기통계", "승무패 배당통계", "승1패 경기통계", "승1패 배당통계", 
                                         "승5패 경기통계", "승5패 배당통계"])
    
    indegree = 30
    if pagedt == "승무패 경기통계":
        m_dt_1all.Crawler("so1",indegree) 
    elif pagedt == "승무패 배당통계":   
        m_dt_1all.Crawler("so2",indegree)
    elif pagedt == "승1패 경기통계": 
        m_dt_1all.Crawler("bb1",indegree)
    elif pagedt == "승1패 배당통계": 
        m_dt_1all.Crawler("bb2",indegree)
    elif pagedt == "승5패 경기통계": 
        m_dt_1all.Crawler("bk1",indegree)
    elif pagedt == "승5패 배당통계": 
        m_dt_1all.Crawler("bk2",indegree)
        
elif choice == "조합기": 

    pagejo = st.sidebar.radio("조합기", 
                              ["축구 승무패", "야구 승1패","농구 승5패"])

    if pagejo == "축구 승무패":

        con = sqlite3.connect("c:/Users/iendo/soccer.db")
        cur = con.cursor()
        cur.execute("SELECT 년도, 회차 FROM 승무패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

        row = cur.fetchone()
        year = row[0] 
        count = row[1]  
        # print(year, count)

        con.close() 

        m_jo_1all.Crawler(year,count,'s') 

    elif pagejo == "야구 승1패": 

        con = sqlite3.connect("c:/Users/iendo/baseball.db")
        cur = con.cursor()
        cur.execute("SELECT 년도, 회차 FROM 승1패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

        row = cur.fetchone()
        year = row[0] 
        count = row[1]  
        # print(year, count)

        con.close()  

        m_jo_1all.Crawler(year,count,'b')

    elif pagejo == "농구 승5패": 

        con = sqlite3.connect("c:/Users/iendo/basketball.db")
        cur = con.cursor()
        cur.execute("SELECT 년도, 회차 FROM 승5패_일정결과 GROUP by 년도,회차 order by 년도 desc ,회차 desc ")

        row = cur.fetchone()
        year = row[0] 
        count = row[1]  
        # print(year, count)

        con.close() 

        m_jo_1all.Crawler(year,count,'k')

else:
    st.write("메뉴를 선택하세요")


