from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)

# Model Definition
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)

# CRUD Routes

# Create
@app.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data.get('description', ''))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item created!"}), 201

# Read
@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if item:
        return jsonify({'name': item.name, 'description': item.description})
    return jsonify({"message": "Item not found!"}), 404

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'name': item.name, 'description': item.description} for item in items])

# Update
@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found!"}), 404
    
    data = request.get_json()
    item.name = data['name']
    item.description = data.get('description', '')
    db.session.commit()
    
    return jsonify({"message": "Item updated!"})

# Delete
@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"message": "Item not found!"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item deleted!"})

# Run the App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
