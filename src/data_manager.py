import numpy as np

try:
    from IPython.display import display
except ImportError:
    display = None


def _afficher_tableau(tableau):
    if display is not None:
        display(tableau)
    else:
        print(tableau.to_string())

def inspector(df, nom="DataFrame"):
    # Debut de l'inspection
    print("#####     DEBUT DE L'INSPECTION     #####")
    
    # Structure du DataFrame avec df.shape
    print("\n----------------------")
    print(f"Structure du DataFrame '{nom}':")
    print(f'Nb de lignes: {df.shape[0]} ; Nb de colonnes: {df.shape[1]}')
    
    # Types de données avec df.dtypes
    print("\n----------------------")
    print(f"Types de données du DataFrame '{nom}':")
    print(df.dtypes)
    
    # Présence d'une potentielle clé unique (identifiant) avec df.nunique()
    print("\n----------------------")
    print(f"Nombre de valeurs uniques dans le DataFrame '{nom}' (pour identifiant PK / FK):")
    print(df.nunique())
    
    # Présence de valeurs manquantes avec df.isnull().sum()
    print("\n----------------------")
    print(f"Valeurs manquantes dans le DataFrame '{nom}':")
    print(df.isnull().sum())
    
    # Fin de l'inspection
    print("\n#####     FIN DE L'INSPECTION     #####")

def inspecter_dataframe(df, nom="DataFrame"):
    """
    Génère un rapport d'inspection complet pour un DataFrame.

    Paramètres:
    -----------
    df : pandas.DataFrame
        Le DataFrame à inspecter
    nom : str
        Le nom du DataFrame (pour l'affichage)

    Retourne:
    ---------
    None (affiche le rapport dans le terminal)
    """

    # Séparateur visuel
    separateur = "=" * 70

    # === EN-TÊTE ===
    print(f"\n{separateur}")
    print(f"📊 RAPPORT D'INSPECTION : {nom.upper()}")
    print(f"{separateur}\n")

    # === 1. DIMENSIONS ===
    print(f"📐 DIMENSIONS")
    print(f"   - Nombre de lignes   : {df.shape[0]:,}")
    print(f"   - Nombre de colonnes : {df.shape[1]}")
    print()

    # === 2. TYPES DE DONNÉES ===
    print(f"📋 COLONNES ET TYPES")
    print("-" * 40)
    for col in df.columns:
        print(f"   {col:25} → {df[col].dtype}")
    print()

    # === 3. VALEURS MANQUANTES ===
    print(f"❓ VALEURS MANQUANTES (NA)")
    print("-" * 40)
    na_counts = df.isna().sum()
    na_total = na_counts.sum()

    if na_total == 0:
        print("   ✅ Aucune valeur manquante !")
    else:
        print(f"   ⚠️  Total de valeurs manquantes : {na_total:,}")
        for col in df.columns:
            if na_counts[col] > 0:
                pct = (na_counts[col] / len(df)) * 100
                print(f"   - {col:25} : {na_counts[col]:,} ({pct:.1f}%)")
    print()

    # === 4. RECHERCHE DE CLÉ UNIQUE ===
    print(f"🔑 RECHERCHE DE CLÉ UNIQUE (IDENTIFIANT)")
    print("-" * 40)
    cle_trouvee = False

    for col in df.columns:
        nb_valeurs_uniques = df[col].nunique()
        nb_lignes = len(df)

        # Une colonne est une clé unique si chaque valeur est différente
        if nb_valeurs_uniques == nb_lignes:
            print(f"   ✅ '{col}' est une clé unique ({nb_valeurs_uniques:,} valeurs uniques)")
            cle_trouvee = True
        elif nb_valeurs_uniques == nb_lignes - df[col].isna().sum():
            # Cas où il y a des NA mais les valeurs non-NA sont uniques
            print(f"   ⚠️  '{col}' pourrait être une clé (unique hors NA)")
            cle_trouvee = True

    if not cle_trouvee:
        print("   ❌ Aucune colonne n'est une clé unique")
        print("   💡 Les colonnes avec le plus de valeurs uniques :")
        # Afficher les 3 colonnes avec le plus de valeurs uniques
        for col in df.columns[:3]:
            print(f"      - {col}: {df[col].nunique():,} valeurs uniques")
    print()

    # === 5. STATISTIQUES DESCRIPTIVES ===
    print(f"📈 STATISTIQUES DESCRIPTIVES")
    print("-" * 40)

    # Colonnes numériques
    cols_numeriques = df.select_dtypes(include=[np.number]).columns.tolist()
    if cols_numeriques:
        print("\n   Colonnes numériques :")
        _afficher_tableau(df[cols_numeriques].describe().round(2))

    # Colonnes catégorielles (texte)
    cols_categorielles = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()
    if cols_categorielles:
        print("\n   Colonnes catégorielles :")
        _afficher_tableau(df[cols_categorielles].describe())

    print(f"\n{separateur}")
    print(f"Fin du rapport pour {nom}")
    print(f"{separateur}\n")