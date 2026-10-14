import re

def is_palindrome(phrase):
    # Quitar lo que no sea a-z o A-Z. Poner todo en minusculas
    clean_text = re.sub(r"[^a-zA-Z]", "", phrase).lower()
    print(clean_text) 
    reversed_text = ""
    # Dar la vuelta al texto y comparar si son iguales
    for l in clean_text:
        reversed_text = l + reversed_text
    print(reversed_text)
    return clean_text == reversed_text

# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome("dabale arroz a la zorra el abad"))  # true
