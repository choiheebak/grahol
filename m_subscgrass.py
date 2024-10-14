#
# 제목 : soccer 경기별 리그 상대전적 sub(EPL,LLG,SER,BDL,KL1,FLG _일정결과) (subscgrass)
#        전체 맞대결
import pandas as pd
import sqlite3

def wdl_cnt(hteam, ateam, league_gubun, game, gubun):
   
    # print(hteam, ateam, league_gubun, game, gubun)
    gamesu = int(game)
    con = sqlite3.connect("c:/Users/iendo/soccer.db")  
   
    cur = con.cursor()
    sql = "SELECT 조회팀명 FROM 팀명 where 팀명 = ?"    
    data = (hteam,)
    cur.execute(sql,data)

    row = cur.fetchone()
    hteamc = row[0]

    hteamv = hteamc.replace("%","")
    hteamv.strip()

    cur = con.cursor()
    sql = "SELECT 조회팀명 FROM 팀명 where 팀명 = ?"    
    data = (ateam,)
    cur.execute(sql,data)

    row = cur.fetchone()
    ateamc = row[0]
    
    ateamv = ateamc.replace("%","")
    ateamv.strip()

    # print(hteam, hteamc, hteamv, ateam, ateamc, ateamv, league_gubun, gamesu)
      
    cur = con.cursor()  
    if league_gubun == 'E': #EPL
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM EPL_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?    \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM EPL_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 "  
        # sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM EPL_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?   \
        #        UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM EFL_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  order by 년도 , 월 , 일자 "  

    elif league_gubun == 'G':  
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM EFL_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM EFL_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 
        # sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM EFL_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?     \
        #        UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM EPL_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'X':  
        # sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도 FROM EFL_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  order by 년도 , 월 , 일자 " 
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM UEC_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?     \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM UEC_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?     \
               UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM UEF_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?     \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM UEF_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?     \
               UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM UEO_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?     \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM UEO_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'L': #Laliga
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM LLG_일정결과 WHERE 홈팀 like ? AND 원정팀 like ? \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM LLG_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'S': #Serie
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM SER_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM SER_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'B': #Bundesleague
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM BDL_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM BDL_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'K': #Kleague1        
        if hteam == "수원삼성":        
            sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM KL1_일정결과 WHERE 홈팀 = ? AND 원정팀 like ?   \
                   UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM KL1_일정결과 WHERE 원정팀 = ? AND 홈팀 like ?  order by 년도 , 월 , 일자 "  
        else:
            sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM KL1_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
                   UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM KL1_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

        if ateam == "수원삼성":        
            sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM KL1_일정결과 WHERE 홈팀 like ? AND 원정팀 = ?  \
                   UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM KL1_일정결과 WHERE 원정팀 like ? AND 홈팀 = ?  order by 년도 , 월 , 일자 "  
        else:
            sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM KL1_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
                   UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM KL1_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'F': #f league1
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM FLG_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM FLG_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'J': #f league1
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM JL1_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM JL1_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'Q': #k league2
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM KL2_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM KL2_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'N': #eredivish
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM NED_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?   \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM NED_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'A': #uefa nations league     
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM UEN_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?     \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM UEN_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?     \
               UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?     \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM URO_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?     \
               UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM WCP_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?     \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM WCP_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?     \
               UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM WCP_일정예선 WHERE 홈팀 like ? AND 원정팀 like ?     \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM WCP_일정예선 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 
        # if hteam == "아일랜드":        
        #     sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 = ? AND 원정팀 like ?  \
        #            UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 = ? AND 원정팀 like ?  order by 년도 , 월 , 일자 "
        # else:
        #     sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
        #            UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  order by 년도 , 월 , 일자 " 
        
        # if ateam == "아일랜드":        
        #     sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 like ? AND 원정팀 = ?  \
        #            UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 like ? AND 원정팀 = ?  order by 년도 , 월 , 일자 "
        # else:
        #     sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
        #            UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM URO_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'M': #MLS league
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM MLS_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM MLS_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'C': #uefa champions league
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM UEC_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM UEC_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'U': #uefa champions league
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM UEF_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM UEF_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'W': #world cup
        if hteam == "인도":        
            sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM WCP_일정예선 WHERE 홈팀 = ? AND 원정팀 like ?  \
                UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM WCP_일정결과 WHERE 원정팀 = ? AND 홈팀 like ?  order by 년도 , 월 , 일자 "
        else: 
            sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM WCP_일정예선 WHERE 홈팀 like ? AND 원정팀 like ?  \
                UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM WCP_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 
        
        if ateam == "인도":        
            sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM WCP_일정예선 WHERE 홈팀 like ? AND 원정팀 = ?  \
                UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM WCP_일정결과 WHERE 원정팀 like ? AND 홈팀 = ?  order by 년도 , 월 , 일자 "
        else: 
            sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM WCP_일정예선 WHERE 홈팀 like ? AND 원정팀 like ?  \
                UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM WCP_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'O': #world cup
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM WWP_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?   \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM WWP_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'D': #JL2
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM JL2_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM JL2_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'R': #JL2
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM NOR_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM NOR_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    elif league_gubun == 'Y': #f league1
        sql = "SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM JL1_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM JL1_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  \
               UNION SELECT  일자, 홈팀, 홈팀점수, 원정팀, 원정팀점수, 년도, 월 FROM JL2_일정결과 WHERE 홈팀 like ? AND 원정팀 like ?  \
               UNION SELECT  일자, 원정팀, 원정팀점수, 홈팀, 홈팀점수, 년도, 월 FROM JL2_일정결과 WHERE 원정팀 like ? AND 홈팀 like ?  order by 년도 , 월 , 일자 " 

    # if league_gubun == 'E' or league_gubun == 'G': #EPL    
    #     data = [hteamc, ateamc, hteamc, ateamc]
    #     cur.execute(sql,data)
    if league_gubun == 'X': #EPL    
        data = [hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc]
        cur.execute(sql,data)
    elif league_gubun == 'W': #World Cup 
        data = [hteamc, ateamc, hteamc, ateamc]
        cur.execute(sql,data)
    elif league_gubun == 'A': #친선경기
        data = [hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc]
        cur.execute(sql,data)
    elif league_gubun == 'Y': #J리그컵
        data = [hteamc, ateamc, hteamc, ateamc, hteamc, ateamc, hteamc, ateamc]
        cur.execute(sql,data)
    else:
        data = [hteamc, ateamc, hteamc, ateamc]
        cur.execute(sql,data)

    # data = [hteamc, ateamc]
    # cur.execute(sql,data)

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
    # # print(home_list, len(home_list))  
    # # print(home_jumsu, len(home_jumsu))  

    if gamesu > len(ilja_list):
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
            hwdl = 3
        elif hj1 == hj2:
            hwdl = 1
        elif hj1 < hj2:
            hwdl = 0            
    
        hil_list.append(hil)
        hteam_list.append(hte) 
        ateam_list.append(ate) 
        hjumsu1_list.append(hj1) 
        hjumsu2_list.append(hj2) 
        hwdl_list.append(hwdl)      
    
    con.close()

    return hil_list, hteam_list, ateam_list, hjumsu1_list, hjumsu2_list, hwdl_list