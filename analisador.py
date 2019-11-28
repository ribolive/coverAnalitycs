import dao
import datetime


def getVideoByPeriod(videos):
    videosDict = {}

    for video in videos:
        period = datetime.date(video.date_get.year, video.date_get.month, video.date_get.day)
        videoID = video.id_video
        
        if (not period in videosDict):
            videosDict[period] = {}
        if (not videoID in videosDict[period]):
            videosDict[period][videoID] = []

        videosDict[period][videoID].append(video)
    print("aqui")  
    


if __name__ == "__main__":
    try:
        videos = dao.getVideos()
        getVideoByPeriod(videos)
    except NameError:
        print("error ")
