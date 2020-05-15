#!/usr/bin/env python
# coding=utf-8
from flask import Flask, request, jsonify
from ner_function import question_ner

app = Flask(__name__)


@app.route('/ner')
def forestry_named_entity_recognize():
    question = request.args.get('question')
    ner_res = question_ner(question)
    print(ner_res)
    result = {'status': 200, 'data': ner_res}
    return jsonify(result)


if __name__ == '__main__':
    app.run('127.0.0.1', '5051', False)