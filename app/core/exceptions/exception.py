class DeveloperNotFoundException(Exception):
    def __init__(self, developer_id):
        self.message = f"Developer with ID {developer_id} not found."
        super().__init__(self.message)