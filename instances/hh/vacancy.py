from instances.vacancies.job_classes import Vacancy

from utils.utils import delete_tags


class HHVacancy(Vacancy):  # add counter mixin
	""" HeadHunter Vacancy """

	def __init__(self, data):
		super().__init__()
		self.id = data['id']
		self.url = data['alternate_url']
		self.vacancy_name = data['name']
		self.company_name = data['employer']['name'] or data['department']['name'] or None
		self.snippet = delete_tags(str(data['snippet']['requirement']))
		self.salary = data['salary']['from'] or data['salary']['to'] if data['salary'] else None

	def __str__(self):
		return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'
