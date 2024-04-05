matriz_ycmk = []
matriz_rgb = []

# Matriz de conversão
matriz_conversao = [
    [0.3, 0.6, 0.1],
    [0.7, -0.6, -0.1],
    [-0.3, -0.6, 1],
    [1, 1, 1]
]

def conversao_impressora(r, g, b):
    y = matriz_conversao[0][0] * r + matriz_conversao[0][1] * g + matriz_conversao[0][2] * b
    c = matriz_conversao[1][0] * r + matriz_conversao[1][1] * g + matriz_conversao[1][2] * b
    m = matriz_conversao[2][0] * r + matriz_conversao[2][1] * g + matriz_conversao[2][2] * b
    k = matriz_conversao[3][0] * r + matriz_conversao[3][1] * g + matriz_conversao[3][2] * b
    conversao_inteiro(y, c, m, k)
    
def conversao_inteiro(y, c, m, k):
    y_ideal = round(y)
    c_ideal = round(c)
    m_ideal = round(m)
    k_ideal = round(k)
    matriz_ycmk.append((y_ideal, c_ideal, m_ideal, k_ideal))
    flag_convertido()
    
def flag_convertido():
    print("Conversão Realizada com Sucesso!")
    print(f"Os números foram convertidos para: Y: {matriz_ycmk[-1][0]}, C: {matriz_ycmk[-1][1]}, M: {matriz_ycmk[-1][2]}, K: {matriz_ycmk[-1][3]}")

r = int(input("Digite o valor de R: "))
g = int(input("Digite o valor de G: "))
b = int(input("Digite o valor de B: "))

conversao_impressora(r, g, b)

