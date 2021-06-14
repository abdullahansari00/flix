# import graphene
# from graphql_auth.schema import UserQuery, MeQuery
# from users.schema import AuthMutation
# from geek.schema import Query as GeekQuery

# class Query(GeekQuery, UserQuery, MeQuery, graphene.ObjectType):
# 	pass

# class Mutation(AuthMutation, graphene.ObjectType):
# 	pass

# schema = graphene.Schema(query=Query, mutation=Mutation)