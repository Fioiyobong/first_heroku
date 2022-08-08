from flask import Blueprint, jsonify


api = Blueprint("api",__name__)

data = [
    {
        "id" : 1,
        "name" : "stone"

    },
    {
        "id" : 2,
        "name" : "fish"
    },
    {
        "id" : 3,
        "name" : "vegetables"
    },
    {
        "id" : 4,
        "name" : "beans"
    },
    {
        "id" : 5,
        "name" : "air-purifier"
    }
]


@api.route("/blogs/")
def blog_list():
    return jsonify([
        {
            "name":"anies",
            "position":20
        },

        {
            "name":"fioiyobong",
            "age":2
        },
        {
            "school":"aptech",
            "address":"worldwide"
        },
        {
            "gender":"female",
            "blood-type":"AB+"
        }
    ])


@api.get("/blogs/<int:id>")
def blog_retrieve(id):
    # fun function that filter a list of dictionary
    return "blog with id "+str(id)