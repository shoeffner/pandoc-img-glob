# -*- coding: utf-8 -*-

from setuptools import setup

import re

from pandoc_img_glob import __version__

REPOSITORY = 'https://github.com/shoeffner/pandoc-img-glob'

README = ''
with open('README.rst', 'r') as f:
    README = f.read()
README = re.sub(r' _(.+): ([^(http)].+)', r' _\1: {}/blob/master/\2'
                .format(REPOSITORY), README)

setup(
  name='pandoc-img-glob',
  version=__version__,
  description='A pandoc filter for globbing image paths in multi file projects.',  # noqa
  long_description=README,
  entry_points={'console_scripts': ['pandoc-img-glob = pandoc_img_glob:main']},
  author='Sebastian Höffner',
  author_email='info@sebastian-hoeffner.de',
  url=REPOSITORY,
  download_url='{}/tarball/{}'.format(REPOSITORY, __version__),
  packages=['pandoc_img_glob'],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Programming Language :: Python :: 3.6',
      'Topic :: Text Processing :: Filters',
  ],
  install_requires=['panflute'],
  license='MIT',
  keywords=['pandoc', 'image', 'multifile', 'filter'],
)
