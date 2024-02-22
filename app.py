from flask import Flask, jsonify, render_template, request
from models import db, Student
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:latest#1234@dev_mysql_container/student'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/students', methods=['POST'])
def create_student():
    try:
        name = request.json.get('name')
        course = request.json.get('course')
        date_joined_str = request.json.get('date_joined')

        try:
            # Parse the date string and convert it to a timestamp
            date_joined = datetime.strptime(date_joined_str, '%Y-%m-%d').timestamp()
        except ValueError:
            return jsonify({'error': 'Invalid date format for date_joined. Use YYYY-MM-DD.'}), 400

        # Convert the timestamp to an integer
        date_joined = int(date_joined)

        student = Student(name=name, course=course, date_joined=date_joined)
        db.session.add(student)
        db.session.commit()

        return jsonify({'message': 'Student created successfully'})
    except Exception as e:
        print(f"Error creating student: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/students', methods=['GET'])
def get_students():
    name = request.args.get('name')

    if name:
        students = Student.query.filter_by(name=name).all()
    else:
        students = Student.query.all()

    result = []

    for student in students:
        if isinstance(student.date_joined, int):
            # Convert timestamp to datetime object and then format it
            date_joined = datetime.fromtimestamp(student.date_joined).strftime('%Y-%m-%d')
        elif isinstance(student.date_joined, datetime):
            date_joined = student.date_joined.strftime('%Y-%m-%d')
        else:
            date_joined = None

        result.append({
            'name': student.name,
            'course': student.course,
            'date_joined': date_joined
        })

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

