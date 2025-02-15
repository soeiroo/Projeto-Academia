import json

print("Sistema da FitGym")
print("")
users = []

def user_registration():
  global users
  
  try:
    with open("users.json", "r", encoding="utf-8") as arquivo:
      users = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    users = []
  
  dados = {}
  dados['name'] = input("Nome completo: ")
  dados['age'] = input("Idade: ")
  
  users.append(dados)
  with open("users.json", "w", encoding="utf-8") as arquivo:
    json.dump(users, arquivo, indent=4, ensure_ascii=False)

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
    
    salvar_usuario = input("Deseja salvar o usuário? (sim/não) ").lower()
    if salvar_usuario == "sim":
        break
    else:
        break

print(users)