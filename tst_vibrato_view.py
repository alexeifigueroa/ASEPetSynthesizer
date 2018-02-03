'''
Created on 5 Jan 2018

@author: Alexei Figueroa

This is a unit test testing the vibrato View state behaviour
'''
import unittest
from view import VibratoView
import pygame

class Test(unittest.TestCase):
    def setUp(self):
        pygame.init()
        screen = None   #No screen device will be present in the engine
        self.vibrato_view=VibratoView(screen)
    def tearDown(self):
        pass
    def test_vibrato(self):
        self.vibrato_view.set_vibrato(True)
        self.assertEqual(True, self.vibrato_view.vibrato, "The vibrato field is set")


if __name__ == "__main__":
    unittest.main()