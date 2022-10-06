#!/usr/bin/python

from os import getcwd, system
import sys

def main():

  target_dir = getcwd()
  source_dir = __file__

  langs = ["r", "python"]
  lang = sys.argv[1]
  
  if lang not in langs: 
  
    print("Language not in directory. Choose one of these languages: ")
    
    for language in langs: print(language)
    sys.exit(0)
  
  system("cp {}/shell_{}.nix {}".format(source_dir, lang, target_dir))
  
  print("Copied shell_{}.nix into your directory. Activating nix shell")
  
  system("nix-shell")


