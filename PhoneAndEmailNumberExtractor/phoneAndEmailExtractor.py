import pyperclip
import re

text = '''
Hello,

Please contact us at:
- Main Office: 1-800-555-1234
- Support: 2.888.555.5678
- Email: info@samplecompany.com
- Emergency: 3-777-555 8901 ext. 201

Our branch offices are located at:
- New York: 4 (212)555-7890
- London: 44 20 5555 7890
- Sydney: 61 (2)5555-3456

You can also reach out to our department heads:
- HR: hr@samplecompany.org
- Marketing: marketing@samplecompany.net
- IT Support: support@it.samplecompany.co.uk

Best Regards,
Sample Company
'''

# Phone regex
phoneRegex = re.compile(r'''
    (\d{1})            # Country code
    (\s|-|\.)?         # Separator
    (\d{3}|\(\d{3}\))? # Area code
    (\s|-|\.)?         # Separator
    (\d{3})            # First 3 digits
    (\s|-|\.)          # Separator
    (\d{4})            # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # Extension
    ''', re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''
    ([a-zA-Z0-9.%+-]+   # Username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # Domain name
    \.[a-zA-Z]{2,4})    # Dot-something
    ''', re.VERBOSE)

# text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[0], groups[2], groups[4], groups[6]])
    if groups[8] is not None and groups[8] != '':
        phoneNum += ' x' + groups[9]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
