# Analizador de sentimientos
## Introducción
En el siguiente proyecto presentamos una api que analiza los sentimientos de un chat formado por varios usuarios. A su vez, también recomienda a un nuevo usuario, los usuarios que más se le parecen en base a los sentimientos de los mendsajes que han escrito.

## EndPoints

* /user/create/{userName}
	- Proposito: Crea un nuevo usuario
    - Parámetros: El nobre del usuario
    - Returns: Devuelve el id del usuario creado
* /chat/create
	- Proposito: Crea un nuevo chat
    - Parámetros: La lista de usuarios que componen el chat
    - Returns: Devuelve el id del chat creado
* /chat/{chatId}/adduser
	- Proposito: Añadir un nuevo usuario a un chat
	- Parámetros: El id del chat donde se quiere añadir al nuevo usuario y el id del ususario
	- Returns: el id del chat
* /chat/{chatId}/addmessage
	- Proposito: Añadir un nuevo mensaje a un chat
	- Parámetros: El id del chat donde se quiere añadir el nuevo mensaje y el mensaje
	- Returns: el mensaje que se ha introducido en el chat
* /chat/{chatId}/list
	* /chat/{chatId}/adduser
	- Proposito: Listar todos los mensajes de un chat
	- Parámetros: El id del chat
	- Returns: La lista de mensajes de un chat
* /chat/{chatId}/sentiment
	- Proposito: Analizar los sentimieentos de los mensajes de un chat
	- Parámetros: El id del chat que se quiere analizar
	- Returns: La lista de mensajes con cada mensaje analizado sus sentimientos
* /user/recommend
	- Proposito: Recomendar tres usuarios a un nuevo usuario en base a los sentimientos de los mensajes que han escrito
	- Parámetros: Una lista de mensajes del nuevo usuario al que se le quiere recomendar
	- Returns: Los tres usuarios más parecidos


