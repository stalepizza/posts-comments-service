from flask import Flask, request, jsonify, abort, render_template
from models import db, Post, Comment
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db.init_app(app)

with app.app_context():
    db.drop_all()  # WARNING: This wipes data
    db.create_all()

#Frontend route
@app.route('/')
def index():
    return render_template("index.html")

#API routes
@app.route('/posts', methods=['GET'])
def list_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])

@app.route('/posts', methods=['POST'])
def create_post():
    title = request.form.get('title')
    body = request.form.get('body')
    image_file = request.files.get('image')

    if not title or not body:
        abort(400, "Title and body required")

    filename = None
    if image_file:
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    new = Post(title=title, body=body, image=filename)
    db.session.add(new)
    db.session.commit()
    return jsonify(new.to_dict()), 201

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    Comment.query.filter_by(post_id=post.id).delete()
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted"}), 200

@app.route('/posts/<int:post_id>/comments', methods=['GET'])
def list_comments(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify([c.to_dict() for c in post.comments])

@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json() or {}
    if not data.get('body'):
        abort(400, "Must include body")
    comment = Comment(post_id=post.id, body=data['body'])
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 201

@app.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted"}), 200

#Error handler
@app.errorhandler(400)
@app.errorhandler(404)
def handle_error(err):
    response = jsonify({
        "error": err.name,
        "message": err.description
    })
    response.status_code = err.code
    return response

if __name__ == '__main__':
    app.run(debug=True)
