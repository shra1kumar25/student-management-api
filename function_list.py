def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False


print(validate_email("sravan@gmail.com"))
print(validate_email("sravan@gmail"))
print(validate_email("sravan.com"))



def create_response(status, message, data):
    return {
        "status": status,
        "message": message,
        "data": data
    }

response = create_response(
    "success",
    "Student created successfully",
    {
        "id": 101,
        "name": "Sravan",
        "age": 30
    }
)



def create_response(status, message, data):
    return {
        "status": status,
        "message": message,
        "data": data
    }

response = create_response(
    "success",
    "Student created successfully",
    {
        "id": 101,
        "name": "Sravan",
        "age": 30
    }
)

response = create_response(
    "success",
    "Student created successfully",
    {
        "id": 101,
        "name": "Sravan",
        "age": 30
    }
)

print(response)