
import json
import requests

def request_json_data_from_imio_api(url: str) -> dict:
    """Récupérer les données JSON depuis l'API d'IMIO.

    Cette fonction prend en entrée une URL et effectue une requête HTTP pour
    obtenir les données JSON associées. Si la requête réussit, elle renvoie
    les données JSON sous forme de dictionnaire Python. Si la requête échoue,
    elle lève une exception.

    Args:
        url (str): L'URL de l'API d'IMIO à partir de laquelle les données
            JSON doivent être récupérées.

    Returns:
        dict: Un dictionnaire Python contenant les données JSON.

    Raises:
        requests.exceptions.RequestException: Si la requête HTTP échoue.
        json.JSONDecodeError: Si la réponse HTTP n'est pas au format JSON.
    """

    # Effectuer une requête HTTP pour récupérer les données JSON
    response = requests.get(url)

    # Vérifier si la requête a réussi
    response.raise_for_status()

    # Convertir les données JSON en dictionnaire Python
    json_data = response.json()

    # Renvoyer les données JSON sous forme de dictionnaire
    return json_data



if __name__ == "__main__":
    # URL de l'API d'IMIO
    url = "https://infra-api.imio.be/application/teleservices"

    # Récupérer les données JSON depuis l'API d'IMIO
    data = request_json_data_from_imio_api(url)
    # print(data)
    # print(type(data))

    # Convertir les données JSON en objets Python
    objects = [d for d in data]

    print(objects)

    # Récupérer les clés uniques pour chaque enfant
    keys = set()
    for obj in objects:
        keys.update(obj.keys())

    # Afficher les clés uniques
    for key in keys:
        print(key)

