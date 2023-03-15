#Página de Login e Cadastro
emails = ["."]
senhas = ["."]
opc = input("Digite o que deseja realizar (Login ou Cadastro) \n").upper()
while opc != "LOGIN" and opc != "CADASTRO":
    print("Escolha uma opção existente.")
    opc = input("Digite o que deseja realizar (Login ou Cadastro) \n").upper()
    if opc == "LOGIN" or opc == "CADASTRO":
        break
if opc == "CADASTRO":
    ema = input("Digite seu email para cadastro: \n")
    emails.append(ema)
    sen = input("Digite seu senha: \n")
    senhas.append(sen)
    print("Seu email foi cadastrado em nosso sistema, porfavor realize o login.")
    ems = input("Digite seu email. \n")
    for i in emails:
        while ems != i:
            print("Digite um email existente.")
            ems = input("Digite seu email. \n")
        if ems == i:
            sens = input("Digite sua senha \n")
            for a in senhas:
                while sens != a:
                    print("Digite sua senha novamente")
                    sens = input("Digite sua senha \n")
                if sens == a:
                    print("Bem-vindo")
                    break
if opc == "LOGIN":
    ems = input("Digite o seu email \n")    
    for i in emails:
        if ems == i:
            sens = input("Digite sua senha \n")
            for o in senhas:
                if sens == o:
                    print("Bem-vindo")
                else:
                    print("Senha incorreta.")       
        if ems != i:
            print("Email incorreto ou inexistente.")                   