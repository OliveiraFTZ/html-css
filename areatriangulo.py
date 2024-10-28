def calcular_area(base, altura):
    return (base * altura) / 2

def main():
    while True:
        try:
            base = float(input("Informe a base do triângulo: "))
            altura = float(input("Informe a altura do triângulo: "))
            if base > 0 and altura > 0:
                break
            else:
                print("A base e a altura devem ser números positivos. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    area = calcular_area(base, altura)

    print("\nResultados:")
    print(f"Valor da Base do triângulo: {base}")
    print(f"Valor da Altura do triângulo: {altura}")
    print(f"Valor da Área do triângulo: {area:.2f}")

if __name__ == "__main__":
    main()
