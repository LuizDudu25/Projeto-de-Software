print("Deseja logar ou cadastrar?\n")
print("(1) Logar\n")
print("(2) Cadastrar\n\n")

choice = input("Digite: ")

users = []
passwords = []

if choice == '1':
    user = input("CPF: ")
    password = input("\nSenha: ")
    
    if user not in users:
        print("\nUsuário nao cadastrado, tente novamente\n")
    else:
        if password == passwords[users.index(user)]:
            print("\nLogin realizado com sucesso!\n")
        else:
            print("\nSenha incorreta, tente novamente\n")
elif choice == '2':
    user = input("Digite seu CPF: ")
    password = input("Escolha uma senha: ")
    cpass = input("Confirme a senha: ")
    
    if password == cpass:
        users.append(user)
        passwords.append(password)
        print("\nCadastro criado com sucesso!\n")
    else:
        print("\nAs senhas não correspondem, tente novamente\n")
else:
    print("\nO número digitado não corresponde a um comando\n")