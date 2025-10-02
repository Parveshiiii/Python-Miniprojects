def address(email: str):#we want email to be a string
    if "." in email and "@"  in email:
        return f"Its a valid email --{email}"
    else:
        return f"Its a invalid email --{email}"


test = adress("iamspider@gmail.com")
print(test)

#expected ans = Its a valid email --iamspider@gmail.com
