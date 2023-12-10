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

    l = 0
    disco = {}
    for i in range(num_col):
        col = []
        for j in range(num_row):
            col.append(arr[j][i])
        disco[key[l]] = col
        l = l + 1

    myKeys = list(disco.keys())
    myKeys.sort()
    sorted_dict = {i: disco[i] for i in myKeys}

    result_dict = {key: ''.join(value) for key, value in sorted_dict.items()}
    result_string = ''.join(result_dict.values())

    return result_string

# Example usage:
key = "HACK"
msg = 'Geeks for Geeks'
cipher = encrypt_message(msg, key)
print(cipher)
