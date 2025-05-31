from flask import Blueprint, jsonify, request
from src.factories.author_factory import AuthorFactory

author_endpoints = Blueprint('authors', __name__, url_prefix='/api/v1')

@author_endpoints.route('/authors', methods=['GET'])
def get_all_authors():
    service = AuthorFactory.service()
    authors = service.list()
    return jsonify([author.model_dump() for author in authors])

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