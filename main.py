from os import system
from time import sleep
from page import Page
from scrap_handler import ScrapHandler
from xml_adapter import XmlAdapter

if __name__ == '__main__':
    xml = XmlAdapter()
    while True:
        print('''Welcome, choose the action
1. Add page to scrap
2. Remove page to scrap
3. Get info about one page
4. Get info about multiple page
5. Show available page
    
0. Exit''')
        choose = str(input('Your choose: '))
        match choose:
            case '1':
                system('cls')
                name = str(input('Name page: '))
                url = str(input('Url page: '))
                print('Adding to config...')
                sleep(0.4)
                xml.add_to_xml(name, url)
                print(f'Page {name} added')
                system('pause')
                continue
            case '2':
                name = str(input('Name page: '))
                if xml.remove_from_xml(name) == 0:
                    print('Saved page not exists')
                    sleep(0.4)
                else:
                    print('Removing page...')
                    sleep(0.4)
                    print('Page removed')
                continue
            case '3':
                pass
            case '4':
                pass
            case '5':
                system('cls')
                print('Available page:')

            case '0':
                exit()
            case _:
                print('Choose correct task!!!')
                sleep(1)
                system('cls')
                break
