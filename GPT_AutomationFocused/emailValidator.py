def validateEmail(email):
    if " " in email:
        return "Invalid email : should not contain space"
    if '@' not in email:
        return "Invalid email : should contain @ symbol"
    # split eemail in two part
    parts = email.split('@')

    doeemail_part = parts[1]

    if '.' not in doeemail_part:
        return "Invalid email : should contains ."
    
    return "valid email"

resp = validateEmail("sanju.reso@gmail.")
print(resp)
