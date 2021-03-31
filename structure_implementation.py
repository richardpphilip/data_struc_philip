
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

print(months[2])

birthday_locations = ['home', 'vacation', 'hawaii', 'colorado', 'virginia']

birthday_locations.extend(['LA', 'San Fransisco', 'San Diego'])

print(birthday_locations)

i = 0

while i < len(birthday_locations):
    print(birthday_locations[i])
    i += 1

