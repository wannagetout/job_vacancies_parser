from abc import ABC, abstractmethod
from instances.base.connector import Connector
from requests import request


class Engine(ABC):
	HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'}

	@abstractmethod
	def get_request(self, url: str, params: dict):
		return request(method='GET', url=url, params=params, headers=self.HEADERS)

	@staticmethod
	def get_connector(file_name: str) -> Connector:
		connector = Connector(file_name)
		""" Возвращает экземпляр класса Connector """
		return connector
