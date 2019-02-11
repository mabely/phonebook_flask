import requests
from distance import distance

def sort_p(returned_results):
    sort_yn = (input('''Do you want to sort? (y/n) ''')).lower()
    try:
        if sort_yn == 'y':
            sort_options_p = int(input(
'''What do you want to sort by?
1 Surname
2 Postcode
3 City
4 Distance
(Select 1/2/3/4)
'''))

            if sort_options_p == 1:
                sortSurname(returned_results)
            elif sort_options_p == 2:
                sortPostcode(returned_results)
            elif sort_options_p == 3:
                sortCity(returned_results)
            elif sort_options_p == 4:
                sortDistance(returned_results)
            else:
                print('Sorry we did not recognise that, please try again.')
                sort_p(returned_results)

        elif sort_yn == 'n':
                pass
        else:
            print('Sorry we did not recognise that, please try again.')
            sort_p(returned_results)

    except ValueError:
        print('Please enter a number.')


def sortSurname(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[1])
    print(format_results(y))
    return y

def sortPostcode(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[5])
    print(format_results(y))
    return y

def sortCity(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[3])
    print(format_results(y))
    return y
  

# BUSINESS
def sort_b(returned_results):
    sort_yn = (input('''Do you want to sort? (y/n) ''')).lower()
    try:
        if sort_yn == 'y':
            sort_options_b = int(input(
'''What do you want to sort by?
1 Business Type
2 Business Name
3 City
4 Postcode
5 Distance
(Select 1/2/3/4/5)
'''))

            if sort_options_b == 1:
                sortBusType(returned_results)
            elif sort_options_b == 2:
                sortBusName(returned_results)
            elif sort_options_b == 3:
                sortCity2(returned_results)
            elif sort_options_b == 4:
                sortPostcode2(returned_results)
            elif sort_options_b == 5:
                sortDistance(returned_results)
            else:
                print('Sorry we did not recognise that, please try again.')
                sort_p(returned_results)

        elif sort_yn == 'n':
                pass
        else:
            print('Sorry we did not recognise that, please try again.')
            sort_p(returned_results)

    except ValueError:
        print('Please enter a number.')

def sortBusType(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[7])
    print(format_results(y))
    return y

def sortBusName(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[0])
    print(format_results(y))
    return y

def sortCity2(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[2])
    print(format_results(y))
    return y

def sortPostcode2(returned_results):
    x = list(returned_results)
    y = sorted(x, key=lambda s:s[4])
    print(format_results(y))
    return y

def sortDistance(returned_results):
    coords = currentLocation()
    x = [result + (distance(coords["latitude"], coords["longitude"], result[-1], result[-2]), ) for result in returned_results]
    y = sorted(x, key=lambda result: result[-1])
    print(format_results(y))
    return y

# GETS USER LOCATION AND FINDS LONG AND LAT - FOR SORTING
def currentLocation():
    inputLocation = input("What's your current location? ")    
    inputLocation = inputLocation.replace(" ", "")
    r = requests.get(f"http://api.postcodes.io/postcodes/{inputLocation}")
    lat = r.json().get("result")["latitude"]
    lon = r.json().get("result")["longitude"]
    return {"longitude": lon, "latitude": lat} 


def format_results(returned_results):
    i = "\n".join([str(item) for item in returned_results])
    return i 