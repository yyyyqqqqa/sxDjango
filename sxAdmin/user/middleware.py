from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class AuthMiddleware(MiddlewareMixin):
    first = False

    '''
    登录验证
    '''
    def process_request(self, request):

        aa = request.COOKIES.get('token')

        if '/system/user/login/' == request.path:
            self.first = True
            return None

        elif '/common/download/' == request.path:

            return None

        elif '/system/user/getCode/' == request.path:



            if  not self.first:
                return None
            elif self.first and not aa:
                response = JsonResponse({'code': 401})
                response.status_code = 200
                return response

        else:

            user_jwt = JSONWebTokenAuthentication().authenticate(Request(request))

            if user_jwt is not None:
                user = user_jwt[0]
                request.user = user
                return None

            response = JsonResponse({'detail': 'Permission denied'})
            response.status_code = 403
            return response



