produto = input("Informe o nome do produto: ")
preço = float(input("Informe o preço do produto: "))
quantidade = int(input("Informe a quantidade: "))
total = preço * quantidade

print("O produto %s custa %.2f, você comprou %d e vai pagar %.2f" % (produto, preço, quantidade, total))