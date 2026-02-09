import requests


cities = ["london", "svo", "Череповец"]


def get_url():
    urls = []
    for city in cities:
        urls.append(f"http://wttr.in/{city}")
    return urls


def main(url):
    payload = {"nTqM": "", "lang": "ru"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    urls = get_url()
    for url in urls:
        main(url)

