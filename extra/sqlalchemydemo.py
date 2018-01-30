#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, '.')
from gen.root import *
from gen.root import Base


print('==== Using Database1.xmi')
u1 = Usuario(nombre='yo')
m1 = Mensaje(autor=u1, texto='hola')
print('u1 =', u1, u1.nombre)
print('m1 =', m1)
print(m1.autor == u1)
print('m1.autor =', m1.autor.nombre)


print('\n\n==== Using ClassDiagram1.xmi (transformed by the m2m class2table transformation)')
u1 = Usuario(nombre='yo')
f1 = Foro(nombre='Preguntas generales')
t1 = Tema(nombre=u'Cómo funciona esta mierda?????', foro=f1)
m1 = Mensaje(autor=u1, tema=t1, texto='Hola no funciona. Por favor ayudenme!!!')

print('m1 =', m1)
print('tema =', m1.tema.nombre)
print('foro =', m1.tema.foro.nombre)
print('autor =', m1.autor.nombre)
assert m1.tema.foro == f1

print('\n== Setting up database')

engine = create_engine('sqlite:///:memory:')#, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add_all([u1, f1, t1, m1])
session.commit()

print('u1.id =', u1.id, '==', 'm1.autor_id =', m1.autor_id)
print('t1.pk =', t1.pk, '==', 'm1.tema_pk =', m1.tema_pk)

print('u1 from database:', session.query(Usuario).filter(Usuario.nombre == 'yo').one().id)
