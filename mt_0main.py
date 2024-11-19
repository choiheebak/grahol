import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import mt_ma_1all
import mt_so_1all
import mt_bb_1all
import mt_bk_1all
import mt_dt_1all
import mt_jo_1all
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar

now = datetime.now()
dt_now = now.strftime("%Y-%m-%d %H:%M:%S")

# 1. as sidebar menu
with st.sidebar:
    choice = option_menu("그래홀", ["축구 승무패", '야구 승1패', "농구 승5패", "조합기", "회차 조회", "경기 통계"], 
        menu_icon="cast", default_index=0,
        icons=['life-preserver', 'shadows','dribbble','fan','tablet','graph-up-arrow'], 
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
        
        # print("# hoicha inq-soccer wdl",dt_now)
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

        # print("# hoicha inq-baseball wdl",dt_now)
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

        # print("# hoicha inq-basketball wdl",dt_now)
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

    # print("# soccer wdl-",year,count,dt_now)

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

    # print("# baseball wdl-",year,count,dt_now)

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

    # print("# basketball wdl-",year,count,dt_now)

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
    
    if pagedt == "승무패 경기통계":
        # print("# tongye - soccer wdl",dt_now)
        mt_dt_1all.Crawler("so1") 
    elif pagedt == "승무패 배당통계": 
        # print("# tongye - soccer hml",dt_now)
        mt_dt_1all.Crawler("so2")
    elif pagedt == "승1패 경기통계": 
        # print("# tongye - baseball wdl",dt_now)
        mt_dt_1all.Crawler("bb1")
    elif pagedt == "승1패 배당통계": 
        # print("# tongye - baseball hml",dt_now)
        mt_dt_1all.Crawler("bb2")
    elif pagedt == "승5패 경기통계": 
        # print("# tongye - basketball wdl",dt_now)
        mt_dt_1all.Crawler("bk1")
    elif pagedt == "승5패 배당통계": 
        # print("# tongye - basketball hml",dt_now)
        mt_dt_1all.Crawler("bk2")
        
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

        # print("# johap - soccer wdl",dt_now)

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

        # print("# johap - baseball wdl",dt_now)

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

        # print("# johap - basketball wdl",dt_now)

        mt_jo_1all.Crawler(year,count,'k')

# elif choice == "게시판": 
#      # 게시글 데이터를 저장할 DataFrame 생성
#     if 'posts' not in st.session_state:
#         st.session_state.posts = pd.DataFrame(columns=['Title', 'Content'])

#     # 제목
#     st.title('게시판')

#     # 새 게시글 작성
#     st.subheader('새 게시글 작성')
#     st.markdown(":red[**- 게시판은 익명 미보관용으로, 시스템 상황에 따라 수시로 삭제될 수 있습니다. 비방이나 욕설은 삼가해 주세요.**]")
#     title = st.text_input('제목')
#     content = st.text_area('내용')
#     if st.button('게시'):
#         new_post = pd.DataFrame({'Title': [title], 'Content': [content]})
#         st.session_state.posts = pd.concat([st.session_state.posts, new_post], ignore_index=True)
#         st.success('게시글이 작성되었습니다.')

#     # 게시글 목록 표시
#     st.subheader('게시글 목록')
#     st.table(st.session_state.posts)

#     # 게시글 상세 보기
#     try:
#         post_index = st.number_input('상세히 볼 게시글 번호를 입력하세요', min_value=0, max_value=len(st.session_state.posts)-1, step=1)
#         if st.button('게시글 보기'):
#             if not st.session_state.posts.empty and post_index < len(st.session_state.posts):
#                 st.subheader(st.session_state.posts.iloc[post_index]['Title'])
#                 st.write(st.session_state.posts.iloc[post_index]['Content'])
#             else:
#                 st.error('유효하지 않은 게시글 번호입니다.')  
#     except:
#         pass
    
else:
    st.write("메뉴를 선택하세요")


