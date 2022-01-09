import requests
import arrow


class ArrivalEstimates:

    def __init__(self, data_class):
        self.data_class = data_class

    def validate_response_status_code(self):
        """
        Проверка кода ответа
        """
        request_get_status_code = requests.get(self.data_class.urls["url"], headers=self.data_class.header,
                                               params=self.data_class.params).status_code
        assert request_get_status_code == 200,f"Код ответа {request_get_status_code}, ожидается 200"

    def validate_response_json(self):
        """
        Проверка возвращающегося json
        """
        obj_json = requests.get(url=self.data_class.urls["url"], headers=self.data_class.header,
                                params=self.data_class.params).json()
        assert obj_json["rate_limit"] == 1, f"Неверный ответ {obj_json['rate_limit']}, ожидается 1"
        assert obj_json["expires_in"] == 5, f"Неверный ответ {obj_json['expires_in']}, ожидается 300"
        assert obj_json["api_latest_version"] == '1.2', f"Неверный ответ {obj_json['api_latest_version']}, ожидается 1.2"
        # TODO arrow не успевает подставить нормальное время
        assert obj_json["generated_on"][:16] == str(arrow.now())[:16], \
            f"Неверный ответ {obj_json['generated_on'][:16]}, ожидается {str(arrow.now())[:16]}"
        assert len(obj_json["data"]) == 0, f"Неверный ответ {len(obj_json['data'])}, ожидается 0"
        assert obj_json["api_version"] == '1.2', f"Неверный ответ {obj_json['api_version']}, ожидается 1.2"