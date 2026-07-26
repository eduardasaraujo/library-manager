import requests

def get_author_name(author_key):
    url = f"https://openlibrary.org{author_key}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return "Autor desconhecido"

    data = response.json()

    return data["name"]

def search_by_isbn(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    author_name = get_author_name(data["authors"][0]["key"])

    return {
        "title": data["title"],
        "author": author_name,
        "publish_date": data.get("publish_date"),
        "pages": data.get("number_of_pages")
    }