# class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def browse_internet(self):
        return f"{self.brand} {self.model} is browsing the internet."

    def __str__(self):
        return f"Smartphone({self.brand}, {self.model}, Battery: {self.battery_life}hrs)"


# Derived class (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, gpu):
        super().__init__(brand, model, battery_life)
        self.gpu = gpu  # extra attribute

    def browse_internet(self):  # Polymorphism (different behavior)
        return f"{self.brand} {self.model} with {self.gpu} GPU is browsing in ultra-fast gaming mode!"

    def play_game(self, game):
        return f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!"


# Another derived class
class CameraPhone(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Captured a stunning photo with {self.camera_megapixels}MP camera!"

    def browse_internet(self):  # Polymorphism
        return f"{self.brand} {self.model} is browsing Instagram with {self.camera_megapixels}MP photos!"


# --- Testing the classes ---
phone1 = Smartphone("Samsung", "Galaxy S24", 20)
gaming_phone = GamingPhone("Asus", "ROG Phone 8", 15, "Adreno 750")
camera_phone = CameraPhone("iPhone", "15 Pro Max", 18, 48)

print(phone1)
print(phone1.make_call("07-07-137-207"))

print(gaming_phone)
print(gaming_phone.play_game("PUBG Mobile"))
print(gaming_phone.browse_internet())  # Polymorphism in action

print(camera_phone)
print(camera_phone.take_photo())
print(camera_phone.browse_internet())  # Polymorphism in action
