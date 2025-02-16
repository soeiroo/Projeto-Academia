import json

print("Sistema da FitGym")
print("")
users = []

def user_edition():
    global users  
    try:
        with open("./users.json", "r", encoding="utf-8") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    dados = {}
    id = input("Id do usuario: ")
    dados['name'] = input("Novo nome completo: ")
    dados['age'] = input("Nova idade: ")
    dados['id'] = int(id)
    positionOfUser = -1
    for index, user in enumerate(users):
      if "id" in user:
          if user["id"] == int(id):
              positionOfUser = index
              break

    if positionOfUser != -1:  
        users[positionOfUser] = dados  
        with open("users.json", "w", encoding="utf-8") as arquivo:
            json.dump(users, arquivo, indent=4, ensure_ascii=False)
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado!")

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
    dados['id'] = len(users) + 1  

    users.append(dados)
    with open("users.json", "w", encoding="utf-8") as arquivo:
        json.dump(users, arquivo, indent=4, ensure_ascii=False)
    print("Usuário cadastrado com sucesso!")

while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Editar usuários")
    print("4 - Sair")
    print(" ")
    option = int(input("Escolha uma opção: "))
    
    if option == 1:
        user_registration()
    elif option == 3:
        user_edition()
    elif option == 4:
        break
    else:
        print("Opção inválida")
    
    salvar_usuario = input("Deseja salvar as alterações? (sim/não) ").lower()
    if salvar_usuario == "sim":
        break
    else:
        continue

print(users)
