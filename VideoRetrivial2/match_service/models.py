from django.db import models

# Create your models here.

class OriginalSearchQuery(models.Model):
    '''
    Как проснуться?
    '''
    string = models.TextField()
    category = models.CharField(max_length=255)

class TranslateSource(models.Model):
    '''
    Google Translate, Yandex, Bing
    '''
    title = models.CharField(max_length=255)


class TranslateSearchQuery(models.Model):
    '''
    How to wakeup
    '''
    translate_source = models.ForeignKey('TranslateSource')
    string = models.TextField()

class VideoSource(models.Model):
    '''
    YouTube
    '''
    title = models.CharField(max_length=255)

class VideoMovie(models.Model):
    '''
    Ролик с Ютуба/Ещё откуда-то
    '''
    video_source = models.ForeignKey(
        'VideoSource', related_name='video_source'
    )
    translate_search_query = models.ForeignKey(
        'TranslateSearchQuery', related_name='translate_search_query'
    )
    counter = models.BigIntegerField() # ?

class VideoMovieComment(models.Model):
    '''
    Коммент под видео
    '''
    video_movie = models.ForeignKey('VideoMovie', related_name='video_movie')
    text = models.TextField()
    date = models.DateTimeField()
