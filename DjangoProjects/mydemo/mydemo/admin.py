from django.contrib import admin
from mydemo.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # fields=["username", "name", "email"]
    list_display=["username", "name", "email", "address"]
    save_as=True
    fieldsets = (
        ("Name", {
            'fields': ["username","name"],
        }),
        ("Details", {
            'fields':["email"],
        })
    )
    