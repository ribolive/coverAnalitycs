import json
import os
import google_auth_oauthlib.flow
from googleapiclient.discovery import *
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/youtubepartner"]

DEVELOPER_KEY = "AIzaSyCtBEekkOLo_xmlQZjo2GWhO7tqBt-E1Og"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search_list(channelID, max_results=10):
  # Call the search.list method to retrieve results matching the specified
  # query term.
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
    search_response = youtube.search().list(
        #q=q,
        #procurar como incluir busca por id de canal
        part='id,snippet',
        channelId=channelID,
        maxResults=max_results,
        order='date'
      ).execute()

    return search_response

def youtube_search_video(channelID, max_results=5):
    max_results = max_results
    order = "viewCount"
    token = None
    location = None
    location_radius = None
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
    #Return list of matching records up to max_search
    search_result = youtube_search_list(channelID, max_results)

    videos_list = []
    for r in search_result.get("items", []):

        if r["id"]["kind"] == 'youtube#video':
            temp_dict_ = {}
            temp_dict_["channelId"] = channelID
            
            #Available from initial search
            temp_dict_['title'] = r['snippet']['title']  
            temp_dict_['vidId'] = r['id']['videoId']  

            #Secondary call to find statistics results for individual video
            response = youtube.videos().list(
                part='statistics, snippet', 
                id=r['id']['videoId']
                    ).execute()  
            response_statistics = response['items'][0]['statistics']
            response_snippet = response['items'][0]['snippet']


            snippet_list = ['publishedAt','channelId', 'description', 
                            'channelTitle', 'tags', 'categoryId', 
                            'liveBroadcastContent', 'defaultLanguage', ]
            for val in snippet_list:
                try:
                    temp_dict_[val] = response_snippet[val]
                except:
                    #Not stored if not present
                    temp_dict_[val] = 'xxNoneFoundxx'    

            stats_list = ['favoriteCount', 'viewCount', 'likeCount', 
                          'dislikeCount', 'commentCount']
            for val in stats_list:
                try:
                    temp_dict_[val] = response_statistics[val]
                except:
                    #Not stored if not present
                    temp_dict_[val] = 'xxNoneFoundxx'

            #add back to main list
            videos_list.append(temp_dict_)

    return videos_list

def youtube_search_channel(channelID):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
    channelStatistics = youtube.channels().list(
                    part='id, snippet, statistics', id=channelID).execute()
    channelStatistics = channelStatistics["items"][0] 
    
    channel = {}
    channel["id"] = channelID
    channel["title"] = channelStatistics["snippet"]["title"]
    channel["channelViews"] = channelStatistics["statistics"]["viewCount"]
    channel["channelSubscriber"] = channelStatistics["statistics"]["subscriberCount"]
    channel["channelVideoCount"] = channelStatistics["statistics"]["videoCount"]

    return channel