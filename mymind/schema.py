import graphene

import mymind.users.schema
import mymind.moods.schema


class Query(mymind.moods.schema.Query, mymind.users.schema.Query, graphene.ObjectType):
    pass


class Mutation(mymind.users.schema.Mutation, graphene.ObjectType,):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
