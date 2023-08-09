import iodxf, ezdxf

class Upg:
    def __init__(self) -> None:       
        self.entities = []
        self.entities_celected = []
        
    def load_entities(self, path):
        self.entities = iodxf.inputDxf(path)