import sys
import os

def findWords(words):
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    result = []
    for word in words:
        lower_word = set(word.lower())
        if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
            result.append(word)
    return result

# Ejemplos de uso
words1 = ["Hello", "Alaska", "Dad", "peace"]
words2 = ["omk"]
words3 = ["adsdf", "sfd"]

print(findWords(words1))  # Salida: ["Alaska", "Dad"]
print(findWords(words2))  # Salida: []
print(findWords(words3))  # Salida: ["adsdf", "sfd"]
if __name__ == "__main__":

    # Change the current working directory to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Run the script
    os.system(f'python "{os.path.basename(__file__)}"')