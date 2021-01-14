'''
Functions to work with the saved glossary text file
Assumes format: key\tvalue\n
'''

def create_dictionary(filename):
    d = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.split('\t')
            d[key] = value
    return d


def add_glossary(key, value, filename):
    with open(filename, 'a') as file:
        file.write(f'{key}\t{value}')


def edit_glossary(key, value, filename):   
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not line.startswith(f'{key}\t'):
                file.write(line)
        file.truncate()
        file.write(f'{key}\t{value}')
