'''
Created on 27 de ene. de 2016

@author: jferrerm
'''
import wxversion
wxversion.select("2.8")
import AvanzaWomsInterface
import gettext
#import os
#from WOMPendientesTXT import WOMPendientesTXT

if __name__ == '__main__':

    '''
    ObtenID = WOMPendientesTXT('C:\Users\Admin\Desktop\ID_WOM.txt')
    ObtenID.ConectaBD()
    ObtenID.ObtenListaWomsBD()
    ObtenID.ValoresColumnaToTxtFile()


    #Ejecuta script sikuli Avanzar WOM FInalizados
    print("Ejecutando sikuli...")
    #print('C:\Users\Admin\Documents\Sikuli\\runsikulix.cmd -r "C:\Users\Admin\Documents\Avanzar WOM Finalizados.sikuli"')
    os.execl('C:\Users\Admin\Documents\Sikuli\\runsikulix.cmd',
             'C:\Users\Admin\Documents\Sikuli\\runsikulix.cmd',
             '-r','"C:\Users\Admin\Documents\Avanzar WOM finalizados.sikuli"')
             

    '''
    gettext.install("app") # replace with the appropriate catalog name

    app = AvanzaWomsInterface.FramePrin(0)
    app.MainLoop()
    