import collections


def top10(text, coding):
    with open(text, encoding=coding) as f:
        all_news = [f.read().strip('\n')]
        words = all_news[0].split()
        freq = collections.Counter()
        for word in words:
            if len(word) > 6:
                freq[word] += 1
        sorted_count_pairs = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        top10 = sorted_count_pairs[:10]
        for word, freq in top10:
            print('Слово {} встретилось {} раз'.format(word, freq))


def program():
    print('введите команду: ')
    print('1 - вывод по всем файлам')
    print('2 - ручной ввод')
    command = input('введите команду: ')
    if command == '1':
        print('файл newsafr.txt')
        top10('newsafr.txt', 'UTF-8')
        print()
        print('файл newscy.txt')
        top10('newscy.txt', 'KOI8-R')
        print()
        print('файл newsfr.txt')
        top10('newsfr.txt', 'ISO-8859-5')
        print()
        print('файл newsit.txt')
        top10('newsit.txt', 'CP1251')
        print()
        program()
    elif command == '2':
        text = input('Введите название текста с расширением ')
        coding = input('Введите кодировку файла ')
        top10(text, coding)
        program()


program()
