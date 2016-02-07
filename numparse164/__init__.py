# import phonenumbers
import re


def parse_num(raw_phone):
    return re.sub(r'(?!^\+)\D', r'', raw_phone)


"""
def convert_to_e164(raw_phone):
    try:
        if not raw_phone:
            return

        if raw_phone[0] == '+':
            # Phone number may already be in E.164 format.
            parse_type = None
        else:
            # If no country code information present, assume it's a UK number
            parse_type = "GB"

        phone_representation = phonenumbers.parse(raw_phone, parse_type)
        return phonenumbers.format_number(phone_representation,
            phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print e
"""


# request number
# raw = raw_input("Phone Number >> ")
# clean input
# num = parse_num(raw)
# print num
# convert to e164
# print convert_to_e164(num)   # prints +12125551234
