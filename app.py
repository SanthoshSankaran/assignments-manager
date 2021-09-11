from flask import Flask, request, jsonify, render_template
from service import AssignmentsService

app = Flask(__name__)
service = AssignmentsService()

@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')

@app.get("/assignments")
def get_assignment():
    args = request.args
    return service.get_assignment_by_id(args.get('id'))

@app.post("/assignments")
def add_assignment():
    data = request.get_json()
    print(data)
    return service.add_assignment(data)

@app.get("/assignments/tag")
def search_by_tag():
    args = request.args
    print(args.get('tag'))
    return service.search_assignments(args.get('tag'))

if __name__ == '__main__':
   app.run()
