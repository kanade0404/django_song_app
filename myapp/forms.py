from django.forms import ModelForm
from myapp.models import Song, Comment


class SongForm(ModelForm):
    """曲のフォーム"""
    class Meta:
        model = Song
        fields = ('name', 'singer_name', 'anime_title',)


class CommentForm(ModelForm):
    """コメントのフォーム"""
    class Meta:
        model = Comment
        fields = ('comment', )
