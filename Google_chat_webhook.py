from httplib2 import Http
from json import dumps

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    url = 'https://chat.googleapis.com/v1/spaces/AAAA8WQFzDY/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=-YMDgAnzq3G4Z2VYvP978pm8o7INXivGGw9A9ez_kUM%3D'
    bot_message = {
        'text' : 'webhook'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()
