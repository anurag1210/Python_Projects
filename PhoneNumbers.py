import phonenumbers

from phonenumbers import geocoder,carrier

phone_number = phonenumbers.parse('+447496981474')
country = geocoder.description_for_number(phone_number,'en')
print(country)