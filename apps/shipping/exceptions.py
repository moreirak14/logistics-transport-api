class InvalidBase(Exception):
    public_message: str


class ZipCodeInvalid(InvalidBase):
    public_message = "CEP inválido"
