import unittest
import controller
from mockData import mockData


class ControllerTest(unittest.TestCase):

    def startCrawling(self):
        res = controller.startCrawling(mockData['url'])
    def save(self):
        res = controller.save(mockData)
        self.assertEqual(res, "saved")

    def findById(self):
        res = controller.findById(mockData['id'])
        self.assertEqual(res['id'], mockData['id'])

    def getlist(self):
        res = controller.getList({"page": 0, "per": 1})
        self.assertEqual(res['total'], 1)
        self.assertEqual(len(res['data']), 1)
