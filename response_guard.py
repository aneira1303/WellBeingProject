class ResponseGuard:
    def validate(self, response):
        return response.strip()
