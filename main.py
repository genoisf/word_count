#créé par Francis Genois
#créé en 2023
#projet tp1 qui sert à calculer le nombre de mot dans une phrase

#Je compte le nombre de mots d'une chaîne de caractère
def count_word(phrase):
    return len(phrase.split(" "))

x = count_word("trash")
print(x)