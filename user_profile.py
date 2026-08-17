class UserProfile:
    def __init__(self):
        self.data = {}

    def get(self, user_id):
        return self.data.get(user_id, {})
