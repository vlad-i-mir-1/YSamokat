# Владимир Селянин, 7-ой поток — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import configuration
import data

# Тест. Создание заказа, запрос только что созданного заказа по его номеру и проверка статуса этого запроса
def test_create_order_and_get_back_order_get_success_response():
    # В переменную response сохраняется результат запроса на создание заказа
    response = sender_stand_request.post_new_message(data.order_body, configuration.CREATE_ORDER_PATH)
    # В переменную track сохраняется номер трека заказа
    track = response.json()["track"]
    # В переменную response сохраняется результат запроса на получение заказа по треку заказа
    response = sender_stand_request.get_message(configuration.GET_ORDER_PATH, track)
    # Проверяю, что код ответа равен 200
    assert response.status_code == 200
