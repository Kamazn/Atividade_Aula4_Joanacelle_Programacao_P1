peso = float(input("Digite o seu peso: ")) # Recebe o peso que o usuario coloca
altura = float(input("Digite a sua altura: ")) # Recebe a altura que o usuario coloca
imc = peso / (altura ** 2) # Calcula o IMC dividindo o peso pela altura elevada ao quadrado

print("Resultado do IMC:", imc) # Printa o resultado do índice de massa (IMC)
