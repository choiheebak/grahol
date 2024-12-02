import streamlit as st
from streamlit_option_menu import option_menu
import mt_pr_1all
import mt_ma_1all
import mt_so_1all
import mt_so_2all
import mt_bb_1all
import mt_bb_2all
import mt_bk_1all
import mt_bk_2all
import mt_dt_1all
import mt_jo_1all
from datetime import datetime

now = datetime.now()
dt_now = now.strftime("%Y-%m-%d %H:%M:%S")

# 세션 상태 초기화
if 'submenu_indices' not in st.session_state:
    st.session_state.submenu_indices = {"축구 승무패": 0, "야구 승1패": 0, "농구 승5패": 0}
if 'selected_sport' not in st.session_state:
    st.session_state.selected_sport = "축구 승무패"

def on_sport_change(key):
    st.session_state.selected_sport = st.session_state.sport_select

def on_submenu_change(key):
    st.session_state.submenu_indices[st.session_state.selected_sport] = submenu_options[st.session_state.selected_sport].index(st.session_state.submenu_select)

# 페이지 설정
# st.set_page_config(page_title="그래홀", page_icon="🏠", layout="wide")

# 사이드바
with st.sidebar:
    st.title("🏠 그래홀")
    
    selected_sport = option_menu("스포츠", ["축구 승무패", "야구 승1패", "농구 승5패"],
                                 icons=['life-preserver', 'shadows', 'dribbble'],
                                 menu_icon="list", 
                                 default_index=["축구 승무패", "야구 승1패", "농구 승5패"].index(st.session_state.selected_sport),
                                 key="sport_select",
                                 on_change=on_sport_change,
                                 styles={
                                     "container": {"padding": "0!important", "background-color": "#fafafa"},
                                     "icon": {"color": "#A52A2A", "font-size": "25px"},
                                     "nav-link": {"font-size": "16px", "font-weight": "bold", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
                                     "nav-link-selected": {"background-color": "#08c7b4", "font-weight": "bold"},
                                 })

    submenu_options = {
        "축구 승무패": ["경기별 분석", "순위추이 분석", "조합기", "예측", "경기 통계", "회차 조회"],
        "야구 승1패": ["경기별 분석", "순위추이 분석", "조합기", "예측", "조합기", "경기 통계", "회차 조회"],
        "농구 승5패": ["경기별 분석", "순위추이 분석", "조합기", "예측", "조합기", "경기 통계", "회차 조회"]
    }
    
    icons = ['zoom-in', 'tropical-storm', 'fan', 'yelp', 'graph-up-arrow', 'tablet']
    
    current_submenu_index = st.session_state.submenu_indices[st.session_state.selected_sport]
    if current_submenu_index >= len(submenu_options[st.session_state.selected_sport]):
        current_submenu_index = len(submenu_options[st.session_state.selected_sport]) - 1
    
    submenu = option_menu(None, submenu_options[st.session_state.selected_sport],
                          icons=icons[:len(submenu_options[st.session_state.selected_sport])],
                          menu_icon="list", 
                          default_index=current_submenu_index,
                          key="submenu_select",
                          on_change=on_submenu_change,
                          styles={
                              "container": {"padding": "0!important", "background-color": "#fafafa"},
                              "icon": {"color": "#4E342E", "font-size": "20px"}, 
                              "nav-link": {"font-size": "14px", "font-weight": "bold", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                              "nav-link-selected": {"background-color": "#08c7b4", "font-weight": "bold"},
                          })
       
def soccer_predict():

    fr = open('soccer_wdl_all.txt', 'r', encoding='UTF8')

    rdr1 = fr.readlines()
    year = []
    count = []
    for line in rdr1:
        for j in range(len(line)):
            if line[j] == ";":
                year.append(line[:j])  
                count.append(line[j+1:])

    mt_pr_1all.Crawler(year,count,'s') 
        
def baseball_predict():

    fr = open('baseball_wdl_all.txt', 'r', encoding='UTF8')

    rdr1 = fr.readlines()
    year = []
    count = []
    for line in rdr1:
        for j in range(len(line)):
            if line[j] == ";":
                year.append(line[:j])  
                count.append(line[j+1:])

    mt_pr_1all.Crawler(year,count,'b')     
   
def basketball_predict():

    fr = open('basketball_wdl_all.txt', 'r', encoding='UTF8')

    rdr1 = fr.readlines()
    year = []
    count = []
    for line in rdr1:
        for j in range(len(line)):
            if line[j] == ";":
                year.append(line[:j])  
                count.append(line[j+1:])

    mt_pr_1all.Crawler(year,count,'k')
            
def soccer_johap():

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
        
def baseball_johap():

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
   
def basketball_johap():

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
     
def soccer_gameanalyst():

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

    pageso = st.sidebar.radio("축구 승무패 - 경기 선택", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])
    
    # print("축구 승무패",year,count)

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

def baseball_gameanalyst():

    pagebb = st.sidebar.radio("야구 승1패 - 경기 선택", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])
    
    fr = open('baseball_wdl.txt', 'r', encoding='UTF8')
    # fr = open('baseball_wdl.txt', 'r', encoding='UTF8')

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
    
    # print("야구 승1패",year,count)

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

def basketball_gameanalyst():

    pagebk = st.sidebar.radio("농구 승5패 - 경기 선택", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
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

    # print("농구 승5패",year,count)

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
        
def soccer_seqanalyst():
 
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

    pageso = st.sidebar.radio("축구 승무패", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
                                    "8경기", "9경기", "10경기", "11경기", "12경기", "13경기", "14경기"])
    
    # print("축구 승무패",year,count)

    if pageso == "1경기":
        mt_so_2all.Crawler(year,count,1) 
    elif pageso == "2경기":   
        mt_so_2all.Crawler(year,count,2)
    elif pageso == "3경기": 
        mt_so_2all.Crawler(year,count,3)
    elif pageso == "4경기": 
        mt_so_2all.Crawler(year,count,4)
    elif pageso == "5경기": 
        mt_so_2all.Crawler(year,count,5)
    elif pageso == "6경기": 
        mt_so_2all.Crawler(year,count,6)
    elif pageso == "7경기": 
        mt_so_2all.Crawler(year,count,7)
    elif pageso == "8경기": 
        mt_so_2all.Crawler(year,count,8)
    elif pageso == "9경기": 
        mt_so_2all.Crawler(year,count,9)
    elif pageso == "10경기": 
        mt_so_2all.Crawler(year,count,10)
    elif pageso == "11경기": 
        mt_so_2all.Crawler(year,count,11)
    elif pageso == "12경기": 
        mt_so_2all.Crawler(year,count,12)
    elif pageso == "13경기": 
        mt_so_2all.Crawler(year,count,13)
    elif pageso == "14경기": 
        mt_so_2all.Crawler(year,count,14)       

def baseball_seqanalyst():

    pagebb = st.sidebar.radio("야구 승1패 - 경기 선택", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
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

    if pagebb == "1경기":
        mt_bb_2all.Crawler(year,count,1) 
    elif pagebb == "2경기":   
        mt_bb_2all.Crawler(year,count,2)
    elif pagebb == "3경기": 
        mt_bb_2all.Crawler(year,count,3)
    elif pagebb == "4경기": 
        mt_bb_2all.Crawler(year,count,4)
    elif pagebb == "5경기": 
        mt_bb_2all.Crawler(year,count,5)
    elif pagebb == "6경기": 
        mt_bb_2all.Crawler(year,count,6)
    elif pagebb == "7경기": 
        mt_bb_2all.Crawler(year,count,7)
    elif pagebb == "8경기": 
        mt_bb_2all.Crawler(year,count,8)
    elif pagebb == "9경기": 
        mt_bb_2all.Crawler(year,count,9)
    elif pagebb == "10경기": 
        mt_bb_2all.Crawler(year,count,10)
    elif pagebb == "11경기": 
        mt_bb_2all.Crawler(year,count,11)
    elif pagebb == "12경기": 
        mt_bb_2all.Crawler(year,count,12)
    elif pagebb == "13경기": 
        mt_bb_2all.Crawler(year,count,13)
    elif pagebb == "14경기": 
        mt_bb_2all.Crawler(year,count,14)

def basketball_seqanalyst():

    pagebk = st.sidebar.radio("농구 승5패 - 경기 선택", ["1경기", "2경기", "3경기", "4경기", "5경기", "6경기", "7경기",
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

    # print("농구 승5패",year,count)

    if pagebk == "1경기":
        mt_bk_2all.Crawler(year,count,1) 
    elif pagebk == "2경기":   
        mt_bk_2all.Crawler(year,count,2)
    elif pagebk == "3경기": 
        mt_bk_2all.Crawler(year,count,3)
    elif pagebk == "4경기": 
        mt_bk_2all.Crawler(year,count,4)
    elif pagebk == "5경기": 
        mt_bk_2all.Crawler(year,count,5)
    elif pagebk == "6경기": 
        mt_bk_2all.Crawler(year,count,6)
    elif pagebk == "7경기": 
        mt_bk_2all.Crawler(year,count,7)
    elif pagebk == "8경기": 
        mt_bk_2all.Crawler(year,count,8)
    elif pagebk == "9경기": 
        mt_bk_2all.Crawler(year,count,9)
    elif pagebk == "10경기": 
        mt_bk_2all.Crawler(year,count,10)
    elif pagebk == "11경기": 
        mt_bk_2all.Crawler(year,count,11)
    elif pagebk == "12경기": 
        mt_bk_2all.Crawler(year,count,12)
    elif pagebk == "13경기": 
        mt_bk_2all.Crawler(year,count,13)
    elif pagebk == "14경기": 
        mt_bk_2all.Crawler(year,count,14)
           
def soccer_states():
 
    pagedt = st.sidebar.radio("경기 통계", ["승무패 경기통계", "승무패 배당통계"])    
    
    if pagedt == "승무패 경기통계":
        # print("경기 통계-승무패 경기통계")
        mt_dt_1all.Crawler("so1") 
    elif pagedt == "승무패 배당통계": 
        # print("경기 통계-승무패 배당통계")  
        mt_dt_1all.Crawler("so2")        

def baseball_states():
 
    pagedt = st.sidebar.radio("경기 통계", ["승1패 경기통계", "승1패 배당통계"])    
    
    if pagedt == "승1패 경기통계": 
        # print("경기 통계-승1패 경기통계")
        mt_dt_1all.Crawler("bb1")
    elif pagedt == "승1패 배당통계": 
        # print("경기 통계-승1패 배당통계")
        mt_dt_1all.Crawler("bb2")
        

def basketball_states():
 
    pagedt = st.sidebar.radio("경기 통계", ["승5패 경기통계", "승5패 배당통계"])    
    
    if pagedt == "승5패 경기통계": 
        # print("경기 통계-승5패 경기통계")
        mt_dt_1all.Crawler("bk1")
    elif pagedt == "승5패 배당통계": 
        # print("경기 통계-승5패 배당통계")
        mt_dt_1all.Crawler("bk2")

def soccer_allinq():
 
    # print("회차조회-축구 승무패")
    fr = open('soccer_wdl_all.txt', 'r', encoding='UTF8')

    rdr1 = fr.readlines()
    year = []
    count = []
    for line in rdr1:
        for j in range(len(line)):
            if line[j] == ";":
                year.append(line[:j])  
                count.append(line[j+1:])

    mt_ma_1all.Crawler(year,count,'s') 

def baseball_allinq():
 
    # print("회차조회-야구 승1패")
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

def basketball_allinq():
 
    # print("회차조회-농구승5패")
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
         
# 메인 콘텐츠 영역
if selected_sport == "축구 승무패": 

    if submenu == "예측":
       
        soccer_predict()

    elif submenu == "조합기":
       
        soccer_johap()

    elif submenu == "경기별 분석":

        soccer_gameanalyst()

    elif submenu == "경기 통계":

        soccer_states()

    elif submenu == "회차 조회":

        soccer_allinq()

    elif submenu == "순위추이 분석":

        soccer_seqanalyst()

elif selected_sport == "야구 승1패":

    if submenu == "예측":
       
        baseball_predict()

    elif submenu == "조합기":

        baseball_johap()

    elif submenu == "경기별 분석":

        baseball_gameanalyst()

    elif submenu == "경기 통계":

        baseball_states()

    elif submenu == "회차 조회":

        baseball_allinq()

    elif submenu == "순위추이 분석":

        baseball_seqanalyst()

elif selected_sport == "농구 승5패":

    if submenu == "예측":
       
        basketball_predict()

    elif submenu == "조합기":

        basketball_johap()

    elif submenu == "경기별 분석":

        basketball_gameanalyst()

    elif submenu == "경기 통계":

        basketball_states()

    elif submenu == "회차 조회":

        basketball_allinq()

    elif submenu == "순위추이 분석":

        basketball_seqanalyst()
