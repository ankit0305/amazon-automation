import json

class AllUtils:
    def __init__(self) -> None:
        pass

    def load_json_from_file(self):
        """
        Loads data from a json file
        return: A json object is returned
        """
        with open("testdata.json", "r") as f:
            json_obj = json.load(f)
        return json_obj