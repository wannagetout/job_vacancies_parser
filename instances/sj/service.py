import os

from requests import request

from instances.base.engine_classes import Engine
from instances.vacancies.job_classes import Vacancy


class SuperJob(Engine):

	BASE_URL = 'https://api.superjob.ru/2.0/vacancies/'

	def __init__(self, vacancy: str = 'Python'):
		"""
		Создает список вакансий
		:param vacancy: Пользовательский ввод позиции, default='Python'
		"""
		self.vacancy = vacancy

		self.vacancy_params = {
			'keywords': self.vacancy,
			'count': 20,
			'page': 1
		}
		self.HEADERS = {
			'Host': 'api.superjob.ru',
			'X-Api-App-Id': os.getenv('SJ_API_KEY'),
			'Authorization': 'Bearer r.000000010000001.example.access_token',
			'Content-Type': 'application/x-www-form-urlencoded'
		}
		self.vacancies = self.get_vacancies_from_request()
		super().__init__()

	def get_request(self, url: str = BASE_URL, params: dict = None) -> request:
		if params:
			self.vacancy_params = params
		return request(method='GET', url=url, headers=self.HEADERS, params=self.vacancy_params)

	def get_vacancies_from_request(self):
		vacancies_list = []
		id_counter = 500
		while self.vacancy_params['page'] < 5:
			vacancies = self.get_request().json()['objects']
			for vacancy in vacancies:
				if not vacancy['payment_to'] or not vacancy['payment_from']:
					continue
				id_counter += 1
				vac = Vacancy()
				vac.id = id_counter
				vac.vacancy_name = vacancy['profession']
				vac.company_name = vacancy['agency']['title']
				vac.salary = vacancy['payment_to'] if vacancy['payment_to'] else vacancy['payment_from'] or None
				vac.url = vacancy['link']
				vac.snippet = vacancy['candidat']
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
