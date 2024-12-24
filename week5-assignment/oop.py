# Base class: Smartphone
class Smartphone:
    def __init__(self, brand:str, model, price, battery_life, camera_quality):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_life = battery_life  # in hours
        self.camera_quality = camera_quality  # in megapixels

    # Method to make a call
    def make_call(self, number):
        print(f"Calling {number}...")

    # Method to take a photo
    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} MP camera!")

    # Method to display battery status
    def battery_status(self):
        print(f"The battery life is {self.battery_life} hours.")

    # Method to display smartphone details
    def display_details(self):
        print(f"Smartphone Details: \nBrand: {self.brand}\nModel: {self.model}\nPrice: ${self.price}\nBattery Life: {self.battery_life} hours\nCamera Quality: {self.camera_quality} MP")

# Subclass: SmartphoneWith5G
class SmartphoneWith5G(Smartphone):
    def __init__(self, brand, model, price, battery_life, camera_quality, is_5g_supported=True):
        # Call the constructor of the base class (Smartphone)
        super().__init__(brand, model, price, battery_life, camera_quality)
        self.is_5g_supported = is_5g_supported  # New attribute for 5G support

    # Overriding the battery_status method to include 5G feature
    def battery_status(self):
        if self.is_5g_supported:
            print(f"With 5G support, the battery life is {self.battery_life - 2} hours.")  # Consumes more battery with 5G
        else:
            super().battery_status()

    # Method to display details including 5G info
    def display_details(self):
        super().display_details()
        print(f"5G Support: {'Yes' if self.is_5g_supported else 'No'}")

    # New method to demonstrate 5G capabilities
    def use_5g_network(self):
        if self.is_5g_supported:
            print("Using 5G network for high-speed browsing and streaming.")
        else:
            print("This device does not support 5G.")

# Create an object of the Smartphone class
phone1 = Smartphone("Samsung", "Galaxy S21", 799, 24, 108)
phone1.display_details()
phone1.make_call("123-456-7890")
phone1.take_photo()
phone1.battery_status()

print("\n-------------------\n")

# Create an object of the SmartphoneWith5G subclass
phone2 = SmartphoneWith5G("Apple", "iPhone 14 pro-max", 999, 20, 12)
phone2.display_details()
phone2.make_call("987-654-3210")
phone2.take_photo()
phone2.battery_status()
phone2.use_5g_network()

