#Example of script without Regual Expression
def isPhoneNumber(text):
    if len(text) != 14:
        return False
    for i in range(0,1):
        if not text[i].isdecimal():
            return False
    if text[1] != '-':
        return False
    for i in range(2,5):
        if not text[i].isdecimal():
            return False
    if text[5] != '-':
        return False
    for i in range(6,9):
        if not text[i].isdecimal():
            return False
    if text[9] != '-':
        return False
    for i in range(10,13):
        if not text[i].isdecimal():
            return False
    return True        
    
message = 'Call me once again, tommorrow. My numbers are 8-777-777-7777, 8-777-666-5555.'
for i in range(len(message)):
    chunk = message[i:i+14]
    if(isPhoneNumber(chunk)):
        print('Phone number found: ' + chunk)
print('Done')

#Example of script with Regular Expression
import re
phoneNumRegex = re.compile(r'\d-\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.findall('My phone number is 8-777-777-7777. Work number is: 8-888-888-8888')
print(mo)


heroRegex = re.compile(r'Rakhin|Mura')
mo1 = heroRegex.search('Mura and Rakhin')
print(mo1.group())

nameRegex = re.compile(r'Rakh(inator|in|ina)')
mo2 = nameRegex.search('Rakhina is a Rakhinator')
print(mo2.group())
print(mo2.group(1))

songRegex = re.compile(r'When the (?:sun ) ?stars go blue')
mo3 = songRegex.search('Where do you go when you are lonely, When the sun stars go blue')
print(mo3.group())

compRegex = re.compile(r'\d[^,]+')
mo4 = compRegex.findall('1.Class, 2.Dumbest, 3.Have Fun, 4.Goodbye')
print(mo4)

wildRegex = re.compile(r'.in')
mo5 = wildRegex.findall('I have been in a lot beginnings where in last streaming')
print(mo5)

myNameRegex = re.compile(r'rakhin', re.I)
nameRegex = myNameRegex.findall('RAKHIN IS HERE, AND THAT IS VERY GOOD')
print(nameRegex)