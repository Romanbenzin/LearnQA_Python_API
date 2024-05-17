import json.decoder
from requests import Response
class BaseCase:
    token = None
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Не могу найти куки {cookie_name} в последнем ответе"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Не могу найти хедер {headers_name} в последнем ответе"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()

        except json.decoder.JSONDecodeError:
            assert False, F"Ответ не в формате json, ответ такой: '{response.text}'"

        assert name in response_as_dict, f"В ответе json отсутствует ключ '{name}'"

        return response_as_dict[name]
