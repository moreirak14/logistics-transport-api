import requests

from config import settings
from src.services.exceptions import PageNotLoaded


class GeolocationAPI:

    @staticmethod
    def geolocation(zip_code: str) -> None:
        url = f"{settings.URL_GEOLOCATION}/?zip={zip_code}"
        response = requests.get(url=url)

        if response.status_code != 200:
            raise PageNotLoaded

        return response.json()
