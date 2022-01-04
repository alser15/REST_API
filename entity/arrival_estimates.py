from method.methods import Method
from status_code import StatusCode
import arrow


class ArrivalEstimates(Method):

    def __init__(self, url=None, header=None, param=None,data=None):
        self.url = url
        self.header = header
        self.param = param
        self.data = data

    def validate_response_status_code(self):
        """
        Проверка кода ответа
        """
        assert ArrivalEstimates.get(self.url, headers=self.header, params=self.param).status_code == \
               StatusCode.success, \
               f"Код ответа {ArrivalEstimates.get(self.url, headers=self.header, params=self.param).status_code}, " \
               f"ожидается {StatusCode.success}"

    def validate_response_json(self):
        """
        Проверка возвращающегося json
        """
        answer = ArrivalEstimates.get(self.url, headers=self.header, params=self.param).json()
        assert answer["rate_limit"] == 1, f"Неверный ответ {answer['rate_limit']}, ожидается 1"
        assert answer["expires_in"] == 5, f"Неверный ответ {answer['expires_in']}, ожидается 300"
        assert answer["api_latest_version"] == '1.2', f"Неверный ответ {answer['api_latest_version']}, ожидается 1.2"
        # TODO arrow не успевает подставить нормальное время
        assert answer["generated_on"][:16] == str(arrow.now())[:16], \
            f"Неверный ответ {answer['generated_on'][:16]}, ожидается {str(arrow.now())[:16]}"
        assert len(answer["data"]) == 0, f"Неверный ответ {len(answer['data'])}, ожидается 0"
        assert answer["api_version"] == '1.2', f"Неверный ответ {answer['api_version']}, ожидается 1.2"