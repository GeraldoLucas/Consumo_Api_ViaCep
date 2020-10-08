import requests, time

cep = input("Digite um Cep com 8 Dígitos: ")

while len(cep) != 8:
  time.sleep(1)
  print("Cep Inválido. Tente Novamente...")
  time.sleep(1)
  cep = input("Digite um Cep com 8 Dígitos: ")

# print(f"Cep {cep} Válido...")

url = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

url = url.json()

# print(url_t)

for k, v in url.items():
  print(f"-- {k}: {v}")
  time.sleep(0.4)
