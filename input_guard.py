class InputGuard:
    def validate(self, text):
        return bool(text and text.strip())
