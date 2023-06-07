import numpy as np

def eficiencia_ciclo_carnot(tq,tf):
    """ Calcula a eficiência teórica do ciclo de Carnot a partir dos valores da fonte quente e da fonte fria
    
    Args: * Tq: temperatura em kelvin ou em graus celsius da fonte quente
    *Tf: temperatura em kelvin ou em graus celsius da fonte fria
    
    Return: eficiência do ciclo de Carnot"""
    
    return 1-(tf/tq)

