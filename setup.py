from setuptools import setup, find_packages

project_name = 'Contas a pagar e receber'
version = '0.0.1'
description = 'Projeto simples utilizando o Fastapi para contruir APIS Rest'
author = 'Tiago Nunes da Silva'
author_email = 'tiagofalcaoshow12@gmail.com'
url = 'https://github.com/tiago-falcao12/contas-a-pagar-e-receber-fastapi.git'
license = 'MIT'

# Leitura do README para usar como descrição longa
# with open('README.md', 'r', encoding='utf-8') as f:
#     long_description = f.read()

# Lista de dependências do projeto
dependencies = [
    'fastapi==0.79.0',
    'requests>=2.0',
    'uvicorn==0.14.0',
    'python-decouple==3.8'
]

setup(
    name=project_name,
    version=version,
    description=description,
    # long_description=long_description,
    long_description_content_type='text/markdown',
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    packages=find_packages(),
    install_requires=dependencies,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
