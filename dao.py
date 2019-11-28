import pymysql


class Video:
    def __init__(self, id, id_video, id_channel, view_count, like_count, comment_count, date_get, dislike_count):
        self.id_video = id_video  
        self.id_channel = id_channel  
        self.view_count = view_count  
        self.like_count = like_count  
        self.comment_count = comment_count  
        self.date_get = date_get  
        self.dislike_count = dislike_count

def insertChannel(id_channel, name, subscriber_count, video_count, views_count, date_get):
    try:
        con = pymysql.connect(host="ribo.live", db="cover_analitycs", user="ribolive", password="6428")

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
        con = pymysql.connect(host="ribo.live", db="cover_analitycs", user="ribolive", password="6428")
        
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
        con = pymysql.connect(host="159.203.102.25", db="cover_analitycs", user="ribolive", password="6428")
        
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
        print("Error")
        return None

def getChannels():
    try:
        con = pymysql.connect(host="159.203.102.25", db="cover_analitycs", user="ribolive", password="6428")
        
        cursor = con.cursor()
        sql =  "SELECT * FROM chennel"

        cursor.execute(sql)
        channels = cursor.fetchall()
        con.commit()
        con.close()
        return channels

    except NameError:
        print("Error")
        return channels