from nltk.corpus import brown
import time
import nltk
import os
from Analysis import TokenListToList, StrToList

#Достаём список txt файлов с первым постом и собираем всё в AllText.txt
files = os.listdir('HTML')
txt = filter(lambda x: x.endswith('.txt'), files)
bigString = ''
for i in txt:
    with open ('HTML/' + str(i), 'r') as input_file:
        bigString += input_file.read() + '\n'
        print(i)
with open ('AllText.txt', 'wb') as output_file:
    output_file.write(bigString.encode('cp1251'))
    print('WRITE COMPLETE.')


# компонуем wordsInPosts.csv из слов с количеством их вхождений
words_list = brown.words()
words_set = set(words_list)
print("Время с запуска до начала токенизации текста: ", time.clock()-t)
post_tags = StrToList(bigString, words_set)
print(nltk.pos_tag(post_tags))
post_tags = TokenListToList(post_tags)
print(post_tags)

csv = "word;frequency;sentiment\n"
for i in post_tags:
    csv = csv + str(i[0]) + ';' + str(i[1]) + ';0;\n'

with open("wordsInPosts.csv", 'w') as output_file:
    output_file.write(csv)