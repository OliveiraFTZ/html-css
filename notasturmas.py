def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def main():
    while True:
        try:
            quantidade_alunos = int(input("Informe a quantidade de alunos (entre 2 e 7): "))
            if 2 <= quantidade_alunos <= 7:
                break
            else:
                print("Por favor, informe um número entre 2 e 7.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    alunos = {}

    for _ in range(quantidade_alunos):
        nome = input("Informe o nome do aluno: ")
        while True:
            try:
                nota1 = float(input(f"Informe a primeira nota de {nome} (entre 0.0 e 10.0): "))
                nota2 = float(input(f"Informe a segunda nota de {nome} (entre 0.0 e 10.0): "))
                if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
                    break
                else:
                    print("As notas devem estar entre 0.0 e 10.0. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        media = calcular_media(nota1, nota2)
        alunos[nome] = media

    media_turma = sum(alunos.values()) / quantidade_alunos
    aluno_maior_media = max(alunos, key=alunos.get)
    aluno_menor_media = min(alunos, key=alunos.get)

    print("\nResultados:")
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Quantidade de alunos na turma: {quantidade_alunos}")
    print(f"Aluno com a maior média: {aluno_maior_media} com média {alunos[aluno_maior_media]:.2f}")
    print(f"Aluno com a menor média: {aluno_menor_media} com média {alunos[aluno_menor_media]:.2f}")

if __name__ == "__main__":
    main()
