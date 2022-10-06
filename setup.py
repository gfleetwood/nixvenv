from setuptools import setup, find_packages
from pathlib import Path
from os import getcwd, system
import sys

home_dir = Path.home()
target_dir = getcwd()
source_dir = __file__

system("mkdir -p {}/.config/nixvenv".format(home_dir))
system("cp {}/shell*.nix {}/.config/nixvenv/".format(source_dir, target_dir))

setup(
  name = 'nixvenv',
  version = '0.1.0',
  description = 'Useful functions',
  url = '',
  author = 'gfleetwood',
  author_email = 'github.4esih@slmail.me',
  packages = find_packages(),
  license = 'MIT',
  zip_safe = False,
  entry_points = {'console_scripts': ['nixvenv = nixvenv.nixvenv:main']}
)
