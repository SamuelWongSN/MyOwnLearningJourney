'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 3:07 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex11_1test.py
 @Software: PyCharm
'''

import unittest

from ex11_1 import city

print(city('beijing','china'))
class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        result = city('beijing','china')
        self.assertEqual(result,'Beijing China-0')

    def test_city_pollution(self):
        result = city('tianjin','china',50000)
        self.assertEqual(result,'Tianjin China-50000')
if __name__ == "__main__":
    unittest.main()
