import os
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API-KEY')

# создание специального объекта для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:

    def __init__(self, video_id):
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.__video_id = video_id

        try:
            video = youtube.videos().list(id=self.__video_id, part='snippet,statistics').execute()
            self.title = video['items'][0]['snippet']['title']
            self.url = f'https://www.youtube.com/watch?v={self.__video_id}'
            self.view_count = int(video['items'][0]['statistics']['viewCount'])
            self.like_count = int(video['items'][0]['statistics']['likeCount'])

        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        """Возвращает название видео"""
        return f'{self.title}'

    @property
    def video_id(self):
        return self.__video_id


class PLVideo(Video):

    def __init__(self, __video_id, playlist_id):
        """Экземпляр инициализируется id видео и id плэйлиста."""
        super().__init__(__video_id)
        self.playlist_id = playlist_id
