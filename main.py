from http.server import BaseHTTPRequestHandler, HTTPServer
#  from urllib.parse import urlparse, parse_qs

# Параметры хост и порт для запуска web-сервера
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """ Класс управления web-сервером"""

    @staticmethod
    def __get_index():
        """ Метод получения данных индексной страницы """
        with open("index.html") as file:  # открываем файл index.html
            content = file.read()  # читаем данные из файла
        return content  # возвращаем html-страницу

    def do_GET(self):
        """ Метод обработки GET-запросов """
        # query_components = parse_qs(urlparse(self.path).query)  # парсинг url. Будет использован в будущих задачах
        # page_address = query_components.get('page')  # адрес страницы. Будет использован в будущих задачах

        page_content = self.__get_index()  # получаем данные страницы
        self.send_response(200)  # отправляем код ответа 200 (OK)
        self.send_header("Content-type", "text/html")  # указываем тип данных как text/html
        self.end_headers()  # заканчиваем формирование заголовков страницы
        self.wfile.write(bytes(page_content, "utf-8"))  # указываем кодировку страницы


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)  # запускаем web-сервер с указанными параметрами
    print("Server started http://%s:%s" % (hostName, serverPort))  # выводим сообщение об успешном запуске сервера

    try:
        webServer.serve_forever()  # запускаем бесконечный цикл обработки запросов
    except KeyboardInterrupt:  # останавливаем web-сервер при получении команды с клавиатуры
        pass

    webServer.server_close()  # закрываем соединение
    print("Server stopped.")  # выводим сообщение об остановке web-сервера
