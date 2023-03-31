class Vacancy:
	__slots__ = ('id', 'url', 'vacancy_name', 'company_name', 'snippet', 'salary')

	def __str__(self):
		return f"Вакансия: {self.vacancy_name} ЗП: {self.salary}, Требования: {self.snippet} Ссылка {self.url}"

#
# class CountMixin:
#
# 	@property
# 	def get_count_of_vacancy(self):
# 		"""
# 		Вернуть количество вакансий от текущего сервиса.
# 		Получать количество необходимо динамически из файла.
# 		"""
# 		pass
