'''
Created on 21/02/2016

@author: joan
'''
import wxversion
wxversion.select("2.8")
import AvanzaWomsInterface
class VentanaPrin(AvanzaWomsInterface.FramePrin):
    
    def __init__(self):
        AvanzaWomsInterface.FramePrin(0)
        
    
    