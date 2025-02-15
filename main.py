import json

print("Sistema da FitGym")
print("")
users = []

def user_registration():
  dados = {}
  dados['name'] = input("Nome completo: ")
  dados['age'] = input("Idade: ")
  
  users.append(dados)
  
with open("users.json", "w", encoding="utf-8") as arquivo:
  json.dump(users, arquivo, indent=4, ensure_ascii=False)
  
  