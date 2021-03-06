import urllib.parse
import urllib.request
import json


def get_access_token():
    params = urllib.parse.urlencode({
        'client_id': '5319349',
        'client_secret': '2E1nv4i8Po0sMYSbaorQ',
        'grant_type': 'client_credentials',
    })
    url = 'https://oauth.vk.com/access_token?' + params
    with urllib.request.urlopen(url) as http_response:
        http_response = json.loads(http_response.read().decode("utf-8", "ignore"))
        return http_response['access_token']


class request:
    """
    Основной класс Запроса к API Вконтакте
    """
    params = {}

    def __init__(self, method=''):
        self.method = method
        self.set_param('v', '5.52')
        self.set_param('lang', 'ru')

    def exec(self):
        url = 'https://api.vk.com/method/' + self.method
        params = urllib.parse.urlencode(self.params)
        # params = params.encode('ascii')
        # request = urllib.request.Request(url, params)
        request = url + '?' + params
        print(request)
        with urllib.request.urlopen(request) as http_response:
            http_response = json.loads(http_response.read().decode("utf-8", "ignore"))
            self.response = response(http_response)

        return self

    def set_param(self, param_name, value):
        self.params[param_name] = value
        return self

    def get_response(self):
        return self.response

    def get_param(self, param_name, default=None):
        if param_name in self.params:
            return self.params[param_name]
        return default


class response:
    """
    Основной класс Ответа от API Вконтакте
    """

    def __init__(self, http_response):
        self.http_response = http_response
        pass

    def is_error(self):
        if 'error' in self.http_response:
            return True
        else:
            return False

    def get_error(self):
        if self.is_error():
            return self.http_response['error']
        return None

    def get_response(self):
        return self.http_response['response']


class list:
    """
    Класс для Списков
    """
    count = 0
    items = []

    def __init__(self, first_request):
        """

        :param first_request: request
        """
        self.first_request = first_request
        pass

    def get_count(self):
        return self.count

    def set_count(self, count):
        self.param_count = count
        return self

    def set_offset(self, offset):
        self.param_offset = offset
        return self

    def exec(self):
        self.first_request.exec()
        first_response = self.first_request.get_response().get_response()
        count = int(first_response['count'])
        self.count = count
        items = first_response['items']
        if len(items) < 1:
            return
        self.items = self.items + items
        offset = self.first_request.get_param('offset', 0)
        while offset < count:
            offset += 100
            self.first_request.set_param('offset', offset)
            self.first_request.exec()
            current_response = self.first_request.get_response().get_response()
            items = current_response['items']
            if len(items) < 1:
                return
            self.items = self.items + items

    def get_items(self):
        return self.items
