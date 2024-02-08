from gendiff.utils import parse_files


def generate_diff(file_path1, file_path2):
    '''

    '''
    list_of_changes = []
    first_file, sec_file = parse_files(file_path1, file_path2)
    full_changes = sec_file.copy()
    full_changes.update(first_file)
    for key, value in full_changes.items():
        if isinstance(value, bool):
            value_str = str(value).lower()
        else:
            value_str = str(value)

        if key not in sec_file:
            list_of_changes.append(('  - ', key, value_str))
        else:
            if value == sec_file.get(key):
                if key not in first_file:
                    list_of_changes.append(('  + ', key, value_str))
                else:
                    list_of_changes.append(('    ', key, value_str))
            else:
                list_of_changes.append(('  - ', key, value_str))
                new_value = sec_file.get(key)
                if isinstance(new_value, bool):
                    new_value = str(new_value).lower()
                list_of_changes.append(('  + ', key, new_value))
    list_of_changes.sort(key=lambda x: x[1])
    return transform_view(list_of_changes)


def transform_view(list_of_changes):
    answer = '{\n'
    for action, key, value in list_of_changes:
        answer = answer + action + str(key) + ': ' + str(value) + '\n'
    return answer + '}\n'
