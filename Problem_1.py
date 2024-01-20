def full_name():
    try:
        first_name = str(input("Enter your first name:"))
        last_name = str(input("Enter your last name:"))
        if validate_inp(first_name) and validate_inp(last_name):
            full_name= first_name +" "+last_name
            print(full_name)
            return full_name
        else:
            print("please enter a valid string")
    except Exception as error:
        print("Error Occured {}".format(error))

def validate_inp(input_value):
    if input_value != '' and input_value is not None and input_value.isspace() != True and input_value.isnumeric() != True:
        return True
    else:
        return False
def string_alternative(full_name):
    try:
        inp_1= full_name
        print(inp_1[::2])
    except Exception as error:
        print("Error Occured {}".format(error))
if __name__ == '__main__':
    f=full_name()
    string_alternative(f)

