from gendiff.utils import parse_files


def generate_diff(file_path1, file_path2):
    '''
    Compares two files as data structures. Supports json and yaml formats

        Params:
            file_path1 (PosixPath): the file to compare with
            file_path2 (PosixPath): the file to be compared

        Return:
            result (str): the result of the comparison
    '''
    list_of_changes = []
    first_file, sec_file = parse_files(file_path1, file_path2)
    full_changes = sec_file.copy()
    full_changes.update(first_file)
    for key, value in full_changes.items():
        
        value_view = str(value).lower() if isinstance(value, bool) else str(value)
        
        element_deleted = key not in sec_file
        if element_deleted:
            list_of_changes.append(('  - ', key, value_view))
            continue

        element_add = key not in first_file
        if element_add:
            list_of_changes.append(('  + ', key, value_view))
            continue
            
        element_same = value == sec_file.get(key)
        if element_same:
            list_of_changes.append(('    ', key, value_view))
            continue
        else: # element_changed
            list_of_changes.append(('  - ', key, value_view))
            new_value = sec_file.get(key)
            new_value_view = str(new_value).lower() if isinstance(new_value, bool) else str(new_value)
            list_of_changes.append(('  + ', key, new_value_view))        

    list_of_changes.sort(key=lambda x: x[1])
    return transform_view(list_of_changes)


def transform_view(list_of_changes):
    answer = '{\n'
    for action, key, value in list_of_changes:
        answer = answer + action + str(key) + ': ' + str(value) + '\n'
    return answer + '}\n'
