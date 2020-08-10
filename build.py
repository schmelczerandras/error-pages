from typing import NamedTuple, Dict, List, Type
from os import makedirs, path
from sys import argv
from pathlib import Path


template_path = Path('template.html')
result_directory = Path('built')


class Substitutions(NamedTuple):
    title: str
    description: str


error_messages: Dict[str, Substitutions] = {
    '403': Substitutions(
        title='403 - Forbidden',
        description='You are not allowed to view this resource.'
    ), 
    '404': Substitutions(
        title='404 - Not found',
        description='The requested resource cannot be found.'
    ),
    '502': Substitutions(
        title='502 - Server error',
        description='Service is under maintenance.'
    ), 
    '50x': Substitutions(
        title='50x - Server error',
        description='There was a problem on our side.'
    )
}


def substitute(source: str, substitutions: Substitutions) -> str:
    for i, property_name in enumerate(Substitutions._fields):
        source = source.replace(f'{{{property_name}}}', str(substitutions[i]))
    return source


if __name__ == '__main__':
    pages_to_be_built = {k: v for k, v in error_messages.items() if k in argv[1:]}

    result_directory.mkdir(parents=True, exist_ok=True)

    with open(template_path) as f:
        template = f.read()

    for name, substitutions in pages_to_be_built.items():
        html = substitute(template, substitutions)
        with open(Path(result_directory, f'{name}.html'), 'w') as f:
            f.write(html)
