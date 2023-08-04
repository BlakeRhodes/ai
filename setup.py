import setuptools

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name='ai',
    version='0.0.1',
    author='Blake Rhodes',
    author_email='blakewrhodes@gmail.com',
    description='Your own, personal, AI, assistant.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BlakeRhodes/ai',
    project_urls={
        'Bug Tracker': 'https://github.com/BlakeRhodes/ai/issues'
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'langchain==0.0.251',
        'openai==0.27.8',
        'setuptools==68.0.0',
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'ai = ai.ai:main',
        ]
    }
)
