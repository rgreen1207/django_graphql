Steps for setup:
1. create local env `python -m venv env`
2. `source env/bin/activate activate`
3. `pip install django graphene-django`
4. `cd /movies`
5. `python manage.py runserver`
6. navigate to /movies in browser window
---
---
---
All graphql queries and mutations are working via `/graphql`:
---
Example query for all movies:

    query{
        allMovies{
            id
            title
            reason
            likes
        }
    }
---
Example query for specific movie:
    
    query{
        movie(movieId:1){
            id
            title
            reason
            likes
        }
    }
---
Example mutation for creating movie:

    mutation{
        createMovie(title:"Training Day", likes:"24", reason:"24 hours in a day"){
            movie{
                id
                title
                reason
                likes
            }
        }
    }
---
Example mutation for updating a movie:

    mutation{
        updateMovie(movieData:{id:8, title:"Training Day", likes:8, reason:"Baseball Steak is 8oz"}){
            movie{
                id
                title
                likes
                reason
            }
        }
    }
---
Example mutation for deleting movie:
    
    mutation{
        deleteMovie(id:8){
            movie{
                id
            }
        }
    }
---
In all queries above, the `reason` field is to explain why I chose that specific number for the default amount of likes. Consider it an "easter egg". When manually creating/updating a movie, the field is required, but can be removed in the schema.