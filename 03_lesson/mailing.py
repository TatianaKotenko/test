class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.Address1 = to_address
        self.Address = from_address
        self.Nul = cost
        self.Str = track

    def __str__(self):
        return (f"Отправление {self.Str} из {self.Address} в {self.Address1}."
                f"Стоимость {self.Nul} рублей.")
