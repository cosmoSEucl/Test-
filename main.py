from pathlib import Path

project_root = Path(__file__).parent

csv_file = project_root.joinpath('data', 'example.csv')

print(csv_file.exists())
