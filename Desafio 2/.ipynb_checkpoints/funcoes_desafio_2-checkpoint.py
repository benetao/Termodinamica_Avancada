def entalpia_de_form_mistura(frac_molar1, entalpia1, entalpia2, entalpia_mix):
    frac_molar2 = 1 - frac_molar1
    return entalpia1*frac_molar1 + entalpia2*frac_molar2 + entalpia_mix

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