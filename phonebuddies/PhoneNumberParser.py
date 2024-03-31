import re
import phonenumbers
class PhoneNumberParser:
    @staticmethod
    def parse_to_valid_whatsapp(phone_number):
        print (phone_number)
        # Remove any non-digit characters from the phone number
        no_whitespace = phone_number.replace(' ','').replace('+','')
        digits_only = re.sub(r'\D', '', no_whitespace)

        print(digits_only)

        # Special cases for Afghan numbers without country codes
        if digits_only.startswith('760'):
            return '+93' + digits_only
        elif digits_only.startswith('740'):
            return '+93' + digits_only

        # If the phone number starts with '00', remove the leading '00'
        if digits_only.startswith('00'):
            digits_only = digits_only[2:]
        
        # Dictionary mapping country codes to their respective international dialing codes
        country_codes = {
            '1': '+1',  # United States
            '44': '+44',  # United Kingdom
            '93': '+93', # Afghanistan
            # Add more country codes as needed
        }

        # Iterate over country codes to find a match
        for code, dialing_code in country_codes.items():
            if digits_only.startswith(code):
                # Get the city code and local number
                city_code = digits_only[len(code):len(code) + 3]
                local_number = digits_only[len(code) + 3:]
                
                # Construct the full international format with leading zeros retained
                
                print(f'{dialing_code}{city_code}{local_number}'.strip())

                return f'{dialing_code}{city_code}{local_number}'.strip()  # Strip any whitespace



        ready_for_phonenumbers_module = '+' + digits_only
        return ready_for_phonenumbers_module
        '''
        parsed_number = phonenumbers.parse(ready_for_phonenumbers_module, 
None)
        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164) 
        '''