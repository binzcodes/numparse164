import re
from .uk import convert_to_e164


def parse_num(raw_phone):
    return re.sub(r'(?!^\+)\D', r'', raw_phone)



# request number
# raw = raw_input("Phone Number >> ")
# clean input
# num = parse_num(raw)
# print num
# convert to e164
# print convert_to_e164(num)   # prints +12125551234
