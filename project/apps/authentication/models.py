from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from apps.common.models import(
    BaseModel
)


#======================================================================
# Custom User
#======================================================================
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email: 
            raise ValueError(
                "Email is required!"
            )
        normalized_email = self.normalize_email(email=email)
        
        user = self.model(
            email=normalized_email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, email, password=None, username=None, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields["is_staff"] is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields["is_superuser"] is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        
        return self.create_user(email=email,username=username,password=password,**extra_fields)
    
    

class User(AbstractUser):
    class RolesChoices(models.TextChoices):
        GUEST = "guest", "Guest"
        USER = "user", "User"
        MANAGER = "manager", "Manager"
        ADMIN = "admin", "Admin"
    
    email = models.EmailField(
        "Email Address",
        max_length=200,
        unique=True,
    )    
    username = models.CharField(
        max_length=150, 
        unique=True,
        blank=True,
        null=True,
        error_messages={
            "unique":"User already exists!"
        }
    )
    middle_name = models.CharField(
        max_length=100
    )
    role = models.CharField(
        choices=RolesChoices.choices,
        max_length=20,
        default=RolesChoices.GUEST
    )
    is_verified = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.username} ----- {self.role}"
    
    

#======================================================================
# Business Element
#======================================================================

class BusinessElement(BaseModel):
    
    title = models.CharField(
        max_length=100
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Business Element"
        verbose_name_plural = "Business Elements"
    


#======================================================================
# Access Rules
#======================================================================

class AccessRules(BaseModel):
    
    role = models.CharField(
        choices=User.RolesChoices.choices,
        max_length=20
    )
    element = models.ForeignKey(
        BusinessElement,
        related_name="accessrules", 
        on_delete=models.CASCADE
    )
    can_read = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.role 
    
    