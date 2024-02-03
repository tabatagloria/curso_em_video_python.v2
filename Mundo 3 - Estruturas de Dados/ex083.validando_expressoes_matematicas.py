# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input('Digite uma expressão matemática: ')
chaves1 = expressao.count('{')
chaves2 = expressao.count('}')
colchetes1 = expressao.count('[')
colchetes2 = expressao.count(']')
parenteses1 = expressao.count('(')
parenteses2 = expressao.count(')')
if chaves1 == chaves2 and colchetes1 == colchetes2 and parenteses1 == parenteses2:
    print('A expressão matemática é válida!')
else:
    print('A expressão matemática é inválida!')



