begin;

\ir ../gen/root.sql

insert into usuario values (42, 'soy yo');
insert into foro values ('preguntas',1);
insert into tema values('como va', 9, 1);
insert into mensaje values('ayudenme porfa', 100,42,9);

select texto, usuario.nombre, tema.nombre from mensaje,usuario,tema where autor_id=usuario.id and tema_pk=tema.pk;
--      texto      | nombre | nombre  
-- ----------------+--------+---------
--  ayudenme porfa | soy yo | como va
-- (1 row)

rollback;
