import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from mymind.moods.models import Mood

# Create a GraphQL type for the movie model


class MoodType(DjangoObjectType):
    class Meta:
        model = Mood


class CreateMood(graphene.Mutation):
    id = graphene.Int()
    description = graphene.String()
    mood = graphene.Int()

    class Arguments:
        mood = graphene.Int(required=True)
        description = graphene.String(required=True)

    def mutate(self, info, mood, description):
        mood = Mood(
            mood=mood,
            description=description,
        )
        mood.save()

        return CreateMood(
            id=mood.id,
            mood=mood.mood,
            description=mood.description,
        )


class Query(ObjectType):
    mood = graphene.Field(MoodType, id=graphene.Int())
    moods = graphene.List(MoodType)

    def resolve_mood(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Mood.objects.get(pk=id)

        return None

    def resolve_moods(self, info, **kwargs):
        return Mood.objects.all()


class Mutation(graphene.ObjectType):
    create_mood = CreateMood.Field()
