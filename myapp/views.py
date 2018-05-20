from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from myapp.models import Song, Comment
from myapp.forms import SongForm, CommentForm
from django.views.generic.list import ListView


def song_list(request):
    """曲の一覧表示"""
    songs = Song.objects.all().order_by('id')
    return render(request,
                  'myapp/song_list.html',  # 使用するテンプレート
                  {'songs': songs})         # テンプレートに渡すデータ


def song_edit(request, song_id=None):
    """曲の編集"""
    # song_idが指定されているなら修正、指定されていないなら追加
    if song_id:
        song = get_object_or_404(Song, pk=song_id)
    else:
        song = Song()
    # POSTされたrequestデータからフォームを作成
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            return redirect('myapp:song_list')
        # GETの時
    else:
        # songインスタンスからフォームを作成
        form = SongForm(instance=song)
    return render(request, 'myapp/song_edit.html', dict(form=form, song_id=song_id))


def song_del(request, song_id):
    """曲の削除"""
    song = get_object_or_404(Song, pk=song_id)
    song.delete()
    return redirect('myapp:song_list')


class CommentList(ListView):
    """感想の一覧"""
    context_object_name = 'comment'
    template_name = 'myapp/comment_list.html'
    # 1ページは最大2件ずつでページングする
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        song = get_object_or_404(Song, pk=kwargs['song_id'])  # 親の曲を読む
        comment = song.comment.all().order_by('id')           # 曲の子供の、コメントを読む
        self.object_list = comment

        context = self.get_context_data(object_list=self.object_list, song=song)
        return self.render_to_response(context)


def comment_edit(request, song_id, comment_id=None):
    """コメントの編集"""
    song = get_object_or_404(Song, pk=song_id)  # 親の曲を読む
    # comment_idが指定されている（修正時）
    if comment_id:
        comment = get_object_or_404(Comment, pk=comment_id)
    # comment_idが指定されていない（追加時）
    else:
        comment = Comment()

    if request.method == 'POST':
        # POSTされたrequestデータからフォームを作成
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.song = song
            comment.save()
            return redirect('myapp:comment_list', song_id=song_id)
        else:  # GETの時
            form = CommentForm(instance=comment)

        return render(request, 'myapp/comment_edit.html', dict(form=form, song_id=song_id, comment_id=comment_id))


def comment_del(request, song_id, comment_id):
    """コメントの削除"""
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('myapp:comment_list', song_id=song_id)
