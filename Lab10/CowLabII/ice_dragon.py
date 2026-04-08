from cow import Cow


class IceDragon(Cow):
    def __init__(self, _name, _image):
        super().__init__(_name)
        super().set_image(_image)

    def can_breath_fire(self):
        return False
