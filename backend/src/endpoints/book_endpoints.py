from flask import Blueprint, jsonify, request
from src.datalayer.repositories.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from src.factories.book_factory import BookFactory

book_endpoints = Blueprint('books', __name__, url_prefix='/api/v1')

@book_endpoints.route('/books', methods=['GET'])
def get_all_books():
    page = request.args.get("page", DEFAULT_PAGE, type=int)
    page_size = request.args.get("page_size", DEFAULT_PAGE_SIZE, type=int)
    
    service = BookFactory.service()
    books = service.list(page=page, page_size=page_size)
    
    return jsonify(books.model_dump())

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