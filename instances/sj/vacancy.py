from instances.vacancies.job_classes import Vacancy


class SJVacancy(Vacancy):  # add counter mixin
	""" SuperJob Vacancy """

	def __str__(self):
		return f'SJ: {self.comany_name}, зарплата: {self.salary} руб/мес'
