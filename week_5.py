def describe_city(city, country='chile'):
    """Describe a city."""
    msg= city.title()  + " is in " +  country.title() + "."
    print(msg)

describe_city('Reykjavik', 'Iceland')
describe_city('Santiago')
describe_city('Puntas Arenas')

def prod_num(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

def describe_country(country, *cities):
    """ Describe a country with given cities. """
    for city in cities:
        print(city + " is in " + country)

describe_country('England', 'Liverpool', 'Manchester', 'London')
describe_country('England', 'Liverpool')
