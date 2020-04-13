'''
Created on 2 abr. 2020

python -m PyQt5.uic.pyuic -o ventana_registrar_accesorios.py ventana_registrar_accesorios.ui

python -m PyQt5.uic.pyuic -o ventana_registrar_accesorios.py ventana_registrar_accesorios.ui
python -m PyQt5.uic.pyuic -o ventana_principal.py ventana_principal.ui
python -m PyQt5.uic.pyuic -o ventana_listado_accesorios.py ventana_listado_accesorios.ui
python -m PyQt5.uic.pyuic -o ventana_list_widget.py ventana_list_widget.ui
python -m PyQt5.uic.pyuic -o ventana_table_widget.py ventana_table_widget.ui
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ventanas import ventana_principal, ventana_listado_accesorios, ventana_list_widget, ventana_table_widget, ventana_registrar_accesorios
from modelo.clases import Accesorio
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton
from _functools import partial


#variable con el resultado de base de datos
lista_resultado = None

def registrar_accesorios():
    accesorio = Accesorio()
    accesorio.mascota = ui_registrar_accesorios.entrada_mascota_accesorios.text()
    accesorio.accesorio = ui_registrar_accesorios.entrada_accesorios.text()
    accesorio.talla = ui_registrar_accesorios.entrada_talla_accesorios.text()
    accesorio.tipo = ui_registrar_accesorios.entrada_tipo_accesorios.text()
    accesorio.precio = ui_registrar_accesorios.entrada_precio_accesorios.text()
    
   
    operaciones_bd.registrar_accesorios(accesorio)
    QMessageBox.about(MainWindow,"Info","Registro de accesorio ok")
       
def mostar_registro_accesorio():
    ui_registrar_accesorios.setupUi(MainWindow)
    ui_registrar_accesorios.boton_registrar_accesorios.clicked.connect(registrar_accesorios)
    
                                                                    
    
def mostrar_listado_accesorios():
    ui_listar_accesorios.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_accesorios()
    texto = ""
    for l in lista_resultado:
        texto += "id: " + str(l[0]) + " mascota: " + str(l[1])+ " accesorio: " + str(l[2])+ " talla: " + str(l[3]) + " tipo: " + str(l[4]) + " precio: " +str(l[5]) + "\n"
    ui_listar_accesorios.listado_accesorios.setText(texto)
def mostrar_list_widget():
    global lista_resultado
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_accesorios()
    #voy a rellenar el list widget
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget.addItem(l[1] + " accesorio: " + str(l[2]) + " talla: " + str(l[3]) + " tipo: " + str(l[4]) + " precio: " +str(l[5]) + "\n")
        
    ui_ventana_list_widget.list_widget.itemClicked.connect(mostrar_registro)
#funcion  que muestra toda la informacion cuando se haga click 
#en un elemento del list widget    
def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget.currentRow()
    texto = ""
    texto += "mascota: " + str(lista_resultado[indice_seleccionado][1]) + "\n"
    texto += "accesorio: " + str(lista_resultado[indice_seleccionado][2]) + "\n"
    texto += "talla: " + str(lista_resultado[indice_seleccionado][3]) + "\n"
    texto += "tipo: " + str(lista_resultado[indice_seleccionado][4]) + "\n"

def mostrar_table_widget():
    ui_ventana_table_widget.setupUi(MainWindow)
    #vamos a rellenar la tabla
    accesorios = operaciones_bd.obtener_accesorios()
    fila = 0
    for l in accesorios:
        ui_ventana_table_widget.tabla_accesorios.insertRow(fila) #creo la fila
        #y ahora meto las celdas correspondientes en la fila
        columna_indice = 0
        for valor in l:
            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.tabla_accesorios.setItem(fila,columna_indice,celda)
            columna_indice += 1
        #despues de rellenar los datos en la fila
        #meto un boton de borrar
        boton_borrar = QPushButton("BORRAR") #metodo para crear un boton
        boton_borrar.clicked.connect(partial(borrar_accesorio,l[0]))
        ui_ventana_table_widget.tabla_accesorios.setCellWidget(fila,5,boton_borrar) #para crear el boton en cada celda       
        

        
        fila += 1
        
def borrar_accesorio(id):
    res = QMessageBox.question(MainWindow,"Info","Vas a borrar un registro de id: " + str(id))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_accesorio(id)
        mostrar_table_widget()

        
def mostrar_inicio():
    ui.setupUi(MainWindow)

#inicio aplicacion principal:
app = QtWidgets.QApplication(sys.argv) #linea obligatoria para usar pyqt5
MainWindow = QtWidgets.QMainWindow() #crea una ventana principal con pyqt5
ui = ventana_principal.Ui_MainWindow() #creo el interfaz definido por ventana_principal.py
#que es el archivo generado desde la consola a partir
#del archivo de diseño ventana_principal.ui
ui_registrar_accesorios = ventana_registrar_accesorios.Ui_MainWindow() #lo mismo pero para registrar libro
ui_listar_accesorios = ventana_listado_accesorios.Ui_MainWindow()#lo mismo pero para listar libros
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()

ui.setupUi(MainWindow)#todo lo que tiene el interfaz de la ventana principal lo pongo en el MainWindow

ui.submenu_registrar_accesorios.triggered.connect(mostar_registro_accesorio)
ui.submenu_listar_accesorios.triggered.connect(mostrar_listado_accesorios)
ui.submenu_list_widget_accesorios.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_accesorios.triggered.connect(mostrar_table_widget)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
    
                      
MainWindow.show()#mostrar la ventana principal de pyqt5
sys.exit(app.exec_())#cerrar la aplicacion cuando se cierra la ventana MainWindow