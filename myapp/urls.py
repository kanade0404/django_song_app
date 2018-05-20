from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    # 曲
    # 一覧
    path('song/', views.song_list, name='song_list'),
    # 登録
    path('song/add/', views.song_edit, name='song_add'),
    # 修正
    path('song/mod/<int:song_id>/', views.song_edit, name='song_mod'),
    # 削除
    path('song/del/<int:song_id>/', views.song_del, name='song_del'),
    # 感想
    # 一覧
    path('comment/<int:song_id>/', views.CommentList.as_view(), name='comment_list'),
    # 登録
    path('comment/add/<int:song_id>/', views.comment_edit, name='comment_add'),
    # 修正
    path('comment/mod/<int:song_id>/<int:comment_id>/', views.comment_edit, name='comment_mod'),
    # 削除
    path('comment/del/<int:song_id>/<int:comment_id>', views.comment_del, name='comment_del'),
]