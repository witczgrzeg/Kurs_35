import json
from pathlib import Path

class FileHandler:
    def __init__(self, file_path):
        self.file = Path(file_path)
        self.file.write_text("{}", encoding="utf-8") if not self.file.exists() else None
        self.data = self._read()

    def _read(self):
        return json.loads(self.file.read_text(encoding="utf-8"))

    def __getitem__(self, key):
        city, date = key
        return self.data.get(city, {}).get(date, "Data not found")

    def __setitem__(self, key, value):
        city, date = key
        self.data.setdefault(city, {})[date] = value

    def save(self):
        self.file.write_text(json.dumps(self.data, indent=4, ensure_ascii=False), encoding="utf-8")

    def items(self):
        for city, dates in self.data.items():
            for date, info in dates.items():
                yield city, date, info
