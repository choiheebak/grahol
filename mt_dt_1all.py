import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
import plotly.graph_objects as go

def Crawler(gubun):

    # print(gubun,indegree)
    
    def read_all_txt(g,k):
        if g == '01':
            f = open('soccer_so4_wdltong.txt', 'r', encoding='UTF8')
        elif g == '02':
            f = open('baseball_bb4_wdltong.txt', 'r', encoding='UTF8')
        elif g == '03':
            f = open('basketball_bk4_wdltong.txt', 'r', encoding='UTF8')
        elif g == '04':
            f = open('soccer_so4_hmltong.txt', 'r', encoding='UTF8')
        elif g == '05':
            f = open('baseball_bb4_hmltong.txt', 'r', encoding='UTF8')
        elif g == '06':
            f = open('basketball_bk4_hmltong.txt', 'r', encoding='UTF8')
        # if g == '01':
        #     f = open('D:/datagithub/soccer/soccer_so4_wdltong.txt', 'r', encoding='UTF8')
        # elif g == '02':
        #     f = open('D:/datagithub/baseball/baseball_bb4_wdltong.txt', 'r', encoding='UTF8')
        # elif g == '03':
        #     f = open('D:/datagithub/basketball/basketball_bk4_wdltong.txt', 'r', encoding='UTF8')
        # elif g == '04':
        #     f = open('D:/datagithub/soccer/soccer_so4_hmltong.txt', 'r', encoding='UTF8')
        # elif g == '05':
        #     f = open('D:/datagithub/baseball/baseball_bb4_hmltong.txt', 'r', encoding='UTF8')
        # elif g == '06':
        #     f = open('D:/datagithub/basketball/basketball_bk4_hmltong.txt', 'r', encoding='UTF8')

        rdr1 = f.readlines()    

        team_read = []
        for line in rdr1:
            if int(line[:3]) == int(k):
                l = line[4:]
                l = l.replace("\n","")
                team_read.append(l)
                
        f.close

        return team_read

    if gubun == "so1":

        year = []
        degree = []
        seq = []
        result = []
        year30 = []
        degree30 = []
        seq30 = []
        result30 = []
        tcntw = []
        tcntd = []
        tcntl = []
        tcntw30 = []
        tcntd30 = []
        tcntl30 = []

        team_read = read_all_txt('01','999')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd.append(team_read[q][s:r])
                        s = r+1
                        tcntl.append(team_read[q][s:])

        team_read = read_all_txt('01','300')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw30.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd30.append(team_read[q][s:r])
                        s = r+1
                        tcntl30.append(team_read[q][s:])

        team_read = read_all_txt('01','100')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        result30.append(team_read[q][:r]) 
                        s = r+1
                        degree30.append(team_read[q][s:])

        st.markdown(":soccer: :violet[**전체 승무패 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw,tcntd,tcntl]), 

                index= ["승","무","패"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)

        colors = ['#FFA07A', '#F0E68C', '#87CEFA']
        labels = ['승','무','패']
        values0 = [tcntw[0], tcntd[0], tcntl[0]]
        values1 = [tcntw[1], tcntd[1], tcntl[1]]
        values2 = [tcntw[2], tcntd[2], tcntl[2]]
        values3 = [tcntw[3], tcntd[3], tcntl[3]]
        values4 = [tcntw[4], tcntd[4], tcntl[4]]
        values5 = [tcntw[5], tcntd[5], tcntl[5]]
        values6 = [tcntw[6], tcntd[6], tcntl[6]]
        values7 = [tcntw[7], tcntd[7], tcntl[7]]
        values8 = [tcntw[8], tcntd[8], tcntl[8]]
        values9 = [tcntw[9], tcntd[9], tcntl[9]]
        values10 = [tcntw[10], tcntd[10], tcntl[10]]
        values11 = [tcntw[11], tcntd[11], tcntl[11]]
        values12 = [tcntw[12], tcntd[12], tcntl[12]]
        values13 = [tcntw[13], tcntd[13], tcntl[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        st.markdown(":soccer: :violet[**최근 30 회차 승무패 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw30,tcntd30,tcntl30]), 

                index= ["승","무","패"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)

        values0 = [tcntw30[0], tcntd30[0], tcntl30[0]]
        values1 = [tcntw30[1], tcntd30[1], tcntl30[1]]
        values2 = [tcntw30[2], tcntd30[2], tcntl30[2]]
        values3 = [tcntw30[3], tcntd30[3], tcntl30[3]]
        values4 = [tcntw30[4], tcntd30[4], tcntl30[4]]
        values5 = [tcntw30[5], tcntd30[5], tcntl30[5]]
        values6 = [tcntw30[6], tcntd30[6], tcntl30[6]]
        values7 = [tcntw30[7], tcntd30[7], tcntl30[7]]
        values8 = [tcntw30[8], tcntd30[8], tcntl30[8]]
        values9 = [tcntw30[9], tcntd30[9], tcntl30[9]]
        values10 = [tcntw30[10], tcntd30[10], tcntl30[10]]
        values11 = [tcntw30[11], tcntd30[11], tcntl30[11]]
        values12 = [tcntw30[12], tcntd30[12], tcntl30[12]]
        values13 = [tcntw30[13], tcntd30[13], tcntl30[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        # st.markdown(":soccer: :violet[**최근 10회차 결과**]")

        # rede10_def(result30,degree30,'s','1')

    elif gubun == "bb1":
        
        year = []
        degree = []
        seq = []
        result = []
        year30 = []
        degree30 = []
        seq30 = []
        result30 = []
        tcntw = []
        tcntd = []
        tcntl = []
        tcntw30 = []
        tcntd30 = []
        tcntl30 = []
        
        team_read = read_all_txt('02','999')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd.append(team_read[q][s:r])
                        s = r+1
                        tcntl.append(team_read[q][s:])

        team_read = read_all_txt('02','300')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw30.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd30.append(team_read[q][s:r])
                        s = r+1
                        tcntl30.append(team_read[q][s:])

        team_read = read_all_txt('02','100')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        result30.append(team_read[q][:r]) 
                        s = r+1
                        degree30.append(team_read[q][s:])

        st.markdown(":baseball: :violet[**전체 승①패 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw,tcntd,tcntl]), 

                index= ["승","①","패"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)

        colors = ['#FFA07A', '#F0E68C', '#87CEFA']
        labels = ['승','①','패']
        values0 = [tcntw[0], tcntd[0], tcntl[0]]
        values1 = [tcntw[1], tcntd[1], tcntl[1]]
        values2 = [tcntw[2], tcntd[2], tcntl[2]]
        values3 = [tcntw[3], tcntd[3], tcntl[3]]
        values4 = [tcntw[4], tcntd[4], tcntl[4]]
        values5 = [tcntw[5], tcntd[5], tcntl[5]]
        values6 = [tcntw[6], tcntd[6], tcntl[6]]
        values7 = [tcntw[7], tcntd[7], tcntl[7]]
        values8 = [tcntw[8], tcntd[8], tcntl[8]]
        values9 = [tcntw[9], tcntd[9], tcntl[9]]
        values10 = [tcntw[10], tcntd[10], tcntl[10]]
        values11 = [tcntw[11], tcntd[11], tcntl[11]]
        values12 = [tcntw[12], tcntd[12], tcntl[12]]
        values13 = [tcntw[13], tcntd[13], tcntl[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        st.markdown(":baseball: :violet[**최근 30 회차 승①패 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw30,tcntd30,tcntl30]), 

                index= ["승","①","패"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 


        st.dataframe(df)
 
        values0 = [tcntw30[0], tcntd30[0], tcntl30[0]]
        values1 = [tcntw30[1], tcntd30[1], tcntl30[1]]
        values2 = [tcntw30[2], tcntd30[2], tcntl30[2]]
        values3 = [tcntw30[3], tcntd30[3], tcntl30[3]]
        values4 = [tcntw30[4], tcntd30[4], tcntl30[4]]
        values5 = [tcntw30[5], tcntd30[5], tcntl30[5]]
        values6 = [tcntw30[6], tcntd30[6], tcntl30[6]]
        values7 = [tcntw30[7], tcntd30[7], tcntl30[7]]
        values8 = [tcntw30[8], tcntd30[8], tcntl30[8]]
        values9 = [tcntw30[9], tcntd30[9], tcntl30[9]]
        values10 = [tcntw30[10], tcntd30[10], tcntl30[10]]
        values11 = [tcntw30[11], tcntd30[11], tcntl30[11]]
        values12 = [tcntw30[12], tcntd30[12], tcntl30[12]]
        values13 = [tcntw30[13], tcntd30[13], tcntl30[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        # st.markdown(":baseball: :violet[**최근 10회차 결과**]")

        # for s in range(len(result30)):
        #     if result30[s] == "1":
        #         result30[s] = "①"
                
        # rede10_def(result30,degree30,'b','1')

    elif gubun == "bk1":
        
        year = []
        degree = []
        seq = []
        result = []
        year30 = []
        degree30 = []
        seq30 = []
        result30 = []
        tcntw = []
        tcntd = []
        tcntl = []
        tcntw30 = []
        tcntd30 = []
        tcntl30 = []
        
        team_read = read_all_txt('03','999')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd.append(team_read[q][s:r])
                        s = r+1
                        tcntl.append(team_read[q][s:])

        team_read = read_all_txt('03','300')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw30.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd30.append(team_read[q][s:r])
                        s = r+1
                        tcntl30.append(team_read[q][s:])

        team_read = read_all_txt('03','100')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        result30.append(team_read[q][:r]) 
                        s = r+1
                        degree30.append(team_read[q][s:])

        st.markdown(":basketball: :violet[**전체 승⑤패 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw,tcntd,tcntl]), 

                index= ["승","⑤","패"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)

        colors = ['#FFA07A', '#F0E68C', '#87CEFA']
        labels = ['승','⑤','패']
        values0 = [tcntw[0], tcntd[0], tcntl[0]]
        values1 = [tcntw[1], tcntd[1], tcntl[1]]
        values2 = [tcntw[2], tcntd[2], tcntl[2]]
        values3 = [tcntw[3], tcntd[3], tcntl[3]]
        values4 = [tcntw[4], tcntd[4], tcntl[4]]
        values5 = [tcntw[5], tcntd[5], tcntl[5]]
        values6 = [tcntw[6], tcntd[6], tcntl[6]]
        values7 = [tcntw[7], tcntd[7], tcntl[7]]
        values8 = [tcntw[8], tcntd[8], tcntl[8]]
        values9 = [tcntw[9], tcntd[9], tcntl[9]]
        values10 = [tcntw[10], tcntd[10], tcntl[10]]
        values11 = [tcntw[11], tcntd[11], tcntl[11]]
        values12 = [tcntw[12], tcntd[12], tcntl[12]]
        values13 = [tcntw[13], tcntd[13], tcntl[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        st.markdown(":basketball: :violet[**최근 30 회차 승⑤패 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw30,tcntd30,tcntl30]), 

                index= ["승","⑤","패"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)
 
        values0 = [tcntw30[0], tcntd30[0], tcntl30[0]]
        values1 = [tcntw30[1], tcntd30[1], tcntl30[1]]
        values2 = [tcntw30[2], tcntd30[2], tcntl30[2]]
        values3 = [tcntw30[3], tcntd30[3], tcntl30[3]]
        values4 = [tcntw30[4], tcntd30[4], tcntl30[4]]
        values5 = [tcntw30[5], tcntd30[5], tcntl30[5]]
        values6 = [tcntw30[6], tcntd30[6], tcntl30[6]]
        values7 = [tcntw30[7], tcntd30[7], tcntl30[7]]
        values8 = [tcntw30[8], tcntd30[8], tcntl30[8]]
        values9 = [tcntw30[9], tcntd30[9], tcntl30[9]]
        values10 = [tcntw30[10], tcntd30[10], tcntl30[10]]
        values11 = [tcntw30[11], tcntd30[11], tcntl30[11]]
        values12 = [tcntw30[12], tcntd30[12], tcntl30[12]]
        values13 = [tcntw30[13], tcntd30[13], tcntl30[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        # st.markdown(":basketball: :violet[**최근 10회차 결과**]")

        # for s in range(len(result30)):
        #     if result30[s] == "5":
        #         result30[s] = "⑤"
                
        # rede10_def(result30,degree30,'k','1')
    
    elif gubun == "so2":

        year = []
        degree = []
        seq = []
        result = []
        win = []
        draw = []
        lose = []
        year30 = []
        degree30 = []
        seq30 = []
        result30 = []
        tcntw = []
        tcntd = []
        tcntl = []
        tcntw30 = []
        tcntd30 = []
        tcntl30 = []
         
        team_read = read_all_txt('04','999')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd.append(team_read[q][s:r])
                        s = r+1
                        tcntl.append(team_read[q][s:])

        team_read = read_all_txt('04','300')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw30.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd30.append(team_read[q][s:r])
                        s = r+1
                        tcntl30.append(team_read[q][s:])

        team_read = read_all_txt('04','100')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        result30.append(team_read[q][:r]) 
                        s = r+1
                        degree30.append(team_read[q][s:])

        st.markdown(":soccer: :violet[**전체 고중저 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw,tcntd,tcntl]), 

                index= ["고","중","저"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)

        colors = ['#2F4F4F', '#696969', '#C0C0C0']
        labels = ['고','중','저']
        values0 = [tcntw[0], tcntd[0], tcntl[0]]
        values1 = [tcntw[1], tcntd[1], tcntl[1]]
        values2 = [tcntw[2], tcntd[2], tcntl[2]]
        values3 = [tcntw[3], tcntd[3], tcntl[3]]
        values4 = [tcntw[4], tcntd[4], tcntl[4]]
        values5 = [tcntw[5], tcntd[5], tcntl[5]]
        values6 = [tcntw[6], tcntd[6], tcntl[6]]
        values7 = [tcntw[7], tcntd[7], tcntl[7]]
        values8 = [tcntw[8], tcntd[8], tcntl[8]]
        values9 = [tcntw[9], tcntd[9], tcntl[9]]
        values10 = [tcntw[10], tcntd[10], tcntl[10]]
        values11 = [tcntw[11], tcntd[11], tcntl[11]]
        values12 = [tcntw[12], tcntd[12], tcntl[12]]
        values13 = [tcntw[13], tcntd[13], tcntl[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                try:
                    st.plotly_chart(fig0, theme=None)
                except:
                    st.plotly_chart(fig0)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                try:
                    st.plotly_chart(fig1, theme=None)
                except:
                    st.plotly_chart(fig1)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                try:
                    st.plotly_chart(fig2, theme=None)
                except:
                    st.plotly_chart(fig2)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                try:
                    st.plotly_chart(fig3, theme=None)
                except:
                    st.plotly_chart(fig3)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                try:
                    st.plotly_chart(fig4, theme=None)
                except:
                    st.plotly_chart(fig4)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                try:
                    st.plotly_chart(fig5, theme=None)
                except:
                    st.plotly_chart(fig5)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                try:
                    st.plotly_chart(fig6, theme=None)
                except:
                    st.plotly_chart(fig6)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                try:
                    st.plotly_chart(fig7, theme=None)
                except:
                    st.plotly_chart(fig7)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                try:
                    st.plotly_chart(fig8, theme=None)
                except:
                    st.plotly_chart(fig8)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                try:
                    st.plotly_chart(fig9, theme=None)
                except:
                    st.plotly_chart(fig9)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                try:
                    st.plotly_chart(fig10, theme=None)
                except:
                    st.plotly_chart(fig10)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                try:
                    st.plotly_chart(fig11, theme=None)
                except:
                    st.plotly_chart(fig11)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                try:
                    st.plotly_chart(fig12, theme=None)
                except:
                    st.plotly_chart(fig12)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                try:
                    st.plotly_chart(fig13, theme=None)
                except:
                    st.plotly_chart(fig13)

        st.markdown(":soccer: :violet[**최근 30 회차 고중저 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw30,tcntd30,tcntl30]), 

                index= ["고","중","저"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)
   
        values0 = [tcntw30[0], tcntd30[0], tcntl30[0]]
        values1 = [tcntw30[1], tcntd30[1], tcntl30[1]]
        values2 = [tcntw30[2], tcntd30[2], tcntl30[2]]
        values3 = [tcntw30[3], tcntd30[3], tcntl30[3]]
        values4 = [tcntw30[4], tcntd30[4], tcntl30[4]]
        values5 = [tcntw30[5], tcntd30[5], tcntl30[5]]
        values6 = [tcntw30[6], tcntd30[6], tcntl30[6]]
        values7 = [tcntw30[7], tcntd30[7], tcntl30[7]]
        values8 = [tcntw30[8], tcntd30[8], tcntl30[8]]
        values9 = [tcntw30[9], tcntd30[9], tcntl30[9]]
        values10 = [tcntw30[10], tcntd30[10], tcntl30[10]]
        values11 = [tcntw30[11], tcntd30[11], tcntl30[11]]
        values12 = [tcntw30[12], tcntd30[12], tcntl30[12]]
        values13 = [tcntw30[13], tcntd30[13], tcntl30[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        # st.markdown(":soccer: :violet[**최근 10회차 결과**]")

        # rede10_def(result30,degree30,'s','2')

    elif gubun == "bb2":

        year = []
        degree = []
        seq = []
        result = []
        win = []
        draw = []
        lose = []
        year30 = []
        degree30 = []
        seq30 = []
        result30 = []
        tcntw = []
        tcntd = []
        tcntl = []
        tcntw30 = []
        tcntd30 = []
        tcntl30 = []
         
        team_read = read_all_txt('05','999')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd.append(team_read[q][s:r])
                        s = r+1
                        tcntl.append(team_read[q][s:])

        team_read = read_all_txt('05','300')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw30.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd30.append(team_read[q][s:r])
                        s = r+1
                        tcntl30.append(team_read[q][s:])

        team_read = read_all_txt('05','100')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        result30.append(team_read[q][:r]) 
                        s = r+1
                        degree30.append(team_read[q][s:])

        st.markdown(":baseball: :violet[**전체 고중저 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw,tcntd,tcntl]), 

                index= ["고","중","저"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)

        colors = ['#2F4F4F', '#696969', '#C0C0C0']
        labels = ['고','중','저']
        values0 = [tcntw[0], tcntd[0], tcntl[0]]
        values1 = [tcntw[1], tcntd[1], tcntl[1]]
        values2 = [tcntw[2], tcntd[2], tcntl[2]]
        values3 = [tcntw[3], tcntd[3], tcntl[3]]
        values4 = [tcntw[4], tcntd[4], tcntl[4]]
        values5 = [tcntw[5], tcntd[5], tcntl[5]]
        values6 = [tcntw[6], tcntd[6], tcntl[6]]
        values7 = [tcntw[7], tcntd[7], tcntl[7]]
        values8 = [tcntw[8], tcntd[8], tcntl[8]]
        values9 = [tcntw[9], tcntd[9], tcntl[9]]
        values10 = [tcntw[10], tcntd[10], tcntl[10]]
        values11 = [tcntw[11], tcntd[11], tcntl[11]]
        values12 = [tcntw[12], tcntd[12], tcntl[12]]
        values13 = [tcntw[13], tcntd[13], tcntl[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        st.markdown(":baseball: :violet[**최근 30 회차 고중저 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw30,tcntd30,tcntl30]), 

                index= ["고","중","저"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)
     
        values0 = [tcntw30[0], tcntd30[0], tcntl30[0]]
        values1 = [tcntw30[1], tcntd30[1], tcntl30[1]]
        values2 = [tcntw30[2], tcntd30[2], tcntl30[2]]
        values3 = [tcntw30[3], tcntd30[3], tcntl30[3]]
        values4 = [tcntw30[4], tcntd30[4], tcntl30[4]]
        values5 = [tcntw30[5], tcntd30[5], tcntl30[5]]
        values6 = [tcntw30[6], tcntd30[6], tcntl30[6]]
        values7 = [tcntw30[7], tcntd30[7], tcntl30[7]]
        values8 = [tcntw30[8], tcntd30[8], tcntl30[8]]
        values9 = [tcntw30[9], tcntd30[9], tcntl30[9]]
        values10 = [tcntw30[10], tcntd30[10], tcntl30[10]]
        values11 = [tcntw30[11], tcntd30[11], tcntl30[11]]
        values12 = [tcntw30[12], tcntd30[12], tcntl30[12]]
        values13 = [tcntw30[13], tcntd30[13], tcntl30[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        # st.markdown(":baseball: :violet[**최근 10회차 결과**]")
       
        # rede10_def(result30,degree30,'b','2')

    elif gubun == "bk2":
        
        year = []
        degree = []
        seq = []
        result = []
        win = []
        draw = []
        lose = []
        year30 = []
        degree30 = []
        seq30 = []
        result30 = []
        tcntw = []
        tcntd = []
        tcntl = []
        tcntw30 = []
        tcntd30 = []
        tcntl30 = []
        
        team_read = read_all_txt('06','999')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd.append(team_read[q][s:r])
                        s = r+1
                        tcntl.append(team_read[q][s:])

        team_read = read_all_txt('06','300')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        tcntw30.append(team_read[q][:r]) 
                        s = r+1
                    elif rcnt == 2:
                        tcntd30.append(team_read[q][s:r])
                        s = r+1
                        tcntl30.append(team_read[q][s:])

        team_read = read_all_txt('06','100')

        for q in range(len(team_read)):
            rcnt = 0
            for r in range(len(team_read[q])):
                if team_read[q][r] == ";":
                    rcnt += 1
                    if rcnt == 1:
                        result30.append(team_read[q][:r]) 
                        s = r+1
                        degree30.append(team_read[q][s:])

        st.markdown(":basketball: :violet[**전체 고중저 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw,tcntd,tcntl]), 

                index= ["고","중","저"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)

        colors = ['#2F4F4F', '#696969', '#C0C0C0']
        labels = ['고','중','저']
        values0 = [tcntw[0], tcntd[0], tcntl[0]]
        values1 = [tcntw[1], tcntd[1], tcntl[1]]
        values2 = [tcntw[2], tcntd[2], tcntl[2]]
        values3 = [tcntw[3], tcntd[3], tcntl[3]]
        values4 = [tcntw[4], tcntd[4], tcntl[4]]
        values5 = [tcntw[5], tcntd[5], tcntl[5]]
        values6 = [tcntw[6], tcntd[6], tcntl[6]]
        values7 = [tcntw[7], tcntd[7], tcntl[7]]
        values8 = [tcntw[8], tcntd[8], tcntl[8]]
        values9 = [tcntw[9], tcntd[9], tcntl[9]]
        values10 = [tcntw[10], tcntd[10], tcntl[10]]
        values11 = [tcntw[11], tcntd[11], tcntl[11]]
        values12 = [tcntw[12], tcntd[12], tcntl[12]]
        values13 = [tcntw[13], tcntd[13], tcntl[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        st.markdown(":basketball: :violet[**최근 30 회차 고중저 경기통계**]")
        df = pd.DataFrame(data=np.array([tcntw30,tcntd30,tcntl30]), 

                index= ["고","중","저"], 
                columns=["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"]) 

        st.dataframe(df)
    
        values0 = [tcntw30[0], tcntd30[0], tcntl30[0]]
        values1 = [tcntw30[1], tcntd30[1], tcntl30[1]]
        values2 = [tcntw30[2], tcntd30[2], tcntl30[2]]
        values3 = [tcntw30[3], tcntd30[3], tcntl30[3]]
        values4 = [tcntw30[4], tcntd30[4], tcntl30[4]]
        values5 = [tcntw30[5], tcntd30[5], tcntl30[5]]
        values6 = [tcntw30[6], tcntd30[6], tcntl30[6]]
        values7 = [tcntw30[7], tcntd30[7], tcntl30[7]]
        values8 = [tcntw30[8], tcntd30[8], tcntl30[8]]
        values9 = [tcntw30[9], tcntd30[9], tcntl30[9]]
        values10 = [tcntw30[10], tcntd30[10], tcntl30[10]]
        values11 = [tcntw30[11], tcntd30[11], tcntl30[11]]
        values12 = [tcntw30[12], tcntd30[12], tcntl30[12]]
        values13 = [tcntw30[13], tcntd30[13], tcntl30[13]]

        fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
        fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
        fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
        fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
        fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
        fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
        fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
        fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
        fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
        fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
        fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
        fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
        fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
        fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
           = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
        with tab1:
            try:
                st.plotly_chart(fig0)
            except:
                st.plotly_chart(fig0, theme=None)
        with tab2:
            try:
                st.plotly_chart(fig1)
            except:
                st.plotly_chart(fig1, theme=None)
        with tab3:
            try:
                st.plotly_chart(fig2)
            except:
                st.plotly_chart(fig2, theme=None)
        with tab4:
            try:
                st.plotly_chart(fig3)
            except:
                st.plotly_chart(fig3, theme=None)
        with tab5:
            try:
                st.plotly_chart(fig4)
            except:
                st.plotly_chart(fig4, theme=None)
        with tab6:
            try:
                st.plotly_chart(fig5)
            except:
                st.plotly_chart(fig5, theme=None)
        with tab7:
            try:
                st.plotly_chart(fig6)
            except:
                st.plotly_chart(fig6, theme=None)
        with tab8:
            try:
                st.plotly_chart(fig7)
            except:
                st.plotly_chart(fig7, theme=None)
        with tab9:
            try:
                st.plotly_chart(fig8)
            except:
                st.plotly_chart(fig8, theme=None)
        with tab10:
            try:
                st.plotly_chart(fig9)
            except:
                st.plotly_chart(fig9, theme=None)
        with tab11:
            try:
                st.plotly_chart(fig10)
            except:
                st.plotly_chart(fig10, theme=None)
        with tab12:
            try:
                st.plotly_chart(fig11)
            except:
                st.plotly_chart(fig11, theme=None)
        with tab13:
            try:
                st.plotly_chart(fig12)
            except:
                st.plotly_chart(fig12, theme=None)
        with tab14:
            try:
                st.plotly_chart(fig13)
            except:
                st.plotly_chart(fig13, theme=None)

        # st.markdown(":basketball: :violet[**최근 10회차 결과**]")

        # rede10_def(result30,degree30,'k','2')

def rede10_def(result30,degree30,g1,g2): 
    resultn1 = result30[:10]
    degreen1 = degree30[:10]
    resultn2 = result30[30:40]
    degreen2 = degree30[30:40]
    resultn3 = result30[60:70]
    degreen3 = degree30[60:70]
    resultn4 = result30[90:100]
    degreen4 = degree30[90:100]
    resultn5 = result30[120:130]
    degreen5 = degree30[120:130]
    resultn6 = result30[150:160]
    degreen6 = degree30[150:160]
    resultn7 = result30[180:190]
    degreen7 = degree30[180:190]
    resultn8 = result30[210:220]
    degreen8 = degree30[210:220]
    resultn9 = result30[240:250]
    degreen9 = degree30[240:250]
    resultn10 = result30[270:280]
    degreen10 = degree30[270:280]
    resultn11 = result30[300:310]
    degreen11 = degree30[300:310]
    resultn12 = result30[330:340]
    degreen12 = degree30[330:340]
    resultn13 = result30[360:370]
    degreen13 = degree30[360:370]
    resultn14 = result30[390:400]
    degreen14 = degree30[390:400]

    df1 = pd.DataFrame(data=np.array([resultn1,degreen1]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"])
    df2 = pd.DataFrame(data=np.array([resultn2,degreen2]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 
    df3 = pd.DataFrame(data=np.array([resultn3,degreen3]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"])
    df4 = pd.DataFrame(data=np.array([resultn4,degreen4]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 
    df5 = pd.DataFrame(data=np.array([resultn5,degreen5]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"])
    df6 = pd.DataFrame(data=np.array([resultn6,degreen6]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 
    df7 = pd.DataFrame(data=np.array([resultn7,degreen7]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"])
    df8 = pd.DataFrame(data=np.array([resultn8,degreen8]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 
    df9 = pd.DataFrame(data=np.array([resultn9,degreen9]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"])
    df10 = pd.DataFrame(data=np.array([resultn10,degreen10]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 
    df11 = pd.DataFrame(data=np.array([resultn11,degreen11]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 
    df12 = pd.DataFrame(data=np.array([resultn12,degreen12]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 
    df13 = pd.DataFrame(data=np.array([resultn13,degreen13]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 
    df14 = pd.DataFrame(data=np.array([resultn14,degreen14]), 
            index= ["결과","회차"], 
            columns=["1","2","3","4","5","6","7","8","9","10"]) 

    if g2 == '1':
        cw1 = resultn1.count("승")
        cl1 = resultn1.count("패")
        cw2 = resultn2.count("승")
        cl2 = resultn2.count("패")
        cw3 = resultn3.count("승")
        cl3 = resultn3.count("패")
        cw4 = resultn4.count("승")
        cl4 = resultn4.count("패")
        cw5 = resultn5.count("승")
        cl5 = resultn5.count("패")
        cw6 = resultn6.count("승")
        cl6 = resultn6.count("패")
        cw7 = resultn7.count("승")
        cl7 = resultn7.count("패")
        cw8 = resultn8.count("승")
        cl8 = resultn8.count("패")
        cw9 = resultn9.count("승")
        cl9 = resultn9.count("패")
        cw10 = resultn10.count("승")
        cl10 = resultn10.count("패")
        cw11 = resultn11.count("승")
        cl11 = resultn11.count("패")
        cw12 = resultn12.count("승")
        cl12 = resultn12.count("패")
        cw13 = resultn13.count("승")
        cl13 = resultn13.count("패")
        cw14 = resultn14.count("승")
        cl14 = resultn14.count("패")

        if g1 == 's':
            cd1 = resultn1.count("무")
            cd2 = resultn2.count("무")
            cd3 = resultn3.count("무")
            cd4 = resultn4.count("무")
            cd5 = resultn5.count("무")
            cd6 = resultn6.count("무")
            cd7 = resultn7.count("무")
            cd8 = resultn8.count("무")
            cd9 = resultn9.count("무")
            cd10 = resultn10.count("무")
            cd11 = resultn11.count("무")
            cd12 = resultn12.count("무")
            cd13 = resultn13.count("무")
            cd14 = resultn14.count("무")
        elif g1 == 'b':
            cd1 = resultn1.count("①")
            cd2 = resultn2.count("①")
            cd3 = resultn3.count("①")
            cd4 = resultn4.count("①")
            cd5 = resultn5.count("①")
            cd6 = resultn6.count("①")
            cd7 = resultn7.count("①") 
            cd8 = resultn8.count("①")
            cd9 = resultn9.count("①")
            cd10 = resultn10.count("①")
            cd11 = resultn11.count("①")
            cd12 = resultn12.count("①")
            cd13 = resultn13.count("①")
            cd14 = resultn14.count("①")
        elif g1 == 'k':
            cd1 = resultn1.count("⑤")
            cd2 = resultn2.count("⑤")
            cd3 = resultn3.count("⑤")
            cd4 = resultn4.count("⑤")
            cd5 = resultn5.count("⑤")
            cd6 = resultn6.count("⑤")
            cd7 = resultn7.count("⑤")
            cd8 = resultn8.count("⑤")
            cd9 = resultn9.count("⑤")
            cd10 = resultn10.count("⑤")
            cd11 = resultn11.count("⑤")
            cd12 = resultn12.count("⑤")
            cd13 = resultn13.count("⑤")
            cd14 = resultn14.count("⑤")

    elif g2 == '2':
        cw1 = resultn1.count("고")
        cl1 = resultn1.count("저")
        cw2 = resultn2.count("고")
        cl2 = resultn2.count("저")
        cw3 = resultn3.count("고")
        cl3 = resultn3.count("저")
        cw4 = resultn4.count("고")
        cl4 = resultn4.count("저")
        cw5 = resultn5.count("고")
        cl5 = resultn5.count("저")
        cw6 = resultn6.count("고")
        cl6 = resultn6.count("저")
        cw7 = resultn7.count("고")
        cl7 = resultn7.count("저")
        cw8 = resultn8.count("고")
        cl8 = resultn8.count("저")
        cw9 = resultn9.count("고")
        cl9 = resultn9.count("저")
        cw10 = resultn10.count("고")
        cl10 = resultn10.count("저")
        cw11 = resultn11.count("고")
        cl11 = resultn11.count("저")
        cw12 = resultn12.count("고")
        cl12 = resultn12.count("저")
        cw13 = resultn13.count("고")
        cl13 = resultn13.count("저")
        cw14 = resultn14.count("고")
        cl14 = resultn14.count("저")
        cd1 = resultn1.count("중")
        cd2 = resultn2.count("중")
        cd3 = resultn3.count("중")
        cd4 = resultn4.count("중")
        cd5 = resultn5.count("중")
        cd6 = resultn6.count("중")
        cd7 = resultn7.count("중")
        cd8 = resultn8.count("중")
        cd9 = resultn9.count("중")
        cd10 = resultn10.count("중")
        cd11 = resultn11.count("중")
        cd12 = resultn12.count("중")
        cd13 = resultn13.count("중")
        cd14 = resultn14.count("중")      
    
    if g2 == '1':    
        colors = ['#FFA07A', '#F0E68C', '#87CEFA'] 
        if g1 == 's': 
            labels = ['승','무','패']
        elif g1 == 'b': 
            labels = ['승','①','패']
        elif g1 == 'k': 
            labels = ['승','⑤','패']
    elif g2 == '2':
        colors = ['#2F4F4F', '#696969', '#C0C0C0']
        labels = ['고','중','저']

    values0 = [cw1, cd1, cl1]
    values1 = [cw2, cd2, cl2]
    values2 = [cw3, cd3, cl3]
    values3 = [cw4, cd4, cl4]
    values4 = [cw5, cd5, cl5]
    values5 = [cw6, cd6, cl6]
    values6 = [cw7, cd7, cl7]
    values7 = [cw8, cd8, cl8]
    values8 = [cw9, cd9, cl9]
    values9 = [cw10, cd10, cl10]
    values10 = [cw11, cd11, cl11]
    values11 = [cw12, cd12, cl12]
    values12 = [cw13, cd13, cl13]
    values13 = [cw14, cd14, cl14]

    fig0 = go.Figure(data=[go.Pie(labels=labels, values=values0)])
    fig0.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values1)])
    fig1.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values2)])
    fig2.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig3 = go.Figure(data=[go.Pie(labels=labels, values=values3)])
    fig3.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig4 = go.Figure(data=[go.Pie(labels=labels, values=values4)])
    fig4.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig5 = go.Figure(data=[go.Pie(labels=labels, values=values5)])
    fig5.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig6 = go.Figure(data=[go.Pie(labels=labels, values=values6)])
    fig6.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig7 = go.Figure(data=[go.Pie(labels=labels, values=values7)])
    fig7.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig8 = go.Figure(data=[go.Pie(labels=labels, values=values8)])
    fig8.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig9 = go.Figure(data=[go.Pie(labels=labels, values=values9)])
    fig9.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig10 = go.Figure(data=[go.Pie(labels=labels, values=values10)])
    fig10.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig11 = go.Figure(data=[go.Pie(labels=labels, values=values11)])
    fig11.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig12 = go.Figure(data=[go.Pie(labels=labels, values=values12)])
    fig12.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))
    fig13 = go.Figure(data=[go.Pie(labels=labels, values=values13)])
    fig13.update_traces(textfont_size=20,marker=dict(colors=colors, line=dict(color='#FFFFFF', width=3)))

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 \
        = st.tabs(["1경기","2경기","3경기","4경기","5경기","6경기","7경기","8경기","9경기","10경기","11경기","12경기","13경기","14경기"])
    with tab1:
        st.dataframe(df1)
        st.plotly_chart(fig0, theme="streamlit")
    with tab2:
        st.dataframe(df2)
        st.plotly_chart(fig1, theme="streamlit")
    with tab3:
        st.dataframe(df3)
        st.plotly_chart(fig2, theme="streamlit")
    with tab4:
        st.dataframe(df4)
        st.plotly_chart(fig3, theme="streamlit")
    with tab5:
        st.dataframe(df5)
        st.plotly_chart(fig4, theme="streamlit")
    with tab6:
        st.dataframe(df6)
        st.plotly_chart(fig5, theme="streamlit")
    with tab7:
        st.dataframe(df7)
        st.plotly_chart(fig6, theme="streamlit")
    with tab8:
        st.dataframe(df8)
        st.plotly_chart(fig7, theme="streamlit")
    with tab9:
        st.dataframe(df9)
        st.plotly_chart(fig8, theme="streamlit")
    with tab10:
        st.dataframe(df10)
        st.plotly_chart(fig9, theme="streamlit")
    with tab11:
        st.dataframe(df11)
        st.plotly_chart(fig10, theme="streamlit")
    with tab12:
        st.dataframe(df12)
        st.plotly_chart(fig11, theme="streamlit")
    with tab13:
        st.dataframe(df13)
        st.plotly_chart(fig12, theme="streamlit")
    with tab14:
        st.dataframe(df14)
        st.plotly_chart(fig13, theme="streamlit")
