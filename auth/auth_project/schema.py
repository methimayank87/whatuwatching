import graphene
from graphene_django import DjangoObjectType

from auth_app.models import UserProfile, Shows

class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = ("id", "username", "email", "age")

class ShowsType(DjangoObjectType):
    class Meta:
        model = Shows
        fields = ("id", "title", "platform", "genre", "rating", "episode")

class Query(graphene.ObjectType):
    all_users = graphene.List(UserProfileType)
    shows_by_platform = graphene.Field(ShowsType, platform=graphene.String(required=True))
    shows_by_title = graphene.Field(ShowsType, title=graphene.String(required=True))
    def resolve_all_users(root, info):
        # We can easily optimize query count in the resolve method
        return UserProfile.objects.all()

    def resolve_shows_by_title(root, info, title):
        try:
            return Shows.objects.get(title=title)
        except Shows.DoesNotExist:
            return None

    def resolve_shows_by_platform(root, info, platform):
        try:
            return Shows.objects.get(platform=platform)
        except Shows.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)