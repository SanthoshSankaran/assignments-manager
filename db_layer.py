import psycopg2
from flask import jsonify, make_response
import json

class DBLayer:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
        )

    def fetch_assignment(self, id):
        try:
            cursor = self.conn.cursor()
            query = f"SELECT id, name, title, description, type, duration::TEXT FROM assignments WHERE id = {id};"

            print(query)

            cursor.execute(query)
            results = cursor.fetchone()
            response = []
            for row in results:
                response.append(row)

            print(response)

            self.conn.commit()

            message = jsonify(response)

            return make_response(message, 200)
        except psycopg2.Error as err:
            print(err)
        except Exception as err:
            print(err)
        finally:
            cursor.close()

    def fetch_assignments_by_tag(self, tag):
        try:
            cursor = self.conn.cursor()
            query = f"SELECT id, name, title, description, type, duration::TEXT FROM assignments WHERE '{tag}' = ANY(tags);"

            cursor.execute(query)
            results = cursor.fetchall()
            self.conn.commit()

            return make_response(jsonify(data=results), 200)
        except psycopg2.Error as err:
            print(err)
        except Exception as err:
            print(err)
        finally:
            cursor.close()
    
    def create_assignment(self, data):
        try:
            cursor = self.conn.cursor()
            tags = str(json.dumps(data['tags'])).replace('[', '{').replace(']', '}')
            tags = tags.replace('\'', '"')
            print(tags)
            query = f""" INSERT INTO assignments (name, title, description, type, duration, tags)
            VALUES ('{data['name']}', '{data['title']}', '{data['description']}', '{data['type']}', {data['duration']},
            '{tags}') RETURNING *;"""

            print(query)

            cursor.execute(query)
            self.conn.commit()
            results = cursor.fetchall()
            print(results)
            message = 'Successfully created assignment' + str(results)
            if not results:
                message = jsonify(message='Unable to create the assignment')
                return make_response(message, 400)
            
            return make_response(message, 201)
        except psycopg2.Error as err:
            print(err)
        except Exception as err:
            print(err)
        finally:
            cursor.close()
