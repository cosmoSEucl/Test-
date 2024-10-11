from pathlib import Path

src_directory = Path(__file__).parent

project_root = src_directory.parent

csv_file = project_root.joinpath('data', 'example.csv')

if csv_file.exists():
    print("CSV file found.")
else:
    print("CSV file not found.")
