def troca(lista, i, j):  #Função faz a troca entre dois itens de uma lista
    lista[i], lista[j] = lista[j], lista[i]

def empurra(s):  #Função que "empurra" o maior valor da lista para o fim
    n = len(s)
    for i in range(n-1):
        if s[i] > s[i+1]:
            troca(s, i, i+1)

def bubble_sort(s):  #Função de ordenação de uma lista, comparando pares de itens
                     #Ordena o itens em ordem crescente
    n = len(s)
    while n > 1:
        empurra(s)
        n -= 1

if __name__ == '__main__':
    lista = [40, 30, 50, 10, 20]
    print(lista)
    bubble_sort(lista)
    print(lista)
