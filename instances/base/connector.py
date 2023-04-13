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

    def __init__(self, filename: str):
        self.__data_file = filename

    @property
    def data_file(self) -> str:
        return self.__data_file

    @data_file.setter
    def data_file(self, filename: str = 'python') -> None:
        file = open(f'{filename}.json', 'a+')
        file.close()
        self.__data_file = filename
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        if not os.path.isfile(f'/home/wannagetout/job_vacancies_parser/{self.__data_file}'):
            raise FileNotFoundError(f"Файл {self.__data_file} отсутствует")
        with open(self.__data_file, 'r', encoding="utf8") as file:
            json_reader = json.load(file)
            if not isinstance(json_reader, list):
                raise Exception('Файл должен содержать список')

    def insert(self, datafile, data: List[dict]) -> None:
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(datafile, 'w', encoding="UTF-8") as file:
            json.dump([e for e in data], file, indent=4, ensure_ascii=False, skipkeys=True, sort_keys=True)

    def select(self, query: dict) -> List:
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        result = []
        with open(self.__data_file, 'r', encoding="UTF-8") as file:
            data = json.load(file)  # считывает файл и возвразает объекты Python

        if not query:
            return data

        for item in data:
            print(item)
            for key, value in query.items():
                if item.get(key) == value:
                    result.append(item)

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

            for vacancy in data:
                if vacancy[query_key] == query_value:
                    data.remove(vacancy)
            # data = json.dumps(data, ensure_ascii=False)
            with open(f'{self.data_file}', 'w', encoding='utf-8') as new_file:
                json.dump([d for d in data], new_file, indent=4, ensure_ascii=False, skipkeys=True, sort_keys=True)

