class Patron:
    def __init__(self, name: str, membership_id: str):
        self.name = name
        self.membership_id = membership_id

    def __str__(self):
        return f'Patron: {self.name}, Membership ID: {self.membership_id}'