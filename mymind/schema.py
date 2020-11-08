import graphene
import graphql_jwt

import mymind.users.schema
import mymind.moods.schema


class Query(mymind.moods.schema.Query, mymind.users.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    mymind.moods.schema.Mutation, mymind.users.schema.Mutation, graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
