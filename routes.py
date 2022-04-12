
from flask_restful import Resource
from repository import Repository
from flask import request

repository = Repository()


class BookList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        return [book.__dict__ for book
         in self.repo.books_get_all()]
    
    def post(self, req=request): 
       data = req.get_json()
       return self.repo.book_add(data).__dict__


class Book(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self, book_id):
        return self.repo.book_get_by_id(int(book_id)).__dict__

class ReviewList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
    
    def get(self, book_id):
        return [review.__dict__ for review in self.repo.reviews_get_by_book_id(int(book_id))]

class Review(Resource):
    def __init__(self, repo=repository):
        self.repo = repo

    def post(self):
        data = request.get_json()
        return self.repo.review_add(data).__dict__

