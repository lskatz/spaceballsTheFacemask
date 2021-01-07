#!/usr/bin/env python

from advent import *

spec = {}

def showHelp():
  print("""
  This would show some help and maybe even draw from the JSON for the spec
  """)

game = Game()

lobby = game.new_location(
"Lobby", """
There is a desk with a spreadsheet
""")

spreadsheet = lobby.new_object("spreadsheet",
  "a copy of the SARS-CoV-2 metadata spec")

def fill(self, actor, noun, words):
  if not noun:
    print(showHelp())
    return True
  if (noun and noun != "in") and words:
    return False
  key = words[0]
  spec[key] = words[1]
  return True
lobby.add_verb(Verb(fill,'fill'))

def make(self, actor, noun, words):
  if (noun and (noun != "spec" or noun != "spreadsheet")) and words:
    return False
  tsv = ""
  for field in spec.keys():
    tsv += field + "\t"
  tsv += "\n"
  for field in spec.keys():
    tsv += spec[field] + "\t"
  tsv += "\n"
  print(tsv)
  return True

lobby.add_verb(Verb(make,'make'))

hero = game.new_player(lobby)

game.run()

