"""
Декоратор - де'коратор - де-каринг - замыкание , построенное на функции
Декорарование - способ наделить фукнции дополнительными способностями, засчет уже реализованных
функциональных замыканий.
"""


def request_config(request_func):
    """
    Описание функции request_config
    """
    def wrapper():
        """
        Описание фукнции wrapper
        """
        print("Проверяем, есть ли интернет?")
        print("Проверяем, доступен ли сервер?")

        request_func()

        print("Отключаемся от интернета")
        print("Уходим в туман. Перезагружаемся. Переподключаемся")
    return wrapper



@request_config  # get_decorators = request_config(get)
def get():
    """
    Функция выполняет запрос get для сервера...
    """
    print("Выполянем GET запрос......")

@request_config
def post():
    """
    Фукнция выполняет запрос post на сервер
    """
    print("Выполняем POST запрос.......")
@request_config
def put():
    """
    """
    print("Выполняем запрос PUT....")


# get = request_config(get)
#post = request_config(post)
#put = request_config(put)
get()
post()
put()
#input = request_config(input)




