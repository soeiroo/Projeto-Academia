import json


#Função que puxa as informações do {users.json} para a variável users. Usem!
def users_db():
  global users
  
  try:
    with open("users.json", "r", encoding="utf-8") as arquivo:
      users = json.load(arquivo)
  except (FileNotFoundError, json.JSONDecodeError):
    users = []

users = []

def user_registration():
  global users
  
  users_db()
  
  dados = {}
  
#Fique a vontade para adicionar mais dados
  dados["id"] = 1
  dados["name"] = input("Nome completo: ")
  dados["status"] = "Ativo"
  dados["age"] = int(input("Idade: "))
  dados["cpf"] = int(input("CPF: "))
  
  if ( dados["age"] > 16):
    print("Esse usuário não está apto para se registrar.")
    awaiting = input(" - Digite qualquer coisa para voltar - ") 
    return
  #Esse return não está funcionando, procurar uma solução

  
#Faça uma função que forneça id únicos para os usuários de forma crescente, ex: 1 - Pedro, 2 - Maria
  
  users.append(dados)
  
#Código que permite o salvamento de informações dentro do {users.json}
  with open("users.json", "w", encoding="utf-8") as arquivo:
    json.dump(users, arquivo, indent=4, ensure_ascii=False)

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
        awaiting = input(" - Digite qualquer coisa para voltar - ")
    else:
      print("ID inválido/Não existente")
      awaiting = input(" - Digite qualquer coisa para voltar - ")


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
    print("3 - Modificar informações de um usuário")
    print("4 - Remover informações de um usuário")
    print("5 - Sair")
    print("--------------------")
    
    option = int(input("Escolha uma opção: "))
    if option == 1:
      user_registration()   
    elif option == 2:
      users_list()
    elif option == 3:
      break
    elif option == 4:
      users_remove()
    elif option == 5:
      break
    else:
      print("Opção inválida")
        