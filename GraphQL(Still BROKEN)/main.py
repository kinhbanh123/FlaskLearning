from flask import Flask
from graphene import ObjectType, String, Int, Field, List, Schema
from graphene.types import ResolveInfo
from flask_graphql import GraphQLView

app = Flask(__name__)

class Author(ObjectType):
    name = String()
    birth_year = Int()

class Book(ObjectType):
    title = String()
    year = Int()
    author = Field(Author)

class Query(ObjectType):
    books = List(Book)

    def resolve_books(root, info: ResolveInfo):
        return [
            Book(title="Book 1", year=2020, author=Author(name="Author 1", birth_year=1990)),
            Book(title="Book 2", year=2022, author=Author(name="Author 2", birth_year=1985))
        ]

schema = Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)