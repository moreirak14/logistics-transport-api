class InvalidBase(Exception):
    public_message: str


class VehicleTypeInvalid(InvalidBase):
    public_message = "Tipo de veiculo inválido"
