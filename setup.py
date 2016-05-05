from setuptools import setup, find_packages

setup(
    name="seed-identity-store",
    version="0.1",
    url='http://github.com/praekelt/seed-identity-store',
    license='BSD',
    author='Praekelt Foundation',
    author_email='dev@praekeltfoundation.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django==1.9.1',
        'djangorestframework==3.3.2',
        'dj-database-url==0.3.0',
        'psycopg2==2.6.1',
        'raven==5.10.0',
        'gunicorn==19.4.5',
        'django-filter==0.12.0',
        'whitenoise==2.0.6',
        'celery==3.1.19',
        'django-celery==3.1.17',
        'redis==2.10.5',
        'pytz==2015.7',
        'django-rest-hooks==1.2.1',
        'go-http==0.3.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
