from django.shortcuts import render
from .api.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# APIView 공통적인 함수 재사용 가능, DRY 정책을 따르도록 하는 강력한 패턴 제공
from rest_framework.view import APIView
from .models import Post
from django.http import Http404
from rest_framework import status

class PostList(APIView):
    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data) 

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

    


@api_view(['GET', 'POST'])
def PostList(request):
    # 읽기 
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        # many=True ?? Post.objects.all()로 검색한 객체는 list 형태다
        # serializer은 한개의 객체만 이해할수 있고, 리스트는 이해할 수 없다.
        # 따라서 many=True를 추가해 중복 표현 값에 대한 list를 받게끔 해주는 것이다.

        return Response(serializer.data)
        # Response의 정체???
        # TemplateResponse 객체의 일종으로 렌더링되지 않은 컨텐츠를 가져오고
        # 클라이언트에게 반환할 올바른 컨텐츠 유형을 결정한다!

    # 생성
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        # request.data는??
        # DRF가 제공하는 것으로 기존의 HttpRequest를 request객체로 확장하여, 
        # 더 유연한 요청 피싱을 제공한다고 한다
        # 핵심적인 기능은 form에서 썻던 request.POST와 유사하지만 웹 API에 더 유용한 속성
        
        if serializer.is_valid():
            # POST요청 -> 유효성 검사 필수
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)
        # status= 의 정체는?? 
        # DRF가 제공하는 HTTP 상태코드다! 에러 종류에 따라 더욱 명시적인 식별자를 제공

@api_view(['GET', 'PUT', 'DELETE'])
def PostDetail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # 우선 pk에 해당하는 post가 존재하는지! 없으면 404 에러를 띄워주도록

    # Detail
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    #Update
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        # request 요청이 들어온 그 post를 serializer 틀에 담아 가져옴

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)