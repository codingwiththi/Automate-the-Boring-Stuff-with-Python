# Escreva uma função que receba um número e retorne:
# - "Fizz" se o número for divisível por 3
# - "Buzz" se o número for divisível por 5
# - "FizzBuzz" se o número for divisível por ambos
# - O próprio número como string se não for divisível por nenhum
def fizzbuzz(number):
    if number % 3 == 0 and number % 8 == 0:
        return "FizzBuzz"
    else:
        if number % 3 == 0:
            return "Fizz"
        if number % 8 == 0:
            return "Buzz"
    return str(number) 

def main():
    number = int(input("Digite um número: "))
    print(fizzbuzz(number))

if __name__ == "__main__":
    main()

