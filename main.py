import django_setup
from lesson.models import User




user1 = User.objects.create(name="Андрій", email="ostapenko.andrii@gmail.com", role="admin")
user2 = User.objects.create(name="Кирило", email="grashanov.kirilo@gmail.com", role="user")
user3 = User.objects.create(name="Вова", email="lebedenko.vova@gmail.com", role="user")

print(User.objects.all())

user2.role = "admin"
user2.save()


print(User.objects.get(id=2))
