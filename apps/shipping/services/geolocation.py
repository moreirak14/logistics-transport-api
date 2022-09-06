import requests

from apps.shipping.services.exceptions import PageNotLoaded
from config import settings


class GeolocationAPI:
    @staticmethod
    def geolocation_api(zip_code: str) -> None:
        url = f"{settings.URL_GEOLOCATION}/?zip={zip_code}"
        response = requests.get(url=url)

        if response.status_code != 200:
            raise PageNotLoaded

        return response.json()

    def get_geolocation(self, zip_code: str) -> None:
        return self.geolocation_api(zip_code=zip_code)
