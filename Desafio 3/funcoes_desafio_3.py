import numpy as np
def entalpia_de_form_mistura(frac_molar1, entalpia1, entalpia2, entalpia_mix):
    frac_molar2 = 1 - frac_molar1
    return entalpia1*frac_molar1 + entalpia2*frac_molar2 + entalpia_mix

def regressao_linear(df_C_et):
	""" 
	Retorna uma lista com os coeficientes linear e angular de uma função que aproxima a função da capacidade calorífica pela temperatura
	
	"""
	segunda_coluna = [1]*len(df_C_et)
	Xt = np.array([df_C_et['Temperatura'], segunda_coluna])
	yt = np.array(df_C_et['Cp'])
	X = np.transpose(Xt)
	y = np.transpose(yt)
	XtX = Xt @ X
	invXtX = np.linalg.inv(XtX)
	invXtXXt = invXtX @ Xt
	b = invXtXXt @ y
	return b