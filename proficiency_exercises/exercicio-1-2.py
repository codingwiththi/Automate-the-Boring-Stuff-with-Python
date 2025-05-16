# Escreva uma função que receba uma lista de números e retorne
# uma nova lista contendo apenas os números pares elevados ao quadrado
def square_even_numbers(numbers):
    newList = []
    for i in range(len(numbers)):
        if(numbers[i] % 2 == 0):
            newList.append(numbers[i] ** 2)

    return newList

def main():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print(square_even_numbers(numbers))
    

if __name__ == "__main__":
    main()