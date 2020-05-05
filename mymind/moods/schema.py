import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from mymind.moods.models import Mood

# Create a GraphQL type for the movie model


class MoodType(DjangoObjectType):
    class Meta:
        model = Mood


class Query(ObjectType):
    mood = graphene.Field(MoodType, id=graphene.Int())
    moods = graphene.List(MoodType)

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Mood.objects.get(pk=id)

        return None

    def resolve_movies(self, info, **kwargs):
        return Mood.objects.all()
