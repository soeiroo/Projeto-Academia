import json
import os

#Função que puxa as informações do {users.json} para a variável users. Usem!
def users_db():
  global users
  
  try:
    with open("users.json", "r", encoding="utf-8") as arquivo:
      users = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    users = []

def clear():
  os.system('cls')


def user_registration():
    global users 
    
    users_db()
    
    dados = {}
    dados['name'] = input("Nome completo: ")
    dados['age'] = int(input("Idade: "))
    #Criar funcionalidade que torna os ID's em números únicos para cada usuário
    dados['id'] = len(users) + 1

    if ( dados['age'] < 16):
      print("Esse usuário não está apto para se registrar.")
      return

    users.append(dados)
    with open("users.json", "w", encoding="utf-8") as arquivo:
        json.dump(users, arquivo, indent=4, ensure_ascii=False)
    print("Usuário cadastrado com sucesso!")


def user_edition():
    global users  
    
    
    users_db()

    dados = {}
    id = input("Id do usuario: ")
    dados['name'] = input("Novo nome completo: ")
    dados['age'] = int(input("Nova idade: "))
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
    if ( user['id'] == temp_ID ):
      print(f"Tem certeza que deseja remover a conta de {user['name']} ?")
      response = input("(Y/N): ").lower()
      if ( response == 'y' ):
        users.remove(user)
        with open("users.json", "w", encoding="utf-8") as arquivo:
          json.dump(users, arquivo, indent=4, ensure_ascii=False)
        
        print("Usuário removido com sucesso!")
        
      else:
        print("ID inválido/Não existente")
      
def user_details():
  users_db()

  print("Detalhes ()")

def users_list():
  global users
  try:
    with open("users.json", "r", encoding="utf-8") as arquivo:
      users = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    users = []
  
  for user in users:
    print(f"{user['id']} - {user['name']}")


while True:
    print("-------FITGYM-------")
    print("--------------------")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Editar usuários")
    print("4 - Remover informações de um usuário")
    print("5 - Sair")
    print("6 - Teste")
    print("--------------------")
    option = int(input("Escolha uma opção: "))
    
    if option == 1:
      clear()
      user_registration()   
    elif option == 2:
      clear()
      users_list()
    elif option == 3:
      clear()
      user_edition()
    elif option == 4:
      clear()
      users_remove()
    elif option == 5:
      clear()
      break
    elif option == 6:
      clear()
      print("Use para testar")
    else:
        print("Opção inválida")
    
    salvar_usuario = input("Deseja voltar ao menu principal? (Y/N) ").lower()
    if salvar_usuario == 'n':
        break
    else:
        clear()
        continue

