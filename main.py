import json


def users_db():
  global users
  
  try:
    with open("users.json", "r", encoding="utf-8") as arquivo:
      users = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    users = []



def user_registration():
    global users 
    
    users_db()
    
    dados = {}
    dados['name'] = input("Nome completo: ")
    dados['age'] = input("Idade: ")
    dados['id'] = len(users) + 1  
    
    #Esse return não está funcionando, procurar uma solução
    #if ( dados["age"] > 16):
    #  print("Esse usuário não está apto para se registrar.")
    #  awaiting = input(" - Digite qualquer coisa para voltar - ") 
    #  return

    users.append(dados)
    with open("users.json", "w", encoding="utf-8") as arquivo:
        json.dump(users, arquivo, indent=4, ensure_ascii=False)
    print("Usuário cadastrado com sucesso!")
#Função que puxa as informações do {users.json} para a variável users. Usem!


def user_edition():
    global users  
    
    users_db()

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
        
        
def users_remove():
  global users

  users_db()
    
  temp_ID = int(input("Insira o ID do usuário que deseja remover: "))
  for user in users:
    if ( user["id"] == temp_ID ):
      print(f"Tem certeza que deseja remover a conta de {user['name']} ?")
      response = input("(Y/N): ")
      if ( response == 'y' or 'Y' ):
        users.remove(user)
        with open("users.json", "w", encoding="utf-8") as arquivo:
          json.dump(users, arquivo, indent=4, ensure_ascii=False)
        
        print("Usuário removido com sucesso!")
        
    else:
      print("ID inválido/Não existente")
      


def users_list():
  global users
  try:
    with open("users.json", "r", encoding="utf-8") as arquivo:
      users = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    users = []
  
  counter = 0
  for user in users:
    counter+=1
    print(f"{counter} - {user['name']}")


while True:
    print("-------FITGYM-------")
    print("--------------------")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Editar usuários")
    print("4 - Remover informações de um usuário")
    print("5 - Sair")
    print("--------------------")
    option = int(input("Escolha uma opção: "))
    
    if option == 1:
      user_registration()   
    elif option == 2:
      users_list()
    elif option == 3:
        user_edition()
    elif option == 4:
      users_remove()
    elif option == 5:
      break
    else:
        print("Opção inválida")
    
    salvar_usuario = input("Deseja voltar ao menu principal? (Y/N) ").lower()
    if salvar_usuario == 'n':
        break
    else:
        continue

