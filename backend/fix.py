import copy

def auto_correct_query(json_data):
    modified_json = copy.deepcopy(json_data)
    try:
        for must_item in modified_json["query"]["bool"]["must"]:
            if "match" in must_item:
                for field_name, field_value in must_item["match"].items():
                    if isinstance(field_value, dict):
                        range_condition = {}

                        if "lte" in field_value:
                            range_condition["lte"] = field_value["lte"]
                        if "gte" in field_value:
                            range_condition["gte"] = field_value["gte"]

                        if range_condition:
                            must_item["range"] = {
                                field_name: range_condition
                            }
                            del must_item["match"]
                            break
    except:
        pass            
    return modified_json

# Original JSON
original_json = {
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "property_type": "apartment"
                    }
                },
                {
                    "range": {
                        "price": {
                            "gte": 5000000000,
                            "lte": 4000000000
                        }
                    }
                }
            ]
        }
    }
}

# Auto-correct queries in JSON
corrected_json = auto_correct_query(original_json)

# Print the corrected JSON
import json
# print(json.dumps(corrected_json, indent=2))
