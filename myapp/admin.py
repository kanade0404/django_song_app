from django.contrib import admin
from myapp.models import Song, Comment

# Register your models here.
# admin.site.register(Song)
# admin.site.register(Comment)


class SongAdmin(admin.ModelAdmin):
    # 一覧ぎ出したい項目
    list_display = ('id', 'name', 'singer_name', 'anime_title',)
    # 修正リンクでクリックできる項目
    list_display_links = ('id', 'name',)


admin.site.register(Song, SongAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）
    raw_id_fields = ('song_name',)


admin.site.register(Comment, CommentAdmin)
