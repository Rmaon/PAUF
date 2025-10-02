import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 34, 45, 29],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'Moroso': [False, True, False, True]
}

df = pd.DataFrame(data)

print(df.iloc[0:3])
print("-*-")
print(df['Edad'])
print("-*-")
print(df['Edad'].mean())
print("-*-")
print(df['Nombre'].sort_values())
print("-*-")
print(df['Nombre'].sort_values(ascending=False))
print("-*- F I L T R A D O   P O R   E D A D-*-")
print( df[(df['Edad'] < 30 ) & (df['Edad'] > 20 )] )
print("-*- F I L T R A D O   P O R   M O R O S O S -*-")
print( df[df['Moroso'] == True] )


datos = [
    {"ID": 1, "Nombre": "Ana",    "Edad": 20, "Curso": "DAW2", "Grupo": "A", "Ciudad": "Puertollano", "Nota": 7.5, "Becado": True,  "Creditos": 60, "FechaMatricula": "2024-09-10"},
    {"ID": 2, "Nombre": "Luis",   "Edad": 35, "Curso": "DAW2", "Grupo": "B", "Ciudad": "Ciudad Real", "Nota": 4.0, "Becado": False, "Creditos": 55, "FechaMatricula": "2024-09-12"},
    {"ID": 3, "Nombre": "María",  "Edad": 60, "Curso": "DAW1", "Grupo": "A", "Ciudad": "Toledo",       "Nota": 9.2, "Becado": True,  "Creditos": 65, "FechaMatricula": "2024-09-09"},
    {"ID": 4, "Nombre": "Pedro",  "Edad": 15, "Curso": "DAW1", "Grupo": "C", "Ciudad": "Albacete",     "Nota": 5.5, "Becado": False, "Creditos": 58, "FechaMatricula": "2024-09-15"},
    {"ID": 5, "Nombre": "Lucía",  "Edad": 22, "Curso": "DAW2", "Grupo": "A", "Ciudad": "Puertollano", "Nota": 8.8, "Becado": False, "Creditos": 61, "FechaMatricula": "2024-09-11"},
    {"ID": 6, "Nombre": "Diego",  "Edad": 44, "Curso": "DAW1", "Grupo": "B", "Ciudad": "Toledo",       "Nota": 6.2, "Becado": True,  "Creditos": 59, "FechaMatricula": "2024-09-13"},
    {"ID": 7, "Nombre": "Elena",  "Edad": 28, "Curso": "DAW2", "Grupo": "C", "Ciudad": "Ciudad Real", "Nota": 3.2, "Becado": False, "Creditos": 40, "FechaMatricula": "2024-09-10"},
    {"ID": 8, "Nombre": "Sergio", "Edad": 41, "Curso": "DAW1", "Grupo": "A", "Ciudad": "Albacete",     "Nota": 9.8, "Becado": True,  "Creditos": 66, "FechaMatricula": "2024-09-08"},
    {"ID": 9, "Nombre": "Nuria",  "Edad": 19, "Curso": "DAW2", "Grupo": "B", "Ciudad": "Puertollano", "Nota": 7.9, "Becado": True,  "Creditos": 62, "FechaMatricula": "2024-09-16"},
    {"ID":10, "Nombre": "Javier", "Edad": 52, "Curso": "DAW1", "Grupo": "C", "Ciudad": "Toledo",       "Nota": 4.9, "Becado": False, "Creditos": 48, "FechaMatricula": "2024-09-14"},
]

