def transform_view(list_of_changes):
    answer = '{\n'
    for action, key, value in list_of_changes:
        answer = answer + action + str(key) + ': ' + str(value) + '\n'
    return answer + '}\n'
