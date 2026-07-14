import pandas as pd
import os
import glob

raw_dir = 'data/raw'
csv_files = glob.glob(os.path.join(raw_dir, '*.csv'))

print("--- 1. Column names and dtypes ---")
dfs = {}
for f in csv_files:
    name = os.path.basename(f)
    try:
        df = pd.read_csv(f)
        dfs[name] = df
        print(f"\nFile: {name}")
        print(df.dtypes)
        print(f"Shape: {df.shape}")
    except Exception as e:
        print(f"Error reading {name}: {e}")

print("\n--- 2. Country alignment: Population.csv vs RegionCountry.csv ---")
pop_df = dfs.get('Population.csv')
reg_df = dfs.get('RegionCountry.csv')

if pop_df is not None and reg_df is not None:
    # Identify country column names (assuming they might differ slightly)
    pop_col = 'Country' if 'Country' in pop_df.columns else None
    reg_col = 'Country' if 'Country' in reg_df.columns else None
    
    if pop_col and reg_col:
        pop_countries = set(pop_df[pop_col].unique())
        reg_countries = set(reg_df[reg_col].unique())
        
        unmatched_in_pop = pop_countries - reg_countries
        unmatched_in_reg = reg_countries - pop_countries
        
        print(f"Unique countries in Population.csv: {len(pop_countries)}")
        print(f"Unique countries in RegionCountry.csv: {len(reg_countries)}")
        print(f"Count unmatched in Population.csv: {len(unmatched_in_pop)} ({len(unmatched_in_pop)/len(pop_countries)*100:.2f}%)")
        print(f"Examples unmatched in Population.csv: {sorted(list(unmatched_in_pop))[:5]}")
        print(f"Count unmatched in RegionCountry.csv: {len(unmatched_in_reg)} ({len(unmatched_in_reg)/len(reg_countries)*100:.2f}%)")
        print(f"Examples unmatched in RegionCountry.csv: {sorted(list(unmatched_in_reg))[:5]}")
    else:
        print(f"Column 'Country' not found. Pop cols: {pop_df.columns.tolist()}, Reg cols: {reg_df.columns.tolist()}")

print("\n--- 3. Population values inspection ---")
if pop_df is not None:
    val_col = 'Value' if 'Value' in pop_df.columns else None
    if val_col:
        sample_vals = pop_df[val_col].dropna().head(10).tolist()
        print(f"Sample values: {sample_vals}")
        print(f"Contains decimals: {pop_df[val_col].apply(lambda x: isinstance(x, float) and not x.is_integer()).any()}")
        print(f"Range: {pop_df[val_col].min()} to {pop_df[val_col].max()}")
        # Check for x1000 scaling plausibility (e.g. if China is ~1.4M instead of 1.4B)
        year_col = 'Year' if 'Year' in pop_df.columns else None
        if year_col:
            china_pop = pop_df[pop_df[pop_col].str.contains('China', na=False) & (pop_df[year_col] == 2018)][val_col]
            if not china_pop.empty:
                print(f"China 2018 Value: {china_pop.values[0]}")
    else:
        print("Value column not found in Population.csv")

print("\n--- 4. Schema Patterns ---")
for name, df in dfs.items():
    print(f"{name}: {df.columns.tolist()[:10]}")
