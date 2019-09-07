import pandas as pd
import numpy as np

df = pd.read_csv("athlete_events.csv")
df_sum = df[df["Season"] == "Summer"]
ejercicio_1 = df.shape
ejercicio_2 = df.Games.nunique()
ejercicio_3 = df["Season"].value_counts(normalize=True)
ejercicio_4 = df[df["Season"] == "Summer"].sort_values(by="Year")[["City"]].iloc[0]
ejercicio_5 = df[df["Season"] == "Winter"].sort_values(by="Year")[["City"]].iloc[0]
ejercicio_6 = df["NOC"].value_counts().head(10)
ejercicio_7 = df["Medal"].value_counts(normalize=True)
ejercicio_8 = df_sum[df_sum["Year"] == df_sum["Year"].min()].NOC.unique()
