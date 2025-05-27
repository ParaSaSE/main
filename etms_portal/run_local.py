import os
import subprocess

# Set environment variables (if needed)
os.environ['DJANGO_SETTINGS_MODULE'] = 'etms_portal.settings'
os.environ['DEBUG'] = 'True'

# Run the Django development server
try:
    subprocess.run(['python', 'manage.py', 'runserver'], check=True)
except KeyboardInterrupt:
    print("\nServer stopped.")