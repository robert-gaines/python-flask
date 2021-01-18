# For creating DB entries

from models import db,Employee,Role,Manager

# Create 2 x Employees

Bob = Employee('Bob')
Steve = Employee('Steve')

# Add to DB

db.session.add_all([Bob,Steve])

db.session.commit()

# Check DB Commit

print(Employee.query.all())

Bob = Employee.query.filter_by(name='Bob').first() # Return the first value from the query

Jim = Manager('Jim',Bob.id)

# Assign roles

role_primary = Role('Custodian',Bob.id)
role_secondary = Role('Security Guard',Bob.Id)

db.session.add_all([Jim,role,primary_role,role_secondary])

db.session.commit()

# Query to confirm
Bob = Employee.query.filter_by(name='Bob').first()

print(Bob)

print(Bob.IdentifyRoles())
