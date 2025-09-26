import random
random.seed(18)

colisionTimes:int = 0

def main():
    global colisionTimes
    vet: int = [0] * 101

    printarVetor(vet)
    gerarVetorHash(vet, 60, 101)
    printarVetor(vet)
    print(f"Quantidade de colisoes ocorridas: {colisionTimes}")
    colisionTimes = 0

    vet = [0] * 211

    printarVetor(vet)
    gerarVetorHash(vet, 60, 211)
    printarVetor(vet)
    print(f"Quantidade de colisoes ocorridas: {colisionTimes}")
    colisionTimes = 0

    vet = [0] * 307

    printarVetor(vet)
    gerarVetorHash(vet, 60, 307)
    printarVetor(vet)
    print(f"Quantidade de colisoes ocorridas: {colisionTimes}")
    colisionTimes = 0

    return

#--------------------------------------------------------------------------------------

def gerarVetorHash(vet, keys, sizeArray):
    value: int
    for i in range(keys):
        value = random.randint(100000, 200000)
        print(value)
        hashing(vet, value, sizeArray)
    return

def hashing(vet, value, sizeArray):
    index:int = value % sizeArray
    if vet[index] != 0:
        colision(vet, index, value, sizeArray)
        return
    vet[index] = value
    return

def colision(vet, index, value, sizeArray):
    global colisionTimes
    colisionTimes += 1
    for i in range(index + 1, sizeArray):
        if vet[i] == 0:
            vet[i] = value
            break
    return

def printarVetor(vet):
    print("[ ", end='')
    for i in vet:
        print(f"{i} ", end = '')
    print("]")
    return

#--------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
