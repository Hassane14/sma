Class Project *Desarollo de Software Basado en Modelos y Aspectos*
Universida de Sevilla, Curso 2017/18

Design Decisions
================

Metamodel
---------
* Primary Key is an element of the column, not of the table, because the table
  can be deduced from the Column, but not the other way around, so this way
  modeling is less work (and transformations are easier, too). As we don't
  support multi-column primary keys anyway this doesn't do any harm. 
* Restrictions that seem unnecessary, but ensure transformations work well:
  - The class diagram must have a name.
  - Names of primary keys and foreign keys must not collide.
  - Columns that have an associated foreign key must be named `fk_pk`, where
    `fk` and `pk` are the names of the foreign key and primary key on the
    referenced table, respectively. Accordingly, classes must not have an
    attribute named `ref_pk` if they have a reference named `ref` pointing to a
    class whose primary key is `pk`.
  - A class must define a primary key if there is a reference pointing to it.
