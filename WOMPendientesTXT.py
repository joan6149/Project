#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
Created on 27 de ene. de 2016

@author: jferrerm
'''
#Consulta: select fit.wom from FIT_PROYECTOS as fit inner join WOM_ESTADO as wom on fit.Wom = wom.WOM_PROYECTO where wom.WOM_TAREA = 'Pendiente Fin Proyecto'  and fit.Actividad in('Cierre Proyecto','FIN Activado y Validado','RFS')
#sys.path.append('/usr/local/lib/python2.7/dist-packages/openpyxl')

import pymssql


class WOMPendientesTXT(object):
    '''
    classdocs
    '''


    def __init__(self, rutaDestinoTXT):
        '''
        Constructor que abre un objeto tipo workbook solo para ser leido, una lista vacia y un objeto WorkSheet que representa una pestaña
        '''
        self.RutaDestino = rutaDestinoTXT
        self.sql = ["select fit.wom from FIT_PROYECTOS as fit inner join WOM_ESTADO as wom on fit.Wom = wom.WOM_PROYECTO where wom.WOM_TAREA = 'Pendiente Fin Proyecto'  and fit.Actividad in('Cierre Proyecto','FIN Activado y Validado','RFS')",
        "select Wom from FIT_IMPORTED_DATA where \[Motivo Inc\] = 'Pdte. Formalizar Cancelación' AND Actividad = 'FIN Cancelado'",
        "select Wom from FIT_IMPORTED_DATA where Actividad = 'Cierre Proyecto'","select Wom from FIT_IMPORTED_DATA where Actividad = 'Ventana Cambio'"]
        self.li = [] #lista donde se guardan los woms por finalizar
    
    def ConectaBD(self):
        self.bd = pymssql.connect(server="10.148.85.84",
                                  user="sa",
                                  password="Sqladmin*15",
                                  database="orange_cdm_industrializado")
        if self.bd != None:
            print("Conectado a bd")
        self.cursor = self.bd.cursor()
        
        if self.cursor != None:
			print("Cursor Creado")
			
    def ObtenListaWomsBD(self):
		
		i = ["Pendiente Fin Proyecto","Actor BC","Chequeo Condiciones salida","Configuracion Radius Hosting"]
		cont = 0
		for query in self.sql:		
			try:
				self.li.append(str(i[cont]))
				self.cursor.execute(query)
				for row in self.cursor:
					self.li.append(str(row[0]))
			except:
				print("No se obtuvieron los WOMID")
				
			self.li.append(str("---"))
			cont +=1
            
    def ValoresColumnaToTxtFile(self):
        
        try:
            outfile= open(self.RutaDestino, 'w')
            for wom in self.li:
                outfile.write(str(wom+"\n"))

            #outfile.close()
            print("Fichero "+self.RutaDestino+" Generado con exito!")
        except Exception as e:

            print(e)

        outfile.close()
        self.bd.close()