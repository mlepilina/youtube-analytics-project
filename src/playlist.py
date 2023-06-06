import datetime
import os
from googleapiclient.discovery import build
import isodate


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API-KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class PlayList:
    """Экземпляр инициализируется id плэйлиста. Дальше все данные будут подтягиваться по API."""

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id

        playlist = youtube.playlists().list(part='snippet',
                                            id=self.playlist_id,
                                            fields='items(id,snippet(title,channelId,channelTitle))'
                                            ).execute()
        self.title = playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

        # получение данных по видеороликам в плейлисте
        self.playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()

        # получение всех id видеороликов из плейлиста
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]

        # получение статистики видео по id
        self.video_response = youtube.videos().list(part='contentDetails',
                                                    id=','.join(self.video_ids)
                                                    ).execute()

    @property
    def total_duration(self):
        """Возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста"""

        total_duration = datetime.timedelta(hours=0, minutes=0, seconds=0)
        total_seconds = 0
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
            total_seconds += duration.total_seconds()

        return total_duration

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""

        most_likes = 0
        video_likes_dict = {}
        for v_id in self.video_ids:
            video_info = youtube.videos().list(id=v_id, part='snippet,statistics').execute()
            like_count = int(video_info['items'][0]['statistics']['likeCount'])
            video_likes_dict[like_count] = v_id

            if like_count > most_likes:
                most_likes = like_count

        best_video_id = video_likes_dict[most_likes]
        return f"https://youtu.be/{best_video_id}"
