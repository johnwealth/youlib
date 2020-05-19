from celery import shared_task
import requests
import json
from isodate import parse_duration
from django.conf import settings



@shared_task
def videos():
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'
        params = {
                'part' : 'snippet',
                'forUsername' : 'khanacademy',
                'key' : settings.YOUTUBE_API_KEY,
                'type': 'video'
        }
        r = requests.get(search_url, params=params)
        results = r.json()['items']
        videos = []
        for result in results:
                video_data = {
                        'title': result['snippet']['title'],
                        'id' : result['id'],
                  #     'duration': parse_duration(result['contentDetails']['duration']).total_seconds()//60,
                        'thumbnail': result['snippet']['thumbnails']['high']['url']
                }

        videos.append(video_data)
        return videos
@shared_task       
def channel_statistic():
        channel_url='https://www.googleapis.com/youtube/v3/channels'
        params = {
                'part' : 'statistics',
                'forUsername' : 'khanacademy',
                'key' : settings.YOUTUBE_API_KEY,
        }
        r = requests.get(channel_url, params=params)
        results = json.loads(r.text)
        
        try:
                results = results['items'][0]['statistics']
        except KeyError:
                results = None
        channel_statistics = results
        return results

