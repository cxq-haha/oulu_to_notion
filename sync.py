import argparse

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
    # 获取欧酷中所有单词本、所有单词
    books = oulu.get_vocabulary_books()
    for book in books:
        book_id = book["id"]
        words = oulu.get_words(book_id)
        for word_item in words:
            word = word_item["word"]
            exp = word_item["exp"]
            if word not in old_words.keys():
                notion.insert_word(word, exp, '')
