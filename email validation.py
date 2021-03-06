# Welcome to my Email Syntax Validator.
#a few notes. this program only works for emails ending in .com, and also the address cannot contain any special characters such as ?,!,*, etc.

vemail = False
while not vemail:
    email = input("What is your email adress?") #email adress
    atpos = email.find("@") #finds the @ symbol
    atcount = email.count("@")#sees how many @ symbols there are
    dotcount = email.count(".")#counts how many full stops there are
    elen = len(email)#takes the length of the email
    prefix = slice(0, atpos,1) #takes the prefix of the email. IE: "kenny@domain.com" ---> "kenny"
    suffix = slice(atpos,elen,1)#takes the suffix of the email. IE: "kenny@domain.com" ---> "@domain.com"
    emailstart = email[prefix]#splits the email into the prefix
    emailend = email[suffix]#splits the email into the suffix
    sufdotpos = emailend.index(".")#finds where the full stop is located in the email suffix
    eendlen = len(emailend)#email suffix length
    eepre = slice(1,sufdotpos,1)#takes the first part of the suffix. IE: "@domain.com" ---> "domain"
    eesuf = slice(sufdotpos + 1,eendlen,1)#takes the last part of the suffix. IE: "@domain.com" ---> "com"
    if emailstart.isalnum() and atcount == 1 and dotcount == 1 and emailend.startswith("@") and emailend[eepre].isalnum() and emailend[eesuf].isalnum():#see bottom for explanation.
        print("email syntax valid")
        vemail = True #ends the loop is conditions are met, email is valid
    else:
        print("email syntax invalid!")

    #if statement ensures the email is correctly syntaxed:
        #contains no specal characters
        #is alphanumeric (a-z 0-9)
        #ends in .com,.net.org, etc. (NO .CO.UK AND SIMILAR ENDS)