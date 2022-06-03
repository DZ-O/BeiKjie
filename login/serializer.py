from django.core.validators import RegexValidator
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, validators
from login.models import UserDetail


class UserDetailSerializer(ModelSerializer):
    username = serializers.CharField(max_length=8, min_length=1, validators=[
        validators.UniqueValidator(queryset=UserDetail.objects.all(), message="用户昵称必须唯一"),
        RegexValidator("^[\u4e00-\u9fa5_a-zA-Z0-9]+$", message='昵称不能含有特殊字符')],
                                     error_messages={
                                         'max_length': '昵称最多8位',
                                         'min_length': '昵称至少1位',
                                         'blank':'不能为空',
                                     })
    password = serializers.CharField(write_only=True, max_length=18, min_length=6, error_messages={
        'max_length': '密码最多18位',
        'min_length': '密码至少6位',
        'blank': '不能为空'
    }, validators=[
       RegexValidator("^(?=.*?[a-z])(?=.*?[0-9])([^\\u4E00-\\u9FFF]){6,18}$", message='密码有字母数字组成')], )
    email = serializers.EmailField(validators=[
        RegexValidator("^[a-zA-Z0-9][a-zA-Z0-9_\\-\\.]{0,19}@(?:[a-zA-Z0-9\\-]+\\.)+[a-zA-Z]+$",
                                  message='邮箱格式错误')],error_messages={
                                         'blank':'不能为空'
                                     })

    signature = serializers.CharField(max_length=50, error_messages={
        'max_length': '个性签名最多50字',
        'blank': '不能为空'
    })
    identity = serializers.CharField(read_only=True)
    subscribe_count = serializers.IntegerField(read_only=True)
    collect_count = serializers.IntegerField(read_only=True)
    fans_count = serializers.IntegerField(read_only=True)
    subscribe_count = serializers.IntegerField(read_only=True)
    been_read_count = serializers.IntegerField(read_only=True)
    SignIn = serializers.IntegerField(read_only=True)



    class Meta:
        model = UserDetail
        fields = ['username','password',  'email', 'signature', 'identity', 'subscribe_count', 'collect_count',
                  'fans_count', 'been_read_count', 'SignIn']
