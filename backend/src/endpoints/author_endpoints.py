from flask import Blueprint, jsonify, request
from src.datalayer.repositories.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from src.factories.author_factory import AuthorFactory

author_endpoints = Blueprint('authors', __name__, url_prefix='/api/v1')

@author_endpoints.route('/authors', methods=['GET'])
def get_all_authors():
    page = request.args.get("page", DEFAULT_PAGE, type=int)
    page_size = request.args.get("page_size", DEFAULT_PAGE_SIZE, type=int)
    filters = request.args.get("filters", None, type=str)

    service = AuthorFactory.service()
    authors = service.list(page=page, page_size=page_size, filters=filters)

    return jsonify(authors.model_dump())

@author_endpoints.route('/authors/<author_id>', methods=['GET'])
def get_author_by_id(author_id):
    service = AuthorFactory.service()
    author = service.get_by_id(author_id)
    return jsonify(author.model_dump())

@author_endpoints.route('/authors', methods=['POST'])
def create_author():
    service = AuthorFactory.service()
    author = service.create(request.get_json())
    return jsonify(author.model_dump())

@author_endpoints.route('/authors/<author_id>', methods=['PUT'])
def update_author(author_id):
    service = AuthorFactory.service()
    author = service.update(author_id, request.get_json())
    return jsonify(author.model_dump()) 

@author_endpoints.route('/authors/<author_id>', methods=['DELETE'])
def delete_author(author_id):
    service = AuthorFactory.service()
    service.delete(author_id)
    return jsonify({'message': 'Author deleted successfully'})