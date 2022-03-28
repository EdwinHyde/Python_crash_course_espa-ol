# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
#           keys in your dictionary. Create a dictionary of information about each city and
#           include the country that the city is in, its approximate population, and one fact
#           about that city. The keys for each city’s dictionary should be something like
#           country, population, and fact. Print the name of each city and all of the information
#           you have stored about it.

ciudades = {
    'ibagué': {
        'departamento': 'tolima',
        'clima': 'cálido',
        'población': '2 millones',
        'sobre la ciudad': 'llamada la capital musical de Colombia, se caracteriza por ser pequeña '
                           'y acogedora, llena de muchos músicos en sus calles.',
        },
    'manizales':{
        'departamento': 'caldas',
        'clima': 'frío',
        'población': '1.5 millones',
        'sobre la ciudad': 'una ciudad que se caracteriza por sus continuas faldas o lomas, tiene'
                           'entre sus atractivos muchos parques y la calidez de su gente.',
        },
    'bogotá':{
        'departamento': 'cundinamarca',
        'clima': 'frío',
        'población': '15 millones',
        'sobre la ciudad': 'la capital del país, la Sillicon Valley de latinoamerica, es una ciudad'
                           'muy poblada e insegura, aunque acoge a muchisimas personas del interior.',
        },

    }

for ciudad, datos in ciudades.items():
    print(f"\nLa ciudad de {ciudad.title()}, se encuentra en el departamento de {datos['departamento'].title()}"
          f", posee un clima {datos['clima']} y actualmente cuenta con una población de aproximadamente "
          f"{datos['población']} de habitantes. De esta ciudad se puede decir que es {datos['sobre la ciudad']}")


    # ----OTRA FORMA DE SOLUCIONARLO----

    # print(f"\nNombre de la ciudad: {ciudad.title()}")
    # print(f"\tDepartamento: {datos['departamento'].title()}")
    # print(f"\tClima: {datos['clima'].title()}")
    # print(f"\tPoblación: {datos['población']}")
    # print(f"\tAcerca de la ciudad: {datos['sobre la ciudad'].title()}")