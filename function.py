import json
from flask import request


def open_json():
    """Чтение списков постов и комментариев.
    Расчет количества комментариев к каждому посту"""

    with open('data.json', encoding='utf-8') as f:
        posts = json.load(f)

    with open('comments.json', encoding='utf-8') as f:
        comments = json.load(f)

    dict_comments = {}
    for comment in comments:
        if comment['post_id'] in dict_comments:
            dict_comments[comment['post_id']] = dict_comments[comment['post_id']] + 1
        else:
            dict_comments[comment['post_id']] = 1

    for number_post in dict_comments.keys():
        for post in posts:
            if post["pk"] == number_post:
                post["count_comments"] = dict_comments[number_post]

    return posts, comments


def one_post(postid: int):
    """Получение комментария из файла comments.json и вывод поста,
    у которых соответствующий postid"""

    comments_id = []
    post_id = []
    posts, comments = open_json()
    count_comments = ''

    for post in posts:
        if post["pk"] == postid:
            post_id.append(post)
    for comment in comments:
        if comment["post_id"] == postid:
            comments_id.append(comment)
            count_comments = len(comments_id)
    return comments_id, post_id, count_comments


def found_post():
    """Поиск по вхождению ключевого слово в текст поста"""
    posts, comments = open_json()
    input_text = str(request.args.get('input_text'))
    response = []
    for post in posts:
        if input_text.lower() in post["content"].lower():
            response.append(post)
    return response


def user_post(username):
    """Вывод постов выбранного пользователя по порядку"""
    name_post = []
    posts, comments = open_json()
    for post in posts:
        if post["poster_name"] == username:
            name_post.append(post)
    return name_post
