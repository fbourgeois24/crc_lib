""" Calcul de CRC en tout genre """

def validate_data(data, taille):
	""" Valider les données """
	if type(taille) == int:
		taille = [taille,]
	elif type(taille) == tuple:
		taille = list(taille)
	elif type(taille) != list:
		raise ValueError("Le paramètre taille doit être de type int, tuple ou liste ! ")

	data = str(data)
	if not data.isdigit():
		raise ValueError("Les données ne peuvent comporter que des chiffres !")

	if len(data) not in taille:
		raise ValueError(f"Les données doivent comporter {str(taille).replace(',', ' OU').replace('[', '').replace(']', '')} chiffres !")
	
	return data

def vcs(data):
	""" Calcul de la somme de contrle d'un vcs (virement structuré) 
		si data contient le vcs complet, on le vérifie. Sinon on renvoie le vcs complet
	"""
	data = validate_data(data, (10, 12))

	def crc_calc(payload):
		crc = str(int(payload[:10]) % 97).zfill(2)
		if crc == '00':
			crc = '97'
		return crc

	if len(data) == 12:
		# Si vcs complet on le vérifie
		if data == data[:10] + crc_calc(data):
			return True
		else:
			return False

	else:
		# Si vcs incomplet on le renvoie complet
		return data + crc_calc(data)



def bban_iban(data):
	""" Calcul les deux premiers chiffres à ajouter devant un compte bban pour le transformer en iban """
	data = validate_data(data, 12)

	return 98 - (int(data[10:10+2] + data[10:10+2] + '111400') % 97)


def tva(data):
	""" Numéro de TVA
		Data doit contenir les 8 ou 10 chiffres sans les 2 premières lettres
	"""
	data = validate_data(data, (8, 10))

	def crc_calc(payload):
		# crc = str(int(payload[:-2]) % 97).zfill(2)
		crc = str(97 - int(payload) % 97).zfill(2)
		if crc == '00':
			crc = '97'
		return crc

	if len(data) == 10:
		# Si vcs complet on le vérifie
		if data == data[:-2] + crc_calc(data[:-2]):
			return True
		else:
			return False

	else:
		# Si vcs incomplet on le renvoie complet
		return data + crc_calc(data)



def ean_18_crc_calc(payload):
		""" Calcul de la clé de contrôle de l'ean """
		sum = 0
		for seq, digit in enumerate(payload[:17]):
			if seq % 2 == 0:
				weight = 3
			else:
				weight = 1
			sum += weight * int(digit)
		crc = str(10 - (sum % 10))
		if crc == '10':
			crc = '0'
		return crc

def ean_18_generate(data):
	""" Calcul de la somme de contrôle d'un ean (18 chiffres)
		si data contient l'ean complet, on le vérifie. Sinon on renvoie l'ean complet
	"""
	try:
		data = validate_data(data, 17)
	except Exception as e:
		print(e)
		return None
	else:
		return data + ean_18_crc_calc(data)


def ean_18_validate(data):
	""" Valider un code EAN à 18 chiffres 
		Renvoie vrai ou faux si l'ean est valide ou non
	"""
	try:
		data = validate_data(data, 18)
	except Exception as e:
		print(e)
		return False
	else:
		if data == data[:17] + ean_18_crc_calc(data):
			return True
		else:
			return False