import json
import os
from typing import List


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """

    __data_file = None

    @property
    def data_file(self) -> str:
        return self.__data_file

    @data_file.setter
    def data_file(self, filename: str = 'vacancies') -> None:
        self.filename = filename
        file = open(f'{self.filename}.json', 'a+')
        file.close()
        self.__data_file = file.name
        self.__connect()

    def __connect(self) -> None:
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        pass

    def insert(self, data: List[dict]) -> None:
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(f'{self.data_file}', 'w+', encoding='utf-8') as file:
            json_data = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)
            file.write(json_data)

    def select(self, query: dict) -> List:
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        with open(f'{self.data_file}', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            query_params = list(query.items())[0]
            print(query_params)
            query_key = query_params[0]
            query_value = query_params[1]
            result = []

            for vacancy in data['items']:
                if vacancy['vacancy'][query_key] == query_value:
                    result.append(vacancy)
            return result

    def delete(self, query: dict) -> None:
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        with open(f'{self.data_file}', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            query_params = list(query.items())[0]
            query_key = query_params[0]
            query_value = query_params[1]
            result = []

            for vacancy in data['items']:
                if vacancy['vacancy'][query_key] == query_value:
                    data['items'].remove(vacancy)
            data = json.dumps(data, ensure_ascii=False)
            with open(f'{self.data_file}', 'w', encoding='utf-8') as file:
                file.write(data)
