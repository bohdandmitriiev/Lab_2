def get_words_array (sentence):  
    words = sentence.split()
    print (f"Кількість символів у реченні-{len(sentence)}")
    print (f"Кількість слів в реченні-{len(words)}")
    return words

def print_letters_count (words_array):
    for word in words_array:
        print (f"Кількість букв у слові \"{word}\"-{len(word)}")


def get_reversed_string(string):
    res=''
    for i in range(len(string)-1,-1,-1):
        res+=string[i]
    print (f"Відзеркалене речення-{res}")


sentence = (input("Введіть речення-"))
get_reversed_string(sentence)
array = get_words_array(sentence)
print_letters_count(array)


