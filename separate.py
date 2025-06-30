import pandas as pd

# === SETTINGS ===
input_file = "Costar_Propoerties.xlsx"  # Replace with your Excel file name
sheet_name = 0  # or use the actual sheet name like "Sheet1"
chunk_size = 30000  # Number of rows per smaller file
output_prefix = "costar_Properties_"  # Base name for output files

# === LOAD FILE ===
print("Loading Excel file...")
df = pd.read_excel(input_file, sheet_name=sheet_name)

# === SPLIT & EXPORT ===
total_rows = len(df)
num_parts = (total_rows + chunk_size - 1) // chunk_size

print(f"Total rows: {total_rows}, splitting into {num_parts} files...")

for i in range(num_parts):
    start_row = i * chunk_size
    end_row = start_row + chunk_size
    chunk_df = df.iloc[start_row:end_row]
    output_file = f"{output_prefix}{i+1}.xlsx"
    chunk_df.to_excel(output_file, index=False)
    print(f"Saved: {output_file}")

print("✅ Splitting complete.")
