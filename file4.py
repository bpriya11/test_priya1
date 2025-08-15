# Long function, no docstring, magic numbers and nested logic
def process(data):
    for i in range(len(data)):
        if data[i] % 2 == 0:
            data[i] = data[i] * 123
            if data[i] > 250:
                data[i] = 0
        else:
            data[i] = data[i] * 7
            if data[i] < 10:
                data[i] = -1
    return data
