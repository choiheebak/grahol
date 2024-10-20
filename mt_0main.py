import streamlit as st
import pandas as pd
import numpy as np
import mt_ma_1all
import mt_so_1all
import mt_bb_1all
import mt_bk_1all
# import mt_so_1all
import mt_jo_1all
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar

# 1. as sidebar menu
with st.sidebar:
    choice = option_menu("그래홀", ["조합기", "축구 승무패", '야구 승1패', "농구 승5패", "경기 통계", "회차 조회"], 
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
        
        fr = open('soccer_wdl_all.txt', 'r', encoding='UTF8')

        rdr1 = fr.readlines()
        year = []
        count = []
        for line in rdr1:
            for j in range(len(line)):
                if line[j] == ";":
                    year.append(line[:j])  
                    count.append(line[j+1:])
                    break

        mt_ma_1all.Crawler(year,count,'s') 

    elif pagema == "야구 승1패": 

        fr = open('baseball_wdl_all.txt', 'r', encoding='UTF8')

        rdr1 = fr.readlines()
        year = []
        count = []
        for line in rdr1:
            for j in range(len(line)):
                if line[j] == ";":
                    year.append(line[:j])  
                    count.append(line[j+1:])
                    break

        mt_ma_1all.Crawler(year,count,'b')


    elif pagema == "농구 승5패": 

        fr = open('basketball_wdl_all.txt', 'r', encoding='UTF8')

        rdr1 = fr.readlines()
        year = []
        count = []
        for line in rdr1:
            for j in range(len(line)):
                if line[j] == ";":
                    year.append(line[:j])  
                    count.append(line[j+1:])
                    break

        mt_ma_1all.Crawler(year,count,'k')

elif choice == "축구 승무패":

    fr = open('soccer_wdl.txt', 'r', encoding='UTF8')

    rdr1 = fr.readlines()
    year = 0
    count = 0
    for line in rdr1:
        for j in range(len(line)):
            if line[j] == ";":
                year = line[:j]  
                count = line[j+1:]
                break
    # fr.close

    pageso = st.sidebar.radio("축구 승무패", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])

    if pageso == "1경기":
        mt_so_1all.Crawler(year,count,1) 
    elif pageso == "2경기":   
        mt_so_1all.Crawler(year,count,2)
    elif pageso == "3경기": 
        mt_so_1all.Crawler(year,count,3)
    elif pageso == "4경기": 
        mt_so_1all.Crawler(year,count,4)
    elif pageso == "5경기": 
        mt_so_1all.Crawler(year,count,5)
    elif pageso == "6경기": 
        mt_so_1all.Crawler(year,count,6)
    elif pageso == "7경기": 
        mt_so_1all.Crawler(year,count,7)
    elif pageso == "8경기": 
        mt_so_1all.Crawler(year,count,8)
    elif pageso == "9경기": 
        mt_so_1all.Crawler(year,count,9)
    elif pageso == "10경기": 
        mt_so_1all.Crawler(year,count,10)
    elif pageso == "11경기": 
        mt_so_1all.Crawler(year,count,11)
    elif pageso == "12경기": 
        mt_so_1all.Crawler(year,count,12)
    elif pageso == "13경기": 
        mt_so_1all.Crawler(year,count,13)
    elif pageso == "14경기": 
        mt_so_1all.Crawler(year,count,14)

elif choice == "야구 승1패":

    pagebb = st.sidebar.radio("야구 승1패", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])
    
    fr = open('baseball_wdl.txt', 'r', encoding='UTF8')

    rdr1 = fr.readlines()
    year = 0
    count = 0
    for line in rdr1:
        for j in range(len(line)):
            if line[j] == ";":
                year = line[:j]  
                count = line[j+1:]
                break
    # fr.close

    if pagebb == "1경기":
        mt_bb_1all.Crawler(year,count,1) 
    elif pagebb == "2경기":   
        mt_bb_1all.Crawler(year,count,2)
    elif pagebb == "3경기": 
        mt_bb_1all.Crawler(year,count,3)
    elif pagebb == "4경기": 
        mt_bb_1all.Crawler(year,count,4)
    elif pagebb == "5경기": 
        mt_bb_1all.Crawler(year,count,5)
    elif pagebb == "6경기": 
        mt_bb_1all.Crawler(year,count,6)
    elif pagebb == "7경기": 
        mt_bb_1all.Crawler(year,count,7)
    elif pagebb == "8경기": 
        mt_bb_1all.Crawler(year,count,8)
    elif pagebb == "9경기": 
        mt_bb_1all.Crawler(year,count,9)
    elif pagebb == "10경기": 
        mt_bb_1all.Crawler(year,count,10)
    elif pagebb == "11경기": 
        mt_bb_1all.Crawler(year,count,11)
    elif pagebb == "12경기": 
        mt_bb_1all.Crawler(year,count,12)
    elif pagebb == "13경기": 
        mt_bb_1all.Crawler(year,count,13)
    elif pagebb == "14경기": 
        mt_bb_1all.Crawler(year,count,14)
        
elif choice == "농구 승5패":
    pagebk = st.sidebar.radio("농구 승5패", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])
     
    fr = open('basketball_wdl.txt', 'r', encoding='UTF8')

    rdr1 = fr.readlines()
    year = 0
    count = 0
    for line in rdr1:
        for j in range(len(line)):
            if line[j] == ";":
                year = line[:j]  
                count = line[j+1:]
                break

    if pagebk == "1경기":
        mt_bk_1all.Crawler(year,count,1) 
    elif pagebk == "2경기":   
        mt_bk_1all.Crawler(year,count,2)
    elif pagebk == "3경기": 
        mt_bk_1all.Crawler(year,count,3)
    elif pagebk == "4경기": 
        mt_bk_1all.Crawler(year,count,4)
    elif pagebk == "5경기": 
        mt_bk_1all.Crawler(year,count,5)
    elif pagebk == "6경기": 
        mt_bk_1all.Crawler(year,count,6)
    elif pagebk == "7경기": 
        mt_bk_1all.Crawler(year,count,7)
    elif pagebk == "8경기": 
        mt_bk_1all.Crawler(year,count,8)
    elif pagebk == "9경기": 
        mt_bk_1all.Crawler(year,count,9)
    elif pagebk == "10경기": 
        mt_bk_1all.Crawler(year,count,10)
    elif pagebk == "11경기": 
        mt_bk_1all.Crawler(year,count,11)
    elif pagebk == "12경기": 
        mt_bk_1all.Crawler(year,count,12)
    elif pagebk == "13경기": 
        mt_bk_1all.Crawler(year,count,13)
    elif pagebk == "14경기": 
        mt_bk_1all.Crawler(year,count,14)
        
elif choice == "경기 통계":
    pagedt = st.sidebar.radio("경기통계", ["승무패 경기통계", "승무패 배당통계", "승1패 경기통계", "승1패 배당통계", 
                                         "승5패 경기통계", "승5패 배당통계"])
    
    indegree = 30
    if pagedt == "승무패 경기통계":
        mt_so_1all.Crawler("so1",indegree) 
    elif pagedt == "승무패 배당통계":   
        mt_so_1all.Crawler("so2",indegree)
    elif pagedt == "승1패 경기통계": 
        mt_so_1all.Crawler("bb1",indegree)
    elif pagedt == "승1패 배당통계": 
        mt_so_1all.Crawler("bb2",indegree)
    elif pagedt == "승5패 경기통계": 
        mt_so_1all.Crawler("bk1",indegree)
    elif pagedt == "승5패 배당통계": 
        mt_so_1all.Crawler("bk2",indegree)
        
elif choice == "조합기": 

    pagejo = st.sidebar.radio("조합기", 
                              ["축구 승무패", "야구 승1패","농구 승5패"])

    if pagejo == "축구 승무패":

        fr = open('soccer_wdl.txt', 'r', encoding='UTF8')

        rdr1 = fr.readlines()
        year = 0
        count = 0
        for line in rdr1:
            for j in range(len(line)):
                if line[j] == ";":
                    year = line[:j]  
                    count = line[j+1:]
                    break

        mt_jo_1all.Crawler(year,count,'s') 

    elif pagejo == "야구 승1패": 
  
        fr = open('baseball_wdl.txt', 'r', encoding='UTF8')

        rdr1 = fr.readlines()
        year = 0
        count = 0
        for line in rdr1:
            for j in range(len(line)):
                if line[j] == ";":
                    year = line[:j]  
                    count = line[j+1:]
                    break

        mt_jo_1all.Crawler(year,count,'b')

    elif pagejo == "농구 승5패": 
 
        fr = open('basketball_wdl.txt', 'r', encoding='UTF8')

        rdr1 = fr.readlines()
        year = 0
        count = 0
        for line in rdr1:
            for j in range(len(line)):
                if line[j] == ";":
                    year = line[:j]  
                    count = line[j+1:]
                    break

        mt_jo_1all.Crawler(year,count,'k')

else:
    st.write("메뉴를 선택하세요")


