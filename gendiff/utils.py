import argparse, json, pathlib
    
def parse_args():    
    parser = argparse.ArgumentParser(description='Compares files and outputs the result')
    parser.add_argument("firstfile", type=pathlib.Path, help="the file to compare with")
    parser.add_argument("secondfile", type=pathlib.Path, help="the file to be compared")
    return parser.parse_args()

def parse_files(*filepaths):
    result = []
    for filepath in filepaths: 
        with open(filepath, 'r', encoding='utf-8') as f:
            result.append(json.load(f))
    return result
