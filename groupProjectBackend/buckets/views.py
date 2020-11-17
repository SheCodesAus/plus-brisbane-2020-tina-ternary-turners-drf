from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from .models import Bucket, Pipe
from .serializers import BucketSerializer, PipeSerializer,BucketDetailSerializer,PipeDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

class BucketList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        buckets = Bucket.objects.all()
        serializer = BucketSerializer(buckets, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BucketSerializer(data=request.data)
        # return Response(serializer.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
            )
        return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

class BucketDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            bucket = Bucket.objects.get(pk=pk)
            self.check_object_permissions(self.request, bucket)
            return bucket

        except Bucket.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bucket = self.get_object(pk)
        serializer = BucketDetailSerializer(bucket)
        return Response(serializer.data)

    def put(self, request, pk):
        # it is for update 
        bucket = self.get_object(pk)
        data = request.data
        serializer = BucketDetailSerializer(instance=bucket, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        bucket = self.get_object(pk)
        data = request.data
        bucket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PipeList(APIView):
    def get(self, request):
        pipes = Pipe.objects.all()
        serializer = PipeSerializer(pipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
            )
        return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

class PipeDetailList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsSupporterOrReadOnly]

    def get_object(self, pk):
        try:
            pipe = Pipe.objects.get(pk=pk)
            self.check_object_permissions(self.request, pipe)
            return pipe

        except Bucket.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pipe = self.get_object(pk)
        serializer = PipeDetailSerializer(pipe)
        return Response(serializer.data)

    def put(self, request, pk):
        # it is for update 
        pipe = self.get_object(pk)
        data = request.data
        serializer = PipeDetailSerializer(instance=pipe, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

