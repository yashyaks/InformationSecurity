'''Row Transposition'''

import math

def encrypt_message(msg, key):
    msg_len = len(msg)
    msg_lst = list(msg)

    num_col = len(key)
    num_row = int(math.ceil(msg_len / num_col))

    fill_null = int((num_row * num_col) - msg_len)
    msg_lst.extend('_' * fill_null)

    k = 0
    arr = []
    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(msg_lst[k])
            k = k + 1
        arr.append(row)

    # Rearrange rows based on the key
    sorted_rows = [arr[i] for i in key]

    result_string = ''.join(''.join(row) for row in sorted_rows)

    for i in arr:
        print(i)
    print('\n')
    for i in sorted_rows:
        print(i)

    return result_string

# Example usage:
key = [2, 0, 1, 3]  # Example key for row transposition
msg = 'Geeks for Geeks'
cipher = encrypt_message(msg, key)
print(cipher)
