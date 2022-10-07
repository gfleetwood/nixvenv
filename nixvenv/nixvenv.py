#!/usr/bin/python

from os import getcwd, system, chdir
import sys
from pathlib import Path

home_dir = Path.home()
target_dir = getcwd()
source_dir = __file__

def init():

  config_dir = "{}/.config/nixvenv".format(home_dir)

  system("mkdir -p {}".format(config_dir))
  chdir(config_dir)

  system("git clone https://github.com/gfleetwood/nixvenv")
  system("mv nixvenv/shells/* .")
  system("rm -rf nixvenv")

def create():

  target_dir = getcwd()
  source_dir = __file__

  langs = ["r", "python"]
  lang = sys.argv[1]
  
  if lang not in langs: 
  
    print("Language not in directory. Choose one of these languages: ")
    
    for language in langs: print(language)
    sys.exit(0)
  
  system("cp {}/.config/nixvenv/shell_{}.nix {}/shell.nix".format(home_dir, lang, target_dir))
  print("Copied shell_{}.nix into your directory. Activating nix shell".format(lang))
  system("nix-shell")
  


