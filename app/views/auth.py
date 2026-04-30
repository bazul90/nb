from flask import Blueprint, request, jsonify
from app.extensions import db
from app.domain.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    # Must be JSON
    if not data:
        return jsonify({
            "status": "error",
            "message": "Request must be JSON"
        }), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Required fields check
    if not username or not email or not password:
        return jsonify({
            "status": "error",
            "message": "Username, email and password are required"
        }), 400

    # 🔐 Password strength check
    if len(password) < 6:
        return jsonify({
            "status": "error",
            "message": "Password must be at least 6 characters"
        }), 400

    # Normalize input
    username = username.strip()
    email = email.lower().strip()

    # Duplicate checks
    if User.query.filter_by(email=email).first():
        return jsonify({
            "status": "error",
            "message": "Email already registered"
        }), 400

    if User.query.filter_by(username=username).first():
        return jsonify({
            "status": "error",
            "message": "Username already taken"
        }), 400

    # Create user
    user = User(
        username=username,
        email=email
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User registered successfully",
        "data": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request must be JSON"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "status": "error",
            "message": "Email and password required"
        }), 400

    email = email.lower().strip()

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({
            "status": "error",
            "message": "Invalid credentials"
        }), 401

    return jsonify({
        "status": "success",
        "message": "Login successful",
        "data": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200