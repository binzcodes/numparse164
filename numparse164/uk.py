import phonenumbers


def convert_to_e164(raw_phone):
    try:
        if not raw_phone:
            return

        if raw_phone[0] == '+':
            # Phone number may already be in E.164 format.python
            parse_type = None
        else:
            # If no country code information present, assume it's a UK number
            parse_type = "GB"

        phone_representation = phonenumbers.parse(raw_phone, parse_type)
        return phonenumbers.format_number(phone_representation,
            phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print e