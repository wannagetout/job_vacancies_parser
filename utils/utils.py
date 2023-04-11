import re
import json


def sorting(vacancy_json):
	""" Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
	vac_list = vacancy_json
	vac_sorted = sorted(
		vac_list, key=lambda vacancy: vacancy["salary"], reverse=True
	)
	return {"items": vac_sorted}


def get_top(name):
	""" Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
	with open(f"{name}.json", "r", encoding="utf-8") as file:
		data = json.load(file)
		top_10 = sorting(data)["items"][0:10]
	return top_10


def delete_tags(text: str):
	return re.sub(r"<[^>]+>", "", str(text), flags=re.S)
