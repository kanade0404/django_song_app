from django.db import models


class Song(models.Model):
    name = models.CharField('曲名', max_length=100)
    singer_name = models.CharField('歌手名', max_length=200)
    anime_title = models.CharField('アニメタイトル', max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    song_name = models.ForeignKey(Song, verbose_name='曲名', related_name='comment', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment
