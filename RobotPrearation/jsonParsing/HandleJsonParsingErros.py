import json

class JsonParsingErrors:
    def jsonParsingErrors(self):
        try:
            parse_data = json.loads(ABC)
        except json.JSONDecodeError as e:
            print(f"JSON Parsing error: {e}")

jsons = JsonParsingErrors()
jsons.jsonParsingErrors()