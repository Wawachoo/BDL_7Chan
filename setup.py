from setuptools import setup


setup(name='bdl.engines.sevenchan',
      version='1.0.0',
      description='7chan.org engine for BDL',
      url='https://www.github.com/Wawachoo/BDL_7Chan',
      author='Wawachoo',
      author_email='Wawachoo@users.noreply.github.com',
      license='GPLv3',
      classifiers = ['Development Status :: 3 - Alpha',
                     'Environment :: Console',
                     'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 3 :: Only',
                     'Communications :: File Sharing',
                     'Topic :: Internet'],
      keywords='7Chan download',
      packages=['bdl.engines.sevenchan', ],
      entry_points = {'bdl.engines': ['module=bdl.engines.sevenchan']},
      install_requires=['lxml', 'requests'],
      package_data={"bdl.engines.sevenchan": ["sites.json", ]})
