def read_data():
    with open('files\input\data.csv', 'r') as file:
        data = file.readlines()
        data = [line.strip().split('\t') for line in data]
    return data