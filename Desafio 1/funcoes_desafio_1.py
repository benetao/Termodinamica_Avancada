def entalpia_de_form_mistura(frac_molar1, entalpia1, entalpia2, entalpia_mix):
    frac_molar2 = 1 - frac_molar1
    return entalpia1*frac_molar1 + entalpia2*frac_molar2 + entalpia_mix