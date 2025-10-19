# CSV Merger & Cleaner Script

This Python script automatically merges all `.csv` files in the `data/` folder into a single cleaned file.

## Features

- Merge all CSV files from the `data/` directory
- Remove empty rows and duplicate entries
- Standardize the `produit` column: remove spaces and convert to lowercase
- Create a `revenu` column: `quantité * prix_unitaire`
- Generate a `compte_rendu.txt` report containing:
  - Number of files merged
  - Number of rows before and after cleaning
  - Total revenue

## How to Use

1. Place your CSV files inside the `data/` folder
2. Run the script:
   ```bash
   python fusion_ventes.pyThis scripts takes the .csv files in data/ . 


