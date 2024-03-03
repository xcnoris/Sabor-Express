import datetime

# Lista de números de 1 a 10
numeros = list(range(1, 11))

# Lista com quatro nomes
nomes = ['João', 'Maria', 'Pedro', 'Ana']

print("Lista de números de 1 a 10:", numeros)
print("Lista com quatro nomes:", nomes)

# Obtendo o ano atual
ano_atual = datetime.datetime.now().year

ano_nascimento = 2000

anos = [ano_nascimento, ano_atual]

print("Lista com o ano de nascimento e o ano atual:", anos)

# Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.


for i in numeros:
    print(f'.{i}')

for num in range(10, 0, -1):
    print(num)

# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

def imprimindo_tabuada(num):
   
    for multiplicador in numeros:
        resultado = multiplicador * num
        print(f'{multiplicador} X {num} = ', resultado)
        

imprimindo_tabuada(7)

# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.



def somando_numeros_da_lista():
    lista_numeros = list(range(0,101))
    somador = 0
    for i in lista_numeros:
        somador += i
    print(f'\nA soma de todos os numeros da lista é {somador}')

somando_numeros_da_lista()

def somando_medias_de_lista():
    
    lista_numeros = [9, 8, 4, 7]
    try:
        somador = 0
        for i in lista_numeros:
            somador += i
        media = somador / int(len(lista_numeros))
        print(f'\nA media das notas é {media}')
    except:
        print('\n[Error] Valor invalido na lista')

somando_medias_de_lista()