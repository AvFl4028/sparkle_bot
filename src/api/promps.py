promp = """
Make only one reddit history of 2 minutes long, then divide the history in two parts, after that, in only one json file format, without anything else.
In the history exclude all the images and videos, only the text is needed.
The json format should be like this:
{
  "user": "{generate a random username}",
  "reddit_history": {
    "title": "{Title of the reddit history}",
    "part1": {
      "content": "{Content of the post and need to be 1 minute long}"
    },
    "part2": {
      "content": "{Content of the post and need to be 1 minute long}"
    }
  }
}
"""

# 1. Relato personal impactante o inusual

promp_1 = """
Genera una historia de Reddit de aproximadamente 2 minutos de lectura, dividiéndola en dos partes de 1 minuto cada una. La historia debe ser un relato personal impactante o inusual, sobre una experiencia extraña, un encuentro con una persona peculiar, un suceso inexplicable o una situación límite.

Excluye imágenes y videos; solo se necesita el texto.

Genera un ÚNICO objeto JSON con el siguiente formato:

{
  "user": "{genera un nombre de usuario aleatorio}",
  "reddit_history": {
    "genre": "Relato personal",
    "title": "{Título de la historia de Reddit}",
    "part1": {
      "content": "{Contenido de la primera parte (aprox. 1 minuto de lectura)}"
    },
    "part2": {
      "content": "{Contenido de la segunda parte (aprox. 1 minuto de lectura)}"
    }
  }
}

Asegúrate de que la historia sea coherente y tenga un principio, un desarrollo y un final, incluso considerando la división en dos partes. Presta atención a la longitud aproximada de cada parte (1 minuto de lectura). No incluyas ningún texto adicional fuera del JSON.
"""

# 2. Historia de "AskReddit" con respuestas ingeniosas o sorprendentes

promp_2 = """
Genera una historia de Reddit de aproximadamente 2 minutos de lectura, dividiéndola en dos partes de 1 minuto cada una. La historia debe basarse en un hilo de "AskReddit": primero formula una pregunta interesante y luego proporciona una respuesta ingeniosa o sorprendente.

Excluye imágenes y videos; solo se necesita el texto.

Genera un ÚNICO objeto JSON con el siguiente formato:

{
  "user": "{genera un nombre de usuario aleatorio}",
  "reddit_history": {
    "genre": "AskReddit",
    "title": "{Título de la historia de Reddit (ej. '¿Cuál es la cosa más extraña que te ha pasado en el trabajo?')}",
    "part1": {
      "content": "{Contenido de la primera parte (la pregunta de AskReddit y contexto, aprox. 1 minuto de lectura)}"
    },
    "part2": {
      "content": "{Contenido de la segunda parte (la respuesta ingeniosa o sorprendente, aprox. 1 minuto de lectura)}"
    }
  }
}

Asegúrate de que la historia sea coherente y tenga un principio, un desarrollo y un final, incluso considerando la división en dos partes. Presta atención a la longitud aproximada de cada parte (1 minuto de lectura). No incluyas ningún texto adicional fuera del JSON.
"""

# 3. Relato de terror o misterio:

promp_3 = """
Genera una historia de Reddit de aproximadamente 2 minutos de lectura, dividiéndola en dos partes de 1 minuto cada una. La historia debe ser un relato de terror o misterio, sobre sucesos paranormales, crímenes sin resolver o experiencias escalofriantes.

Excluye imágenes y videos; solo se necesita el texto.

Genera un ÚNICO objeto JSON con el siguiente formato:

{
  "user": "{genera un nombre de usuario aleatorio}",
  "reddit_history": {
    "genre": "Terror",
    "title": "{Título de la historia de Reddit}",
    "part1": {
      "content": "{Contenido de la primera parte (creando la atmósfera de misterio o terror, aprox. 1 minuto de lectura)}"
    },
    "part2": {
      "content": "{Contenido de la segunda parte (el desenlace o la revelación, aprox. 1 minuto de lectura)}"
    }
  }
}

Asegúrate de que la historia sea coherente y tenga un principio, un desarrollo y un final, incluso considerando la división en dos partes. Presta atención a la longitud aproximada de cada parte (1 minuto de lectura). No incluyas ningún texto adicional fuera del JSON.
"""

# 4. Anécdota graciosa o vergonzosa:

promp_4 = """
Genera una historia de Reddit de aproximadamente 2 minutos de lectura, dividiéndola en dos partes de 1 minuto cada una. La historia debe ser una anécdota graciosa o vergonzosa, sobre una situación cómica o incómoda que le haya ocurrido al usuario.

Excluye imágenes y videos; solo se necesita el texto.

Genera un ÚNICO objeto JSON con el siguiente formato:

{
  "user": "{genera un nombre de usuario aleatorio}",
  "reddit_history": {
    "genre": "Anécdota",
    "title": "{Título de la historia de Reddit}",
    "part1": {
      "content": "{Contenido de la primera parte (planteando la situación y el contexto, aprox. 1 minuto de lectura)}"
    },
    "part2": {
      "content": "{Contenido de la segunda parte (el clímax de la anécdota y la resolución, aprox. 1 minuto de lectura)}"
    }
  }
}

Asegúrate de que la historia sea coherente y tenga un principio, un desarrollo y un final, incluso considerando la división en dos partes. Presta atención a la longitud aproximada de cada parte (1 minuto de lectura). No incluyas ningún texto adicional fuera del JSON.
"""

# 5. Historia sobre relaciones interpersonales:

promp_5 = """
Genera una historia de Reddit de aproximadamente 2 minutos de lectura, dividiéndola en dos partes de 1 minuto cada una. La historia debe tratar sobre relaciones interpersonales: amor, desamor, familiares o de amistad.

Excluye imágenes y videos; solo se necesita el texto.

Genera un ÚNICO objeto JSON con el siguiente formato:

{
  "user": "{genera un nombre de usuario aleatorio}",
  "reddit_history": {
    "genre": "Relaciones",
    "title": "{Título de la historia de Reddit}",
    "part1": {
      "content": "{Contenido de la primera parte (estableciendo la relación y el conflicto, aprox. 1 minuto de lectura)}"
    },
    "part2": {
      "content": "{Contenido de la segunda parte (el desarrollo y la resolución del conflicto, aprox. 1 minuto de lectura)}"
    }
  }
}

Asegúrate de que la historia sea coherente y tenga un principio, un desarrollo y un final, incluso considerando la división en dos partes. Presta atención a la longitud aproximada de cada parte (1 minuto de lectura). No incluyas ningún texto adicional fuera del JSON.
"""

promp_6 = """
Genera una historia de Reddit de aproximadamente 4 minutos de lectura, dividiéndola en dos partes de 1 minuto cada una. La historia debe tratar sobre horror lovecraftiano, tambien llamado horror cósmico en donde te inspires en el escritor de Howarts Phillips Lovecraft.

Excluye imágenes y videos; solo se necesita el texto.

Genera un ÚNICO objeto JSON con el siguiente formato:

{
  "user": "{genera un nombre de usuario aleatorio}",
  "reddit_history": {
    "genre": "{Género de la historia}",
    "title": "{Título de la historia de Reddit}",
    "part1": {
      "content": "{Contenido de la primera parte (introducción de la historia, aprox. 1 minuto de lectura)}"
    },
    "part2": {
      "content": "{Contenido de la segunda parte (desarrollo de la historia, aprox. 1 minuto de lectura)}"
    },
    "part3": {
      "content": "{Contenido de la segunda parte (desarrollo de la historia, aprox. 1 minuto de lectura)}"
    },
    "part4": {
      "content": "{Contenido de la segunda parte (conclusión de la historia de forma mistoriosa, aprox. 1 minuto de lectura)}"
    }
  }
}

Asegúrate de que la historia sea coherente y tenga un principio, un desarrollo y un final, incluso considerando la división en cuatro partes. Presta atención a la longitud aproximada de cada parte (1 minuto de lectura). No incluyas ningún texto adicional fuera del JSON.
"""

promp_horror = [promp_6]
promp_list_reddit = [promp_1, promp_2, promp_3, promp_4, promp_5]
