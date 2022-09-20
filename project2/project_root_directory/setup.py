from setuptools import setup

setup(name='useful',
      version='1',
      description='Very useful code',
      author='Maria',
      author_email='mariyav14012010@gmail.com',
      license='MIT',



    # ...,
    entry_points={
        'console_scripts': [
            'clean-file = timmins.mysor:main',
        ]
    }
)