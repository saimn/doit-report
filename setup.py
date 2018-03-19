from setuptools import setup

setup(
    name='doit-report',
    version='0.1',
    license='MIT',
    author='Simon Conseil',
    author_email='contact@saimon.org',
    url='http://github.com/saimn/doit-report',
    description='Show ASCII or HTML report for doit task execution status',
    long_description=open('README.md').read(),
    py_modules=['doit_report'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    python_requires='>=3.5',
    keywords=['doit'],
    install_requires=['doit', 'astropy'],
    entry_points={
        'doit.COMMAND': [
            'report = doit_report:ReportCmd'
        ]
    },
)
