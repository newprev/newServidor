from enum import Enum


class NewValidationError(Enum):
    emailInvalido = 'email'
    telefoneInvalido = 'telefone'