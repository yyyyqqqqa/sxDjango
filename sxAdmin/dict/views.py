import os
import time,pandas as pd

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dict.models import DictDataModel

from dict.serializer import DictDataModelSerializer

from dict.models import DictTypeModel
from dict.serializer import DictTypeModelSerializer

from datetime import datetime

from sx import settings


class DictTypeViewSet(viewsets.GenericViewSet):



    def getList(self,request):

        pageNum = int(request.query_params.get('pageNum',1))
        pageSize = int(request.query_params.get('pageSize',10))

        data = DictTypeModel.objects.all()

        dictName = request.query_params.get('dictName')
        if dictName:
            data = data.filter(dictName__contains=dictName)

        dictType = request.query_params.get('dictType')
        if dictType:
            data = data.filter(dictType__contains=dictType)

        status = request.query_params.get('status')

        if status:
            data = data.filter(status=status)

        beginTime = request.query_params.get('beginTime')
        endTime = request.query_params.get('endTime')

        if beginTime:
            beginTime = datetime.strptime(beginTime, '%Y-%m-%d').date()
            endTime = datetime.strptime(endTime, '%Y-%m-%d').date()

            data = data.filter(createTime__gt=beginTime).filter(createTime__gt=endTime)

        c = len(data)
        data = data[(pageNum - 1) * pageSize:pageNum * pageSize]

        data = DictTypeModelSerializer(data, many=True).data

        return data,c




    @action(methods=['get'],detail=True)
    def dictType(self,request,pk):

        datas = DictDataModel.objects.filter(dictType=pk)

        data = DictDataModelSerializer(datas,many=True).data

        return Response({
            'code':200,
            'msg':'操作成功',
            'data':data
        })


    @action(methods=['get'],detail=False)
    def typeList(self,request):

        data,c= self.getList(request)
        return Response({
            'code':200,
            'msg':'操作成功',
            'rows':data,
            'total':c
        })





    @action(methods=['get'],detail=True)
    def getType(self,request,pk):

        data = DictTypeModel.objects.get(dictId=pk)

        data = DictTypeModelSerializer([data],many=True).data

        return Response({
            'code':200,
            'msg':'操作成功',
            'data':data[0]
        })

    @action(methods=['PUT','post'],detail=False)
    def type(self,request):


        if request.method == 'POST':
            data = dict(request.data)

            data['createBy'] = request.user.username
            DictTypeModel.objects.create(**data)

            return Response({
                'code': 200,
                'msg': '操作成功'
            })
        else:

            data = request.data

            del data['createBy']
            del data['createTime']
            data['updateTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data['updateBy'] = request.user.username

            DictTypeModel.objects.filter(dictId=data['dictId']).update(**data)
            return Response({
                'code':200,
                'msg':'操作成功'
            })


    @action(methods=['delete'],detail=True)
    def deleteType(self,request,pk):

        # 多个的删除
        if ',' in pk:

            pks = pk.split(',')

            for pk in pks:
                dict = DictTypeModel.objects.get(dictId=pk)
                dict.delete()

        else:

            #单个删除
            dict = DictTypeModel.objects.get(dictId=pk)
            dict.delete()



        return Response({
            'code':200,
            'msg':'操作成功'
        })

    @action(methods=['get'],detail=False)
    def typeExport(self,request):


        data = self.getList(request)[0]


        out = ['dictId','dictName','dictType','status']

        datas = [{i: d[i] for i in d.keys() if i in out} for d in data]

        df = pd.DataFrame(datas)
        df.columns = ['字典主键','字典名称','字典类型','状态']


        file_name = str(time.time()).replace('.',"") +'字典类型'


        df.to_excel(os.path.join(settings.MEDIA_FILE ,file_name+'.xlsx'),index=False)
        return Response({
            'code':200,
            'msg':file_name+'.xlsx'
        })



class DictDataViewSet(viewsets.GenericViewSet):


    def getList(self,request):

        infos = request.query_params

        pageNum = int(infos.get('pageNum', 1))
        pageSize = int(infos.get('pageSize', 10))
        dictType = infos.get('dictType')

        dictDatas = DictDataModel.objects.filter(dictType=dictType)

        status = infos.get('status')
        dictLabel = infos.get('dictLabel')

        if status:
            dictDatas = dictDatas.filter(status=status)
        if dictLabel:
            dictDatas = dictDatas.filter(dictLabel__contains=dictLabel)

        c = len(dictDatas)

        dictDatas = dictDatas[(pageNum - 1) * pageSize:pageNum * pageSize]

        datas = DictDataModelSerializer(dictDatas, many=True).data

        return datas,c




    @action(methods=['get'],detail=False)
    def dataList(self,request):

        datas, c = self.getList(request)

        return Response({
            'code':200,
            'rows':datas,
            'total':c
        })


    @action(methods=['post'],detail=False)
    def addData(self,request):


        info = request.data
        info['createBy'] = request.user.username

        DictDataModel.objects.create(**info)

        return Response({
            'code':200,
            'msg':'操作成功'
        })

    @action(methods=['delete'],detail=True)
    def delData(self,request,pk):

        if ',' in pk:

            for i in pk.split(','):
                dictData = DictDataModel.objects.get(dictCode=i)

                dictData.delete()

        else:

            dictData = DictDataModel.objects.get(dictCode=pk)

            dictData.delete()

        return Response({
            'code':200,
            'msg':'操作成功'
        })


    @action(methods=['put'],detail=False)
    def eidtData(self,request):


        infos = request.data
        infos['updateBy'] = request.user.username
        infos['updateTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        DictDataModel.objects.filter(dictCode=infos['dictCode']).update(**infos)

        return Response({
            'code':200,
            'msg':'操作成功'
        })

    @action(methods=['get'],detail=True)
    def getData(self,request,pk):

        datas = DictDataModel.objects.get(dictCode=pk)
        data = DictDataModelSerializer([datas],many=True).data
        return Response({
            'code':200,
            'msg':'操作成功',
            'data':data[0]
        })


    @action(methods=['get'],detail=False)
    def dataExport(self,request):


        data = self.getList(request)[0]

        out = ['dictCode','dictSort','dictLabel','dictValue','dictType','isDefault','status']

        datas = [{i: d[i] for i in d.keys() if i in out} for d in data]

        df = pd.DataFrame(datas)
        df.columns = ['字典编码','字典排序','字典标签','字典键值','字典类型','是否默认','状态']

        file_name = str(time.time()).replace('.',"") +'字典数据'

        df.to_excel(os.path.join(settings.MEDIA_FILE ,file_name+'.xlsx'),index=False)
        return Response({
            'code':200,
            'msg':file_name+'.xlsx'
        })

