# data_string = """address: ["Oakwood"] 
# price: [<5000000000]
# property_type: ["house"]
# area: [180] 
# bedrooms: [3]
# bathrooms: [2]
# house_direction: ["south"]
# description: null
# floors: null
# installment_payment: null
# furniture: ["unfurnished"]
# balcony_direction: ["west"]"""

def convert_to_dict(data_string):
    # Create an empty dictionary to store the parsed data
    data_dict = {}

    # Split the string into lines and process each line
    for line in data_string.split("\n"):
        key, value = map(str.strip, line.split(":", 1))
        if value.lower() == "null":
            value = None
        elif value.startswith("[") and value.endswith("]"):
            value = value[1:-1].split(",")
            value = [item.strip() for item in value]
        else:
            value = value.strip()
        
        data_dict[key] = value
    return data_dict
    # print(data_dict)

    # data_dict = {
    #     'address': ['"Oakwood"'],
    #     'price': ['<5000000000'],
    #     'property_type': ['"house"'],
    #     'area': ['180'],
    #     'bedrooms': ['3'],
    #     'bathrooms': ['2'],
    #     'house_direction': ['"south"'],
    #     'description': None,
    #     'floors': None,
    #     'installment_payment': None,
    #     'furniture': ['"unfurnished"'],
    #     'balcony_direction': ['"west"']
    # }
def convert_to_string(data_dict):
    # Convert dictionary items to formatted strings
    formatted_strings = []
    for key, value in data_dict.items():
        if value is None:
            formatted_strings.append(f"{key}: null")
        elif isinstance(value, list):
            formatted_value = ", ".join(value)
            formatted_strings.append(f"{key}: [{formatted_value}]")
        else:
            formatted_strings.append(f"{key}: {value}")

    # Join the formatted strings with line breaks
    result_string = "\n".join(formatted_strings)
    return result_string
    # print(result_string)

# input_data = {
#     "address": None,
#     "price": None,
#     "property_type": None,
#     "area": None,
#     "bedrooms": None,
#     "bathrooms": None,
#     "house_direction": None,
#     "description": ["parking"],
#     "floors": [4],
#     "installment_payment": None,
#     "furniture": None,
#     "balcony_direction": None
# }

# output_data = {
#     "address": ["Hanoi"],
#     "price": None,
#     "property_type": ["house"],
#     "area": None,
#     "bedrooms": None,
#     "bathrooms": None,
#     "house_direction": None,
#     "description": None,
#     "floors": None,
#     "installment_payment": None,
#     "furniture": None,
#     "balcony_direction": None
# }
def merge_keyword(input_data, output_data):
    for key in input_data:
        if input_data[key] is not None:
            output_data[key] = input_data[key]
    return output_data


