from database import Sample, db
from application import application
import jsonpickle

@application.route('/sample')
def sample():
    instance = db.session.query(Sample).first()
    return jsonpickle.encode(instance)
