import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    # Добавляем стили для таблицы
    styles = '''
    <style>
        table {
            border-collapse: collapse;
            display: inline-table; /* Делаем таблицу inline, чтобы она адаптировалась к содержимому */
            font-family: Arial, sans-serif;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
            white-space: nowrap; /* Предотвращаем перенос текста в ячейках */
        }
        tr:nth-child(even) {
            background-color: #dddddd;
        }
    </style>
    '''
    text = '<h1>Курс валют</h1>'
    text += styles # Добавляем стили в начало HTML
    text += '<table>'
    text += '<tr>'
    # Добавляем названия столбцов
    text += '<th>Код1 валюты</th>'
    text += '<th>Код2 валюты</th>'
    text += '<th>Сокращение</th>'
    text += '<th>Единица измерения</th>'
    text += '<th>Название валюты</th>'
    text += '<th>Рублей покупка</th>'
    text += '<th>Рублей продажа</th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


# def create_html(valutes):
#     text = '<h1>Курс валют</h1>'
#     text += '<table>'
#     text += '<tr>'
#     for _ in valutes[0]:
#         text += f'<th><th>'
#     text += '</tr>'
#     for valute in valutes:
#         text += '<tr>'
#         for v in valute.values():
#             text += f'<td>{v}</td>'
#         text += '</tr>'

#     text += '</table>'
#     return text



@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()