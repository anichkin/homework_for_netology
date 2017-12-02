import collections


def top10(text):
    from xml.etree import ElementTree as ET

    tree = ET.parse(text)
    root = tree.getroot()
    channel = root.find('channel')
    news_items = channel.findall('item')
    all_news = []
    words = []
    for i, news in enumerate(news_items):
        all_news.append((news_items[i][2].text).split())
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
        print('файл newsafr.xml')
        top10('newsafr.xml')
        print()
        print('файл newscy.xml')
        top10('newscy.xml')
        print()
        print('файл newsfr.xml')
        top10('newsfr.xml')
        print()
        print('файл newsit.xml')
        top10('newsit.xml')
        print()
        program()
    elif command == '2':
        text = input('Введите название текста с расширением ')
        top10(text)
        program()


program()
