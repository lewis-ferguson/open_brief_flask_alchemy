from app import db


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    points = db.Column(db.Integer)
    drivers = db.relationship('Driver', backref='team')#this allows us to call driver.team
    
    def __repr__(self):
        return f'<Team {self.id} {self.name} {self.points}'


class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key = True)
    driver_number = db.Column(db.Integer)
    name = db.Column(db.String(64))
    points = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    
    def __repr__(self):
        return f'<Driver {self.driver_number}: {self.name} {self.points} {self.team_id}>'
    
    
def remove_driver(driver_number):
    driver = Driver.query.get(driver_number)
    db.session.delete(driver)
    db.session.commit()

def add_new_driver(driver):
    db.session.add(driver)
    db.session.commit()