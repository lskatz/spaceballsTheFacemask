#!/usr/bin/env python

from advent import *

game = Game()

lobby = game.new_location(
"Lobby", """
There is a desk with a spreadsheet
""")

spec = lobby.new_object("spreadsheet",
  "a copy of the SARS-CoV-2 metadata spec")

def fill(self, actor, noun, words):
  if (noun and noun != "out") or words:
    return False
  print("You fill out the form like a true public health hero!")
  return True

lobby.add_verb(Verb(fill,'fill'))

hero = game.new_player(lobby)

game.run()

