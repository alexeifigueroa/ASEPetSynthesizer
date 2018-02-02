'''
Created on 5 Jan 2018

@author: Alexei Figueroa

This is a unit test testing the vibrato view state behaviour
'''
import unittest
from view import vibratoView
import pygame

class Test(unittest.TestCase):
    def setUp(self):
        pygame.init()
        screen = None   #No screen device will be present in the engine
        self.vibrato_view=vibratoView(screen)
    def tearDown(self):
        pass
    def test_vibrato(self):
        self.vibrato_view.setVibrato(True)
        self.assertEqual(True, self.vibrato_view.vibrato, "The vibrato field is set")


if __name__ == "__main__":
    unittest.main()