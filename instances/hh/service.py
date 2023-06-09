from instances.base.engine_classes import Engine
from requests import request

from instances.vacancies.job_classes import Vacancy
from utils.utils import delete_tags


class HH(Engine):

	BASE_URL = 'https://api.hh.ru/vacancies'

	def __init__(self, vacancy: str = 'Python'):
		"""
		Создает список вакансий
		:param vacancy: Пользовательский ввод позиции, default='Python'
		"""
		self.vacancy = vacancy

		self.vacancy_params = {
			'area': 113,
			'page': 1,
			'per_page': 100,
			'text': self.vacancy
		}
		self.vacancies = self.get_vacancies_from_request()
		super().__init__()

	def get_request(self, url: str = BASE_URL, params: dict = None) -> request:
		if params is None:
			params = self.vacancy_params
		return request(method='GET', url=url, params=params)

	def get_vacancies_from_request(self) -> list[Vacancy]:
		vacancies_list = []
		id_counter = 0
		while len(vacancies_list) < 500:
			vacancies_json = self.get_request().json()['items']
			for vacancy in vacancies_json:
				if vacancy['salary'] is None:
					continue
				id_counter += 1
				vac = Vacancy()
				vac.id = id_counter
				vac.vacancy_name = vacancy['name']
				vac.company_name = vacancy['department']['name'] if vacancy['department'] else vacancy['employer']['name']
				vac.salary = vacancy['salary']['from'] or vacancy['salary']['to']
				vac.url = vacancy['url']
				vac.snippet = delete_tags(vacancy['snippet']['requirement'])
				vacancies_list.append(vac)
			self.vacancy_params['page'] += 1
		return vacancies_list

	def get_json(self) -> list[dict]:
		result = []
		for vacancy in self.vacancies:
			vacancy_dict = {}
			vacancy_dict['id'] = vacancy.id
			vacancy_dict['url'] = vacancy.url
			vacancy_dict['vacancy_name'] = vacancy.vacancy_name
			vacancy_dict['company_name'] = vacancy.company_name
			vacancy_dict['snippet'] = vacancy.snippet
			vacancy_dict['salary'] = vacancy.salary
			result.append(vacancy_dict)
		return result
