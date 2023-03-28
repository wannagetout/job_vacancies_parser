import re


def sorting(vacancies):
	""" Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
	pass


def get_top(vacancies, top_count):
	""" Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
	pass


def delete_tags(text: str):
	return re.sub(r"<[^>]+>", "", text, flags=re.S)
