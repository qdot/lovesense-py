#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import lovesense

setup(name='lovesense',
      version="{}".format(lovesense.VERSION),
	  description='Python Libraries for accessing and controlling Lovense sex toys (Max, Nora, Lush, Hush, Etc...)',
      long_description=(open('README.rst').read() + '\n' + open(os.path.join('CHANGES.rst')).read()),
      author='qDot',
      author_email='kyle@machul.is',
      url='http://github.com/metafetish/lovesense-py',
      download_url='http://pypi.python.org/packages/source/v/lovesense',
      license='BSD License',
      packages=find_packages(),
      keywords=['hardware', 'driver', 'sextoy', 'teledildonics', 'lovense'],
      install_requires=['pyserial'],
      tests_require=['pytest'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: System :: Hardware :: Hardware Drivers'
      ]
)
