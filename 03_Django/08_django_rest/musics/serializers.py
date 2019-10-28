from rest_framework import serializers
from .models import Music, Artist, Comment

class Musicserializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id', )

class Artistserializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', )

class ArtistDetailSerializer(Artistserializer):
    musics = Musicserializer(source='music_set', many=True)
    musics_count = serializers.IntegerField(source='music_set.count')

    class Meta(Artistserializer.Meta):
        fields = Artistserializer.Meta.fields + ('musics_count', 'musics', )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id', )

# ArtistDetailSerializer와 로직이 똑같똑같
class MusicDetailSerializer(Musicserializer):
    comments = CommentSerializer(source='comment_set', many=True)

    class Meta(Musicserializer.Meta):
        fields = Musicserializer.Meta.fields + ('comments', )