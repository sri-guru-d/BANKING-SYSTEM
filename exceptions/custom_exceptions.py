class InsufficientBalanceException(Exception):

    def __init__(self, message="Insufficient balance"):
        self.message = message
        super().__init__(self.message)


class InvalidAccountTypeException(Exception):

    def __init__(self, message="Invalid account type"):
        self.message = message
        super().__init__(self.message)
