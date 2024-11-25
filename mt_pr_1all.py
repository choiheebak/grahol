import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
from PIL import Image

def Crawler(yearc,countc,gubun):
   
    year = int(yearc)
    count = int(countc)

    if gubun == 's':
      
        st.subheader("축구 승무패 "+ str(year)+"년 "+str(count)+"회차") 
  
        f = open('soccer_so7_predict.txt', 'r', encoding='UTF8')
       
        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            l = line
            l = l.replace("\n","")
            team_read.append(l)

        f.close

        home = []
        away = []
        seq = []
        result = []
        ai2 = []
        predict = []
        big2 = []
        ai = []
        aihml = []
        hwakryul = []
        seqtg = []
        last = []
        hvsa = []
        junjeok = []
        gyung = []
        sun = []
        bae = []
        baeh = []
        tonghap = []

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        seq.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        home.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 3:
                        away.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 4:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 5:
                        ai2.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 6:
                        predict.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 7:
                        big2.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        ai.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        aihml.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
                        hwakryul.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 11:
                        seqtg.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 12:
                        last.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 13:
                        hvsa.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 14:
                        junjeok.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 15:
                        gyung.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 16:
                        sun.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 17:
                        bae.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 18:
                        baeh.append(team_read[q][s:r])
                        s = r+1
                        tonghap.append(team_read[q][s:])

        st.markdown(":soccer: :blue[**AI 빅데이터 예측 결과**]")
        st.markdown("")

        def iljaseq_home(num_rows):
    
            # index = [f"{i}" for i in range(1, (num_rows+1))] 

            index = [f"{i}경기" for i in range(1, 15)]
            홈팀 = [home[i] for i in range(num_rows)]
            원정팀 = [away[i] for i in range(num_rows)]
            빅2 = [big2[i] for i in range(num_rows)]
            AI경기 = [ai[i] for i in range(num_rows)]
            AI배당 = [aihml[i] for i in range(num_rows)]
            예측 = [tonghap[i] for i in range(num_rows)]
            우세 = [predict[i] for i in range(num_rows)]
            해외확률 = [hwakryul[i] for i in range(num_rows)]
            해외배당 = [bae[i] for i in range(num_rows)]
            순위 = [seqtg[i] for i in range(num_rows)]
            최근 = [last[i] for i in range(num_rows)]
            홈맞대결 = [hvsa[i] for i in range(num_rows)]
            총전적 = [junjeok[i] for i in range(num_rows)]
            평균득점 = [sun[i] for i in range(num_rows)]
            경기확률 = [gyung[i] for i in range(num_rows)]
            배당확률 = [baeh[i] for i in range(num_rows)]

            # 딕셔너리로 데이터 구성
            data = {
                # "선수": 선수,
                "홈팀": 홈팀,
                "원정팀": 원정팀,
                "빅2": 빅2,
                "AI경기": AI경기,
                "AI배당": AI배당,
                "예측": 예측,
                "우세": 우세,
                "해외확률": 해외확률,
                "해외배당": 해외배당,
                "순위": 순위,
                "최근": 최근,
                "홈맞대결": 홈맞대결,
                "총전적": 총전적,
                "평균득점": 평균득점,
                "경기확률": 경기확률,
                "배당확률": 배당확률
            }

            # DataFrame 생성
            dfhs = pd.DataFrame(data, index=pd.Index(index, name="일자"))

            return dfhs
   
        dfhs = iljaseq_home(len(home))

        # st.table(dfhs)
        st.dataframe(dfhs, use_container_width=True)   

        st.markdown(":red[* 예측결과는 참조용입니다. 본인이 참조,선택하여 결과를 예측합니다. 모든 책임은 본인에게 있음을 공지합니다.]")
        st.text("< 용어 설명 >")
        st.text("- 빅2 : 빅데이터 2픽 가중치 부여한 결과")
        st.text("- AI경기 : AI딥러닝 전체승무패를 학습시켜서 나온 결과")
        st.text("- AI배당 : AI딥러닝 전체고중저를 학습시켜서 나온 결과")
        st.text("- 우세 : 해외배당, 순위, 최근, 홈맞대결, 총전적, 평균득점, 경기확률, 배당확률 합해서 최다 결과, 같을 경우 홈맞대결, 최근7경기 순")
        st.text("- 해외확률 : 해외배당 빅데이터 중 최다 결과")
        st.text("- 순위 : 팀, 개인 순위 합한 결과")
        st.text("- 최근 : 최근7경기 양팀 결과")
        st.text("- 홈맞대결 : 홈맞대결 7경기 결과 우선, 같을 경우 전체홈맞대결, 원정맞대결 순")
        st.text("- 총전적 : 양팀 총전적 원정, 홈 우선 결과")
        st.text("- 평균득점 : 시즌 평균 득점 결과")
        st.text("- 경기확률 : 전체 대 최근30회차 승무패 확률")
        st.text("- 배당확률 : 전체 대 최근30회차 고중저(득표기준) 확률")

    elif gubun == 'b':
     
        st.subheader("야구 승1패 "+ str(year)+"년 "+str(count)+"회차") 
  
        f = open('baseball_bb7_predict.txt', 'r', encoding='UTF8')
       
        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            l = line
            l = l.replace("\n","")
            team_read.append(l)

        f.close

        home = []
        away = []
        seq = []
        result = []
        ai2 = []
        predict = []
        big2 = []
        ai = []
        aihml = []
        hwakryul = []
        seqtg = []
        last = []
        hvsa = []
        junjeok = []
        gyung = []
        sun = []
        bae = []
        baeh = []
        tonghap = []

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        seq.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        home.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 3:
                        away.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 4:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 5:
                        ai2.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 6:
                        predict.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 7:
                        big2.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        ai.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        aihml.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
                        hwakryul.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 11:
                        seqtg.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 12:
                        last.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 13:
                        hvsa.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 14:
                        junjeok.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 15:
                        gyung.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 16:
                        sun.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 17:
                        bae.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 18:
                        baeh.append(team_read[q][s:r])
                        s = r+1
                        tonghap.append(team_read[q][s:])

        st.markdown(":baseball: :blue[**AI 빅데이터 예측 결과**]")
        st.markdown("")

        def iljaseq_home(num_rows):
    
            # index = [f"{i}" for i in range(1, (num_rows+1))] 

            index = [f"{i}경기" for i in range(1, 15)]
            홈팀 = [home[i] for i in range(num_rows)]
            원정팀 = [away[i] for i in range(num_rows)]
            빅2 = [big2[i] for i in range(num_rows)]
            AI경기 = [ai[i] for i in range(num_rows)]
            AI배당 = [aihml[i] for i in range(num_rows)]
            예측 = [tonghap[i] for i in range(num_rows)]
            우세 = [predict[i] for i in range(num_rows)]
            확률 = [hwakryul[i] for i in range(num_rows)]
            배당 = [bae[i] for i in range(num_rows)]
            순위 = [seqtg[i] for i in range(num_rows)]
            최근 = [last[i] for i in range(num_rows)]
            홈맞대결 = [hvsa[i] for i in range(num_rows)]
            총전적 = [junjeok[i] for i in range(num_rows)]
            평균득점 = [sun[i] for i in range(num_rows)]
            경기확률 = [gyung[i] for i in range(num_rows)]
            배당확률 = [baeh[i] for i in range(num_rows)]

            # 딕셔너리로 데이터 구성
            data = {
                # "선수": 선수,
                "홈팀": 홈팀,
                "원정팀": 원정팀,
                "빅2": 빅2,
                "AI경기": AI경기,
                "AI배당": AI배당,
                "예측": 예측,
                "우세": 우세,
                "확률": 확률,
                "배당": 배당,
                "순위": 순위,
                "최근": 최근,
                "홈맞대결": 홈맞대결,
                "총전적": 총전적,
                "평균득점": 평균득점,
                "경기확률": 경기확률,
                "배당확률": 배당확률
            }

            # DataFrame 생성
            dfhs = pd.DataFrame(data, index=pd.Index(index, name="일자"))

            return dfhs
   
        dfhs = iljaseq_home(len(home))

        # st.table(dfhs)
        st.dataframe(dfhs, use_container_width=True)   

        st.markdown(":red[* 예측결과는 참조용입니다. 본인이 참조,선택하여 결과를 예측합니다. 모든 책임은 본인에게 있음을 공지합니다.]")
        st.text("< 용어 설명 >")
        st.text("- 빅2 : 빅데이터 2픽 가중치 부여한 결과")
        st.text("- AI경기 : AI딥러닝 전체승1패를 학습시켜서 나온 결과")
        st.text("- AI배당 : AI딥러닝 전체고중저를 학습시켜서 나온 결과")
        st.text("- 우세 : 배당, 순위, 최근, 홈맞대결, 총전적, 평균득점, 경기확률, 배당확률 합해서 최다 결과, 같을 경우 홈맞대결, 최근7경기 순")
        st.text("- 확률 : 베트맨배당 빅데이터 중 최다 결과")
        st.text("- 순위 : 팀, 개인 순위 합한 결과")
        st.text("- 최근 : 최근7경기 양팀 결과")
        st.text("- 홈맞대결 : 홈맞대결 7경기 결과 우선, 같을 경우 전체홈맞대결, 원정맞대결 순")
        st.text("- 총전적 : 양팀 총전적 원정, 홈 우선 결과")
        st.text("- 평균득점 : 시즌 평균 득점 결과")
        st.text("- 경기확률 : 전체 대 최근30회차 승무패 확률")
        st.text("- 배당확률 : 전체 대 최근30회차 고중저(득표기준) 확률")

    elif gubun == 'k':     
        
        st.subheader("농구 승5패 "+ str(year)+"년 "+str(count)+"회차") 
  
        f = open('basketball_bk7_predict.txt', 'r', encoding='UTF8')
       
        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            l = line
            l = l.replace("\n","")
            team_read.append(l)

        f.close

        home = []
        away = []
        seq = []
        result = []
        ai2 = []
        predict = []
        big2 = []
        ai = []
        aihml = []
        hwakryul = []
        seqtg = []
        last = []
        hvsa = []
        junjeok = []
        gyung = []
        sun = []
        bae = []
        baeh = []
        tonghap = []

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        seq.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        home.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 3:
                        away.append(team_read[q][s:r]) 
                        s = r+1
                    elif rcnt == 4:
                        result.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 5:
                        ai2.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 6:
                        predict.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 7:
                        big2.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 8:
                        ai.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 9:
                        aihml.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 10:
                        hwakryul.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 11:
                        seqtg.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 12:
                        last.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 13:
                        hvsa.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 14:
                        junjeok.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 15:
                        gyung.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 16:
                        sun.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 17:
                        bae.append(team_read[q][s:r])
                        s = r+1
                    elif rcnt == 18:
                        baeh.append(team_read[q][s:r])
                        s = r+1
                        tonghap.append(team_read[q][s:])

        st.markdown(":basketball: :blue[**AI 빅데이터 예측 결과**]")
        st.markdown("")

        def iljaseq_home(num_rows):
    
            # index = [f"{i}" for i in range(1, (num_rows+1))] 

            index = [f"{i}경기" for i in range(1, 15)]
            홈팀 = [home[i] for i in range(num_rows)]
            원정팀 = [away[i] for i in range(num_rows)]
            빅2 = [big2[i] for i in range(num_rows)]
            AI경기 = [ai[i] for i in range(num_rows)]
            AI배당 = [aihml[i] for i in range(num_rows)]
            예측 = [tonghap[i] for i in range(num_rows)]
            우세 = [predict[i] for i in range(num_rows)]
            확률 = [hwakryul[i] for i in range(num_rows)]
            배당 = [bae[i] for i in range(num_rows)]
            순위 = [seqtg[i] for i in range(num_rows)]
            최근 = [last[i] for i in range(num_rows)]
            홈맞대결 = [hvsa[i] for i in range(num_rows)]
            총전적 = [junjeok[i] for i in range(num_rows)]
            평균득점 = [sun[i] for i in range(num_rows)]
            경기확률 = [gyung[i] for i in range(num_rows)]
            배당확률 = [baeh[i] for i in range(num_rows)]

            # 딕셔너리로 데이터 구성
            data = {
                # "선수": 선수,
                "홈팀": 홈팀,
                "원정팀": 원정팀,
                "빅2": 빅2,
                "AI경기": AI경기,
                "AI배당": AI배당,
                "예측": 예측,
                "우세": 우세,
                "확률": 확률,
                "배당": 배당,
                "순위": 순위,
                "최근": 최근,
                "홈맞대결": 홈맞대결,
                "총전적": 총전적,
                "평균득점": 평균득점,
                "경기확률": 경기확률,
                "배당확률": 배당확률
            }

            # DataFrame 생성
            dfhs = pd.DataFrame(data, index=pd.Index(index, name="일자"))

            return dfhs
   
        dfhs = iljaseq_home(len(home))

        # st.table(dfhs)
        st.dataframe(dfhs, use_container_width=True)   

        st.markdown(":red[* 예측결과는 참조용입니다. 본인이 참조,선택하여 결과를 예측합니다. 모든 책임은 본인에게 있음을 공지합니다.]")
        st.text("< 용어 설명 >")
        st.text("- 빅2 : 빅데이터 2픽 가중치 부여한 결과")
        st.text("- AI경기 : AI딥러닝 전체승5패를 학습시켜서 나온 결과")
        st.text("- AI배당 : AI딥러닝 전체고중저를 학습시켜서 나온 결과")
        st.text("- 우세 : 배당, 순위, 최근, 홈맞대결, 총전적, 평균득점, 경기확률, 배당확률 합해서 최다 결과, 같을 경우 홈맞대결, 최근7경기 순")
        st.text("- 확률 : 베트맨배당 빅데이터 중 최다 결과")
        st.text("- 순위 : 팀, 개인 순위 합한 결과")
        st.text("- 최근 : 최근7경기 양팀 결과")
        st.text("- 홈맞대결 : 홈맞대결 7경기 결과 우선, 같을 경우 전체홈맞대결, 원정맞대결 순")
        st.text("- 총전적 : 양팀 총전적 원정, 홈 우선 결과")
        st.text("- 평균득점 : 시즌 평균 득점 결과")
        st.text("- 경기확률 : 전체 대 최근30회차 승무패 확률")
        st.text("- 배당확률 : 전체 대 최근30회차 고중저(득표기준) 확률")
