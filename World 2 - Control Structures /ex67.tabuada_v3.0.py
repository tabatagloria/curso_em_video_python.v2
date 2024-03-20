# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo:

print('========= Tabuada =========')
n = 0
count = 0
mult = 0
while True:
    n = int(input('Digite um número inteiro, sendo número negativo para parar: '))
    if n < 0:
        print('Fim do programa!')
        break
    else:
        while count <= 10:
            mult = count * n
            print(f'{n} x {count} = {mult}')
            count +=1
        count = 0
            
        
    
        
    
    

