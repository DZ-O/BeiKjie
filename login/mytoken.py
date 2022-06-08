from rest_framework.exceptions import AuthenticationFailed


from login import models
from login.models import UserDetail
from rest_framework.authentication import  BaseAuthentication
from rest_framework_jwt.utils import jwt_decode_handler
import jwt
class EmailAuthBackend(BaseAuthentication):
    def authenticate(self, request):
        jwt_value = request.META.get("HTTP_AUTHORIZATION")
        if jwt_value:
            payload = jwt_decode_handler(jwt_value)
            try:
                payload = jwt_decode_handler(jwt_value)
            except jwt.ExpiredSignature:
                raise AuthenticationFailed('签名过期')
            except jwt.InvalidTokenError:
                raise AuthenticationFailed('用户非法')
            except Exception as e:
                raise AuthenticationFailed(str(e))
            user = models.UserDetail(id=payload.get('id'),phone=payload.get('phone'))
            return user,jwt_value
        raise AuthenticationFailed('您没有携带认证信息')

