import re
from django.core.exceptions import ValidationError

class PasswordValidation:
    def validate(self,password,user=None):
        error = []
        if not re.search(r'\d',password):
            error.append('Password must contain at least one number.')
        if not re.search(r'[A-Z]',password):
            error.append('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]',password):
            error.append('Password must contain at least one lowercase letter')
        if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
            error.append("Password must contain at least one special character [!@#$%^&*(),.?\":|<>].")
        if error:
            raise ValidationError(error)
    
    def get_help_text(self):
        return('''The password must contain at least 8 characters,
                including uppercase letters,lowercase letters,
                symbols,and numbers
                ''')