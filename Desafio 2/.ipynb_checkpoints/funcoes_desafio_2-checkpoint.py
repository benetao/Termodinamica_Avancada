def massa_da_mistura(razao_vol, dens1, dens2):
    
    """ Essa função calcula a razão em massa de uma mistura de 2 substâncias a partir da razão volumétrica e da densidade de cada substância
    
    Args:
    razao_vol: porcentagem em volume da substãncia 1
    dens1: densidade da substância 1
    dens2: densidade da substância 2
    
    Retorna: 
    Razão e massa da mistura"""
    
    massa1= razao_vol*dens1
    massa2= (100-razao_vol)*dens2
    return (massa1/(massa1+massa2))*100

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
    lista= []
    primeiro_valor= encontra_valor_proximo(df, 'Mole Fraction', frac)
    x2= primeiro_valor[0]
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