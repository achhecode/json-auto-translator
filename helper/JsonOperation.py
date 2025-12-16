import json
import copy

class JsonOperation:
    def __init__(self, file_path):
        print("JSON Basic Operations")
        self.file_path = file_path

    def load_json(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def extract_unique_values(self):
        data = self.load_json()
        values = set()
        self._extract_values(data, values)
        return list(values)

    def _extract_values(self, data, values):
        if isinstance(data, dict):
            for value in data.values():
                self._extract_values(value, values)
        elif isinstance(data, list):
            for item in data:
                self._extract_values(item, values)
        else:
            values.add(data)

    def replace_values_and_save(self, translation_map, output_file):
        """
        Replaces only exact value matches (quoted values),
        keys are never modified.
        """
        original_data = self.load_json()
        new_data = copy.deepcopy(original_data)

        self._replace_values(new_data, translation_map)

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(new_data, file, ensure_ascii=False, indent=2)

    def _replace_values(self, data, translation_map):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    self._replace_values(value, translation_map)
                else:
                    if value in translation_map:
                        data[key] = translation_map[value]

        elif isinstance(data, list):
            for i, item in enumerate(data):
                if isinstance(item, (dict, list)):
                    self._replace_values(item, translation_map)
                else:
                    if item in translation_map:
                        data[i] = translation_map[item]
