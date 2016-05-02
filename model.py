from app import db


class ModelMixin:
	
	def serialise(self):
		raise NotImplementedError


class Project(db.Model, ModelMixin):
	__tablename__ = "projects"
	project_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
	name = db.Column(db.Text, nullable=False)
	status_id = db.Column(db.Integer, db.ForeignKey("statuses.status_id"), nullable=False)

	status = db.relationship("Status")

	def serialise(self):
		return {
			"projectId" : self.project_id,
			"name" : self.name,
			"status" : self.status.name,
		}


class Status(db.Model, ModelMixin):
	__tablename__ = "statuses"
	ACTIVE = "Active"
	DISABLED = "Disabled"
	CLOSED = "Closed"

	status_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False, unique=True)

	def serialise(self):
		return {
			"statusId" : self.status_id,
			"name" : self.name,
		}
