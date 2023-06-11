import numpy as np

def eficiencia_ciclo_carnot(tq,tf):
    """ Calcula a eficiência teórica do ciclo de Carnot a partir dos valores da fonte quente e da fonte fria
    
    Args: * Tq: temperatura em kelvin ou em graus celsius da fonte quente
    *Tf: temperatura em kelvin ou em graus celsius da fonte fria
    
    Return: eficiência do ciclo de Carnot"""
    
    tf += 273.15 # temperatura em Kelvin
    tq += 273.15 # temperatura em Kelvin
    
    return 1-(tf/tq)

def entropia_por_temperatura_vapor(T, df, t_init, s_init):
    """ Calcula a entropia em um kilograma de vapor d'água em função da temperatura.
    
    Args:
        T: temperatura (°C)
        df: dataframe contendo dados de calor específico para cada temperatura
        t_init: temperatura inicial (°C)
        s_init: entalpia inicial (kJ/(kg.K))
        
    Return:
        Valor da entropia (kJ/(kg.K))
    """
    temp_col = df.keys()[0] # coluna da temperatura
    calor_col = df.keys()[1] # coluna do calor específico
    
    df = df.loc[df[temp_col] <= T] # cortando o dataframe na temperatura mais alta
    df = df.loc[df[temp_col] >= t_init] # cortando o dataframe na temperatura mais baixa
    
    cp = np.array(df[calor_col]) # definindo a array de calor específico
    t = np.array(df[temp_col]) + 273.15 # definindo a array de temperatura em kelvin
    
    f_t = cp/t # calculando a função que será integrada
    
    s_t = s_init + np.trapz(f_t, t) # calculando a entropia
    
    return s_t

def entalpia_por_temperatura(T, m, df, t_init, h_init):
    """ Calcula a entalpia de uma substância em função da temperatura.
    
    Args:
        T: temperatura (°C)
        df: dataframe contendo dados de calor específico para cada temperatura
        t_init: temperatura inicial (°C)
        h_init: entalpia inicial (kJ/kg)
        
    Return:
        Valor da entalpia (kJ/kg)
    """
    temp_col = df.keys()[0] # coluna da temperatura
    calor_col = df.keys()[1] # coluna do calor específico
    
    df = df.loc[df[temp_col] <= T] # cortando o dataframe na temperatura mais alta
    df = df.loc[df[temp_col] >= t_init] # cortando o dataframe na temperatura mais baixa
    
    cp = np.array(df[calor_col]) # definindo a array de calor específico
    t = np.array(df[temp_col]) + 273.15 # definindo a array de temperatura em kelvin
    
    f_t = cp # calculando a função que será integrada
    
    h_t = h_init + m*np.trapz(f_t, t) # calculando a entropia
    
    return h_t

def entalpia_boiler(T_init, T_evap, T_final, h_evap, m, df_liq, df_vap):
    """ Função que calcula a diferença de entalpia causada pelo boiler no ciclo de rankine
    
    Args:
        T_init: temperatura inicial ou temperatura da fonte fria (°C)
        T_evap: temperatura de evaporação da água (°C)
        T_final: temperatura final ou temperatura da fonte quente (°C)
        h_evap: diferença de entalpia necessária para a evaporação (kJ/kg)
        m: massa de água (kg)
        df_liq: dataframe contendo dados de calor específico para cada temperatura do líquido
        df_vap: dataframe contendo dados de calor específico para cada temperatura do vapor
        
    Return:
        Diferença de entalpia no boiler (kJ)
    """
    h_exp_liq = entalpia_por_temperatura(T_evap, m, df_liq, T_init, 0) # entalpia do aumento de temperatura da água
    
    h_exp_vap = entalpia_por_temperatura(T_final, m, df_vap, T_evap, 0) # entalpia de evaporação da água
    
    h_boiler = h_exp_liq + m*h_evap + h_exp_vap # entalpia do boiler
    
    return h_boiler

def entalpia_condensador(h_cond, m):
    """ Função que calcula a entalpia no condensador
    
    Args:
        h_cond: entalpia de condensação na temperatura fria (kJ/kg)
        m: massa de água (kg)
        
    Return:
        Diferença de entalpia do condensador (kJ)
    """
    h_condensador = h_cond*m
    
    return h_condensador

def eficiencia_rankine(h_boiler, h_condensador):
    """ Função que calcula a eficiência ideal do ciclo de rankine
    
    Args:
        h_boiler: diferença de entalpia no boiler (kJ)
        h_condensador: diferença de entalpia do condensador (kJ)
        
    Return:
        Eficiência do ciclo de rankine (kJ)
    """
    eficiencia = 1 - (- h_condensador)/h_boiler
    
    return eficiencia
