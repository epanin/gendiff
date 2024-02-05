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
    list_of_changes = []
    first_file, sec_file = parse_files(file_path1, file_path2)
    full_changes = sec_file.copy()
    full_changes.update(first_file)
    for key, value in full_changes.items():
        if key not in sec_file:
            list_of_changes.append(('-', key, value))
        else:
            if value == sec_file.get(key):
                if key not in first_file:
                    list_of_changes.append(('+', key, value))
                else:
                    list_of_changes.append((' ', key, value))
            else:
                list_of_changes.append(('-', key, value))
                list_of_changes.append(('+', key, sec_file.get(key)))
    list_of_changes.sort(key=lambda x: x[1])
    return transform_answer(list_of_changes)

def transform_answer(list_of_changes):
    answer = '{\n'
    for action, k, v in list_of_changes:
        answer = answer + action + ' ' + str(k) + ': ' + str(v) + '\n'
    return answer + '}\n'
