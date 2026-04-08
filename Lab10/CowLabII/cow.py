class Cow:
    def __init__(self, _name):
        self.name = _name
        self.image = None
        
    def get_name(self):
        return self.name
    
    def get_image(self):
        return self.image
        
    def set_image(self, _image):
        self.image = _image