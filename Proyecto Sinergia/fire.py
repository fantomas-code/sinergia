# -*- coding: utf-8 -*-
import os, sys
import fdb as sg

#metodo de conexion
def conectar(x):
	# print(x)
	ruta = 'bd/sga.fdb'
	con = sg.connect(
			dsn = ruta,
			user = 'sysdba',#Usuario por defecto en firebird
			password = '',# aqui va la contraseña que pusiste al instalar firebird en tu pc
			charset ='utf8'		
	)

	cx = con.cursor()
	cx.execute(x)
	if x.startswith("SELECT"):
		datos = cx.fetchall()
	else:
		con.commit()
		datos = None
	cx.close()
	con.close()
	return datos
#.........................................................................................................
