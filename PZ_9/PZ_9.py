#Организовать словарь 10 русско-английских слов,
#обеспечивающий перевод русского слова на английский
dictionary = {
    "яблоко": "apple",
    "банан": "banana",
    "вишня": "cherry",
    "апельсин": "orange",
    "мандарин": "grape",
    "киви": "kiwi",
    "черника": "blueberry",
    "ежевика": "blackberry",
    "лимон": "lemon",
    "лайм": "lime"
}
russian_word = input("Введите, пожалуйста, русское слово: ")
if russian_word in dictionary:
    translation = dictionary[russian_word]
    print("Перевод слова", russian_word, "на английский:", translation)
else:
    print("Данного слова, к сожалению, нет в словаре")
