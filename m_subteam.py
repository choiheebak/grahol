#
# 제목 : 팀명을 가지고 팀구분, 순위팀명, TTS팀명, 조회팀명 
#         b : baseball      
#         k : basketball
#         s : soccer
#
import pandas as pd
import sqlite3

def inq_teamn(jongmok, team):
   
    # # print(jongmok, team)
    
    if jongmok == "s": 
        con = sqlite3.connect("c:/Users/iendo/soccer.db")  
        cur = con.cursor()
        sql = "SELECT 팀구분, 팀구분1, 순위팀명, TTS팀명, 조회팀명, 순위팀명1 FROM 팀명 where 팀명 = ?"    
        data = (team,)
        cur.execute(sql,data)    
    elif jongmok == "b": 
        con = sqlite3.connect("c:/Users/iendo/baseball.db")   
        cur = con.cursor()
        sql = "SELECT 팀구분, 팀구분, 순위팀명, TTS팀명, 조회팀명, 팀명1 FROM 팀명 where 팀명 = ?"    
        data = (team,)
        cur.execute(sql,data)    
    elif jongmok == "k": 
        con = sqlite3.connect("c:/Users/iendo/basketball.db") 
        cur = con.cursor()
        sql = "SELECT 팀구분, 팀구분, 순위팀명, TTS팀명, 조회팀명, 팀명1 FROM 팀명 where 팀명 = ?"    
        data = (team,)
        cur.execute(sql,data)     
    
    league_gubun = ""
    league1_gubun = ""
    seq_team = ""
    tts_team = ""
    inq_team = ""
    seq1_team = ""
    row = cur.fetchone()
    league_gubun = row[0]
    league1_gubun = row[1]
    seq_team = row[2]
    tts_team = row[3]
    inq_team = row[4]
    seq1_team = row[5]

    con.close()

    return league_gubun, league1_gubun, seq_team, tts_team, inq_team, seq1_team