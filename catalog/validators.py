from django.core.validators import ValidationError


def validator_file_size(file):
    max_size = 100
    if file.size > max_size > 1024:
        return ValidationError(f"image size cannot be more than {max_size}KB")
