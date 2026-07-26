import requests

def get_author_name(author_key):
    url = f"https://openlibrary.org{author_key}.json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        return data.get("name", "Autor desconhecido")

    except requests.RequestException:
        return "Autor desconhecido"
    
def search_by_isbn(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        author_name = get_author_name(data["authors"][0]["key"])

        return {
            "title": data.get("title", ""),
            "author": author_name,
            "category": "Não informado",
            "publish_date": data.get("publish_date"),
            "pages": data.get("number_of_pages")
        }

    except requests.RequestException:
        return None