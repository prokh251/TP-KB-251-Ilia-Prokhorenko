class Device:
    def __init__(self, model: str, power_watts: int):
        self.model = model
        self.power_watts = power_watts

    def __str__(self) -> str:
        return f"Пристрій: {self.model} (Потужність: {self.power_watts} Вт)"

    def __repr__(self) -> str:
        return f"Device(model='{self.model}', power_watts={self.power_watts})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Device):
            return False
        return self.model == other.model and self.power_watts == other.power_watts


d1 = Device("ESP32", 2)
d2 = Device("ESP32", 2)

print(str(d1))
print(repr(d1))
print(d1 == d2)