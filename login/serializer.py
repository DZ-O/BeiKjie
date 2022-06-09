from django.contrib.auth.hashers import check_password
from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, validators

from login import models
from login.models import UserDetail
from rest_framework_jwt.utils import jwt_encode_handler
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib import auth


# 用户信息序列化器
class UserDetailSerializer(ModelSerializer):
    username = serializers.CharField(max_length=8, min_length=1, validators=[
        validators.UniqueValidator(queryset=UserDetail.objects.all(), message="用户昵称必须唯一"),
        RegexValidator("^[\u4e00-\u9fa5_a-zA-Z0-9]+$", message='昵称不能含有特殊字符')],
                                     error_messages={
                                         'max_length': '昵称最多8位',
                                         'min_length': '昵称至少1位',
                                         'blank': '不能为空',
                                     })
    password = serializers.CharField(write_only=True, max_length=18, min_length=6, error_messages={
        'max_length': '密码最多18位',
        'min_length': '密码至少6位',
        'blank': '不能为空'
    }, validators=[
        RegexValidator("^(?=.*?[a-z])(?=.*?[0-9])([^\\u4E00-\\u9FFF]){6,18}$", message='密码有字母数字组成')], )
    email = serializers.EmailField(write_only=True, validators=[
        RegexValidator("^[a-zA-Z0-9][a-zA-Z0-9_\\-\\.]{0,19}@(?:[a-zA-Z0-9\\-]+\\.)+[a-zA-Z]+$",
                       message='邮箱格式错误')], error_messages={
        'blank': '不能为空'
    })

    signature = serializers.CharField(max_length=50, required=True, allow_blank=True, error_messages={
        'max_length': '个性签名最多50字',
    })
    phone = serializers.IntegerField(write_only=True, validators=[
        RegexValidator("^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$",
                       message='手机格式错误')], error_messages={
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
        fields = ['username', 'password', 'email', 'signature', 'identity', 'subscribe_count', 'collect_count',
                  'fans_count', 'been_read_count', 'SignIn', 'phone']


# 手机注册登录序列化器
class JWT_User(ModelSerializer):
    # id = serializers.IntegerField(write_only=True,required=True)
    username = serializers.CharField(required=True)
    phone = serializers.IntegerField(validators=[
        RegexValidator("^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$",
                       message='手机格式错误')], error_messages={
        'blank': '不能为空'
    })
    icon = serializers.ImageField(read_only=True)
    sms_code = serializers.CharField(label='验证码', write_only=True)

    class Meta:
        model = UserDetail
        fields = ['id', 'username', 'phone', 'sms_code','icon']

    def validate(self, attrs):
        attrs.pop('sms_code')
        return attrs


# 邮箱登录序列化器
class EmailLoginSer(ModelSerializer):
    username = serializers.CharField(read_only=True, max_length=8, min_length=1, validators=[
        validators.UniqueValidator(queryset=UserDetail.objects.all(), message="用户昵称必须唯一"),
        RegexValidator("^[\u4e00-\u9fa5_a-zA-Z0-9]+$", message='昵称不能含有特殊字符')],
                                     error_messages={
                                         'max_length': '昵称最多8位',
                                         'min_length': '昵称至少1位',
                                         'blank': '不能为空',
                                     })
    email = serializers.EmailField(validators=[
        RegexValidator("^[a-zA-Z0-9][a-zA-Z0-9_\\-\\.]{0,19}@(?:[a-zA-Z0-9\\-]+\\.)+[a-zA-Z]+$",
                       message='邮箱格式错误')], error_messages={
        'blank': '不能为空'
    })
    password = serializers.CharField(write_only=True, max_length=18, min_length=6, error_messages={
        'max_length': '密码最多18位',
        'min_length': '密码至少6位',
        'blank': '不能为空'
    }, validators=[
        RegexValidator("^(?=.*?[a-z])(?=.*?[0-9])([^\\u4E00-\\u9FFF]){6,18}$", message='密码有字母数字组成')], )

    class Meta:
        model = UserDetail
        fields = ['id', 'username', 'email', 'password','icon']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = models.UserDetail.objects.filter(email=email).first()

        if user:
            if check_password(password, user.password):
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                self.context['token'] = token
                self.context['username'] = user.username
                self.context['email'] = user.email
                self.context['icon'] = user.icon
                print(user.email)
                print(user.username)
                print('a')
                return attrs
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')


# 头像序列化器
class UserIconSer(ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['icon']