#
# 제목 : baseball 경기별 경기별 리그 상대전적 sub(MLB,KBO_일정결과) (subbbgras)
#
import pandas as pd
import sqlite3

def wdl_cnt(hteam, ateam, game):
    
    gamesu = int(game)
    con = sqlite3.connect("c:/Users/iendo/baseball.db")    
    cur = con.cursor()  
    sql = "SELECT 팀구분, 조회팀명 FROM 팀명 where 팀명 = ?"    
    data = (hteam,)
    cur.execute(sql,data)

    row = cur.fetchone()
    league_gubun = row[0]
    hteamc = row[1]
  
    hteamv = hteamc.replace("%","")
    hteamv.strip()

    cur = con.cursor()
    sql = "SELECT 팀구분, 조회팀명 FROM 팀명 where 팀명 = ?"    
    data = (ateam,)
    cur.execute(sql,data)

    row = cur.fetchone()
    league_gubun = row[0]
    ateamc = row[1]

    ateamv = ateamc.replace("%","")
    ateamv.strip()

    # print(hteam, hteamc, hteamv, ateam, ateamc, ateamv, league_gubun, gamesu)

    if league_gubun == 'M': #NBA
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM MLB_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?   \
               UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM MLB_일정결과 WHERE 홈팀 like ? AND 원정팀 like ? order by 년도 , 월 , 일자 "  

    elif league_gubun == 'K': #KBL
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM KBO_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?    \
               UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM KBO_일정결과 WHERE 홈팀 like ? AND 원정팀 like ? order by 년도 , 월 , 일자 "      
    
    data = [hteamc, ateamc, ateamc, hteamc]
    cur.execute(sql, data)

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
            p5 = str(row[5])       
            p6 = p5[2:]       
            p0 = row[0][:5] 
            p0 = p0.replace("(","")
            ilja_list.append(p6+"."+p0)
            p1 = row[1] 
            home_list.append(p1)
            home_jumsu.append(p2)
            p3 = row[3] 
            away_list.append(p3)        
            p4 = row[4] 
            away_jumsu.append(p4)  
    
    # # print(ilja_list, len(ilja_list))  

    if gamesu >= len(ilja_list):
        hfrom = 0
    else:
        hfrom = len(ilja_list) - gamesu
    hto = len(ilja_list)

    # # print(len(ilja_list), len(rows), gamesu, hfrom, hto) 

    hil_list = []
    hteam_list = []
    ateam_list = []
    hjumsu1_list = []
    hjumsu2_list = []
    hwdl_list = []
    for j in range(hfrom, hto): 
        hil = str(ilja_list[j])

        hte = home_list[j]
        ate = away_list[j]
        hj1 = home_jumsu[j]
        hj2 = away_jumsu[j] 

        if hj1 > hj2:
            if hj1 - hj2 > 1:
               hwdl = 3
            else:
               hwdl = 2
        elif hj1 < hj2:
            if hj2 - hj1 > 1:
               hwdl = 0
            else:
               hwdl = 1 
        else:
            hwdl = 1.5
            
        hil_list.append(hil)
        hteam_list.append(hte)
        ateam_list.append(ate)
        hjumsu1_list.append(hj1) 
        hjumsu2_list.append(hj2) 
        hwdl_list.append(hwdl)    
            
    con.close()
    
    return hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list
