import json

print("Sistema da FitGym")
print("")
users = []

def user_registration():
  dados = {}
  dados['name'] = input("Nome completo: ")
  dados['age'] = input("Idade: ")
  
  users.append(dados)

while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Sair")
    print(" ")
    option = int(input("Escolha uma opção: "))
    if option == 1:
        user_registration()   
    elif option == 3:
        break
    else:
        print("Opção inválida")

print(users)
  
with open("users.json", "w", encoding="utf-8") as arquivo:
  json.dump(users, arquivo, indent=4, ensure_ascii=False)
  
print("mexi no código")