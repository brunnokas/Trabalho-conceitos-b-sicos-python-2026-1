import streamlit as st

# ============================================================
# Portfólio de Exercícios Python — Interface Streamlit
# ============================================================

st.set_page_config(
    page_title="Atividade 1 Sérgio",
    page_icon="🐍",
    layout="centered",
)

# ---------- códigos-fonte originais (para exibição) ----------

CODIGO_1_SOMA = '''\
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

soma = num1 + num2
# exibe o resultado
print (f'A soma dos números {num1} e {num2} é igual a {soma}')
'''

CODIGO_2_MEDIA = '''\
nota1 = float(input('Digite a primeira Nota: '))
nota2 = float(input('Digite a segunda Nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print (f'A media das notas foi de: {media:.2f}')

if media >= 7:
    print ('Você foi Aprovado!')
elif media >=5:
    print ('Você foi reprovado!!')
else:
    print ('Você passou Vergonha!')
'''

CODIGO_3_METROS = '''\
metros = float(input('Digite o valor em metros:'))

centim = metros * 100

print (f'{metros} Metros é igual a {centim} CM')
'''

CODIGO_4_PAROUIMPAR = '''\
num1 = int(input('Digite um número inteiro: '))

if num1 % 2 == 0:
    print (f'{num1} é Par')
else:
    print (f'{num1} é ìmpar')
'''

CODIGO_6_MAIOR_MENOR = '''\
num1 = int(input('Digite o primeiro Número:'))
num2 = int(input('Digite o segundo Número:'))

if num1 > num2:
    print (f'O numero {num1} é maior que o número {num2}!')
elif num2 > num1:
    print(f'O numero {num2} é maior que o número {num1}!')
else:
    print ('Eles são iguais')
'''

CODIGO_7_REPETICAO = '''\
for num in range (1,11):
    print (num)
'''

CODIGO_8_SOMA_NUMEROS = '''\
num1 = int(input('Digite um Número inteiro: '))

soma = 0
for i in range (1,num1 +1):
    soma += i
print (f'A soma de 1 até {num1} é de {soma}')
'''

CODIGO_9_TABUADA = '''\
numero = int(input('Digite um Número: '))

print (f"=-=-=-TABUADA DO {numero} =-=-=-")

for i in range(1,11):
    print(f"{numero} x {i} = {numero *i}")
'''

CODIGO_10_AREA = '''\
print ('=-=-=-=- Calcular a área de um Retangulo =-=-=-=-')

altura = float(input('Digite qual a altura: '))
base = float(input('Digite qual a base: '))

area = base * altura

print (f'A área é igual a {area:.2f}')
'''

CODIGO_11_TEMPERATURA = '''\
celsius = float(input('Digite a temperatura em Celsius:'))

fahrenheit = (celsius * 1.8) + 32

print (f'{celsius}°C é igual a {fahrenheit}°F')
'''

CODIGO_12_PARES = '''\
n = int(input('Digite um número inteiro:'))

print (f'Números pares entre 1 e {n}:')

for i in range (2,n+1,2):
    print (i)
'''

CODIGO_CALCULADORA = '''\
from time import sleep
num1 = int(input('Digite um Número:'))
num2 = int(input('Digite outro Número:'))
opcao = 0
while opcao !=6:
    print (\'\'\'Escolha uma Opção
    [1] Somar
    [2] Multiplicar
    [3] Divisão
    [4] Maior
    [5] Novos Numeros
    [6] Sair do Programa\'\'\')
    opcao = int(input("Qual sua opção?:"))
    print('Processando...')
    sleep (2)
    print ('=-=-='*10)
    if opcao == 1:
        soma = num1 + num2
        print (f'A soma dos números {num1} é {num2} e de {soma}')
        print ('=-=-='*10)
    elif opcao == 2:
        soma = num1 * num2
        print (f'A Multiplicação Dos números {num1} X {num2} e de {soma}')
        print ('=-=-='*10)
    elif opcao == 3:
        soma = num1 / num2
        print (f'Número {num1} Dividido por {num2} e igual a {soma:.1f}')
        print ('=-=-='*10)
    elif opcao == 4:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print (f'Entre {num1} e {num2} o maior valor é {maior}')
        print ('=-=-='*10)
    elif opcao == 5:
        print ('Informe os Números Novamente')
        num1 = int(input('Digite um Número:'))
        num2 = int(input('Digite outro Número:'))
        print ('=-=-='*10)
    elif opcao == 6:
        print ('Finalizando...')
        sleep (2)
    else:
        print ('Opçãon inválida. Tente novamente.')
        sleep (2)
print ('=-=-='*12)
print ('Fim do programa! Volte sempre!')
'''


# ============================================================
#  FUNÇÕES DOS EXERCÍCIOS
# ============================================================

def exercicio_1():
    st.header("1 — Soma de Dois Números")
    st.code(CODIGO_1_SOMA, language="python")

    st.subheader("▶ Versão Interativa")
    num1 = st.number_input("Digite o primeiro valor:", value=0, step=1, key="ex1_num1")
    num2 = st.number_input("Digite o segundo valor:", value=0, step=1, key="ex1_num2")

    if st.button("Calcular", key="ex1_btn"):
        soma = num1 + num2
        st.success(f"A soma dos numeros {num1} e {num2} é igual a {soma}")


def exercicio_2():
    st.header("2 — Média de 3 Notas")
    st.code(CODIGO_2_MEDIA, language="python")

    st.subheader("▶ Versão Interativa")
    nota1 = st.number_input("Digite a primeira Nota:", value=0.0, step=0.1, format="%.1f", key="ex2_nota1")
    nota2 = st.number_input("Digite a segunda Nota:", value=0.0, step=0.1, format="%.1f", key="ex2_nota2")
    nota3 = st.number_input("Digite a terceira Nota:", value=0.0, step=0.1, format="%.1f", key="ex2_nota3")

    if st.button("Calcular", key="ex2_btn"):
        media = (nota1 + nota2 + nota3) / 3
        st.info(f"A media das notas foi de: {media:.2f}")

        if media >= 7:
            st.success("Você foi Aprovado!")
        elif media >= 5:
            st.error("Você foi reprovado!!")
        else:
            st.error("Você passou Vergonha!")


def exercicio_3():
    st.header("3 — Metros para Centímetros")
    st.code(CODIGO_3_METROS, language="python")

    st.subheader("▶ Versão Interativa")
    metros = st.number_input("Digite o valor em metros:", value=0.0, step=0.1, format="%.2f", key="ex3_metros")

    if st.button("Calcular", key="ex3_btn"):
        centim = metros * 100
        st.success(f"{metros} Metros igual a {centim} CM")


def exercicio_4():
    st.header("4 — Par ou Ímpar")
    st.code(CODIGO_4_PAROUIMPAR, language="python")

    st.subheader("▶ Versão Interativa")
    num1 = st.number_input("Digite um número inteiro:", value=0, step=1, key="ex4_num1")

    if st.button("Calcular", key="ex4_btn"):
        if num1 % 2 == 0:
            st.success(f"{num1} é Par")
        else:
            st.info(f"{num1} é ìmpar")


def exercicio_5():
    st.header("5 — Maior e Menor")
    st.code(CODIGO_6_MAIOR_MENOR, language="python")

    st.subheader("▶ Versão Interativa")
    num1 = st.number_input("Digite o primeiro Número:", value=0, step=1, key="ex5_num1")
    num2 = st.number_input("Digite o segundo Número:", value=0, step=1, key="ex5_num2")

    if st.button("Calcular", key="ex5_btn"):
        if num1 > num2:
            st.success(f"O numero {num1} é maior que o número {num2}!")
        elif num2 > num1:
            st.success(f"O numero {num2} é maior que o número {num1}!")
        else:
            st.info("Eles são iguais")


def exercicio_6():
    st.header("6 — Repetição (Números de 1 a N)")
    st.code(CODIGO_7_REPETICAO, language="python")

    st.subheader("▶ Versão Interativa")
    st.caption("O código original exibe de 1 a 10. Aqui você pode escolher N:")
    n = st.number_input("Digite o valor de N:", value=10, min_value=1, step=1, key="ex6_n")

    if st.button("Exibir", key="ex6_btn"):
        saida = "\n".join(str(num) for num in range(1, n + 1))
        st.text(saida)


def exercicio_7():
    st.header("7 — Soma de 1 até N")
    st.code(CODIGO_8_SOMA_NUMEROS, language="python")

    st.subheader("▶ Versão Interativa")
    num1 = st.number_input("Digite um Número inteiro:", value=1, min_value=1, step=1, key="ex7_num1")

    if st.button("Calcular", key="ex7_btn"):
        soma = 0
        for i in range(1, num1 + 1):
            soma += i
        st.success(f"A soma de 1 até {num1} é de {soma}")


def exercicio_8():
    st.header("8 — Tabuada")
    st.code(CODIGO_9_TABUADA, language="python")

    st.subheader("▶ Versão Interativa")
    numero = st.number_input("Digite um Número:", value=1, step=1, key="ex8_numero")

    if st.button("Calcular", key="ex8_btn"):
        linhas = [f"=-=-=-TABUADA DO {numero} =-=-=-"]
        for i in range(1, 11):
            linhas.append(f"{numero} x {i} = {numero * i}")
        st.text("\n".join(linhas))


def exercicio_9():
    st.header("9 — Área do Retângulo")
    st.code(CODIGO_10_AREA, language="python")

    st.subheader("▶ Versão Interativa")
    st.write("=-=-=-=- Calcular a área de um Retangulo =-=-=-=-")
    altura = st.number_input("Digite qual a altura:", value=0.0, step=0.1, format="%.2f", key="ex9_altura")
    base = st.number_input("Digite qual a base:", value=0.0, step=0.1, format="%.2f", key="ex9_base")

    if st.button("Calcular", key="ex9_btn"):
        area = base * altura
        st.success(f"A área é igual a {area:.2f}")


def exercicio_10():
    st.header("10 — Celsius para Fahrenheit")
    st.code(CODIGO_11_TEMPERATURA, language="python")

    st.subheader("▶ Versão Interativa")
    celsius = st.number_input("Digite a temperatura em Celsius:", value=0.0, step=0.1, format="%.1f", key="ex10_celsius")

    if st.button("Calcular", key="ex10_btn"):
        fahrenheit = (celsius * 1.8) + 32
        st.success(f"{celsius}°C é igual a {fahrenheit}°F")


def exercicio_11():
    st.header("11 — Números Pares até N")
    st.code(CODIGO_12_PARES, language="python")

    st.subheader("▶ Versão Interativa")
    n = st.number_input("Digite um número inteiro:", value=10, min_value=2, step=1, key="ex11_n")

    if st.button("Exibir", key="ex11_btn"):
        linhas = [f"Números pares entre 1 e {n}:"]
        for i in range(2, n + 1, 2):
            linhas.append(str(i))
        st.text("\n".join(linhas))


def exercicio_12():
    st.header("12 — Calculadora")
    st.code(CODIGO_CALCULADORA, language="python")

    st.subheader("▶ Versão Interativa")
    num1 = st.number_input("Digite um Número:", value=0, step=1, key="ex12_num1")
    num2 = st.number_input("Digite outro Número:", value=0, step=1, key="ex12_num2")

    opcao = st.selectbox(
        "Escolha uma Opção:",
        ["Somar", "Multiplicar", "Divisão", "Maior"],
        key="ex12_opcao",
    )

    if st.button("Calcular", key="ex12_btn"):
        st.write("=-=-=" * 10)

        if opcao == "Somar":
            soma = num1 + num2
            st.success(f"A soma dos números {num1} é {num2} e de {soma}")

        elif opcao == "Multiplicar":
            soma = num1 * num2
            st.success(f"A Multiplicação dos números {num1} X {num2} é de {soma}")

        elif opcao == "Divisão":
            if num2 == 0:
                st.error("Erro: divisão por zero!")
            else:
                soma = num1 / num2
                st.success(f"Número {num1} Dividido por {num2} e igual a {soma:.1f}")

        elif opcao == "Maior":
            if num1 > num2:
                maior = num1
            else:
                maior = num2
            st.success(f"Entre {num1} e {num2} o maior valor é {maior}")

        st.write("=-=-=" * 10)


# ============================================================
#  MENU LATERAL E ROTEAMENTO
# ============================================================

EXERCICIOS = {
    "1 — Soma de Dois Números": exercicio_1,
    "2 — Média de 3 Notas": exercicio_2,
    "3 — Metros para Centímetros": exercicio_3,
    "4 — Par ou Ímpar": exercicio_4,
    "5 — Maior e Menor": exercicio_5,
    "6 — Repetição (1 a N)": exercicio_6,
    "7 — Soma de 1 até N": exercicio_7,
    "8 — Tabuada": exercicio_8,
    "9 — Área do Retângulo": exercicio_9,
    "10 — Celsius → Fahrenheit": exercicio_10,
    "11 — Números Pares até N": exercicio_11,
    "12 — Calculadora": exercicio_12,
}

st.sidebar.title("🐍 Atividade 1 Sérgio")
st.sidebar.markdown("---")
escolha = st.sidebar.radio("Selecione um exercício:", list(EXERCICIOS.keys()))

# Executa a função do exercício selecionado
EXERCICIOS[escolha]()

