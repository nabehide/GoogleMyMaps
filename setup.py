from setuptools import setup


setup_args = {
    'name': 'GoogleMyMaps',
    'version': '1.1.0',
    'license': 'MIT',
    'description': 'Python parser for Google My Maps.',
    'url': 'https://github.com/nabehide/GoogleMyMaps',
    'package_dir': {
        'GoogleMyMaps': 'GoogleMyMaps',
    },
    'packages': [
        'GoogleMyMaps',
    ],
    'install_requires': [
        'beautifulsoup4',
        'pyjsparser',
    ],
}

setup(**setup_args)
