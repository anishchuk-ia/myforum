from setuptools import setup, find_packages

setup(
    name = "myforum",
    version = "0.1",
    packages = find_packages(),
    package_data={'myforum': [
            'static/myforum/*',
            'static/admin/html/*',
            'static/admin/img/*',
            'static/admin/js/*',
            'static/css/*',
            'static/img/*',
            'static/js/*',
            'templates/*.html',
            'templates/myforum/*.html',
            'templates/registration/*.html',
            'templates/registration/*.txt',
            'fixtures/*'
    ]},
)
