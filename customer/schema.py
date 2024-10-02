import graphene
from graphene_django import DjangoObjectType
from .models import client

class ClientType(DjangoObjectType):
    class Meta:
        model = client
        fields = ('id', 'first_name', 'last_name', 'city')


class Query(graphene.ObjectType):
    all_clients = graphene.List(ClientType)
    def resolve_all_clients(self, info, **kwargs):
        return client.objects.all()

schema = graphene.Schema(query=Query)