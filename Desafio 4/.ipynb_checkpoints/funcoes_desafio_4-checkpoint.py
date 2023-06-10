import numpy as np

def 

def eficiencia_ciclo_carnot(tq,tf):
    """ Calcula a eficiência teórica do ciclo de Carnot a partir dos valores da fonte quente e da fonte fria
    
    Args: * Tq: temperatura em kelvin ou em graus celsius da fonte quente
    *Tf: temperatura em kelvin ou em graus celsius da fonte fria
    
    Return: eficiência do ciclo de Carnot"""
    
    return 1-(tf/tq)

def entropia_por_temperatura_vapor(T, df, t_init, s_init):
    """ Calcula a entropia em um kilograma de vapor d'água em função da temperatura.
    
    Args:
        T: temperatura
        df: dataframe contendo dados de calor específico para cada temperatura
        t_init: temperatura inicial
        s_init: entalpia inicial
        
    Return:
        Valor da entropia
    """
    
    df = df.loc[df['temperatura'] <= T]
    df = df.loc[df['temperatura'] >= t]
    
    cp = np.array(df['calor_especifico'])
    t = np.array(df['temperatura'])
    
    f_t = cp/t
    
    s_t = s_init + np.trapz(f_t, t)
    
    return s_t

def entalpia_por_temperatura(T, m, df, t_init, h_init):
    """ Calcula a entalpia de uma substância em função da temperatura.
    
    Args:
        T: temperatura
        df: dataframe contendo dados de calor específico para cada temperatura
        t_init: temperatura inicial
        h_init: entalpia inicial
        
    Return:
        Valor da entalpia
    """
    df = df.loc[df['temperatura'] <= T]
    df = df.loc[df['temperatura'] >= t]
    
    cp = np.array(df['calor_especifico'])
    t = np.array(df['temperatura'])
    
    f_t = cp
    
    h_t = h_init + m*np.trapz(f_t, t)
    
    return h_init

def entalpia_boiler(T_init, T_evap, T_final, h_evap, m, df_liq, df_vap):
    """ Função que calcula a diferença de entalpia causada pelo boiler no ciclo de rankine
    
    Args:
        T_init: temperatura inicial ou temperatura da fonte fria
        T_evap: temperatura de evaporação da água
        T_final: temperatura final ou temperatura da fonte quente
        h_evap: diferença de entalpia necessária para a evaporação
        m: massa de água
        df_liq: dataframe contendo dados de calor específico para cada temperatura do líquido
        df_vap: dataframe contendo dados de calor específico para cada temperatura do vapor
        
    Return:
        Diferença de entalpia no boiler
    """
    h_exp_liq = entalpia_por_temperatura(T_evap, m, df, T_init, 0)
    
    h_exp_vap = entalpia_por_temperatura(T_final, m, df, T_evap, 0)
    
    h_boiler = h_exp_liq + m*h_evap + h_exp_vap
    
    return h_boiler

def entalpia_condensador(h_cond, m):
    """ Função que calcula a entalpia no condensador
    
    Args:
        h_cond: entalpia de condensação na temperatura fria
        m: massa de água
        
    Return:
        Diferença de entalpia do condensador
    """
    h_condensador = h_cond*m
    
    return h_condensador

def eficiencia_rankine(h_boiler, h_condensador):
    """ Função que calcula a eficiência ideal do ciclo de rankine
    
    Args:
        h_boiler: diferença de entalpia no boiler
        h_condensador: diferença de entalpia do condensador
        
    Return:
        Eficiência do ciclo de rankine
    """
    eficiencia = 1 - (- h_condensador)/h_boiler
    
    return eficiencia