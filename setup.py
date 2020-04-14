from setuptools import setup


setup(
    name='jdv',
    version= '0.1',
    py_modules=['jdv'],
    install_requires=[
        'Click'
    ],
    entry_points ='''
        [console_scripts]
        jdv=jdv:cli
    '''
)