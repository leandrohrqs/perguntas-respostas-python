perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for index_pergunta, pergunta in enumerate(perguntas):
    acertos = 0
    print(f"Questão {index_pergunta + 1}: {pergunta['Pergunta']}")
    for index_opcao, opcao in enumerate(pergunta['Opções']):
        print(f"{index_opcao}) {opcao}")
    resposta = int(input("Digite a resposta correta: "))
    if pergunta["Opções"][resposta] == pergunta["Resposta"]:
        print("Acertou ✔")
        acertos += 1
    else:
        print("Errou ❌")
print(f"Você acertou {acertos} de {len(perguntas)}")
