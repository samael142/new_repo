"""
Ну, если без читерства, то так:
"""


def my_func(word):
    return f'{word[0].upper()}{word[1:]}'


print(my_func('letter'))

many_words = 'mom washed the frame'.split()
for i in many_words:
    print(my_func(i), end=' ')
