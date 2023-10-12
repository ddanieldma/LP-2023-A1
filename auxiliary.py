import numpy as np

# Função auxiliar para rotação e alinhamento dos labels.
def get_label_rotation(angle, offset):
	rotation = np.rad2deg(angle + offset)
	if angle <= np.pi:
		alignment = "right"
		rotation = rotation + 180
	else: 
		alignment = "left"
	return rotation, alignment

# Função que adiciona os labels
def add_labels(angles, values, labels, offset, ax):
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