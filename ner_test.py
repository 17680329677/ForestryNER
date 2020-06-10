#!/usr/bin/env python
# coding=utf-8

from ner_function import question_ner


def test_ner():
    file_path = r'G:\ner_test.txt'
    with open(file_path, "r", encoding='gbk', errors='ignore') as f:
        question = f.readline().replace('\n', '')
        while question:
            ner_res = question_ner(question)
            print(ner_res)
            question = f.readline().replace('\n', '')


if __name__ == '__main__':
    test_ner()