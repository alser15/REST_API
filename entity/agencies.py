import arrow
import requests
import pytest_check as check


class Agencies:

    def __init__(self, data_class):
        self.data_class = data_class

    def validate_response_status_code(self):
        """
        Проверка кода ответа
        """
        s = [i["url"] for i in self.data_class.urls]
        for i in s:
            request_get_status_code = requests.get(i, headers=self.data_class.header,
                                                   params=self.data_class.params).status_code
            check.equal(request_get_status_code, 200, f"Код ответа {request_get_status_code} для {i}, ожидается 200")

    def validate_response_json(self):
        """
        Проверка возвращающегося json
        """

        obj_json = requests.get(url=self.data_class.urls[1]["url"], headers=self.data_class.header,
                                params=self.data_class.params).json()
        check.equal(obj_json["rate_limit"], 1, f"Неверный ответ {obj_json['rate_limit']}, ожидается 1")
        check.equal(obj_json["expires_in"], 300, f"Неверный ответ {obj_json['expires_in']}, ожидается 300")
        check.equal(obj_json["api_latest_version"], '1.2',
                    f"Неверный ответ {obj_json['api_latest_version']}, ожидается 1.2")
        # TODO arrow не успевает подставить нормальное время
        check.equal(obj_json["generated_on"][:16], str(arrow.now())[:16],
                    f"Неверный ответ {obj_json['generated_on'][:16]}, ожидается {str(arrow.now())[:16]}")
        check.equal(obj_json["data"][0]['long_name'], 'GoTriangle',
                    f"Неверный ответ {obj_json['data'][0]['long_name']}, ожидается GoTriangle")
        check.equal(obj_json["data"][0]['language'],  'en',
                    f"Неверный ответ {obj_json['data'][0]['language']}, ожидается en")
        check.equal(len(obj_json["data"]), 1, f"Неверный ответ {len(obj_json['data'])}, ожидается 1")
        check.equal(float(obj_json["data"][0]['position']['lat']), 35.874507,
                    f"Неверный ответ {obj_json['data'][0]['position']['lat']}, ожидается 35.874507")
        check.equal(float(obj_json["data"][0]['position']['lng']), -78.838009,
                    f"Неверный ответ {obj_json['data'][0]['position']['lng']}, ожидается 'lng': -78.838009")
        check.equal(obj_json["data"][0]['name'], "tt", f"Неверный ответ {obj_json['data'][0]['name']}, ожидается tt")
        check.equal(obj_json["data"][0]['short_name'], "GoTriangle",
                    f"Неверный ответ {obj_json['data'][0]['short_name']}, ожидается GoTriangle")
        check.equal(obj_json["data"][0]['phone'], None,
                      f"Неверный ответ {obj_json['data'][0]['phone']}, ожидается None")
        check.equal(obj_json["data"][0]['url'], 'http://www.triangletransit.org/',
                    f"Неверный ответ {obj_json['data'][0]['url']}, ожидается http://www.triangletransit.org/")
        check.equal(obj_json["data"][0]['timezone'], 'America/New_York',
                    f"Неверный ответ {obj_json['data'][0]['timezone']}, ожидается America/New_York")
        check.equal(obj_json["data"][0]['bounding_box'], [{'lat': 35.53135284206374, 'lng': -79.4626675},
                                                          {'lat': 36.13162687597235, 'lng': -78.28778043359375}])
        check.equal(obj_json["data"][0]['agency_id'], '12',
                    f"Неверный ответ {obj_json['data'][0]['agency_id']}, ожидается 12")
        check.equal(obj_json["api_version"], '1.2', f"Неверный ответ {obj_json['api_version']}, ожидается 1.2")
