import sender_request
import data
import configuration
import requests

# Щегловский Сергей, 41-я когорта - Финальный проект, Инжерен по тестированию плюс
def test_create_and_track_order():
    # Создаем заказ
    create_order = sender_request.post_new_orders(data.order)
    assert create_order.status_code == 201
    # Сохраняем трек
    track = create_order.json()["track"]
    
    # Получаем заказ по треку
    get_response = sender_request.get_take_order(track)
    
    # Проверяем код 201
    assert get_response.status_code == 200