import os
import csv

def combine_csv_in_dir(dirpath, result_path):
    csv_files = [f for f in os.listdir(dirpath) if f.endswith('.csv')]

    all_rows = []
    header = None
    
    for csv_file in csv_files:
        filepath = os.path.join(dirpath, csv_file)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            if rows:
                if header is None:
                    header = rows[0]
                    all_rows.append(header)
                all_rows.extend(rows[1:])
    with open(result_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(all_rows)
    
    print(f"Combined {len(csv_files)} CSV files into {result_path}")
