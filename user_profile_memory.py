class UserProfileMemory:
    def __init__(self):
        self.profiles = {}

    def get(self, user_id):
        return self.profiles.get(user_id, {})
