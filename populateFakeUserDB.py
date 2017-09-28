import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django

django.setup()

## FAKE POPULATION SCRIPTS

from level2_ex.models import Users
from faker import Faker

fakegen = Faker()

def populateFakeUserDB(N=5):
	for entry in range(N):

		fake_email = fakegen.email()
		fake_name = fakegen.name()
		fake_lastname = fakegen.name()

		Users.objects.get_or_create(name=fake_name, last_name=fake_lastname, email=fake_email)[0]



if __name__ == '__main__':
	print("Populating DB")
	populateFakeUserDB(20)
	print("Populating DB Done!")
