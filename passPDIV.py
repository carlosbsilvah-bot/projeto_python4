#Declarar

def main():
    valor:int = 0
    result:float = 1
    valor = int(input('Digite um valor: '))
    for num in range(1, valor, +1):
        result = result + divi(1, passParam(num))

    print('A divisão fatorial de', valor, 'é:', result)
def passParam(num):
    result:int = 1
    for num in range(num, 1, -1):
        result = result * num
    return result
def divi(num1, num2):
    return num1 / num2

if (__name__ == '__main__'):
    main()
    
