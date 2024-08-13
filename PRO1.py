def cumprimento(texto):
    return f"Olá, {texto}"

nome_completo = "Alinne Citlali Gutiérrez Rohs"
cumprimento(nome_completo)

import random

def sorteio_media():
    numeros = [random.randint(1, 10**6) for _ in range(3)]
    media = sum(numeros) / len(numeros)
    return numeros, media
numeros, media = sorteio_media()

f"Média aritmética: {media}"
