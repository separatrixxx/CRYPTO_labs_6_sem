filename = 'texts/text1.txt'

with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    non_empty_lines = [line for line in lines if line.strip() != '']

with open(filename, 'w', encoding='utf-8') as file:
    file.writelines(non_empty_lines)