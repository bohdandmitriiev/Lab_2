def get_words_array (sentence):  #параметр функции с которым она работает
    words = sentence.split()
    print (f"Кількість символів у реченні-{len(sentence)}")
    print (f"Кількість слів в реченні-{len(words)}")
    return words

def print_letters_count (words_array):
    for word in words_array:
        print (f"Кількість букв у слові \"{word}\"-{len(word)}")

    

sentence = (input("Введіть речення-"))
array = get_words_array(sentence)
print_letters_count(array)


