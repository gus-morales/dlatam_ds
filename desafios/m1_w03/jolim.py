import pandas as pd

filename = "athlete_events.csv"

df = pd.read_csv(filename)
print(df.columns)
# cantidad de registros y de columnas
ejercicio_1 = df.shape

# total competencias (juegos)
ejercicio_2 = df.Games.nunique()

# % atletas que participaron tanto en los juegos de invierno como de verano
total_ath = df.ID.nunique()
print(total_ath)

for (colName, colData) in df.iteritems():
   if colName == "Season":
       print(colData.values)



#ejercicio_3 = 
