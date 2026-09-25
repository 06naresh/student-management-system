import json
from pathlib import Path

class FileHandler:
    def __init__(self, file_path):
        self.file_path = Path(file_path)


    def read_data(self):
        try:
            if not self.file_path.exists():
                return []

            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print("Error: Student data file contains invalid JSON.")
            return []

        except OSError as err:
            print(f"Error reading file: {err}")
            return []

    def write_data(self,data):
        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            return True
        except OSError as err:
            print(f"Error writing file: {err}")
            return False