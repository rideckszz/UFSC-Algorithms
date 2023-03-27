#Você foi contratado para fazer a autenticação dos usuários de um sistema. Nesse momento de testes,
# o sistema terá 5 nomes de usuários pré-cadastrados, que são eles: Anakin, Darth_Vader, Luke, Leia
#  e Darth_Sid

user = (input("Digite seu usuario: "))

if user == "Anakin" or user == "Darth_Vader" or user == "Luke" or user == "Leia" or user == "Darth_Sid":
    print (user, "Seja muito bem vindo")
else:
    print (user, "Não cadastrado")