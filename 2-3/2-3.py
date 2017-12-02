import json
import collections


def top10(text, coding):
    with open(text, encoding=coding) as news_file:
        all_news = []
        news = json.load(news_file)
        for word in news["rss"]["channel"]['items']:
            all_news.append(word['description'].split())
        words = []
        for i, line in enumerate(all_news):
            for word in line:
                words.append(word)
        freq = collections.Counter()
        for word in words:
            if len(word) > 6:
                freq[word] += 1
        sorted_count_pairs = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        top10 = sorted_count_pairs[:10]
        for word, freq in top10:
            print('Слово "{}" встретилось {} раз'.format(word, freq))


def program():
    print('введите команду: ')
    print('1 - вывод по всем файлам')
    print('2 - ручной ввод')
    command = input('введите команду: ')
    if command == '1':
        print('файл newsafr.json')
        top10('newsafr.json', 'UTF-8')
        print()
        print('файл newscy.json')
        top10('newscy.json', 'KOI8-R')
        print()
        print('файл newsfr.json')
        top10('newsfr.json', 'ISO-8859-5')
        print()
        print('файл newsit.json')
        top10('newsit.json', 'CP1251')
        print()
        program()
    elif command == '2':
        text = input('Введите название текста с расширением ')
        coding = input('Введите кодировку файла ')
        top10(text, coding)
        program()


program()
