from nltk.corpus import brown
import time
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer


#переводит токенизированный список в список содержащий только все встреченные Adverb и Adjective и их количество
def TokenListToList(post_tags):
    _post_tags = nltk.pos_tag(post_tags)
    _answer = []
    _counter = []
    for i in range(post_tags.__len__()):
        if _post_tags[i][1] in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']:
            try:        # метод index выкидывает эксепшен если такого элемента нет
                ind = _answer.index(_post_tags[i][0])
            except ValueError:
                ind = ''
            if ind != '':       # если такой элемент есть, то ind = идексу этого элемента в списке _answer[]
                _counter[ind]+=1
                continue
            _answer.append(_post_tags[i][0])  #Добавляем не всреченное ранее слово и ставим счётчик на 1
            _counter.append(1)
    _answerList = []
    for i in range(_answer.__len__()):
        _answerList.append([_answer[i], _counter[i]])
    return _answerList


#убирает все разделительные символы, а так же разделяет на слова
def StrToList(str, words_set):
    _list = []
    _str = ''
    for _i in str:
        if ((_i >= "a") and _i <= "z") or ((_i >= "A") and _i <= "Z") or _i == "\-" or _i == "\`":
            _str += _i.lower()
        else:
            if _str != '' and (_str in words_set):
                _list.append(_str)
            _str = ''
    if _str != '':
        _list.append(_str)
    return _list


#nltk.download('brown')
words_list = brown.words()
words_set = set(words_list)
t=time.clock()

bigString = ''

with open('AllText.txt', 'r') as input_file:
    bigString += input_file.read() + '\n'

''' Функцинальность перенесена в файл DownloadHTML.py
#   Test url
url = 'https://www.devexpress.com/Support/Center/Question/Details/T690250/how-to-use-stored-procedure-in-transaction-with-xpo-asp-net'
r = requests.get(url)

#   write to test-file
with open('HTML/test.html', 'wb') as output_file:
    output_file.write(r.text.encode('cp1251', errors='replace')) # Кодировка - дефолтная в русской винде,
                                                                 # вылезали нечитаемые символы, отсюда - replace

print("Время с начала до открытия файла: ", time.clock()-t)
#   take text from page
#   scratch text
r = open('HTML/test.html', 'r')
text = r.read()
#print(type(text))
tree = html.fromstring(text)
#print(type(tree))
post = tree.xpath('//div[@class = "edited-text"]/text()')
#print(type(post))
str = ''
for i in post:
    str += i
    str += '\n'
''' #Функциональность перенесена в файл DownloadHTML.py


print("Время с запуска до начала токенизации текста: ", time.clock()-t)
post_tags = StrToList(bigString, words_set)
print(nltk.pos_tag(post_tags))
post_tags = TokenListToList(post_tags)
print(post_tags)

''' Пока заккоментим лемматизацию, она мне всю морфологию ломает
print("Время с начала до лемматизации полученного набора слов: ", time.clock()-t)
#   Lemmatization of words
lem = WordNetLemmatizer()
port = PorterStemmer()
print("Время с начала до применения функций лемматизации", time.clock()-t)
lem_words = []
for i in post_tags:
    cur = port.stem(i)
    if cur in words_set:
        lem_words.append(cur)
    else:
        lem_words.append(lem.lemmatize(i))
print("Время окончания лемматизации: ", time.clock() - t)
print(set(lem_words))
''' #Особенности лемматизации ломают необходимую для покраски морфологию

#post_tags = list(set(post_tags))

csv = "word;frequency;sentiment\n"
for i in post_tags:
    csv = csv + str(i[0]) + ';' + str(i[1]) + ';0;\n'

with open("wordsInPosts.csv", 'w') as output_file:
    output_file.write(csv)
print("Время окончания перевода в set: ", time.clock() - t)