from visualization import visualization
from write_files import write_file_letters, write_file_words


def compare(text1, text2, n):
    counter = 0

    for i in range(n):
        if text1[i] == text2[i] and not text1[i] == ' ':
            counter += 1

    return counter / n

def compare_texts(filename1, filename2, n):
    with open(filename1, 'r', encoding='utf-8') as file1, open(filename2, 'r', encoding='utf-8') as file2:
        text1 = file1.read(n)
        text2 = file2.read(n)

        return compare(text1, text2, n)

def main():
    ans = {
        'tt': [],
        'tl': [],
        'tw': [],
        'll': [],
        'ww': []
    }

    n_values = [1000, 5000, 10000, 25000, 100000]

    ans['tt'].append('Два осмысленных текста')
    ans['tl'].append('Осмысленный текст и текст из случайных букв')
    ans['tw'].append('Осмысленный текст и текст из случайных слов')
    ans['ll'].append('Два текста из случайных букв')
    ans['ww'].append('Два текста из случайных слов')

    for n in n_values:
        write_file_words('texts/words1.txt', n)
        write_file_words('texts/words2.txt', n)
        write_file_letters('texts/letters1.txt', n)
        write_file_letters('texts/letters2.txt', n)

 
        ans['tt'].append(compare_texts('texts/text1.txt', 'texts/text2.txt', n))
        ans['tl'].append(compare_texts('texts/text1.txt', 'texts/letters1.txt', n))
        ans['tw'].append(compare_texts('texts/text1.txt', 'texts/words1.txt', n))
        ans['ll'].append(compare_texts('texts/letters1.txt', 'texts/letters2.txt', n))
        ans['ww'].append(compare_texts('texts/words1.txt', 'texts/words2.txt', n))

    print(f''.ljust(50), f'1000'.ljust(20), f'5000'.ljust(20), f'10000'.ljust(20), f'25000'.ljust(20), f'100000'.ljust(20), end='\n')
    for i in ans:
        print(f'{ans[i][0]}'.ljust(50), f'{ans[i][1]}'.ljust(20), f'{ans[i][2]}'.ljust(20),
              f'{ans[i][3]}'.ljust(20), f'{ans[i][4]}'.ljust(20), f'{ans[i][5]}'.ljust(20), end='\n')
        
    visualization(ans, n_values)


main()