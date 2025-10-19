import django_setup
from lesson.models import User , Task 




user1 = User.objects.create(name="Андрій", email="ostapenko.andrii@gmail.com", role="admin")
user2 = User.objects.create(name="Кирило", email="grashanov.kirilo@gmail.com", role="user")
user3 = User.objects.create(name="Вова", email="lebedenko.vova@gmail.com", role="user")

print(User.objects.all())

user2.role = "admin"
user2.save()


print(User.objects.get(id=2).role)

task1 = Task.objects.create(
title="Зробити систему jackів",
description="Зробити систему управління jackами",
assigned_to=User.objects.get(id=2),
)
task2 = Task.objects.create(
title="Створити Django моделі для системи блогу та коментарів",
description="Створіть екземпляри постів та коментарів та забезпечте взаємодію, наприклад,
додавання коментарів до посту чи редагування посту.");
assigned_to=User.objects.get(id=3),
)
print(Task.objects.all())

task1.status = "completed"
task1.save()
print(task1)

task2.assigned_to = User.objects.get(id=1)
task2.save()
print(task2, task2.assigned_to)