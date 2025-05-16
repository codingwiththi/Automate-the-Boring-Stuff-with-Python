import string
# Escreva uma função que conte a frequência de cada palavra em um texto
# e retorne as 5 palavras mais frequentes em um dicionário
# Ignore pontuação e considere maiúsculas/minúsculas como iguais
def top_five_words(text):
   # 1. Colocar tudo em minúsculas
    text = text.lower()

    # 2. Remover pontuação
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Separar palavras
    text_splitted = text.split()

    dicionario = {}

    for palavra in text_splitted:
        if palavra not in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra] += 1


    top_5 = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True)[:5])
    return top_5

def main():
    texto = "python é uma linguagem de programação poderosa python é fácil de aprender e python é muito popular muitas pessoas usam python para automação ciência de dados e desenvolvimento web python é uma excelente escolha para iniciantes e profissionais"
    print(top_five_words(texto))
    

if __name__ == "__main__":
    main()