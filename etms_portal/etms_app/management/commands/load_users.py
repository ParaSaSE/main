import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Load users from data.json into the database'

    def handle(self, *args, **kwargs):
        # Load the JSON file
        with open('etms_app/static/data.json', 'r') as file:
            data = json.load(file)

            # Ensure the "users" key exists in the JSON
            if 'users' not in data:
                self.stdout.write(self.style.ERROR('No "users" key found in data.json'))
                return

            # Iterate over the users and add them to the database
            for user_data in data['users']:
                username = user_data['username']
                password = user_data['password']
                role = user_data.get('role', 'user')  # Default role is "user"

                # Check if the user already exists
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(
                        username=username,
                        password=password
                    )
                    # Assign staff or superuser roles based on the "role" field
                    if role == 'admin':
                        user.is_staff = True
                        user.is_superuser = True
                    user.save()

            self.stdout.write(self.style.SUCCESS('Users loaded successfully!'))