from db_layer import DBLayer

class AssignmentsService:
    def __init__(self):
        self.database = DBLayer()

    def get_assignment_by_id(self, id):
        return self.database.fetch_assignment(id)

    def add_assignment(self, data):
        return self.database.create_assignment(data)
    
    def search_assignments(self, tag):
        return self.database.fetch_assignments_by_tag(tag)
    