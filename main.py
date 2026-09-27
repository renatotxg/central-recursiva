from central_recursiva.algoritmos import mdc, soma_digitos
from central_recursiva.excecoes import EntradaInvalida, OperacaoInvalida


def processar_operacao(linha):
    dados = linha.split()

    if not dados:
        raise EntradaInvalida()

    operacao = dados[0]

    if operacao == "M":
        if len(dados) != 3:
            raise EntradaInvalida()

        try:
            a = int(dados[1])
            b = int(dados[2])
        except ValueError:
            raise EntradaInvalida()

        if a <= 0 or b <= 0:
            raise EntradaInvalida()

        return f"MDC = {mdc(a, b)}"

    elif operacao == "S":
        if len(dados) != 2:
            raise EntradaInvalida()

        try:
            numero = int(dados[1])
        except ValueError:
            raise EntradaInvalida()

        if numero < 0:
            raise EntradaInvalida()

        return f"SOMA = {soma_digitos(numero)}"

    else:
        raise OperacaoInvalida()


def main():
    try:
        q = int(input())

        if q < 1:
            raise EntradaInvalida()

        for _ in range(q):
            linha = input()

            try:
                resultado = processar_operacao(linha)
                print(resultado)

            except EntradaInvalida:
                print("ERRO: EntradaInvalida")

            except OperacaoInvalida:
                print("ERRO: OperacaoInvalida")

            finally:
                pass

    except ValueError:
        print("ERRO: EntradaInvalida")

    except EntradaInvalida:
        print("ERRO: EntradaInvalida")


if __name__ == "__main__":
    main()
