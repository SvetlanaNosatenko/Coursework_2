from function import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def all_posts():
    """Список всех постов. У каждого выводится автор, укороченный до 50 символов текст,
    количество просмотров и комментариев, ссылка, которая ведет на пост"""

    posts, comments = open_json()
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:postid>')
def post_id(postid: int):
    """Страничка с подробной информацией про пост.
    Ссылка "назад" ведет на главную"""

    comments_id, post_id, count_comments = one_post(postid)
    return render_template("post.html", comments=comments_id, count_comments=count_comments, posts=post_id)


@app.route('/search/')
def post_text():
    """Поиск по вхождению ключевого слово в текст поста"""
    response = found_post()
    return render_template("search.html", posts=response, сount_posts=len(response))


@app.route('/users/<username>')
def user_feed(username):
    """Вывод постов выбранного пользователя по порядку"""
    name_post = user_post(username)
    return render_template("user-feed.html", name=username, posts=name_post)


app.run()
