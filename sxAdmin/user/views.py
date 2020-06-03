from django.contrib.auth import login, authenticate, get_user_model
from django.db.models import F, Q
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from user.models import UserRoleModel

from user.models import UserModel

from menu.models import MenuModel

from role.models import RoleMenuModel
from .serializer import UserModelSerializer


class UserViewSet(viewsets.GenericViewSet):

    serializer_class = UserModelSerializer

    queryset = UserModel.objects.all()

    def get_object(self):
        return self.request.user

    @action(methods=['get'], detail=False)
    def getInfo(self, request):

        #
        user = request.user
        dept = user.dept
        user_dict = user.__dict__
        del user_dict['_state']


        dept_dict = dept.__dict__
        del dept_dict['_state']

        user_dict['common'] = dept_dict

        roles = []
        user_role = UserRoleModel.objects.filter(users=user)
        print(user_role,'aa')
        for item in user_role:

            role_dict = item.roles.__dict__
            del role_dict['_state']
            roles.append(role_dict)
            user_dict['roles'] = roles


        print('aa',roles)
        roleMenu = RoleMenuModel.objects.filter(role=user_role[0].roles)

        per = ['*:*:*']

        if  roleMenu:

            menu_id = []

            for i in roleMenu:
                try:
                    menu_id.append(i.menu.menuId)
                except:
                    continue

            menuModels = MenuModel.objects.filter(menuId__in=menu_id).exclude(perms='').values_list('perms')
            per = [i[0] for i in list(menuModels)]



        res = {
            'msg':'操作成功',
            'code':200,
            'permissions': per,
            'user':user_dict,
            'roles':[i['roleKey'] for i in roles]
        }
        return Response(res)


    @action(methods=['post'],detail=False)
    def login(self,request):

        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if not user:

            return Response({
                'code':500,
                'msg':'账号或密码错误'
            })

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        login(request, user)
        response = JsonResponse({'code': 200, 'token': token,'msg':'操作成功'})
        response.set_cookie('token', token,max_age=24*7*60*60)
        return response


    @action(methods=['get'],detail=False)
    def getCode(self,request):

        return Response({
            'a':"1",
            'code':200
        })