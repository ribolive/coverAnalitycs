import pymysql

def insertChannel(id_channel, name, subscriber_count, video_count, views_count, date_get):
    try:
        con = pymysql.connect(host='localhost', db="cover_analitycs", user="ribolive", password="6428")

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
        con = pymysql.connect(db="cover_analitycs", user="root", passwd="6428")

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
