print("Bem-vindo ao inventario\n")
print("O que deseja fazer?\n")
print("(1) Inserir item no inventario\n")
print("(2) Adicionar item ao inventario\n")
print("(3) Remover item do inventario\n")

oprt = input("Digite: ")

items = []

if oprt == '1':
    item = input("Digite o nome do item: ")
    
    if item not in items:
        print("\nO item nao se encontra no inventario\n")
    else:
        frequencia = items.count(item)
        print("\nO item se encontra no inventario em uma quantidade de ")
        print(frequencia)
        print("\n")
elif oprt == '2':
    item = input("Digite o nome do item: ")
    items.append(item)
    print("Item adicionado com sucesso")
elif oprt == '3':
    item = input("Digite o nome do item: ")
    
    if item not in items:
        print("\nO item nao se encontra no inventario\n")
    else:
        print("\nTem certeza de que deseja remover esse item?\n")
        print("(1) Sim\n")
        print("(2) Nao\n");
        
        choice = input("Digite: ")
        
        if choice == '1':
            print("\nItem removido com sucesso!\n")
        elif choice == '2':
            print("\nOperacao cancelada!\n")
else:
    print("\nO número digitado não corresponde a um comando\n")
