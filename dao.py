import pymysql
from domain import Video

HOST = "ribo.live"
DB = "cover_analitycs"
USER =  "ribolive"
PASSWORD = "6428"


def insertChannel(id_channel, name, subscriber_count, video_count, views_count, date_get):
    try:
        con = pymysql.connect(host = HOST, db = DB, user = USER, password = PASSWORD)

        cursor = con.cursor()
        sql =  "INSERT INTO channel "
        sql += "(id_channel, name, subscriber_count, video_count, views_count, date_get) "
        sql += "VALUES ('{0}', '{1}', {2}, {3}, {4}, '{5}');"
        sql = sql.format(id_channel, name, subscriber_count, video_count, views_count, date_get)

        cursor.execute(sql)
        con.commit()
        con.close()
    except NameError:
        print("Error from insertChannel: ", NameError)

def insertVideo(id_video, id_channel, view_count, like_count, comment_count, date_get, dislike_count):
    try:
        con = pymysql.connect(host = HOST, db = DB, user = USER, password = PASSWORD)
        
        cursor = con.cursor()
        sql =  "INSERT INTO videos "
        sql += "(id_video, id_channel, view_count, like_count, comment_count, date_get, dislike_count) "
        sql += "VALUES ('{0}', '{1}', {2}, {3}, {4}, '{5}', {6});"
        sql = sql.format(id_video, id_channel, view_count, like_count, comment_count, date_get, dislike_count)

        cursor.execute(sql)
        con.commit()
        con.close()
    except NameError:
        print("Error from insertVideo")

def getVideos():
    try:
        # con = pymysql.connect(host="localhost", db=DB, user="root", password = PASSWORD)
        con = pymysql.connect(host = HOST, db=DB, user= USER, password = PASSWORD)
        
        cursor = con.cursor()
        sql =  "SELECT * FROM videos"

        cursor.execute(sql)
        videos = cursor.fetchall()
        outVideos = []
        for video in videos:
            outVideos.append(Video(*video))
        con.commit()
        con.close()
        return outVideos

    except NameError:
        print("Error in GetVideos")
        return None

def getChannels():
    try:
        con = pymysql.connect(host = HOST, db=DB, user= USER, password = PASSWORD)
        
        cursor = con.cursor()
        sql =  "SELECT * FROM channel"

        cursor.execute(sql)
        channels = cursor.fetchall()
        con.commit()
        con.close()
        return channels

    except NameError:
        print("Error in GetVChannels")
        return channels