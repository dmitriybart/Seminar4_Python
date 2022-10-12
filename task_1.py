# Транслетирация
# transleterate = \
# {'а': 'a','б': 'b','в': 'v','г' : 'g','д' : 'd','е' : 'e','ж' : 'zh','з' : 'z','и' : 'i',
# 'й' : 'y','к' : 'k','л' : 'l','м' : 'm','н' : 'n','о' :'o','п' : 'p','р' : 'r','с' : 's',
# 'т' : 't','у' : 'u','ф' : 'f','х' : 'kh','ц' : 'ts','ч' : 'ch','ш' : 'sh','щ' : 'shch',
# 'ь' : '\'','ы' :'y','ъ' : '','э' : 'e','ю' : 'yu','я' : 'ya'}
# text = input('input: ')

# for i in text:
#     print(transleterate[i], end = "")

aplphabetE = \
['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p','r',
's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '\'', 'e', 'yu', 'ya']

aplphabetR = \
['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

base = input('Введите слово: ')
word=[]

for i in range(len(base)):
    word.append(aplphabetR.index(base[i]))
    index = word[i]
    print(aplphabetE[index], end='')