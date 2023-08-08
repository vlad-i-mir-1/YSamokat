import configuration
import requests
import data

#get запрос
def get_message(path_order, track):
    return requests.get(configuration.URL_SERVICE + path_order,   # подставляем полный url
                        params={'t':str(track)})                  # а здесь номер трека
#post запрос
def post_new_message(body, path_order):
    return requests.post(configuration.URL_SERVICE + path_order,  # подставляем полный url
                         json=body,                               # тут тело
                         headers=data.headers)                    # а здесь заголовки


