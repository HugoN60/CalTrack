import pandas as pd
from pathlib import Path


def merge(dfs):
    """
    Merge csv, drop the NaN lines et duplicated lines
    INPUT: A dictionary containing pandas Dataframe
    OUTPUt: A pandas Dataframe 
    """
    merged = pd.concat(dfs.values(), ignore_index=True)
    ligneInit += merged.shape[0]
    merged.dropna(inplace=True)
    merged.drop_duplicates(inplace=True)
    ligneFinal += merged.shape[0]
    return merged

directory = Path("data")

dfs = {}
nbFile = 0
ligneInit = 0
ligneFinal = 0
for i, file in enumerate(directory.iterdir()):
    if file.suffix == ".csv":
        nbFile +=1
        df = pd.read_csv(file)
        dfs[file.stem] = df

df = merge(dfs)

df["produit"] = df["produit"].str.lower()
df["produit"] = df["produit"].str.strip()
df["revenu"] = df["quantité"] * df["prix_unitaire"]
revenueTot = df["revenu"].sum()

df.to_csv("ventes.csv")

with open("compte_rendu.txt", "w", encoding="utf-8") as file:
    file.write(f"Fichiers fusionnés: {nbFile}\n")
    file.write(f"Ligne initiales: {ligneInit}\n")
    file.write(f"Ligne finale: {ligneFinal}\n")
    file.write(f"Revenue total: {revenueTot}\n")








