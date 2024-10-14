#
# 제목 : basketball 경기별 상대전적 sub(NBA,KBL _일정결과) (subbkgrar)
#
import pandas as pd
import sqlite3

def wdl_cnt(hteam, game):
   
    gamesu = int(game)
    con = sqlite3.connect("c:/Users/iendo/basketball.db")  
  
    cur = con.cursor()
    sql = "SELECT 팀구분, 조회팀명 FROM 팀명 where 팀명 = ?"    
    data = (hteam,)
    cur.execute(sql,data)

    row = cur.fetchone()
    league_gubun = row[0]
    hteamc = row[1]

    # 리그 구분
    # league_gubun =  subbkwdle.team_gubun(hteam)

    # hteamc = subbkwdlg.team_change(hteam)
    hteamv = hteamc.replace("%","")
    hteamv.strip()

    # print(hteam, hteamc, hteamv, league_gubun, gamesu)
    
    if league_gubun == 'N': #NBA
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수 FROM NBA_일정결과 WHERE 홈팀 like ? OR 원정팀 like ? order by 년도 , 월 , 일자 "  

    elif league_gubun == 'K': #KBL
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수 FROM KBL_일정결과 WHERE 홈팀 like ? OR 원정팀 like ? order by 년도 , 월 , 일자 " 

    data = [hteamc, hteamc]
    cur.execute(sql,data)

    ilja_list = []
    home_list = []
    home_jumsu = []
    away_list = []
    away_jumsu = []
    rows = cur.fetchall()
    for row in rows:                 
        p2 = row[2] 
        if p2 == "":
            pass
        else:        
            p0 = row[0] 
            ilja_list.append(p0)
            p1 = row[1] 
            home_list.append(p1)
            home_jumsu.append(p2)
            p3 = row[3] 
            away_list.append(p3)        
            p4 = row[4] 
            away_jumsu.append(p4)  
    
    # # print(ilja_list, len(ilja_list))  

    hfrom = len(ilja_list) - gamesu
    hto = len(ilja_list)

    # # print(len(ilja_list), len(rows), gamesu, hfrom, hto) 

    hil_list = []
    hteam_list = []
    hateam_list = []
    hjumsu1_list = []
    hjumsu2_list = []
    hwdl_list = []
    for j in range(hfrom, hto): 
        hil = ilja_list[j]

        if hteamv in home_list[j]:
            # # print("home_list", home_list[j], away_list[j], hteamv)
            hte = home_list[j]
            hj1 = home_jumsu[j]
            hj2 = away_jumsu[j] 
            ate = away_list[j]
        else:
            # # print("away_list", away_list[j], home_list[j], ateamv)
            hte = away_list[j]
            hj1 = away_jumsu[j]
            hj2 = home_jumsu[j]
            ate = home_list[j]

        if hj1 > hj2:
            if hj1 - hj2 > 5:
               hwdl = 3
            else:
               hwdl = 2
        elif hj1 < hj2:
            if hj2 - hj1 > 5:
               hwdl = 0
            else:
               hwdl = 1        
            
        hil_list.append(hil)
        hteam_list.append(hte)
        hateam_list.append(ate)
        hjumsu1_list.append(hj1) 
        hjumsu2_list.append(hj2) 
        hwdl_list.append(hwdl)    
            
    con.close()

    return hil_list, hteam_list, hateam_list, hjumsu1_list, hjumsu2_list, hwdl_list
