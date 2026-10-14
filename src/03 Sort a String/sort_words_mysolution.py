def sort_words(words):
    return " ".join(sorted([text.lower() for text in words.split(" ")]))

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
    print(sort_words('platano naranja manzana'))  # manzana naranja platano
