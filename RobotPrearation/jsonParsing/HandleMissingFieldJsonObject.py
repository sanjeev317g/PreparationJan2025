import json

class handle_missing_fields_objects:
    def handleMissingFieldsObjects(self):
        json_data = {"name": "Alice"}
        age = json_data.get("age")
        age = json_data.get("age", "Unknown")
        
        print(age)
h = handle_missing_fields_objects()
h.handleMissingFieldsObjects()