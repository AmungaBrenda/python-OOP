class ElectronicDevice:
    """Base class for all electronic devices"""
    
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
        self.power_status = False
    
    def power_on(self):
        """Turn on the device"""
        if not self.power_status:
            self.power_status = True
            return f"{self.model} is now powered on."
        return f"{self.model} is already on."
    
    def power_off(self):
        """Turn off the device"""
        if self.power_status:
            self.power_status = False
            return f"{self.model} is now powered off."
        return f"{self.model} is already off."
    
    def get_info(self):
        """Return basic info about the device"""
        return f"Model: {self.model}, Year: {self.year}, Price: ${self.price}"


class AppleDevice(ElectronicDevice):
    """Base class for all Apple devices"""
    
    def __init__(self, model, year, price, os_version):
        super().__init__(model, year, price)
        self.os_version = os_version
        self.brand = "Apple"
    
    def update_os(self, new_version):
        """Update the operating system"""
        self.os_version = new_version
        return f"{self.model} updated to {new_version}."
    
    def get_info(self):
        """Override to include Apple-specific info"""
        basic_info = super().get_info()
        return f"{basic_info}, Brand: {self.brand}, OS: {self.os_version}"


class AppleSmartphone(AppleDevice):
    """Class representing an Apple iPhone"""
    
    def __init__(self, model, year, price, os_version, screen_size, storage, battery_capacity, camera_mp):
        super().__init__(model, year, price, os_version)
        self.screen_size = screen_size  # in inches
        self.storage = storage  # in GB
        self.battery_capacity = battery_capacity  # in mAh
        self.camera_mp = camera_mp  # in megapixels
        self.apps = []
        self.cellular_connection = False
        self.wifi_connection = False
        self.bluetooth_status = False
    
    def make_call(self, number):
        """Make a phone call"""
        if self.power_status and self.cellular_connection:
            return f"Calling {number} from {self.model}..."
        elif not self.power_status:
            return f"{self.model} is powered off. Turn it on first."
        else:
            return f"No cellular connection available on {self.model}."
    
    def send_text(self, number, message):
        """Send a text message"""
        if self.power_status and self.cellular_connection:
            return f"Message sent to {number}: '{message}'"
        elif not self.power_status:
            return f"{self.model} is powered off. Turn it on first."
        else:
            return f"No cellular connection available on {self.model}."
    
    def install_app(self, app_name):
        """Install an app on the phone"""
        if self.power_status:
            if app_name not in self.apps:
                self.apps.append(app_name)
                return f"{app_name} installed on {self.model}."
            return f"{app_name} is already installed on {self.model}."
        return f"{self.model} is powered off. Turn it on first."
    
    def uninstall_app(self, app_name):
        """Uninstall an app from the phone"""
        if self.power_status:
            if app_name in self.apps:
                self.apps.remove(app_name)
                return f"{app_name} uninstalled from {self.model}."
            return f"{app_name} is not installed on {self.model}."
        return f"{self.model} is powered off. Turn it on first."
    
    def toggle_wifi(self):
        """Toggle Wi-Fi connection"""
        if self.power_status:
            self.wifi_connection = not self.wifi_connection
            status = "on" if self.wifi_connection else "off"
            return f"Wi-Fi is now {status} on {self.model}."
        return f"{self.model} is powered off. Turn it on first."
    
    def toggle_bluetooth(self):
        """Toggle Bluetooth connection"""
        if self.power_status:
            self.bluetooth_status = not self.bluetooth_status
            status = "on" if self.bluetooth_status else "off"
            return f"Bluetooth is now {status} on {self.model}."
        return f"{self.model} is powered off. Turn it on first."
    
    def toggle_cellular(self):
        """Toggle cellular connection"""
        if self.power_status:
            self.cellular_connection = not self.cellular_connection
            status = "on" if self.cellular_connection else "off"
            return f"Cellular connection is now {status} on {self.model}."
        return f"{self.model} is powered off. Turn it on first."
    
    def take_photo(self):
        """Take a photo with the phone's camera"""
        if self.power_status:
            return f"Photo taken with {self.model}'s {self.camera_mp}MP camera."
        return f"{self.model} is powered off. Turn it on first."
    
    def get_battery_info(self):
        """Get battery information"""
        if self.power_status:
            # In a real implementation, this would calculate actual battery percentage
            return f"Battery capacity: {self.battery_capacity}mAh"
        return f"{self.model} is powered off. Turn it on first."
    
    def get_storage_info(self):
        """Get storage information"""
        if self.power_status:
            # In a real implementation, this would calculate actual free space
            app_count = len(self.apps)
            return f"Storage: {self.storage}GB, {app_count} apps installed"
        return f"{self.model} is powered off. Turn it on first."
    
    def get_info(self):
        """Override to include iPhone-specific info"""
        basic_info = super().get_info()
        return f"{basic_info}, Screen: {self.screen_size}\", Storage: {self.storage}GB, Battery: {self.battery_capacity}mAh, Camera: {self.camera_mp}MP"


# Example usage
if __name__ == "__main__":
    # Create an iPhone 15 Pro Max
    iphone = AppleSmartphone(
        model="iPhone 15 Pro Max",
        year=2023,
        price=1099.99,
        os_version="iOS 18.4.1",
        screen_size=6.7,
        storage=512,
        battery_capacity=4323,
        camera_mp=48
    )
    
    # Power on the iPhone
    print(iphone.power_on())
    
    # Enable connections
    print(iphone.toggle_cellular())
    print(iphone.toggle_wifi())
    
    # Install some apps
    print(iphone.install_app("Instagram"))
    print(iphone.install_app("Spotify"))
    print(iphone.install_app("Netflix"))
    
    # Make a call and send a text
    print(iphone.make_call("+254-726-013-909"))
    print(iphone.send_text("+254-726-013-909", "Hello! How are you?"))
    
    # Take a photo
    print(iphone.take_photo())
    
    # Get device information
    print(iphone.get_info())
    print(iphone.get_battery_info())
    print(iphone.get_storage_info())
    
    # Update iOS
    print(iphone.update_os("iOS 18.4.1"))
    
    # Power off
    print(iphone.power_off())