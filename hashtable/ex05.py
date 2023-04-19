def comptmot():
    phrase = "je suis beau beau beau"
    mots = phrase.split()
    occurences = {}
    for mot in mots:
        if mot in occurences:
            occurences[mot] += 1
        else:
            occurences[mot] = 1
    print(f"le mot {mot} apparait {occurences} fois dans cette phrase.")
comptmot()
