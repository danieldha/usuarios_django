from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Usuario(AbstractUser):
    pdf_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True)
    pdf_file_2 = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                  blank=True)

    class Meta:
        permissions = (
            ('add_auditoria', 'Puede consultar la auditoría del sistema'),
        )
