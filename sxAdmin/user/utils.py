from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from rest_framework.response import Response


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    :token  返回的jwt
    :user   当前登录的用户信息[对象]
    :request 当前本次客户端提交过来的数据
    """

    return {
        'token': token,
        'msg':'ok',
        'code':200
    }

