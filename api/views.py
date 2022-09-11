# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import VideoSerializer
from .models import Video
from yt_dlp import YoutubeDL
import json
from rest_framework.parsers import JSONParser


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "a": "bcd"
        }
    ]
    return Response(routes)


@api_view(['GET'])
def getVideos(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getVideo(request,pk):
    video = Video.objects.get(id=pk)
    serializer = VideoSerializer(video,many=False)

    return Response(serializer.data)

@api_view(['POST'])
def creteVideo(request):
    data = request.data
    #print(data)


    video = Video.objects.create(
        videourl=data
    )
    serializer = VideoSerializer(video,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def downloadvideo(request):
    # data = request.data
    # print(data)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    data = body['link']

    ydl_opts = {
        'format': 'best',
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(data, download=False)
        url = result.get("url", None)
        title = result.get('title', None)
        extension = result.get('ext', None)
        returnData ={
            "url":url,
            "title":title,
            "ext": extension
        }
    return Response(returnData)