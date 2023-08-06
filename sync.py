import argparse
import time

import notion
import oulu
import constants


def init():
    # 获取参数
    parser = argparse.ArgumentParser()
    parser.add_argument("oulu_token")
    parser.add_argument("notion_token")
    parser.add_argument("database_id")
    options = parser.parse_args()

    constants.OULU_AUTHORIZATION = options.oulu_token
    constants.NOTION_SECRETS = options.notion_token
    constants.NOTION_DATABASE_ID = options.database_id


if __name__ == '__main__':
    init()
    # 获取notion 数据库中所有单词
    old_words = notion.get_words_from_databases()
    print(old_words)
    # 获取欧酷中所有单词本、所有单词
    books = oulu.get_vocabulary_books()
    add_words = []
    update_words = []
    for book in books:
        book_id = book["id"]
        words = oulu.get_words(book_id)
        for word_item in words:
            word = word_item["word"]
            exp = word_item["exp"]
            if word not in old_words.keys():
                notion.insert_word(word, exp, '')
                add_words = add_words + [word]
            else:
                notion.update_word(old_words.get(word), word, exp, '')
                update_words = update_words + [word]
            time.sleep(0.1)
    print("本次新增单词：" + add_words)
    print("本次更新单词：" + update_words)
