# -*- coding: utf-8 -*-

from distutils.core import setup

import re

from pandoc_img_glob import __version__

REPOSITORY = 'https://github.com/shoeffner/pandoc-img-glob'

README = ''
with open('README.rst', 'r') as f:
    README = f.read()
README = re.sub(r' _(.+): ([^(http)].+)', r' _\1: {}/blob/master/\2'
                .format(REPOSITORY), README)

REQUIREMENTS = []
with open('requirements.txt', 'r') as f:
    REQUIREMENTS = filter(None, f.read().split('\n'))

setup(
  name='pandoc-img-glob',
  version=__version__,
  description='',
  long_description=README,
  entry_points={'console_scripts': ['pandoc-img-glob = pandoc_img_glob:main']},
  author='Sebastian Höffner',
  author_email='info@sebastian-hoeffner.de',
  url=REPOSITORY,
  download_url='{}/tarball/{}'.format(REPOSITORY, __version__),
  py_modules=['pandoc_img_glob'],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Programming Language :: Python :: 3.6',
      'Topic :: Text Processing :: Filters',
  ],
  install_requires=REQUIREMENTS,
  license='MIT',
  keywords=['pandoc', 'image', 'multifile', 'filter'],
)
