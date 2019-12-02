import dao
import datetime
from domain import Video

def getVideoByChannelAndPeriod(videos):
    videosDict = {}

    for video in videos:
        videoChannel = video.id_channel
        period = datetime.date(video.date_get.year, video.date_get.month, video.date_get.day)
        videoID = video.id_video
        
        if (not videoChannel in videosDict):
            videosDict[videoChannel] = {}
        if (not period in videosDict[videoChannel]):
            videosDict[videoChannel][period] = {}
        if (not videoID in videosDict[videoChannel][period]):
            videosDict[videoChannel][period][videoID] = []

        videosDict[videoChannel][period][videoID].append(video)
    return videosDict  

def transformVideosByAvarage(videos):
    for channelKey, videosByChannel in videos.items():
        for period, values in videosByChannel.items():
            for videoID, sVideos in values.items():
                averages = {
                    "qComment": 0,
                    "qDislike": 0,
                    "qLike": 0,
                    "qViews": 0
                            }
                amountVideosGet = len(sVideos)
                if not amountVideosGet > 0:
                    continue
                id_channel = sVideos[0].id_channel
                
                for video in sVideos:
                    averages["qComment"] += video.comment_count
                    averages["qDislike"] += video.dislike_count
                    averages["qLike"] += video.like_count
                    averages["qViews"] += video.view_count

                # media dos dados capturados em um mesmo dia
                for key in averages:
                    averages[key] = averages[key] / amountVideosGet 

                videos[channelKey][period][videoID] = Video(None, videoID, id_channel, averages["qViews"], averages["qLike"], averages["qComment"], period, averages["qDislike"])
    return videos

#def deleteIrrelevantInformation(videos):


def preProccess(videos):
    videos = transformVideosByAvarage(videos)

    print("aqui")


if __name__ == "__main__":
    try:
        videos = dao.getVideos()
        videos = getVideoByChannelAndPeriod(videos)
        preProccess(videos)
    except NameError:
        print("Error in Main Function")
