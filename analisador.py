import dao
import datetime
from domain import Video
import pickle

def getVideoByChannelAndPeriod(videos):
    videosDict = {}
    today = datetime.datetime.now()
    lestYear = datetime.datetime.now() - datetime.timedelta(days=365)

    firstDay = datetime.date(today.year, today.month, today.day)
    endDay = datetime.date(lestYear.year, lestYear.month, lestYear.day)

    for video in videos:
        videoChannel = video.id_channel
        period = datetime.date(video.date_get.year, video.date_get.month, video.date_get.day)
        
        if(period < firstDay):
            firstDay = period
        if(period > endDay):
            endDay = period

        videoID = video.id_video
        
        if (not videoChannel in videosDict):
            videosDict[videoChannel] = {}
        if (not videoID in videosDict[videoChannel]):
            videosDict[videoChannel][videoID] = {}
        if (not period in videosDict[videoChannel][videoID]):
            videosDict[videoChannel][videoID][period] = []

        videosDict[videoChannel][videoID][period].append(video)

    # Return Dicionario de videos, Horizonte:[primeiro dia, ultimo dia]
    return videosDict, {"start": firstDay, "end": endDay}

def transformVideosByAvarage(videos):
    for channelKey, videosByChannel in videos.items():
        for videoID, values in videosByChannel.items():
            for period, sVideos in values.items():
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
                    media = averages[key] / amountVideosGet
                    averages[key] = media

                videos[channelKey][videoID][period] = Video(None, videoID, id_channel, averages["qViews"], averages["qLike"], averages["qComment"], period, averages["qDislike"])
    return videos

#def deleteIrrelevantInformation(videos):

def getVideosByDiferenceBetweenThem(videos,horizon):
    for channelKey, videosByChannel in videos.items():
        for videoID, values in videosByChannel.items():
            differenceBetweenDays = {}
            iterateDate = horizon["start"] # inicializando iterador no start
            endTime = horizon["end"]
            notInitialValue = True
            
            while (iterateDate <= endTime):
                currentDay = iterateDate
                lastDataTime = currentDay - datetime.timedelta(days=1)
                if(currentDay in values):
                    if(notInitialValue):
                        notInitialValue = False
                    else:
                        while (not lastDataTime in values):
                            lastDataTime -= datetime.timedelta(days=1)
                        diferenceComment = (values[currentDay].comment_count - values[lastDataTime].comment_count)
                        diferenceDislike = (values[currentDay].dislike_count - values[lastDataTime].dislike_count)
                        diferenceLike = (values[currentDay].like_count - values[lastDataTime].like_count)
                        diferenceViews = (values[currentDay].view_count - values[lastDataTime].view_count)


                        differenceBetweenDays[currentDay] = Video(None, values[currentDay].id_video, values[currentDay].id_channel, diferenceViews, diferenceLike, diferenceComment, currentDay, diferenceDislike)

                    # proxima iteração do while
                iterateDate += datet
                ime.timedelta(days=1)  
            videos[channelKey][videoID] = differenceBetweenDays
    return videos


def preProccess(videos):
    videos, horizon = getVideoByChannelAndPeriod(videos)

    # coletando media de valores por dia de coleta (para cada video)
    videos = transformVideosByAvarage(videos)

    ####
    videos = getVideosByDiferenceBetweenThem(videos, horizon)
    
    sChannels = {}
    for value in channels:
        key = 0
        keySubscribe = 1
        if not key in sChannels:
            sChannels[value[key]] = value[keySubscribe]
        else:
            if sChannels[value[key]] < value[keySubscribe]:
                sChannels[value[key]] = value[keySubscribe]
    
    return videos, sChannels



if __name__ == "__main__":
    try:
        videos = dao.getVideos()
        channels = dao.getChannels()
        
        videos, channels = preProccess(videos, channels)

        pickle.dump(videos, open("rawData.pkl","wb"))
        pickle.dump(channels, open("channelSubscribe.pkl","wb"))

        print("aqui")
    except NameError:
        print("Error in Main Function")
