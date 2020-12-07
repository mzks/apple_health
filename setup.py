import setuptools

with open('requirements.txt') as f:
    requires = [
        r.split('/')[-1] if r.startswith('git+') else r
        for r in f.read().splitlines()]

with open('README.md') as file:
    readme = file.read()


setuptools.setup(
    name='apple_health',
    version='1.1',
    description='Data manager of exported iPhone health data',
    author='Keita Mizukoshi (@mzks)',
    url='https://github.com/mzks/apple_health',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requires,
    python_requires=">=3.6",
    zip_safe=False)
