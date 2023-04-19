import matplotlib.pyplot as plt
import numpy as np
def porcentagem_em_massa(razao_vol, dens1, dens2):
    
    """ Essa função calcula a razão em massa de uma mistura de 2 substâncias a partir da razão volumétrica e da densidade de cada substância
    
    Args:
    razao_vol: porcentagem em volume da substãncia 1
    dens1: densidade da substância 1
    dens2: densidade da substância 2
    
    Retorna: 
    Razão e massa da mistura"""
    
    massa1= razao_vol*dens1
    massa2= (100-razao_vol)*dens2
    porcentagem_em_massa= (massa1/(massa1+massa2))*100
    return porcentagem_em_massa

def volume_total_mistura(densidade_mistura, massa_total):
    """ Essa função calcula o volume total de uma mistura
    
    Args:
    densidade_mistura: Densidade da mistura (geralmente tabelada) (Kg/L)
    massa_total: massa total definida (Kg)
    
    Retorna:
    O volume total da mistura"""
    
    volume_total = massa_total/densidade_mistura
    return volume_total

def encontra_valor_proximo(df, coluna, valor_desejado):
    """Encontra o valor mais próximo de um determinado número em um conjunto de dados
    
    Args:
        df: um pandas dataframe
        coluna: uma coluna do dataframe
        valor_desejado: o número que se quer encontrar
    
    Return:
        O valor mais próximo presente no conjunto de dados e o seu index
    """
    valor_proximo = None
    diferenca_minima = None
    index = 0
    for valor in df[coluna]:
        diferenca = abs(valor - valor_desejado)
        if diferenca_minima is None or diferenca < diferenca_minima:
            diferenca_minima = diferenca
            valor_proximo = valor
            index_valor_proximo = index
            
        index = index + 1
            
    return valor_proximo, index_valor_proximo

def destilacao_fracionada(df, etapas, frac):
    """Simula uma destilação fracionada a partir do diagrama de fases de uma mistura
    
    Args:
        df: dataframe do diagrama de fases
        etapas: número de etapas realizadas para separar a mistura
        frac: fração inicial de etanol
        
    Return:
        Uma lista contendo a coordenada em x dos pontos críticos, uma lista contendo as coordenadas em y dos pontos críticos, a fração final do vapor
    """
    lista= [] # lista que vai conter as tuplas com as coordenadas dos pontos
    primeiro_valor= encontra_valor_proximo(df, 'Mole Fraction', frac) # acha, no dataframe, o valor mais próximo da fração inicial na função
    x2= primeiro_valor[0] # primeiro valor 
    for _ in range (etapas):
        primeiro_valor= encontra_valor_proximo(df, 'Mole Fraction', frac)
        x= x2
        index= primeiro_valor[1]
        y= df['C'][index]
        lista.append([x,y])
        
        segundo_valor= encontra_valor_proximo(df, 'C', y)
        y2= y
        index2= segundo_valor[1]
        x2= df['Mole Fraction.1'][index]
        lista.append([x2,y2])
        frac= x2
    return lista

def intermediario(partida, chegada, passo_x, passo_y):
    """Cria pontos intermediários entre 2 pontos críticos da destilação fracionada, a fim de criar um gif mais fluido
    
    Args:
        partida: tupla com as coordenadas do ponto de partida
        etapas: tupla com as coordenadas do ponto de chegada
        passo_x: valor que cada frame andará, se estiver variando em x
        passo_y: valor que cada frame andará, se estiver variando em y
        
    Return:
        Lista com listas que contêm as coordenadas dos pontos intermediários entre os pontos de partida e chegada
    """
    lista = []
    intermediario = partida
    if partida[0] == chegada[0]:
        while intermediario[1] > chegada[1]:
            lista.append(intermediario)
            y = intermediario[1] - passo_y
            intermediario = (intermediario[0], y)
        lista.append(chegada)
        
    if partida[1] == chegada[1]:
        while intermediario[0] < chegada[0]:
            lista.append(intermediario)
            x = intermediario[0] + passo_x
            intermediario = (x, intermediario[1])
        lista.append(chegada)
        
    return lista


def caminho(lista_criticos, passo_x, passo_y):
    """Cria intermediários entre TODOS os pontos da destilação fracionada
    
    Args:
        lista_criticos: lista com listas que contêm as coordenadas de todos os pontos críticos da destilação fracionada
        passo_x: valor que cada frame andará, se estiver variando em x
        passo_y: valor que cada frame andará, se estiver variando em y
        
    Return:
        Lista com listas que contêm as coordenadas de TODOS os pontos críticos e intermediários
    """
    lista_final = []
    for t in range(len(lista_criticos)-1):
        partida = lista_criticos[t]
        chegada = lista_criticos[t + 1]
        lista_final = lista_final + intermediario(partida, chegada, passo_x, passo_y)
        
    return lista_final
        
def create_frame(t, x, y, df_diagrama):
    """Cria um frame para o gif
    
    Args:
        t: "index" do frame que está sendo criado
        x: lista de coordenadas x
        y: lista de coordenadas y
        df_diagrama: dataframe do diagrama de fases, que será plotado "de fundo"
        
    Return:
        O frame t para o gif
    """
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    df_diagrama.plot('Mole Fraction','C',legend=True, label = "Temperatura de Ebulição", ax=ax1, kind = 'line', color = 'black') # Plotando Temperatura de ebulição
    df_diagrama.plot('Mole Fraction.1','C',legend=True, label = "Composição do Vapor", ax=ax1, kind = 'line', color = 'gray') # Plotando composição do vapor
    plt.title('Diagrama de Fases - Etanol e Água') # Definindo título do gráfico
    plt.xlabel('Fração Molar de Etanol') # Definindo legendas dos eixos
    plt.ylabel('Temperatura (°C)')
    
    plt.plot(x[:(t+1)], y[:(t+1)], color = 'grey' )
    plt.plot(x[t], y[t], color = 'black', marker = 'o' )
    plt.savefig(f'./Figuras - Desafio 2/img_{t}.png', 
                transparent = False,  
                facecolor = 'white'
               )
    plt.close()
    
def delta_S_mistura(x):
    """ Função que calcula variação de entropia de uma mistura a partir da fração molar de etanol na mesma
    Args: 
    x: fração molar de etanol na mistura
        
    Return: valor de variação de entropia nessa fração molar"""
    R= 8.31  #J/K*mol (Constante dos gases)
    a= 1-x
    return -(R*(x*np.log(x)+a*np.log(a)))