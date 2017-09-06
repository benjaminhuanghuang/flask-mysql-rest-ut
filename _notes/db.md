## Connection



## Sqlalchemy
    
    
## Sqlalchemy Relation
    ```
    class StoreModel(db.Model):
        ...
        items = db.relationship('ItemModel', lazy='dynamic')
        
        def json(self):
            return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    
    class ItemModel(db.Model):
        ...
        store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
        store = db.relationship('StoreModel')
    ```