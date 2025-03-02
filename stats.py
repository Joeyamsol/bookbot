def count_words(text):
    words = text.split()
    return len(words)

def dictionary_of_letters(text):
    lower_text = text.lower()
    characters = []

    for character in lower_text:
        if character not in characters:
            characters.append(character)

    result = {}

    for char in characters:
        amount = lower_text.count(char)
        result.update({f'{char}': amount})
    
    return result

def sort_dictionary(dictionary):
    items = dictionary.items()
    sdict =  sorted(items, key=lambda item: item[1], reverse=True)

    return sdict