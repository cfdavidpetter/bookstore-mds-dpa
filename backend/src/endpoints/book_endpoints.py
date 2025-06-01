from flask import Blueprint, jsonify, request
from src.factories.book_factory import BookFactory

book_endpoints = Blueprint('books', __name__, url_prefix='/api/v1')

@book_endpoints.route('/books', methods=['GET'])
def get_all_books():
    service = BookFactory.service()
    books = service.list()
    return jsonify([book.model_dump() for book in books])

@book_endpoints.route('/books/<book_id>', methods=['GET'])
def get_book_by_id(book_id):
    service = BookFactory.service()
    book = service.get_by_id(book_id)
    return jsonify(book.model_dump())

@book_endpoints.route('/books', methods=['POST'])
def create_book():
    service = BookFactory.service()
    book = service.create(request.get_json())
    return jsonify(book.model_dump())

@book_endpoints.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    service = BookFactory.service()
    book = service.update(book_id, request.get_json())
    return jsonify(book.model_dump()) 

@book_endpoints.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    service = BookFactory.service()
    service.delete(book_id)
    return jsonify({'message': 'Book deleted successfully'})