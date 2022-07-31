from django.contrib.auth import get_user_model

UserModel = get_user_model()

if not UserModel.objects.filter(username='admin').exists():
    user=UserModel.objects.create_user('admin2', password='123456')
    user.is_superuser=True
    user.is_staff=True
    user.save()