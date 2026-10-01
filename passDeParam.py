#Declarar

def main():
    valor:int = 0

    valor = int(input('Digite um valor: '))
    print('O fatorial de', valor, 'é:', passParam(valor))

def passParam(num):
    result:int = 1
    for num in range(num, 1, -1):
        result = result * num
    return result

if (__name__ == '__main__'):
    main()
    
