def get_operator(phone_number):
    operators = {
        "017": "Grameenphone",
        "013": "Grameenphone",
        "015": "Teletalk",
        "014": "Banglalink",
        "019": "Banglalink",
        "018": "Robi",
        "016": "Airtel"
    }
    if len(phone_number) != 11:
        return "Invalid number"
    operator_code = phone_number[:3]
    if operator_code not in operators:
        return "Invalid number"
    operator_name = operators[operator_code] 
    return operator_name
phone_number = input("Enter the phone number: ")
result = get_operator(phone_number)
print(result)
