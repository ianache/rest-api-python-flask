from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics
from flasgger import Swagger
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/database'
db = SQLAlchemy(app)
metrics = PrometheusMetrics(app)
Swagger(app)

metrics.start_http_server(5099)

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)

class Sprint(db.Model):
    __tablename__ = 'sprints'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    effort_estimated = db.Column(db.Integer, nullable=False)
    cost_estimated = db.Column(db.Numeric(10,2), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Project(title=data['title'])
    db.session.add(project)
    db.session.commit()

    for sprint_data in data['sprints']:
        sprint = Sprint(
            title=sprint_data['title'],
            effort_estimated=sprint_data['effort_estimated'],
            cost_estimated=sprint_data['cost_estimated'],
            project_id=project.id
        )
        db.session.add(sprint)

    db.session.commit()
    return {'id': project.id}, 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

