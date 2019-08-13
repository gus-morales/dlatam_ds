import pandas as pd
import numpy as np

filename = "athlete_events.csv"
df = pd.read_csv(filename)

# cantidad de registros y de columnas
ejercicio_1 = df.shape

# total competencias (juegos)
ejercicio_2 = df.Games.nunique()

# % atletas que participaron tanto en verano como en invierno
ejercicio_3 = df["Season"].value_counts(normalize=True)

# donde fue la primera celebracion de un juego de verano
ejercicio_4 = df[df["Season"] == "Summer"]\
    .sort_values(by="Year")[["City"]].iloc[0]

# donde fue la primera celebracion de un juego de invierno
ejercicio_5 = df[df["Season"] == "Winter"]\
    .sort_values(by="Year")[["City"]].iloc[0]

# los 10 primeros países con mayor cantidad de atletas participantes
ejercicio_6 = df["NOC"].value_counts().head(10)

# % de medallas asignadas (oro, bronce, plata)
ejercicio_7 = df["Medal"].value_counts(normalize=True)

# los países participantes en las primeras olimpiadas de verano
df_sum = df[df["Season"] == "Summer"]
ejercicio_8 = df_sum[df_sum["Year"] == df_sum["Year"].min()].NOC.unique()
