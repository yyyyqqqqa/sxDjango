from django.http import JsonResponse
from django.views import View

from sxAdmin.menu.models import MenuModel
from sxAdmin.menu.serializer import MenuModelSerializer




class LoginView(View):

    def post(self,request):

        return JsonResponse({
            'code':200,
            'msg':'ok'
        })


    def get(self,request):

        stus = MenuModel.objects.filter(parent_id=0)

        s = MenuModelSerializer(stus,many=True)

        for i in s.data:
            print(dir(i))
            print(dict(i))
            print(i)

            stus1 = MenuModel.objects.filter(parent_id=dict(i)['menu_id'])
            s1 = MenuModelSerializer(stus1, many=True)
            i.setdefault('children',s1.data)

        res = {
            'code':200,
            'msg':'ok',
            'data':s.data
        }

        return JsonResponse(res,safe=False)

