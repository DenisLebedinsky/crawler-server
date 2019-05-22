# coding: utf8
import unittest
import controller
import os
from mongo import statsColl


class ControllerTest(unittest.TestCase):

    def test_startCrawling(self):
        res = controller.startCrawling(
            "http://www.youtube.com/watch?v=-wtIMTCHWuI")

        self.assertEqual(
            res['name'], 'Joel Spolsky: How I Seeded Stack Overflow | Founder Stories')

    def test_save(self):
        mock = {
            "id": "2e8c23dd-3fb3-4ff1-93e8-543edd774167",
            "likes": "12",
            "name": "Joel Spolsky: How I Seeded Stack Overflow | Founder Stories",
            "subscribers": "418 тыс.",
            "dislikes": "1",
            "views": "4695",
            "url": "http://www.youtube.com/watch?v=-wtIMTCHWuI"
        }
        res = controller.save(mock)
        self.assertEqual(res, "saved")

    def test_findById(self):
        id = "2e8c23dd-3fb3-4ff1-93e8-543edd774167"
        res = controller.findById(id)
        self.assertEqual(res['id'], id)

    def test_getlist(self):
        res = controller.getList({"page": 0, "per": 1})
        self.assertEqual(len(res['data']), 1)
