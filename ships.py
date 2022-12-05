class Ships:
    def __init__(self, ship_id,name, type,active):
        self.ship_id = ship_id
        self.name = name
        self.type = type
        self.active = active

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()