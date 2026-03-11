def print_backwards(value):
    if len(value) > 0:
        print(value[len(value) - 1], end='', sep='')
        print_backwards(value[0:len(value) - 1])
    else:
        print()


def format_names(value):
    out = []
    for member in value:
        if member[member.index(" ") - 1] != ",":
            out.append(f"{member.split(' ')[1]}, {member.split(' ')[0]}")
        else:
            out.append(member)
    return out


def sum_a(data):
    a_sum = 0
    for dictionary in data:
        for key, value in dictionary.items():
            if key == 'a':
                a_sum += int(value)
    return a_sum


def process_list(value):
    out = []
    for i in range(0, len(value), 2):
        out.append(str(value[i]))
    for i in range(1, len(value), 2):
        out.append(value[i] * 10)
    return out


def group_by(val, func):
    if not val:
        return {}

    out_dict = group_by(val[:-1], func)
    value = val[-1]
    key = func(value)

    if key in out_dict:
        out_dict[key].append(value)
    else:
        out_dict[key] = [value]

    return out_dict


# group_by([1, 2, 3, 4, 5, 6, 7, 8], lambda x: x % 2 == 0)
print(group_by([1, 2, 3, 4, 5, 6, 7, 8], lambda x: x % 2 == 0))
