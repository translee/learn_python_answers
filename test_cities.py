import unittest
from city_functions import get_city_and_country

class CitiesTestCase(unittest.TestCase):
	"""测试city_functions.py"""
	
	def test_city_coutry(self):
		"""能够处理像Shanghai,China这样的字符吗？"""
		sb = get_city_and_country('shanghai','china')
		self.assertEqual(sb,'Shanghai,China')
		
	def test_city_coutry_population(self):
		"""能够正确处理Shanghai,China,30000000这样的字符吗？"""
		sb = get_city_and_country('shanghai','china',str(30000000))
		self.assertEqual(sb,'Shanghai,China - population 30000000')
		
unittest.main()
