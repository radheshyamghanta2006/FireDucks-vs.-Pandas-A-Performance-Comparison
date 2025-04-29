# Load Libraries
import pandas as pd
import fireducks.pandas as fd
import time

# File Path
file_path = 'large_dataset.csv'

# Helper function to measure execution time
def timed_operation(label, func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(f"{label} Time: {time.time() - start:.4f} seconds")
    return result

# -----------------------------
# 1. Read CSV
pandas_df = timed_operation("Pandas Read", pd.read_csv, file_path)
fd_df = timed_operation("FireDucks Read", fd.read_csv, file_path)

# -----------------------------
# 2. Filter data → amount > 100
pandas_filtered = timed_operation("Pandas Filter", lambda df: df[df['amount'] > 100], pandas_df)
fd_filtered = timed_operation("FireDucks Filter", lambda df: df[df['amount'] > 100], fd_df)

# -----------------------------
# 3. GroupBy category & sum amount
pandas_grouped = timed_operation("Pandas GroupBy", lambda df: df.groupby('category')['amount'].sum().reset_index(), pandas_filtered)
fd_grouped = timed_operation("FireDucks GroupBy", lambda df: df.groupby('category')['amount'].sum().reset_index(), fd_filtered)

# -----------------------------
# 4. Sort by amount descending
pandas_sorted = timed_operation("Pandas Sort", lambda df: df.sort_values(by='amount', ascending=False), pandas_grouped)
fd_sorted = timed_operation("FireDucks Sort", lambda df: df.sort_values(by='amount', ascending=False), fd_grouped)

# -----------------------------
print("Demo Completed Successfully!")
