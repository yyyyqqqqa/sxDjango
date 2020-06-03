from rest_framework import viewsets
from rest_framework.decorators import action

from menu.models import MenuModel
from rest_framework.response import Response


class MenuViewSet(viewsets.GenericViewSet):


    @action(methods=['get'],detail=False)
    def getRouters(self,request):

        infos = MenuModel.objects.filter(parentId=0)
        data = []
        for item in infos:
            new_item = item.__dict__
            del new_item['_state']

            sub_infos = MenuModel.objects.filter(parentId=new_item['menuId'])
            pmenu = {
                'meta': {
                    'title': new_item['menuName'],
                    'icon': new_item['icon']
                },
                'path': new_item['path'],
                'component': 'Layout',
                # 'redirect':'noRedirect',
                'hidden': False
            }

            childrens = []
            for sub in sub_infos:
                new_sub = sub.__dict__
                del new_sub['_state']

                sub_item = {
                    'meta': {
                        'title': new_sub['menuName'],
                        'icon': new_sub['icon']
                    },
                    'component': new_sub['component'],
                    'hidden': False,
                    'path': new_sub['path'],
                    'name': new_sub['path'].capitalize()
                }
                childrens.append(sub_item)

            if sub_infos:
                pmenu['children'] = childrens
                pmenu['alwaysShow'] = True
                pmenu['redirect'] = 'noRedirect'

            data.append(pmenu)

        res = {
            'msg': '操作成功',
            'code': 200,
            'data': data
        }

        return Response(res)

