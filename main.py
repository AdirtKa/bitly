import requests


api_token = "18dfc877e20903001ff83f2b682174bc474b0100"
url = "https://api-ssl.bitly.com/v4/bitlinks"

def shorten_link(long_url):
    payload = {"long_url": long_url}
    response = requests.post(url, headers={"Authorization": "Bearer " + api_token}, json=payload)
    return response.json()["link"]


def main():
    # long_url = "https://www.codewars.com/dashboard"
    long_url = input("Введите ссылку для укорачивания: ")
    try:
        short_link = shorten_link(long_url)
        print("Битлинк:", short_link)
    except:
        print("Ошибка при укорачивании ссылки")
        

if __name__ == '__main__':
    main()
    