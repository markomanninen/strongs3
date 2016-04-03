#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: letter_value.py

class langcode(str):
	pass

# three letter script codes
# http://pydoc.net/Python/Pytomo/3.0.1/pytomo.kaa_metadata.language/
greek = langcode('grc') # ancient greek
hebrew = langcode('heb')
coptic = langcode('cop')
english = langcode('eng')
sanskrit = langcode('san')
arabic = langcode('ara')
#aramea = langcode('arc')
#armenia = langcode('arm')
#ethiopia = langcode('gez')

data = dict()

data[greek] = (
# letters from α to θ (1 to 9)
	[1, 'alpha'], [2, 'beta'], [3, 'gamma'], [4, 'delta'], [5, 'epsilon'], [6, 'digamma'], [7, 'zeta'], [8, 'eta'], [9, 'theta'],
# letters from ι to ϙ (10 to 90)
	[10, 'iota'], [20, 'kappa'], [30, 'lambda'], [40, 'mu'], [50, 'nu'], [60, 'xi'], [70, 'omicron'], [80, 'pi'], [90, 'qoppa'],
# letters from ρ to ϡ (100 to 900)
	[100, 'rho'], [200, 'sigma'], [300, 'tau'], [400, 'upsilon'], [500, 'phi'], [600, 'chi'], [700, 'psi'], [800, 'omega'], [900, 'sampi'],
# letters from ạ to ṭ (1000 to 9000)
	[1000, 'alpha_m'], [2000, 'beta_m'], [3000, 'gamma_m'], [4000, 'delta_m'], [5000, 'epsilon_m'], [6000, 'digamma_m'], [7000, 'zeta_m'], [8000, 'eta_m'], [9000, 'theta_m'],
# letters from ṃ to ? (10000 to ?)
	[10000, 'mu_m'], 
)

data[hebrew] = (
# letters from א to ט (1 to 9)
	[1, 'alef'], [2, 'beth'], [3, 'gimel'], [4, 'daleth'], [5, 'he'], [6, 'vau'], [7, 'zayin'], [8, 'heth'], [9, 'teth'],
# letters from י to צ (10 to 90)
	[10, 'yod'], [20, 'kaph'], [30, 'lamed'], [40, 'mem'], [50, 'nun'], [60, 'samekh'], [70, 'ayin'], [80, 'pe'], [90, 'tsade'],
# letters from ק to ץ (100 to 900)
	[100, 'qoph'], [200, 'resh'], [300, 'shin'], [400, 'tau'], [500, 'final_kaph'], [600, 'final_mem'], [700, 'final_nun'], [800, 'final_pe'], [900, 'final_tsade']
)

data[english] = (
# letters from a to z (1 to 7 and back, Marty Leeds)
	[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd'], [5, 'e'], [6, 'f'], [7, 'g'], [6, 'h'], [5, 'i'], [4, 'j'], [3, 'k'], [2, 'l'], [1, 'm'],
	[1, 'n'], [2, 'o'], [3, 'p'], [4, 'q'], [5, 'r'], [6, 's'], [7, 't'], [6, 'u'], [5, 'v'], [4, 'w'], [3, 'x'], [2, 'y'], [1, 'z']
)

data[coptic] = ()
data[sanskrit] = ()
data[arabic] = ()
