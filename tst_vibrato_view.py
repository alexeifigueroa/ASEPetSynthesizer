'''
Created on 5 Jan 2018

@author: alexei.figueroa
'''
import unittest
from view import vibratoView
import pygame

class Test(unittest.TestCase):
    def setUp(self):
        pygame.init()
        screen = pygame.display.set_mode((400, 300))
        self.vibrato_view=vibratoView(screen)
    def tearDown(self):
        pass
    def test_vibrato(self):
        self.vibrato_view.setVibrato(True)
        self.assertEqual(True, self.vibrato_view.vibrato, "The vibrato field is set")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()