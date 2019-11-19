from youtubeAPI import *
from datetime import datetime
import time
from dao import *

def video_parser(video): 
    relevantInfo = ["vidId", "viewCount", "likeCount", "dislikeCount", "commentCount", "channelId"]
    
    videoOut = {}
    
    for key in relevantInfo:
        videoOut[key] = video[key]
    videoOut["time"] = datetime.now()
    return videoOut

def get_data():
    try:
        i = 0;
        while (True):
            i += 1
            channelList = [
                "UCgc00bfF_PvO_2AvqJZHXFg",
                "UCTOSI18KyJSZWouZM5kADvg",
                "UCtN63iegUVqBAxdYkZ-UslQ",
                "UCfjnEW3mVXfW0Wb602r1IrQ",
                "UCTKDB3h5zMdf_2siDHsd_yw",
                "UCxywry2DJ4iNXINFPqMaYxw",
                "UC2vPHIqjFdpPVMa2PGwJuYg",
                "UC_b5Ew_f185LSJ0jMNZ2CAw",
                "UCmnHY9Uw5pDgn3tvZOtarKw"
                ]

            for channelID in channelList:
                channel = youtube_search_channel(channelID)
                videos = youtube_search_video(channel["id"], 5)

                new_videos = []
                for video in videos:
                    new_videos.append(video_parser(video))
                
                channel["date_get"] = datetime.now()
                insertChannel(channel['id'], channel['title'], channel['channelSubscriber'], channel['channelVideoCount'], channel['channelViews'], channel["date_get"])
            
                mFile  = open("log.txt", "a") 
                mFile.write("Insert Channel: {0} ({1})\n".format(channel['title'], channel["date_get"]))
                mFile.close()

                for item in new_videos:
                    insertVideo(item["vidId"], item["channelId"], item["viewCount"], item["likeCount"], item["commentCount"], item["time"], item["dislikeCount"])
            print("- ", i, " -")

            mFile  = open("log.txt", "a") 
            mFile.write("----------  " + str(i) + "  ----------\n")
            mFile.close()

            time.sleep(3600)
    except NameError:
        mFile  = open("log.txt", "a") 
        mFile.write("----------  Get ERROR, Restart Count  ----------\n")
        mFile.close()
        time.sleep(3600)
        get_data()


if __name__ == "__main__":
    try:
        get_data()
    except NameError:
        mFile  = open("log.txt", "a") 
        mFile.write("----------  Get ERROR, Restart Count  ----------\n")
        mFile.close()
        time.sleep(3600)
        get_data()


