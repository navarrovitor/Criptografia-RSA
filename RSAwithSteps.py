dictionary = {"A": "00", "B": "01", "C": "02", "D": "03", "E": "04", "F": "05", "G": "06", "H": "07", "I": "08", "J": "09", "K": "10", "L": "11" ,"M": "12", "N": "13", "O": "14", "P": "15", "Q": "16", "R": "17", "S": "18", "T": "19", "U": "20", "V": "21", "W": "22", "X": "23", "Y": "24", "Z": "25"}

p = int(input("Qual seu p (um número primo)? "))
q = int(input("Qual seu q (um número primo)? "))

phi = (p-1)*(q-1)
c = 0
a = 0

def mdc(num1, num2):
  resto = None
  while resto != 0:
    resto = num1 % num2
    num1 = num2
    num2 = resto 
  return num1

while a == 0:
  c = int(input("Qual seu c? "))
  if c >= phi or c < 1:
    print("Por favor, escolha um c maior que 1 e menor que %i." % phi)
    continue
  elif mdc(c,phi) != 1:
    print("Por favor, escolha um c para que o mdc ente %i e c seja igual a 1." % phi)
  else:
    break

n = p * q

chave = [n,c]

print("O par (" + str(chave[0]) + ", " + str(chave[1]) + ") é a sua chave pública.")

mensagem = input("Insira a mensagem que deseja codificar com sua chave: ").upper()
mensagem_palavras = mensagem.split()
mensagem_junta = "".join(mensagem_palavras)

print("\nVariável mensagem:")
print(mensagem)
print("\nVariável mensagem_palavras:")
print(mensagem_palavras)
print("\nVariável mensagem_junta:")
print(mensagem_junta)

mensagem_numerada = ""
for character in mensagem_junta:
  print(character)
  mensagem_numerada += dictionary[character]
  print(mensagem_numerada)

print("\nVariável mensagem_numerada:")
print(mensagem_numerada)

mensagem_blocos = [mensagem_numerada[i:i+4] for i in range(0, len(mensagem_numerada), 4)]

print("\nVariável mensagem_blocos:")
print(mensagem_blocos)

rsa = []
for num in mensagem_blocos:
  rsa.append((int(num)**c) % n)

print("\nSua mensagem codificada é a seguinte:")
print(rsa)