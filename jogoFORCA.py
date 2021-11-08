from random import choice
from random import randint

palavras= ['ZOOLÓGICO', 'DELEGACIA', 'PADARIA', 'LIVRARIA', 'LANCHONETE', 'SORVETERIA', 'PIZZARIA', 'SUPER MERCADO' , 'CABELEIREIRO', 'SHOPPING', 'BAR', 'BOATE',
           'FAIXA DE PEDESTRE' ,'ESCOLA', 'HOSPITAL', 'PEDESTRE', 'UNIVERSIDADE', 'PRAÇA DE LAZER', 'POSTO DE GASOLINA', 'POSTO DE SAÚDE', 'PENITENCIÁRIA']

palavra= choice(palavras)

u= []
erros = 0
acertos= 0
dica=True

print('Descubra a palavra secreta que pertence ao assunto "Na cidade".')

def acentuar():
    global u, jogada, palavra
    if jogada in 'AEIOU':   
        for letra in palavra:
            if letra in 'ÁÃÀ' and jogada == 'A':
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
            elif letra in 'É' and jogada == 'E':
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
            elif letra in 'Í' and jogada == 'I' :
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
            elif letra in 'ÓÕ' and jogada == 'O':
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
            elif letra in 'ÚÜ' and jogada == 'U' :
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
def acentuardica():
    global u, l, palavra
    if l in 'AEIOU':   
        for letra in palavra:
            if letra in 'ÁÃÀ' and l == 'A':
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
            elif letra in 'É' and l == 'E':
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
            elif letra in 'Í' and l == 'I' :
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
            elif letra in 'ÓÕ' and l == 'O':
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
            elif letra in 'ÚÜ' and l == 'U' :
                acentuada= letra
                ind_acentuada= palavra.find(acentuada)
                u.pop(ind_acentuada)
                u.insert(ind_acentuada, acentuada)
    

for letra in palavra:
    if letra == ' ':
        u.append(' ')
    else:
        u.append('_')

while True:
    jogada=input('Digite uma letra que você acredita que existe na palavra ou chute ou tecle "enter" para revelar uma letra: ').strip().upper()
    if jogada == palavra:
        print('Parabéns!!!')
        break
    if jogada == '' and dica == True:
        while True:
            indice= randint(0, len(palavra)-1)
            l= palavra[indice]
            if u[indice]== '_':
                break
        acentuardica()
        for c, letra in enumerate(palavra):
            if l == letra:
                u.pop(c)
                u.insert(c, l)
        dica=False
    elif jogada == '' and dica == False:
        print('Ops!!! Você não pode obter mais nenhuma dica.')
        
    
    if jogada in palavra:
        acentuar()
        for c, letra in enumerate(palavra):
            if jogada == letra:
                u.pop(c)
                u.insert(c, letra)
    else:
        erros += 1
        if erros == 6:
            print(f'Você foi enforcado!!!A palavra é "{palavra}".')
            break
        else:
            print(f'Você cometeu {erros} erro(s).Você pode errar mais {5 - erros} vez(es).') 
    
    for item in u:
        print(f' {item}', end= '')
    print()
    for item in u:
        if item == '_':
            break
        else:
            acertos += 1
    if acertos == len(palavra):
        print('Parabéns!!!')
        break
    acertos = 0