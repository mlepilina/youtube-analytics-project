import os
import json
from googleapiclient.discovery import build


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API-KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriber_count = int(channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        """Возвращает название и ссылку на канал"""
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """Выполняет сложение количества подписчиков класса с
        количеством подписчиков другого класса"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """Выполняет вычитание из количества подписчиков класса
        количество подписчиков другого класса"""
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        """Выполняет операцию сравнения подписчиков «меньше»"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """Выполняет операцию сравнения подписчиков «меньше или равно»"""
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        """Выполняет операцию сравнения подписчиков «больше»"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """Выполняет операцию сравнения подписчиков «больше или равно»"""
        return self.subscriber_count >= other.subscriber_count

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.__channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        '''Возвращает объект для работы с YouTube API'''
        return youtube

    def to_json(self, file_name):
        '''Создает файл в формате .json со значениями атрибутов экземпляра класса Channel'''
        channel_dict = {
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count,
        }

        with open(file_name, 'wt', encoding='utf-8') as new_json_file:
            json.dump(channel_dict, new_json_file, ensure_ascii=False)
