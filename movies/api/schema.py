import graphene

from graphene_django import DjangoObjectType, DjangoListField 
from .models import Movie 


class MovieType(DjangoObjectType): 
    class Meta:
        model = Movie
        fields = "__all__"


class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movie = graphene.Field(MovieType, movie_id=graphene.Int())

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_movie(self, info, movie_id):
        return Movie.objects.get(pk=movie_id)



class MovieInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    likes = graphene.Int()
    reason = graphene.String()



class CreateMovie(graphene.Mutation):
    class Arguments:
        movie_data = MovieInput(required=True)

    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, movie_data=None):
        movie_instance = Movie( 
            title=movie_data.title,
            likes=movie_data.likes,
            reason=movie_data.reason,
        )
        movie_instance.save()
        return CreateMovie(movie=movie_instance)



class UpdateMovie(graphene.Mutation):
    class Arguments:
        movie_data = MovieInput(required=True)

    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, movie_data=None):

        movie_instance = Movie.objects.get(pk=movie_data.id)

        if movie_instance:
            movie_instance.title = movie_data.title
            movie_instance.likes = movie_data.likes
            movie_instance.reason = movie_data.reason
            movie_instance.save()

            return UpdateMovie(movie=movie_instance)
        return UpdateMovie(movie=None)


class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, id):
        movie_instance = Movie.objects.get(pk=id)
        movie_instance.delete()

        return None

class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
