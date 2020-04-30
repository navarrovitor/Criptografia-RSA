import RSA

print("Bem vindo,\nNesse programa você pode codificar uma mensagem ou decodificar uma mensagem em RSA.")

while True:
  escolha = int(input("\nEscolha entre as opções:\n1. Codificar\n2. Decodificar\n3. Sair\n"))

  if escolha == 1:
    RSA.codificar()
    continue
  
  elif escolha == 3:
    break

  else:
    print("Por favor, escolha uma opção válida")
    continue