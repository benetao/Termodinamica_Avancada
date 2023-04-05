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