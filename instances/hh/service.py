from instances.base.engine_classes import Engine
from instances.hh.vacancy import HHVacancy
from requests import request


class HH(Engine):

	BASE_URL = 'https://api.hh.ru/vacancies'

	def __init__(self, vacancy: str = 'Python'):
		"""
		Создает список вакансий
		:param vacancy: Пользовательский ввод позиции, default='Python'
		"""
		self.vacancy = vacancy

		super().__init__()
		self.vacancy_params = {
			'area': 113,
			'page': range(1, 5),
			'per_page': 100,
			'text': self.vacancy
		}

	def get_request(self, url: str = BASE_URL, params: dict = None) -> request:
		if params is None:
			params = self.vacancy_params
		return request(method='GET', url=url, params=params)

	def get_json_from_request(self) -> list[dict]:
		vacancies_list = self.get_request().json()['items']
		id_count = 0
		for vacancy in vacancies_list:
			id_count += 1
			vacancy['id'] = id_count
		return vacancies_list

	def get_entities_list(self) -> list[HHVacancy]:
		vacancies = self.get_json_from_request()
		vacancies_list = []
		for vacancy in vacancies:
			if vacancy['salary'] is None:
				continue
			vacancy_entity = HHVacancy(vacancy)
			vacancies_list.append(vacancy_entity)
		return vacancies_list


hh = HH()
vacanciess = hh.get_entities_list()
for v in vacanciess:
	print(v)

# vacancy_id = 0
# vacancies_mapping = []
# for i in vacancies:
# 	vacancy = Vacancy(data=i)
# 	vacancies_mapping.append(vacancy)
# 	print(i)
# 	print(i['id'])
# 	print(i['name'])
# 	print(i['alternate_url'])
# 	print(i.get('salary')['from'] and i.get('salary')['to'] if i.get('salary') else None)
# 	print(i.get('snippet')['requirement'])
# 	print('==============================')
#
# for i in vacancies_mapping:
# 	print(i)
# t = hh.get_request(params={'area': 113, 'page': 1, 'per_page': 20, 'text': 'Python'})

# for a in t.json()['items']:
# 	print(a['name'])
# 	print(a['salary'])
# 	print(a['snippet']['requirement'])
# 	print('======================')
