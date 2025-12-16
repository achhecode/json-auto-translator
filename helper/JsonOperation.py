import json

class JsonOperation:
    def __init__(self, file_path):
        print("JSON Basic Operations")
        self.file_path = file_path

    def extract_all_values_from_json_file(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        values = []
        self._extract_values(data, values)
        return values

    def _extract_values(self, data, values):
        """
        Recursively traverse JSON and collect only values
        """
        if isinstance(data, dict):
            for value in data.values():
                self._extract_values(value, values)
        elif isinstance(data, list):
            for item in data:
                self._extract_values(item, values)
        else:
            values.append(data)


# json_ops = JsonOperation("./en.json")
# result = json_ops.extract_all_values_from_json_file()
# print(result)

