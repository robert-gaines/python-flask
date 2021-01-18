from db_basic import Inventory,db

# CREATE #

ThisInventory = Inventory('Site-One',112)

db.session.add(ThisInventory)

db.session.commit()

# READ #

# Using ORM #

all_items = Inventory.query.all()

print(all_items)

# Select by ID #

single_item = Inventory.query.get(1)

print(single_item.item_name)

# Filter #

specific_item = Inventory.query.filter_by(item_name='Item_One')

print(specific_item.all())

# UPDATE #

target_item = Inventory.query.get(1)
target_item.item_pn = 789
db.session.add(target_item)
db.session.commit()

#DELETE#

del_item = Inventory.query.get(2)
db.session.delete(del_item)
db.session.commit()

#

all_items = Inventory.query.all()
print(all_items)
