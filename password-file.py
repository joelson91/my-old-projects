print('Diário pessoal')
nome = input("Digite sua senha: ")
while nome != "ask12":
    nome = input("Digite novamente ou saia: ")
print ("Fim da execução")
print ("Acesso liberado")
print ("")
print ("Diário pessoal")
print ("escolha uma vítma")
print ("digite 1 para Fulano")
print ("digite 2 para Ciclano")
vitima = float(input("Digite aqui: "))
if vitima == 1:
    print ("Você escolheu Fulano")
    print ("")
    senha = float(input("Digite a senha: "))
    if senha == 123:
        print ("Acesso liberado")
        print ("")
        print ("Ele gosta de goiaba fresca.")
    else:
        print ("Você não tem permição para acessar")
    
if vitima == 2:
    print ("Você escolheu Ciclano")
    print ("")
    senha = float(input("Digite a senha: "))
    if senha == 321:
        print ("Acesso liberado")
        print ("")
        print ("Ele brinca com bonecas.")
