from gendiff.utils import parse_files

def generate_diff(file_path1, file_path2):
    '''
    {
    - follow: false
    host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
    }
    '''
    result = parse_files(file_path1, file_path2)
    print(result)