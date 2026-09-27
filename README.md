#Central Recursiva

#Integrantes
- Daniel Veríssimo Nunes 26.1.16160
- Renato Guido Teixeira  26.1.20345

# Sobre o projeto

O projeto Central Recursiva foi desenvolvido em Python com o objetivo de aplicar conceitos de modularização, recursividade e tratamento de exceções.

O programa possui duas operações principais:

- M: calcula o máximo divisor comum (MDC) de dois números.
- S: calcula a soma dos dígitos de um número.

As duas operações utilizam funções recursivas.

# Estrutura do projeto

```text
central-recursiva/
├── main.py
├── .gitignore
│
└── central_recursiva/
    ├── __init__.py
    ├── algoritmos.py
    ├── excecoes.py
    └── teste.py
```

# Como executar

Para executar o programa, abra o terminal na pasta principal do projeto e utilize:

```bash
python main.py
```

Depois, informe a quantidade de operações e, em seguida, as operações que deseja realizar.

Exemplo:

```text
7
S 12345
M 72 30
M 17 19
S 0
M 0 25
S -50
X 10 20
```

O programa vai mostrar os resultados ou as mensagens de erro correspondentes.

# Módulos

# `main.py`

É o arquivo principal do projeto. Ele recebe as entradas, verifica as operações, valida os valores, chama as funções dos algoritmos e trata as exceções.

# `algoritmos.py`

Contém as duas funções recursivas do projeto:
`mdc(a, b)`: calcula o máximo divisor comum usando o algoritmo de Euclides.
`soma_digitos(numero)`: calcula a soma dos dígitos de um número de forma recursiva.

# `excecoes.py`

Contém as exceções personalizadas utilizadas no programa:

`EntradaInvalida`: usada quando os dados informados são inválidos.
`OperacaoInvalida`: usada quando é informada uma operação diferente de `M` ou `S`.

# `teste.py`

É utilizado para testar as funções `mdc()` e `soma_digitos()` com diferentes valores e verificar se os resultados estão corretos.

# `__init__.py`

Arquivo que faz parte do pacote `central_recursiva`. Neste projeto, ele não possui código, mas permite a organização dos arquivos como um pacote Python.

# Algoritmos recursivos

# MDC:

A função `mdc()` utiliza o algoritmo de Euclides. Ela chama a si mesma usando o segundo número e o resto da divisão entre os dois números.

O processo continua até que o segundo número seja igual a zero. Nesse momento, o primeiro número é retornado como resultado.

Exemplo:

```text
mdc(72, 30)
→ mdc(30, 12)
→ mdc(12, 6)
→ mdc(6, 0)
→ 6
```

# Soma dos dígitos:

A função `soma_digitos()` separa o último dígito do número e soma esse valor ao resultado da próxima chamada da função.

Por exemplo:

```text
soma_digitos(12345)

5 + soma_digitos(1234)
5 + 4 + soma_digitos(123)
5 + 4 + 3 + soma_digitos(12)
5 + 4 + 3 + 2 + soma_digitos(1)
5 + 4 + 3 + 2 + 1

Resultado: 15
```

# Tratamento de exceções

O programa possui duas exceções personalizadas para tratar situações de erro:

* `EntradaInvalida`
* `OperacaoInvalida`

Também são utilizados `try`, `except` e `finally` para tratar erros durante a execução.

Quando uma entrada possui valores inválidos, o programa apresenta:

```text
ERRO: EntradaInvalida
```

Quando a operação informada não é reconhecida, apresenta:

```text
ERRO: OperacaoInvalida
```
# Beecrowd

Problema: CentralRecursivaRobusta

Linguagem: Python

ID da submissão Accepted: # 1618087
