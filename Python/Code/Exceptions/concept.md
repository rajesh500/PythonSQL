# custom exception 
# custom exception needed an empty class 

class AgeErr(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeErr("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except AgeErr as e:
    print(e)