from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Dữ liệu mẫu về người dùng (cần lưu trữ an toàn hơn trong môi trường thực tế)
users = {
    "user": "password",
    "admin": "adminpassword"
}

# Hàm xác thực
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Route yêu cầu xác thực
@app.route('/protected')
@auth.login_required
def protected_route():
    return jsonify({'message': 'This is a protected route'}), 200

if __name__ == '__main__':
    app.run(debug=True)