import json
import os
from rich.console import *
from rich.theme import Theme
from rich.table import Table

custom_theme = Theme({"success": "bold green", "error": "bold red"})
console = Console(theme=custom_theme)

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
    
    console.log(f"Acessando banco de dados...", style="bold underline")
    users_db()
    
    dados = {}
    dados['status'] = "Ativo"
    dados['name'] = input("Nome completo: ")
    dados['age'] = input("Idade: ")
    #Criar funcionalidade que torna os ID's em números únicos para cada usuário
    max_id = int(max((user.get('id', 0) for user in users), default=0))
    dados['id'] = max_id + 1
    
    temp_dados = dados.copy()
    if ( int(temp_dados['age']) < 16):
      print("Esse usuário não está apto para se registrar.")
      return
    
    dados['id'] = str(temp_dados['id'])

    users.append(dados)
    with open("users.json", "w", encoding="utf-8") as arquivo:
        json.dump(users, arquivo, indent=4, ensure_ascii=False)
    console.print("Usuário cadastrado com sucesso!", style="success")

def user_tableDB():
  users_db()
  
  table = Table(title="Informações dos clientes")
  
  table.add_column("ID", style="orange3")
  table.add_column("Name", style="deep_sky_blue1")
  table.add_column("Idade", style="deep_sky_blue1")
  table.add_column("Status", style="magenta")
  
  for user in users:
    table.add_row(user['id'], user['name'], user['age'], user['status'])
  
  console.print(table)
    
def statusChange(userID):  
  dados = {}
  users_db()
  
  console.print("Esse usuário atualmente está:\n[1] Ativo\n[2] Inativo")
  response = int(input(": "))
  
  
  try:  # Converte para inteiro
    match response:
      case 1:
          dados["status"] = "Ativo"
      case 2:
          dados["status"] = "Inativo"
      case _:
          print('Entrada inválida, tente novamente.')
  except ValueError:
    console.print("Entrada [red]inválida![/] Digite um número [cyan]válido[/].")
  
  for user in users:
    if user["id"] == str(userID):
      user["status"] = dados["status"]
    with open("users.json", "w", encoding="utf-8") as arquivo:
        json.dump(users, arquivo, indent=4, ensure_ascii=False)
  print("Usuário atualizado com sucesso!")

#Em progresso...
#def nameChange(userID):
#  def statusChange(userID):  
#    dados = {}
#    users_db()
#    
#    console.print("Esse usuário atualmente está:\n[1] Ativo\n[2] Inativo")
#    response = int(input(": "))
    
    
#    try:  # Converte para inteiro
#      match response:
#        case 1:
#            dados["status"] = "Ativo"
#        case 2:
#            dados["status"] = "Inativo"
#        case _:
#            print('Entrada inválida, tente novamente.')
#    except ValueError:
#      console.print("Entrada [red]inválida![/] Digite um número [cyan]válido[/].")
#    
#    for user in users:
#      if user["id"] == str(userID):
#        user["status"] = dados["status"]
#      with open("users.json", "w", encoding="utf-8") as arquivo:
#          json.dump(users, arquivo, indent=4, ensure_ascii=False)
#    print("Usuário atualizado com sucesso!")
    
def user_edition():
  global users  
    
    
  users_db()


  dados = {}
  id = input("ID do usuario: ")
  for user in users:
    if ( user['id'] == str(id) ):
      console.print(f"[bold]O que você deseja modificar do usuário[/] [bold deep_sky_blue1]{user['name']}[/]?")
      console.print("[1] Alterar seu Status")
      console.print("[2] Alterar seu Nome")
      console.print("[3] Alterar sua idade")
      
    
  response = int(input(": "))
  try:
    match response:
      case 1:
        statusChange(id)
  except (ValueError):
    console.print("Entrada [red]inválida![/] Digite um número [cyan]válido[/].")
      
      
  dados['name'] = input("Novo nome completo: ")
  dados['age'] = input("Nova idade: ")
  dados['id'] = id
#  positionOfUser = -1
#  for index, user in enumerate(users):
#    if "id" in user:
#        if user["id"] == id:
#            positionOfUser = index
#            break

#  if positionOfUser != -1:  
#      users[positionOfUser] = dados  
#      with open("users.json", "w", encoding="utf-8") as arquivo:
#          json.dump(users, arquivo, indent=4, ensure_ascii=False)
#      print("Usuário atualizado com sucesso!")
#  else:
#      print("Usuário não encontrado!")
        
        
def users_remove():
  global users

  users_db()
    
  temp_ID = input("Insira o ID do usuário que deseja remover: ")
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

#Foi substituido pelo users_tableDB
#def users_list():
#  global users
#  try:
#    with open("users.json", "r", encoding="utf-8") as arquivo:
#      users = json.load(arquivo)
#  except (FileNotFoundError, json.JSONDecodeError):
#    users = []
#  
#  for user in users:
#    print(f"{user['id']} - {user['name']}")


while True:
    console.print("-------[bold]FITGYM[/]-------")
    console.print("--------------------")
    console.print("1 - Cadastrar novo usuário", style="bold pale_green1")
    console.print("2 - Listar usuários", style="bold deep_sky_blue1")
    console.print("3 - Editar usuários", style="bold")
    console.print("4 - Remover usuários", style="bold red")
    console.print("5 - Sair", style="bold")
    console.print("6 - Teste")
    console.print("--------------------")
    option = int(input("Escolha uma opção: "))
    
    if option == 1:
      clear()
      user_registration()   
    elif option == 2:
      clear()
      user_tableDB()
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
      print("Teste")
    else:
        print("Opção inválida")
    
    salvar_usuario = console.input("[bold]Deseja voltar ao menu principal?[/] [bold orange3](Y/N)[/] ").lower()
    if salvar_usuario == 'n':
        break
    else:
        clear()
        continue

