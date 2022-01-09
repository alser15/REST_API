import pytest
import json
from pathlib import Path
import data_info


@pytest.fixture(scope='function')
def open_file(request):
    """
    Возвращает распарсенный json файл для передачи мета тест данных
    :param request:  доступен только в функции, где определена параметризация.
    :return: data_class - данные json файла типа dict
    """
    json_file = request.param
    Path.cwd()
    path = Path(Path.home(), 'PycharmProjects', 'pythonProject', 'data', f'{json_file}')
    with open(path) as f:
        file = json.load(f)

    yield data_info.DataClass(**file)

