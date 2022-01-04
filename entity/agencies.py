from method.methods import Method
from status_code import StatusCode
import arrow


class Agencies(Method):

    def __init__(self, url=None, header=None, param=None,data=None):
        self.url = url
        self.header = header
        self.param = param
        self.data = data

    def validate_response_status_code(self):
        """
        Проверка кода ответа
        """
        assert Agencies.get(self.url, headers=self.header, params=self.param).status_code == StatusCode.success, \
            f"Код ответа {Agencies.get(self.url, headers=self.header, params=self.param).status_code}, " \
            f"ожидается {StatusCode.success}"

    def validate_response_json(self):
        """
        Проверка возвращающегося json
        """
        answer = Agencies.get(self.url, headers=self.header, params=self.param).json()
        assert answer["rate_limit"] == 1, f"Неверный ответ {answer['rate_limit']}, ожидается 1"
        assert answer["expires_in"] == 300, f"Неверный ответ {answer['expires_in']}, ожидается 300"
        assert answer["api_latest_version"] == '1.2', f"Неверный ответ {answer['api_latest_version']}, ожидается 1.2"
        # TODO arrow не успевает подставить нормальное время
        assert answer["generated_on"][:16] == str(arrow.now())[:16], \
            f"Неверный ответ {answer['generated_on'][:16]}, ожидается {str(arrow.now())[:16]}"
        assert answer["data"][0]['long_name'] == 'GoTriangle', \
            f"Неверный ответ {answer['data'][0]['long_name']}, ожидается GoTriangle"
        assert answer["data"][0]['language'] == 'en', f"Неверный ответ {answer['data'][0]['language']}, ожидается en"
        assert len(answer["data"]) == 1, f"Неверный ответ {len(answer['data'])}, ожидается 1"
        assert float(answer["data"][0]['position']['lat']) == 35.874507, \
            f"Неверный ответ {answer['data'][0]['position']['lat']}, ожидается 35.874507"
        assert float(answer["data"][0]['position']['lng']) == -78.838009, \
            f"Неверный ответ {answer['data'][0]['position']['lng']}, ожидается 'lng': -78.838009"
        assert answer["data"][0]['name'] == "tt", f"Неверный ответ {answer['data'][0]['name']}, ожидается tt"
        assert answer["data"][0]['short_name'] == "GoTriangle", \
            f"Неверный ответ {answer['data'][0]['short_name']}, ожидается GoTriangle"
        assert answer["data"][0]['phone'] is None, f"Неверный ответ {answer['data'][0]['phone']}, ожидается None"
        assert answer["data"][0]['url'] == 'http://www.triangletransit.org/',\
            f"Неверный ответ {answer['data'][0]['url']}, ожидается http://www.triangletransit.org/"
        assert answer["data"][0]['timezone'] == 'America/New_York', \
            f"Неверный ответ {answer['data'][0]['timezone']}, ожидается America/New_York"
        assert answer["data"][0]['bounding_box'] == [{'lat': 35.53135284206374, 'lng': -79.4626675},
                                                     {'lat': 36.13162687597235, 'lng': -78.28778043359375}],\
            f"Неверный ответ {answer['data'][0]['bounding_box']}, " \
            f"ожидается [{'lat': 35.53135284206374, 'lng': -79.4626675}, " \
            f"{'lat': 36.13162687597235, 'lng': -78.28778043359375}]"
        assert answer["data"][0]['agency_id'] == '12', f"Неверный ответ {answer['data'][0]['agency_id']}, ожидается 12"
        assert answer["api_version"] == '1.2', f"Неверный ответ {answer['api_version']}, ожидается 1.2"
