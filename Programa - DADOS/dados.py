salario = float(input("Informe o valor de seu salário: "))
salario_minimo = float(input("Informe o salário minimo que você receberia: "))
idade = int(input("Informe sua idade (apenas número): "))
resultado = salario > (salario_minimo * 2) and idade > 18
print("O resultado foi", resultado)