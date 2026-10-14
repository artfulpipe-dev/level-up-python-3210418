def sort_words(words):
    # return " ".join(sorted([text.lower() for text in words.split(" ")]))
    return " ".join(sorted(words.split(), key=str.lower))

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
    print(sort_words('platano NARANJA manzana'))  # manzana NARANJA platano
