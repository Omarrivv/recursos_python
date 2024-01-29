# # curso py intermedio
# import requests
# def main():
#     '''
#     This function takes a city and returns 
#     the weather of  that city.
#     '''
#     city = input("Give a city: ")
#     url = f'https://wttr.in/{city}'
#     weather = requests.get(url).text
#     print(weather)
# if __name__ == '__main__':
#     main()
import requests
def main():
    '''
    This function takes a city and returns 
    the weather of that city.
    '''
    while True:
        city = input("Give a city (press 'q' to quit): ")
        # Salir del bucle si se ingresa 'q'
        if city.lower() == 'q':
            break
        url = f'https://wttr.in/{city}'
        weather = requests.get(url).text
        print(weather)
if __name__ == '__main__':
    main()