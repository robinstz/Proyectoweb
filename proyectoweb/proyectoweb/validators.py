# mi_app/validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class RequisitosPersonalizadosValidator:
    def __init__(self, min_length=8, require_uppercase=True, require_digit=True, require_symbol=True):
        self.min_length = min_length
        self.require_uppercase = require_uppercase
        self.require_digit = require_digit
        self.require_symbol = require_symbol

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("La contraseña debe tener al menos %(min_length)d caracteres."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

        if self.require_uppercase and not any(char.isupper() for char in password):
            raise ValidationError(
                _("La contraseña debe contener al menos una letra mayúscula."),
                code='password_no_uppercase',
            )

        if self.require_digit and not any(char.isdigit() for char in password):
            raise ValidationError(
                _("La contraseña debe contener al menos un dígito."),
                code='password_no_digit',
            )

        if self.require_symbol and not any(char.isalnum() for char in password):
            raise ValidationError(
                _("La contraseña debe contener al menos un símbolo."),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "La contraseña debe tener al menos %(min_length)d caracteres y cumplir con los siguientes requisitos: "
            "una letra mayúscula, un dígito y un símbolo."
        ) % {'min_length': self.min_length}
