import os
import requests
from dotenv import load_dotenv


def shorten_link(long_url, api_token):
    request_url = "https://api-ssl.bitly.com/v4/bitlinks"
    payload = {"long_url": long_url}
    response = requests.post(request_url, headers={"Authorization": "Bearer " + api_token}, json=payload)
    return response.json()["link"]

def get_cliks_summary(link, api_token):
    link = link.lstrip("https://")
    request_url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"
    response = requests.get(request_url.format(link), headers={"Authorization": "Bearer " + api_token})
    return response.json()["total_clicks"]

def is_bitlink(link, api_token):
    link = link.lstrip("https://")
    request_url = "https://api-ssl.bitly.com/v4/bitlinks/{}"
    response = requests.get(request_url.format(link), headers={"Authorization": "Bearer " + api_token})
    return response.status_code == 200


def main():
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    long_link = "https://www.codewars.com/dashboard"
    short_link = "https://bit.ly/3s8rXg2"

    #link = input("Введите вашу ссылку: ")
    link = short_link
    if is_bitlink(link, api_token):
        try:
            cliks_summary = get_cliks_summary(link, api_token)
            print("Клики:", cliks_summary)

        except requests.exceptions.HTTPError:
            print("Ошибка при получении кликов")
    
    else:
        try:
            short_link = shorten_link(link, api_token)
            print("Битлинк:", short_link)

        except requests.exceptions.HTTPError:
            print("Ошибка при укорачивании ссылки")
        

if __name__ == '__main__':
    load_dotenv()
    main()
    