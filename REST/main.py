from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data as a dictionary
books = {
    1: {'title': 'Book 1', 'author': 'Author 1'},
    2: {'title': 'Book 2', 'author': 'Author 2'}
}

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    if book_id in books:
        return jsonify(books[book_id])
    else:
        return jsonify({'error': 'Book not found'}), 404

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_id = max(books.keys()) + 1
    books[new_id] = {'title': data['title'], 'author': data['author']}
    return jsonify({'message': 'Book created', 'id': new_id}), 201

# Route to update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if book_id in books:
        data = request.get_json()
        books[book_id] = {'title': data['title'], 'author': data['author']}
        return jsonify({'message': 'Book updated'})
    else:
        return jsonify({'error': 'Book not found'}), 404

# Route to delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return jsonify({'message': 'Book deleted'})
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)