import random

def main():
    ideias = [
        "Criar um aplicativo de lista de tarefas",
        "Desenvolver um site pessoal",
        "Automatizar backups de arquivos",
        "Fazer um bot para redes sociais",
        "Montar um gerador de senhas seguras",
        "Construir um sistema de controle financeiro",
        "Desenvolver um jogo simples em Python",
        "Criar um analisador de textos",
        "Montar um sistema de notificações por email",
        "Fazer um programa de conversão de unidades"
    ]

    ideia_escolhida = random.choice(ideias)
    print("Sua ideia aleatória é:")
    print(ideia_escolhida)

if __name__ == "__main__":
    main()