from django.db.models import Count

from login.models import UserDetail
def radomName():
    num = UserDetail.objects.aggregate(num=Count('pk'))
    print(num)
    return 'BeiKJie-'+str(num['num'])