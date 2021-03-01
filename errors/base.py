class BaseError(Exception):
    expected_value = None
    message = f"error basico"
    def __init__(self,token,*args,**kwargs):
        super().__init__(self.message)
    def __str__(self):
        return self.message

