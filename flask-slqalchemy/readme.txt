pip install sqlalchemy //instalar la libreri de sqlalchemy
pip install flask-sqlalchemy

Luego ingresamos a la terminal de python
python

from app import db //importar la base de datos
db.create_all()
from app import Equipo
barcelona = Equipo(nombre="Barcelona", pais="Esp")
Atletico = Equipo(nombre="Atletico, pais="Esp")
db.session.add(barcelona) 
db.session.add(Atletico)  
db.session.commit()
//consultar todos los valores de la tabla
>>> result = Equipo.query.all()
>>> for r in result:
...     print(r.nombre)
//Cinsultar un dato
bar = Equipo.query.filter_by(nombre="Barcelona").first()
>>> print(bar.nombre) 
Barcelona
>>> print(bar.pais)   
Esp
//otra forma de consultar un dato
bar = Equipo.query.filter(Equipo.nombre=="Barcelona").first()