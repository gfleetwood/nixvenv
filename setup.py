from setuptools import setup, find_packages

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
  entry_points = {'console_scripts': ['nv_create = nixvenv.nixvenv:create', 'nv_init = nixvenv.nixvenv:init']}
)


