class Vacancy:
	__slots__ = ('id', 'url', 'vacancy_name', 'company_name', 'snippet', 'salary')

	def __str__(self):
		return f"Вакансия: {self.vacancy_name} ЗП: {self.salary}, Требования: {self.snippet} Ссылка {self.url}"
