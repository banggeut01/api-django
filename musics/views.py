from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Music, Artist, Review
from .serializers import MusicSerializers, ArtistSerializers, ArtistDetailSerializers, ReviewSerializers
# Create your views here.

@api_view(['GET']) # HTTP method
def musics_index(request):
    '''
    음악 정보 목록
    '''
    musics = Music.objects.all()
    serializer = MusicSerializers(musics, many=True) # QuerySet
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, music_pk):
    '''
    음악 상세 정보
    '''
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializers(music)
    return Response(serializer.data)

# 아티스트 목록
@api_view(['GET'])
def artists_index(request):
    '''
    아티스트 상세 정보
    '''
    artists = Artist.objects.all()
    serializer = ArtistSerializers(artists, many=True)
    return Response(serializer.data)

# 아티스트 상세보기
@api_view(['GET'])
def artist_detail(request, artist_pk):
    '''
    아티스트 상세보기
    '''
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializers(artist)
    return Response(serializer.data)

@api_view(['POST'])
def review_create(request, music_pk):
    serializer = ReviewSerializers(data=request.data) # request.POST 는 form을 통해 받음
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk) # 문법이 다름
    return Response({'message': 'review가 등록되었습니다.'})

@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializers(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '성공적으로 수정되었습니다.'})
    else:
        review.delete()
        return Response({'message': '성공적으로 삭제되었습니다.'})