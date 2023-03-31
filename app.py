from instances.base.connector import Connector
from instances.hh.service import HH
from utils import utils


if __name__ == '__main__':
    keyword = input("Введите ключевую фразу для поиска:")
    file = Connector()
    hh = HH()
    file.insert(hh.get_json_from_request())
    print(
        f"Загружено 1000 вакансий в файл {keyword}.json:\n"
        "Нажмите 1 для просмотра топ 10 вакансий по зарплате\n"
        "Нажмите 2 для поиска вакансий по запросу\n"
        "Нажмите 3 для удаления вакансий из файла\n"
        "Нажмите 4 для выхода\n"
    )
    while True:
        user_input = int(input("Выберите действие:"))
        if user_input == 1:
            top_10 = utils.get_top(keyword)
            for item in top_10:
                print(
                    f'Вакансия: {item["vacancy"]["name"]}\n'
                    f'Зарплата: {item["vacancy"]["salary"]}\n'
                    f'Описание: {item["vacancy"]["description"]}\n'
                    f'Ссылка: {item["vacancy"]["url"]}\n'
                )
        if user_input == 2:
            request_field = input("Введите поле для поиска:")
            request_value = input("Введите информацию для поиска:")
            if request_field == "salary":
                request_value = int(request_value)
            answer = file.select({request_field: request_value})
            for item in answer:
                print(
                    f'Вакансия: {item["vacancy"]["name"]}\n'
                    f'Зарплата: {item["vacancy"]["salary"]}\n'
                    f'Описание: {item["vacancy"]["description"]}\n'
                    f'Ссылка: {item["vacancy"]["url"]}\n'
                )
        if user_input == 3:
            request = input("Введите запрос(dict):")
            key = request.partition(":")[0]
            value = request.partition(":")[2]
            key = key[2: len(key) - 1]
            value = value[0: len(key) - 1]
            answer = file.delete({key: int(value)})
        if user_input == 4:
            break