"""
Introduction to the Python dictionary.
"""


def main():
    """
    Drive the program.
    """
    cities = {'British Columbia': 'Vancouver',
              'Alberta': 'Edmonton',
              'Saskatchewan': 'Regina',
              'Manitoba': 'The Peg',
              'Ontario': 'Niagara Falls'}

    print(len(cities))
    print(cities)
    print('cities[British Columbia]:', cities['British Columbia'])
    print('cities.get(Ontario):', cities.get('Ontario'))
    print('cities.get(Quebec):', cities.get('Quebec'))

    print(cities.values())
    print(type(cities.values()))
    print(cities.keys())
    print(type(cities.keys()))
    print(cities.items())
    print(type(cities.items()))

    print('British Columbia' in cities)
    print('Quebec' not in cities)

    for province in cities:
        print(province, end=', ')
        print(cities[province])

    cities['British Columbia'] = 'Victoria'
    print(cities)
    cities.clear()
    print(cities)

    cities = {'British Columbia': 'Vancouver',
              'Alberta': 'Edmonton',
              'Saskatchewan': 'Regina',
              'Manitoba': 'The Peg',
              'Ontario': 'Niagara Falls'}
    print(cities)
    cities.popitem()
    print(cities)
    cities.pop('Manitoba')
    print(cities)
    del cities['Saskatchewan']
    print(cities)

    print('-' * 25)

    seasons = {'Spring': ('Mar', 'Apr', 'May'),
               'Summer': ('June', 'July', 'August'),
               'Autumn': ('September', 'October', 'November'),
               'Winter': ('December', 'January', 'February')}
    print(seasons['Spring'])
    print(seasons['Spring'][1])

    print('-' * 25)

    print(sorted(cities.keys()))

    key = 'Alberta'

    if key in cities:
        print('Key is present, value =', cities[key])
    else:
        print('Key not present')


if __name__ == '__main__':
    main()
