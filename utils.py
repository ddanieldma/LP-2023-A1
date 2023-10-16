import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import doctest

def check_ethnicity(etnia: str) -> bool:
	"""Verifica se a etnia é válida e, portanto, existe no dataset

	:param str etnia: etnia a ser verificada

	:returns: True se a etnia for válida e False se não for
	
	:rtype: bool
	"""

	try

	etnias_validas = [
		"branca",
		"negra",
		"indigena",
		"amarela"
	]

	if etnia in etnias_validas:
		return True
	else:
		return False

# Função auxiliar para rotação e alinhamento dos labels.
def get_label_rotation(angle: int, offset: int) -> (int, str):
	"""Calcula a rotação do label da barra no plot

	:param int angle: angulo em radianos
	:param int offset: offset em radianos

	:returns: valores para rotação e alinhamento da label em uma tupla
	
	:rtype: tuple

	Exemplo:
	
	>>> rotacao, alinhamento = get_label_rotation(np.pi, np.pi/2)
	... rotacao
	450.0
	>>> alinhamento
	'right'

	>>> get_label_rotation("123", "123")
	Tipo incorreto
	"""

	try:
		if not(isinstance(angle, int) or isinstance(angle, float)):
			raise TypeError
		elif not(isinstance(offset, int) or isinstance(offset, float)):
			raise TypeError
	except TypeError:
		print("Tipo incorreto")
		return None

	rotation = np.rad2deg(angle + offset)
	if angle <= np.pi:
		alignment = "right"
		rotation = rotation + 180
	else: 
		alignment = "left"
	return rotation, alignment

# Função que adiciona os labels
def add_labels(angles: np.ndarray, values: np.ndarray, labels: np.ndarray, offset: np.ndarray, ax ) -> None:
	"""Função auxiliar que adiciona os labels no plot

	:param list angles: lista de ângulos
	:param list values: lista de alturas dos labels
	:param list labels: lista de textos dos labels
	:param int offset: onde começam os labels a ser colocados
	:param matplotlib.projections.polar.PolarAxesSubplot ax: objeto que contém o plot circular

	Exemplo:
	>>> add_labels(5, 6, 7, 8, 9)
	Algum parâmetro tem o tipo incorreto

	>>> angles = np.array([1.2])
	>>> values = np.array([1.2])
	>>> labels = np.array([1.2])
	>>> fig, ax = plt.subplots(figsize=(20, 10))
	>>> add_labels(angles, values, labels, 0, ax)
	Algum array está vazio

	"""

	try:
		if ((not(angles.dtype == np.float64)) or (not(values.dtype == np.float64)) or (not(labels.dtype == object)) or (not(isinstance(offset, float)))):
			raise TypeError
		if angles.size == 0 or values.size == 0 or labels.size == 0:
			raise ValueError
	except (TypeError, AttributeError):
		print("Algum parâmetro tem o tipo incorreto")
		return None
	except ValueError:
		print("Algum array está vazio")
		return None		

	#espaço entre fim da barra e o label
	padding = 4

	for angle, value, label in zip(angles, values, labels):
		angle = angle

		# obtendo rotação e alinhamento
		rotation, alingment = get_label_rotation(angle, offset)

		ax.text(
			x=angle,
			y=value + padding,
			s=label,
			ha=alingment,
			va="center",
			rotation=rotation,
			rotation_mode="anchor"
		)

if __name__ == "__main__":
	doctest.testmod(verbose=True)