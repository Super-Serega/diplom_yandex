import configuration
import requests
import data
# Создать новый заказ
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATED_ORDER, json=body, headers=data.headers)
# Получить заказ по номеру трэка
def get_take_order(track):
    return requests.get(configuration.URL_SERVICE+configuration.TAKE_ORDER+str(track))
