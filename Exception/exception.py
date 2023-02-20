class AuthorNotFound(Exception):
    def __init__(self, message="Author not found"):
        super().__init__(message)
        self.message = message


class AuthorExisted(Exception):
    def __init__(self, message="Author exist"):
        super().__init__(message)
        self.message = message


class BookNotFound(Exception):
    def __init__(self, message="Book not found"):
        super().__init__(message)
        self.message = message


class NoBooks(Exception):
    def __init__(self, message=" Empty"):
        super().__init__(message)
        self.message = message
