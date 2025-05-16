# Escreva uma função que receba uma senha e verifique se é forte
# Para ser forte, deve ter:
# - Pelo menos 8 caracteres
# - Pelo menos uma letra maiúscula
# - Pelo menos um número
# - Pelo menos um caractere especial (!@#$%^&*)
# Retorne True se for forte, False caso contrário
def is_strong_password(password):
    # Seu código aqui
    temMaiuscula = False
    temNumero = False
    temCaractereEspecial = False
    if(len(password) < 8):
        return False
    else:
        for i in range(len(password)):
            especiais = "!@#$%^&*"
            for j in range(len(especiais)):
                if(password[i] == especiais[j]):
                    temCaractereEspecial = True
            if(password[i].isupper()):
                temMaiuscula = True
            if(password[i].isdigit()):
                temNumero = True
            

    if(temCaractereEspecial and temMaiuscula and temNumero):
        return True
    else:
        return False

def main():
    password = "ABCdef@1"
    print(is_strong_password(password))
    

if __name__ == "__main__":
    main()