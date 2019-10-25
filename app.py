from youtubeAPI import *

def video_parser(video): 
    relevantInfo = ["vidId", "viewCount", "likeCount", "dislikeCount", "commentCount", "channelId"]
    
    videoOut = {}
    
    for key in relevantInfo:
        videoOut[key] = video[key]
    videoOut["time"] = datetime.now()
    return videoOut

if __name__ == "__main__":
    channelID = "UCgc00bfF_PvO_2AvqJZHXFg"

    channel = youtube_search_channel(channelID)
    videos = youtube_search_video(channel["id"], 5)

    new_videos = []
    for video in videos:
        new_videos.append(video_parser(video))
        
    print(channel)