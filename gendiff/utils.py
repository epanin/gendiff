import argparse
import json
import yaml
import pathlib


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares files and outputs the result')
    parser.add_argument("firstfile",
                        type=pathlib.Path, help="the file to compare with")
    parser.add_argument("secondfile",
                        type=pathlib.Path, help="the file to be compared")
    return parser.parse_args()


def parse_files(*filepaths):
    result = []
    for filepath in filepaths:
        if filepath.suffix == '.json':
            result.append(read_json(filepath))
        elif filepath.suffix in ('.yaml', '.yml'):
            result.append(read_yaml(filepath))
    return result


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.Loader)
