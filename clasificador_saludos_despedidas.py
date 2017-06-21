# Clasificador de interacciones linguisticas usando un
# 	clasificador bayesiano
# Version 1.0
# Autor: antikytheraton
# Fecha: 7 de junio de 2017


from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import random

def clasificador(mensaje):
	"""Clasificador de saludos"""
	train = [
		("hola papu", 				'sal'),
		("le digo hola",			'sal'),
		("como te va?", 			'sal'),
		("que paso?", 				'sal'),
		("que onda?", 				'sal'),
		("hi",		 				'sal'),
		("hello guy", 				'sal'),
		("que hay?", 				'sal'),
		("holi", 					'sal'),
		("hola", 					'sal'),
		("hola que hace?", 			'sal'),
		("what's up?", 				'sal'),
		("holiii papu", 			'sal'),
		("como va?", 				'sal'),
		("que patso?", 				'sal'),
		("que ondax", 				'sal'),
		("hi5",		 				'sal'),
		("hello guy", 				'sal'),
		("que hay?", 				'sal'),
		("holi", 					'sal'),
		("hola hola", 				'sal'),
		("hola que haciendo?", 		'sal'),
		("what's up nigga?",		'sal'),

		("nos vemos", 				'des'),
		("adios", 					'des'),
		("gracias papu", 			'des'),
		("muchas gracias", 			'des'),
		("bye", 					'des'),
		("good bye", 				'des'),
		("hasta la vista baby", 	'des'),
		("(Y)", 					'des'),
		("ciao",					'des'),

		("quien te creo?", 			'ext'),
		("quien te hizo?", 			'ext'),
		("who has created you?", 	'ext'),
		("quien es tu papa?", 		'ext'),
		("de donde venis boludo?", 	'ext'),

		("que eres?",				'bot'),
		("quien eres?", 			'bot'),
		("who are you?", 			'bot'),
		("que cosa tan rara",		'bot'),
		("eres un bot?",			'bot'),
		("que cosa eres?",			'bot'),
		("what are you?",			'bot'),
		("eres un chatbot?",		'bot'),
		("vas a destruirme?",		'bot')

	]

	test = [
		("holi bot", 				'sal'),
		("hola hola", 				'sal'),
		("que hay papu?", 			'sal'),
		("que ondaaaaaaa?", 		'sal'),

		("hasta la vista bot", 		'des'),
		("nos vemos tio", 			'des'),
		("adieu", 					'des'),
		("(Y)", 					'des'),

		("que eres?", 				'bot'),
		("quien te creo?", 			'ext'),
		("que eres?", 				'bot'),
		("eres un bot?", 			'bot'),

		("hola", 					'sal'),
		("hola que hace?", 			'sal'),
		("what's up?", 				'sal'),
		("holiii papu", 			'sal'),
		("como va?", 				'sal'),
		("que patso?", 				'sal'),
		("que ondax", 				'sal'),

		("nos vemos", 				'des'),
		("adieu", 					'des'),
		("gracias bot", 			'des'),
		("muchas gracias", 			'des'),
		("lol", 					'des'),
		("good bye", 				'des'),
		("buenas noches",		 	'des'),
		("(Y)", 					'des'),

		("quien es tu creador?", 	'ext'),
		("quien te creo?", 			'ext'),
		("who are you?", 			'bot'),
		("who created you?", 		'ext'),
		("quien es tu papa?", 		'ext'),
		("de donde venis?", 		'ext')
	]


	cl = NaiveBayesClassifier(train)


	print("Accuracy: {0}".format(cl.accuracy(test)))
	return cl.classify(mensaje)

# Respuestas

# Saludos
saludo_bot = [
	'hola humano',
	'que onda?',
	'en que te puedo ayudar?',
	'holi holi',
	'hola bro'
]

# Despedidas
despedida_bot = [
	'adios humano',
	'bye human',
	'hasta la vista baby human',
	'adios'
]

# Creador
creador_bot = [
	'naci en mariachi.io',
	'mariachi.io es mi creador',
	'mariachi.io was made me'
]

# Yo chatbot
yo_chatbot = [
	'soy un chatbot',
	'soy un bot',
	'planeo dominar el mundo',
	'voy a destruirte',
	'destruir'
]

tipo = clasificador(str.lower(input("bot classifier test: ")))

if tipo == 'sal':
	print(random.choice(saludo_bot))
elif tipo == 'des':
	print(random.choice(despedida_bot))
elif tipo == 'ext':
	print(random.choice(creador_bot))
elif tipo == 'bot':
	print(random.choice(yo_chatbot))
else:
	print('no te entiendo papu, prueba con un hola :)')
