from gendiff.main import generate_diff


def test_generate_diff():
    result = generate_diff('tests/fixtures/file1.json', 
                           'tests/fixtures/file2.json')
    awaiting = '''{
    - follow: false
    host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
    }'''
    assert result == awaiting