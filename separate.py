import pandas as pd
import os

# === SETTINGS ===
input_file = "Costar_Propoerties.xlsx"  # Replace with your actual Excel file
sheet_name = 0  # Or use actual sheet name like "Sheet1"
group_column = "State"  # Column to group by
chunk_size = 30000  # Rows per chunk
base_output_folder = "output_by_state"  # Main output folder

# === LOAD EXCEL ===
print("Loading Excel file...")
df = pd.read_excel(input_file, sheet_name=sheet_name)

# === REMOVE EMPTY COLUMNS ===
df = df.dropna(axis=1, how='all')

# === CHECK GROUP COLUMN EXISTS ===
if group_column not in df.columns:
    raise ValueError(f"'{group_column}' column not found in Excel file.")

# === CREATE BASE OUTPUT FOLDER ===
os.makedirs(base_output_folder, exist_ok=True)

# === GROUP AND SPLIT ===
grouped = df.groupby(group_column)
print(f"Found {len(grouped)} unique values in '{group_column}' column. Processing...")

for group_name, group_df in grouped:
    clean_group_name = str(group_name).strip().replace(" ", "_").replace("/", "-")
    group_folder = os.path.join(base_output_folder, clean_group_name)
    os.makedirs(group_folder, exist_ok=True)

    total_rows = len(group_df)
    num_chunks = (total_rows + chunk_size - 1) // chunk_size

    for i in range(num_chunks):
        start = i * chunk_size
        end = start + chunk_size
        chunk_df = group_df.iloc[start:end]
        chunk_filename = f"{clean_group_name}_part_{i + 1}.xlsx"
        output_path = os.path.join(group_folder, chunk_filename)
        chunk_df.to_excel(output_path, index=False)
        print(f"Saved: {output_path}")

print("✅ All files saved.")
