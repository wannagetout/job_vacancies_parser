from instances.base.job_classes import Vacancy


class HHVacancy(Vacancy):  # add counter mixin
	""" HeadHunter Vacancy """

	def __str__(self):
		return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'
