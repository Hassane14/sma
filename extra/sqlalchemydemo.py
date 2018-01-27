#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sys
sys.path.insert(0, '.')
from gen.root import *


def do_demo1():
    print('Using Database1.xmi')
    u1 = Usuario(nombre='yo')
    m1 = Mensaje(autor=u1, texto='hola')
    print('u1 =', u1, u1.nombre)
    print('m1 =', m1)
    print(m1.autor == u1)
    print('m1.autor =', m1.autor.nombre)


def do_demo2():
    print('Using ClassDiagram1.xmi (transformed by the m2m class2table transformation)')
    u1 = Usuario(nombre='yo')
    f1 = Foro(nombre='Preguntas generales')
    t1 = Tema(nombre=u'Cómo funciona esta mierda?????', foro=f1)
    m1 = Mensaje(autor=u1, tema=t1, texto='Hola no funciona. Por favor ayudenme!!!')

    print('m1 =', m1)
    print('tema =', m1.tema.nombre)
    print('foro =', m1.tema.foro.nombre)
    print('autor =', m1.autor.nombre)
    assert m1.tema.foro == f1


def main(args):
    cmds = {n[3:]: f for n,f in globals().items() if n.startswith('do_')}
    if not args or args[0] not in cmds:
        print('Available commands:')
        for c in cmds.keys():
            print('  %s' % c)
        return

    cmds[args[0]]()

if __name__ == '__main__':
    main(sys.argv[1:])
