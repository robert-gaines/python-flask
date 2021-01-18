from db_basic import db,Inventory

# -> Create all of the tables from the Model Class

db.create_all()

item_one = Inventory('Item_One',123)
item_two = Inventory('Item_Two',456)

print(item_one.item_name)

# Objects can be added individually or in bulk
# for single addition: db.session.add(item)

db.session.add_all([item_one,item_two])

# Make the changes

db.session.commit()

print(item_one.item_id)
