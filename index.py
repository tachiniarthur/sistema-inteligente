import random

def questionario_tecnologia():
    print("Questionário para Descobrir a Área de Tecnologia Ideal\n")
    nome = input("Por favor, digite seu nome: ")

    print("\nOlá,", nome, "Vamos começar!")

    perguntas = [
        "Qual é a probabilidade de você preferir resolver problemas lógicos e algorítmicos?",
        "Qual é a probabilidade de você gostar mais de trabalhar na interface do usuário?",
        "Qual é a probabilidade de você se sentir confortável trabalhando com servidores e infraestrutura?",
        "Qual é a probabilidade de você preferir aprender e usar novas tecnologias?",
        "Qual é a probabilidade de você gostar de trabalhar em equipe?",
        "Qual é a probabilidade de você preferir trabalhar em regime home-office?",
        "Qual é a probabilidade de você preferir trabalhar em um ambiente de trabalho presencial?",
        "Qual é a probabilidade de você ter experiência com linguagens como PHP, Python ou Java?",
        "Qual é a probabilidade de você ter experiência com tecnologias front-end como HTML, CSS e JavaScript?",
        "Qual é a probabilidade de você ter experiência com ferramentas de automação de infraestrutura como Terraform ou Ansible?",
        "Qual é a probabilidade de você ter experiência com sistemas operacionais como Linux ou Windows?",
        "Qual é a probabilidade de você ter experiência com bancos de dados SQL ou NoSQL?",
        "Qual é a probabilidade de você ter experiência com controle de versão utilizando Git?",
        "Qual é a probabilidade de você ter experiência com desenvolvimento de APIs?"
    ]

    respostas = []

    for i, pergunta in enumerate(perguntas):
        print("\n", pergunta)
        resposta = input("Escolha uma opção de probabilidade de 0 a 100%: ")

        while not resposta.isdigit() or int(resposta) < 0 or int(resposta) > 100:
            print("Por favor, escolha uma probabilidade entre 0 e 100.")
            resposta = input("Escolha uma opção de probabilidade de 0 a 100%: ")

        respostas.append(int(resposta))

    print("\nObrigado por completar o questionário, ", nome, "!\nAqui estão suas respostas:")

    print("\nAgora vamos analisar suas respostas para determinar a área de tecnologia mais adequada para você.\n")

    # Calculando a pontuação para cada área com base nas respostas
    pontuacao_desenvolvimento_backend = (
        respostas[0] * 0.8 + 
        respostas[2] * 0.6 + 
        respostas[3] * 0.7 + 
        respostas[4] * 0.6 +  
        respostas[5] * 0.5 +  
        (100 - respostas[6]) * 0.5 + 
        respostas[7] * 0.7 + 
        respostas[10] * 0.6 + 
        respostas[11] * 0.6 + 
        respostas[12] * 0.7 + 
        respostas[13] * 0.6
    )

    pontuacao_desenvolvimento_frontend = (
        respostas[1] * 0.8 + 
        respostas[3] * 0.6 + 
        respostas[4] * 0.7 +  
        respostas[6] * 0.5 +  
        (100 - respostas[5]) * 0.5 +  
        respostas[8] * 0.7 + 
        respostas[9] * 0.6 + 
        respostas[11] * 0.6 + 
        respostas[12] * 0.7 + 
        respostas[13] * 0.6
    )

    pontuacao_devops = (
        respostas[2] * 0.8 + 
        respostas[3] * 0.7 + 
        respostas[4] * 0.6 +  
        respostas[6] * 0.5 +  
        (100 - respostas[5]) * 0.5 +  
        respostas[9] * 0.7 + 
        respostas[10] * 0.6 + 
        respostas[11] * 0.6 + 
        respostas[12] * 0.7 + 
        respostas[13] * 0.6
    )

    areas = {
        "Desenvolvimento Back-end": pontuacao_desenvolvimento_backend,
        "Desenvolvimento Front-end": pontuacao_desenvolvimento_frontend,
        "DevOps": pontuacao_devops
    }

    area_recomendada = max(areas, key=areas.get)

    print("Com base nas suas respostas, a área de tecnologia recomendada para você é:", area_recomendada)

questionario_tecnologia()
