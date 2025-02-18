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

clear()

def user_registration():
  global users 
    
  console.log(f"Acessando banco de dados...", style="bold underline")
  users_db()
    
  dados = {
      "status": "Ativo",
      "name": input("Nome completo: "),
      "age": input("Idade: ")
  }
    
  max_id = max((int(user.get('id', 0)) for user in users), default=0)
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
  
  current_page = 0
  users_per_page = 10
  total_users = len(users)
  total_pages = (total_users + users_per_page - 1) // users_per_page

  console = Console()

  while True:
      # Cria uma nova tabela a cada iteração
    table = Table(title="Informações dos clientes", caption=f"Página: {current_page + 1}/{total_pages}\n")
    table.add_column("ID", style="orange3", justify="center", min_width=5, max_width=10)
    table.add_column("Nome", style="deep_sky_blue1", min_width=30, max_width=50)
    table.add_column("Idade", style="deep_sky_blue1", justify="center", min_width=5, max_width=7)
    table.add_column("Status", style="magenta", justify="center", min_width=10, max_width=15)

    start_index = current_page * users_per_page
    end_index = min(start_index + users_per_page, total_users)

        # Adiciona as linhas à tabela
    for user in users[start_index:end_index]:
      table.add_row(str(user['id']), user['name'], str(user['age']), user['status'])

    clear()
    console.print(table)

    console.print("[1] [bold orange3]Próxima Página[/]")
    console.print("[2] [bold orange3]Página anterior[/]")
    console.print("[3] [bold]Sair[/]")

    try:
      response = int(input(": "))
    except ValueError:
      console.print("[bold red]Entrada inválida! Por favor, insira um número.[/]")
      continue

    match response:
      case 1:
        if current_page < total_pages - 1:
          current_page += 1
        else:
          console.print("[bold]Não há mais páginas[/]")
      case 2:
        if current_page > 0:
          current_page -= 1
        else:
          console.print("[bold]Você já está na primeira página[/]")
      case 3:
        break
      case _:
        console.print("[bold red]Opção inválida! Por favor, escolha uma opção válida.[/]")
    
  
def user_infoCheck():
  users_db()
  
  userID = int(input("ID do cliente\n: "))
  
  table = Table(title="Informações do cliente")
  
  table.add_column("ID", style="orange3", justify="center")
  table.add_column("Nome", style="deep_sky_blue1")
  table.add_column("Idade", style="deep_sky_blue1", justify="center")
  table.add_column("Status", style="magenta", justify="center")
  
  for user in users:
    if user["id"] == str(userID):
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


def nameChange(userID):  
    dados = {}
    users_db()
    
    console.print("[bold]Qual o nome que deseja colocar a esse usuário?[/]")
    response = input(": ")
   
    dados["name"] = response
    
    for user in users:
      if user["id"] == str(userID):
        user["name"] = dados["name"]
      with open("users.json", "w", encoding="utf-8") as arquivo:
        json.dump(users, arquivo, indent=4, ensure_ascii=False)
    print("Usuário atualizado com sucesso!")
    
def ageChange(userID):
  dados = {}
  users_db()
    
  console.print("[bold]Qual a idade que deseja colocar para esse usuário?[/]")
  response = int(input(": "))
  
  dados["age"] = str(response)
  
  
  for user in users:
    if user["id"] == str(userID):
      user["age"] = dados["age"]
    with open("users.json", "w", encoding="utf-8") as arquivo:
      json.dump(users, arquivo, indent=4, ensure_ascii=False)
  print("Usuário atualizado com sucesso!")
    
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
      case 2:
        nameChange(id)
      case 3:
        ageChange(id)
  except (ValueError):
    console.print("Entrada [red]inválida![/] Digite um número [cyan]válido[/].")
    
  dados['id'] = id
      
        
def users_remove():
  users_db()
  
  user_found = False
  
  temp_ID = console.input("[bold]Insira o [orange3]ID[/] do [deep_sky_blue1]usuário[/] que deseja [red]remover[/]: ")
  
  for user in users:
    if ( user['id'] == temp_ID ):
      user_found = True
      
      console.print(f"[bold]Tem certeza que deseja remover a conta de [deep_sky_blue1]{user['name']}[/]?")
      response = console.input("[orange3](Y/N):[/] ").lower()
      
      if ( response == 'y' ):
        users.remove(user)
        with open("users.json", "w", encoding="utf-8") as arquivo:
          json.dump(users, arquivo, indent=4, ensure_ascii=False)
        
        print("Usuário removido com sucesso!")
        
      else:
        console.print("[bold]Operação [red]cancelada[/].")
  if not user_found:
    console.print("[bold red]ID inválido ou não existente.[/]")
      
      
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
    console.print("3 - Consultar informações de um usuário", style="bold deep_sky_blue2")
    console.print("4 - Editar usuários", style="bold")
    console.print("5 - Remover usuários", style="bold red")
    console.print("6 - Sair", style="bold")
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
      user_infoCheck()
    elif option == 4:
      clear()
      user_edition()
    elif option == 5:
      clear()
      users_remove()
    elif option == 6:
      clear()
      break
    else:
        print("Opção inválida")
    
    salvar_usuario = console.input("[bold]Deseja voltar ao menu principal?[/] [bold orange3](Y/N)[/] ").lower()
    if salvar_usuario == 'n':
        break
    else:
        clear()
        continue

