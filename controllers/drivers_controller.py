from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Driver, Team
from models import remove_driver, add_new_driver

drivers_blueprint = Blueprint("drivers", __name__)

@drivers_blueprint.route("/drivers")
def drivers():
    drivers = Driver.query.all()
    return render_template("index.jinja", drivers = drivers)

@drivers_blueprint.route('/drivers/<id>')
def show(id):
  chosen_driver = Driver.query.get(id)
  return render_template('show.jinja', title="{{driver.name}}" , driver = chosen_driver)

@drivers_blueprint.route('/drivers', methods=['POST'])
def add_driver():
    driver_number = request.form['driver_number']
    name = request.form['name']
    points = request.form['points']
    team_id = request.form['team']
    new_driver = Driver(driver_number = driver_number, name=name, points = points, team_id=team_id)
    add_new_driver(new_driver)
    return redirect('/drivers')


@drivers_blueprint.route('/drivers/<driver_number>/delete', methods=['POST'])
def delete(driver_number):
  remove_driver(driver_number)
  return redirect('/drivers')  

@drivers_blueprint.route('/drivers/<index>/edit')
def get_edit_page(index):
  chosen_driver = Driver.query.get([int(index)])
  return render_template('edit.jinja', title="{{driver.name}}", driver = chosen_driver)

@drivers_blueprint.route('/drivers/<index>', methods=['POST'])
def update_driver(index):
    driver_number = request.form['driver_number']
    name = request.form['name']
    points = request.form['points']
    team_id = request.form['team_id']
    
    driver = Driver.query.get(index)
    driver.driver_number = driver_number
    driver.name = name
    driver.points = points
    driver.team_id = team_id
    
    db.session.commit()
    return redirect('/drivers')