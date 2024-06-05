meme_dict = {
    "CRINGE": "Verguenza ajena",
    "EMO": "Gótico, pesimista, ropa obscura",
    "LOL": "Adj. Algo gracioso ej: Que LOL. Sus. Siglas juego Leage Of Legends ej: Tu juegas LOL. Sus. Expresión de risa (reirse en voz alta)"
            }

            

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

 

if word in meme_dict.keys():

    # ¿Qué debemos hacer si se encuentra la palabra?

    print("Esa palabra significa:",meme_dict[word])

else:

    # ¿Qué hacer si no se encuentra la palabra?

    print("Esa palabra no se encuentra en el meme_dict") 
