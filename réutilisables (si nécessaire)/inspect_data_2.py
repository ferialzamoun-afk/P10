import pandas as pd
import os
import glob

raw_dir = 'data/raw'
dfs = {}
for f in glob.glob(os.path.join(raw_dir, '*.csv')):
    name = os.path.basename(f)
    dfs[name] = pd.read_csv(f)

print("\n--- 2. Country alignment (Improved) ---")
pop_df = dfs.get('Population.csv')
reg_df = dfs.get('RegionCountry.csv')

pop_col = 'Country'
reg_col = 'COUNTRY (DISPLAY)'

pop_countries = set(pop_df[pop_col].unique())
reg_countries = set(reg_df[reg_col].unique())

unmatched_in_pop = pop_countries - reg_countries
unmatched_in_reg = reg_countries - pop_countries

print(f"Unique countries in Population.csv: {len(pop_countries)}")
print(f"Unique countries in RegionCountry.csv: {len(reg_countries)}")
print(f"Count unmatched in Population.csv: {len(unmatched_in_pop)} ({len(unmatched_in_pop)/len(pop_countries)*100:.2f}%)")
print(f"Examples unmatched in Population.csv: {sorted(list(unmatched_in_pop))[:10]}")
print(f"Count unmatched in RegionCountry.csv: {len(unmatched_in_reg)} ({len(unmatched_in_reg)/len(reg_countries)*100:.2f}%)")
print(f"Examples unmatched in RegionCountry.csv: {sorted(list(unmatched_in_reg))[:10]}")

print("\n--- 3. Population values inspection (Revised) ---")
val_col = 'Population'
sample_vals = pop_df[val_col].dropna().head(10).tolist()
print(f"Sample values: {sample_vals}")
print(f"Contains non-integers: {pop_df[val_col].apply(lambda x: x % 1 != 0).any()}")
print(f"Range: {pop_df[val_col].min()} to {pop_df[val_col].max()}")

china_pop = pop_df[pop_df[pop_col].str.contains('China', na=False) & (pop_df['Year'] == 2018)][val_col]
if not china_pop.empty:
    print(f"China 2018 Value: {china_pop.values[0]}")
    # China ~1.4 Billion. If value is ~1.4M, then x1000 is likely.
