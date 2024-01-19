from phonenumbers import geocoder, timezone
from phonenumbers import parse
from phonenumbers import carrier
import phonenumbers
import pyttsx3 as pt
import phonenumbers
from colorama import Fore
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

while True:
    try:
        number = input('Enter the desired number (in international format, e.g., +1234567890): ')
        if number.lower() == "exit":
            break
        else:
            phone_number = phonenumbers.parse(number)
            country = geocoder.description_for_number(phone_number, 'en')
            carrier_name = carrier.name_for_number(phone_number, 'en')
            time_zones = timezone.time_zones_for_number(phone_number)
            region_code = geocoder.region_code_for_number(phone_number)
            city = geocoder.description_for_number(phone_number, 'en')
            possible_location = geocoder.description_for_number(phone_number, 'en')
         

            print(f"Country: {country}")
            print(f"Carrier: {carrier_name}")
            print(f"Time Zones: {time_zones}")
            print(f"Region Code: {region_code}")
            print(f"City: {city}")
            print(f"Possible Location: {possible_location}")
            print(f"number :{phone_number}")
            

            pt.speak(f"The country of the phone number is {country}")
            pt.speak(f"The carrier of the phone number is {carrier_name}")
            pt.speak(f"The time zones for the phone number are {time_zones}")
            pt.speak(f"The region code for the phone number is {region_code}")
            pt.speak(f"The city for the phone number is {city}")
            pt.speak(f"The possible location for the phone number is {possible_location}")
            
    except Exception as ph:
        print(ph)

