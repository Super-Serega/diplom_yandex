import configuration
import requests
import data


# Создать новый заказ
def post_new_orders(body):
    url = configuration.URL_SERVICE+configuration.CREATED_ORDER
    return requests.post(url, json=body, headers=data.headers)
respouns = post_new_orders(data.order)


# Получить заказ по номеру трэка
def get_take_order(track):
    url = configuration.URL_SERVICE+configuration.TAKE_ORDER+str(track)
    return requests.get(url)
