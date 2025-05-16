# Exercícios de Proficiência em Python

Este conjunto de exercícios está organizado por nível de dificuldade e mapeado aos capítulos do livro "Automate the Boring Stuff with Python". Complete-os para identificar quais partes do livro você pode pular.

## Nível 1: Fundamentos Básicos (Capítulos 1-3)

### Exercício 1.1: Operações Básicas
```python
# Escreva uma função que receba um número e retorne:
# - "Fizz" se o número for divisível por 3
# - "Buzz" se o número for divisível por 5
# - "FizzBuzz" se o número for divisível por ambos
# - O próprio número como string se não for divisível por nenhum
def fizzbuzz(number):
    # Seu código aqui
    pass
```

### Exercício 1.2: Funções e Listas
```python
# Escreva uma função que receba uma lista de números e retorne
# uma nova lista contendo apenas os números pares elevados ao quadrado
def square_even_numbers(numbers):
    # Seu código aqui
    pass
```

### Exercício 1.3: Controle de Fluxo
```python
# Escreva uma função que receba uma senha e verifique se é forte
# Para ser forte, deve ter:
# - Pelo menos 8 caracteres
# - Pelo menos uma letra maiúscula
# - Pelo menos um número
# - Pelo menos um caractere especial (!@#$%^&*)
# Retorne True se for forte, False caso contrário
def is_strong_password(password):
    # Seu código aqui
    pass
```

## Nível 2: Estruturas de Dados (Capítulos 4-6)

### Exercício 2.1: Manipulação de Listas
```python
# Escreva uma função que receba uma lista e retorne a mesma lista
# com os valores ordenados, mas mantendo os tipos originais no mesmo lugar
# Exemplo: ["b", 1, "a", 2] retorna ["a", 1, "b", 2]
def sort_by_type(mixed_list):
    # Seu código aqui
    pass
```

### Exercício 2.2: Dicionários
```python
# Escreva uma função que conte a frequência de cada palavra em um texto
# e retorne as 5 palavras mais frequentes em um dicionário
# Ignore pontuação e considere maiúsculas/minúsculas como iguais
def top_five_words(text):
    # Seu código aqui
    pass
```

### Exercício 2.3: Manipulação de Strings
```python
# Escreva uma função que converta um texto em "leet speak"
# Substituições: A->4, E->3, I->1, O->0, S->5, T->7
# Exemplo: "TESTE" se torna "73573"
def to_leet_speak(text):
    # Seu código aqui
    pass
```

## Nível 3: Padrões e Regex (Capítulos 7-9)

### Exercício 3.1: Expressões Regulares Básicas
```python
# Escreva uma função que extraia todos os endereços de email válidos de um texto
# Um email válido tem formato username@dominio.extensão
import re

def extract_emails(text):
    # Seu código aqui
    pass
```

### Exercício 3.2: Validação de Dados
```python
# Escreva uma função que valide um formato de data dd/mm/yyyy
# Considere anos bissextos e número correto de dias por mês
def is_valid_date(date_string):
    # Seu código aqui
    pass
```

### Exercício 3.3: Manipulação de Arquivos
```python
# Escreva uma função que leia um arquivo CSV de produtos
# com colunas "id,nome,preço,quantidade"
# e retorne o valor total do estoque (preço * quantidade para cada item)
def calculate_inventory_value(csv_file_path):
    # Seu código aqui
    pass
```

## Nível 4: Automação de Arquivos (Capítulos 10-11)

### Exercício 4.1: Organização de Arquivos
```python
# Escreva uma função que organize arquivos em uma pasta
# movendo-os para subpastas baseadas na extensão do arquivo
# Ex: .jpg vai para /imagens, .mp3 para /audio, etc.
import os
import shutil

def organize_files_by_type(directory_path):
    # Seu código aqui
    pass
```

### Exercício 4.2: Debugging
```python
# O código abaixo tem bugs. Identifique e corrija-os.
def find_largest_number(filename):
    largest = 0
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                if number > largest:
                    largest = number
            except:
                continue
    return largest
```

## Nível 5: Web e Dados (Capítulos 12-17)

### Exercício 5.1: Web Scraping
```python
# Escreva uma função que extraia os títulos das notícias da página principal do G1
# Utilize requests e BeautifulSoup
import requests
from bs4 import BeautifulSoup

def get_g1_headlines():
    # Seu código aqui
    pass
```

### Exercício 5.2: Planilhas e JSON
```python
# Escreva uma função que leia dados de um arquivo JSON
# e os escreva em uma nova planilha Excel, com formatação
import json
import openpyxl

def json_to_excel(json_file, excel_output):
    # Seu código aqui
    pass
```

### Exercício 5.3: Automação de Tempo e Tarefas
```python
# Escreva uma função que registre o tempo de execução de uma função
# e agende sua execução para rodar a cada 5 minutos
import time
import schedule

def measure_and_schedule(function_to_measure):
    # Seu código aqui
    pass
```

## Nível 6: GUI e Imagens (Capítulos 18-20)

### Exercício 6.1: Manipulação de Imagens
```python
# Escreva uma função que redimensione todas as imagens em uma pasta
# para terem largura máxima de 800px, mantendo a proporção
from PIL import Image

def resize_images(folder_path):
    # Seu código aqui
    pass
```

### Exercício 6.2: Automação de GUI
```python
# Escreva uma função que automatize abrir o Bloco de Notas, 
# digitar uma mensagem e salvá-la com nome específico
import pyautogui
import time

def automate_notepad(message, filename):
    # Seu código aqui
    pass
```

### Exercício 6.3: Projeto Integrado
```python
# Crie um script que:
# 1. Monitore uma pasta por novos arquivos CSV
# 2. Quando um arquivo novo aparecer, leia os dados
# 3. Crie um gráfico com matplotlib baseado nos dados
# 4. Envie o gráfico por email para um endereço específico
# Utilize bibliotecas como watchdog, matplotlib, pandas e smtplib

# Seu código completo aqui
```

## Instruções para Auto-Avaliação

Para cada seção que você conseguir completar confortavelmente **sem consultas**:

- **Nível 1 completo**: Você pode pular os Capítulos 1-3
- **Nível 2 completo**: Você pode pular os Capítulos 4-6
- **Nível 3 completo**: Você pode pular os Capítulos 7-9
- **Nível 4 completo**: Você pode pular os Capítulos 10-11
- **Nível 5 completo**: Você pode pular os Capítulos 12-17
- **Nível 6 completo**: Você pode pular os Capítulos 18-20

Se você fizer um exercício com facilidade, mas precisar de consultas para outro da mesma seção, considere estudar apenas as partes específicas do capítulo relacionadas à sua dificuldade.

## Dicas

- Tente resolver os exercícios sem consulta primeiro
- Se travar em um, anote o conceito específico que você não domina
- Use estes exercícios como referência para revisitar mais tarde
- Os primeiros exercícios são mais simples e os últimos mais desafiadores