import requests


def main():
    cities = ["london", "svo", "Череповец"]
    payload = {"nTqM": "", "lang": "ru"}
    for city in cities:
        url_template = "http://wttr.in/{}"
        url = url_template.format(city)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    main()
