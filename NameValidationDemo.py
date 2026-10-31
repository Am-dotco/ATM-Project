#NameValidationDemo.py<----Main Program
from NameValidation import validation
from NameExeption import InValidNameError, SapceError, EmptyNameError
try:
    name=input("Enter UR Name:")
    vname=validation(name) # Function Call
except InValidNameError:
    print("\tINVALID NAME-TRY AGAIN")
except SapceError:
    print("\tDON'T ENTER SPACE FOR NAME-TRY AGAIN")
except EmptyNameError:
    print("\tU Must Enter UR Name--try again")
else:
    print("\tUR Name:{}".format(vname))