import pickle

flight = {'flight_number': '1700', 'airline': 'Indigo',

'capacity': 225, 'price': 4500,

'source': 'Bangalore', 'destination': 'Hyderabad'}

file_name = 'flight.pkl'

print('Before file:', flight)

with open(file_name, 'wb') as writer:

    pickle.dump(flight, writer)

print('Saved the flight to pickle file')

with open(file_name, 'rb') as reader:

    flight_from_file = pickle.load(reader)

print('Flight after read from pickle file:', flight_from_file)