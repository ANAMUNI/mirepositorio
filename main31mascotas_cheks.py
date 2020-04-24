'''
pyuic5 -x -o ventana_editar_accesorio.py ventana_editar_accesorio.ui
pyuic5 -x -o ventana_table_widget.py ventana_table_widget.ui
pyuic5 -x -o ventana_registrar_accesorio.py ventana_registrar_accesorio.ui
pyuic5 -x -o ventana_list_widget.py ventana_list_widget.ui
pyuic5 -x -o ventana_listado_accesorios.py ventana_listado_accesorios.ui
pyuic5 -x -o ventana_principal.py ventana_principal.ui
pyuic5 -x -o ventana_ver_detalles_accesorio.py ventana_ver_detalles_accesorio.ui

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_editar_accesorio, ventana_list_widget, ventana_listado_accesorios, ventana_principal, ventana_registrar_accesorio, ventana_table_widget, ventana_ver_detalles_accesorio
import sys
from modelo.clases import Accesorio
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton, QFileDialog,\
    QPixmap, QLabel
from _functools import partial
import shutil 
from pathlib import Path
from validadores import  validadores_accesorio
from modelo.operaciones_bd import borrar_accesorio, guardar_cambios_accesorio

lista_resultado = None



def registrar_accesorio():
    accesorio = Accesorio()

    accesorio.mascota = ui_registrar_accesorio.entrada_mascota_accesorio.text()
    accesorio.mascota = accesorio.mascota.strip()
    resultado_validar_mascota = validadores_accesorio.validar_mascota(accesorio.mascota)
    if resultado_validar_mascota == None :
        ui_registrar_accesorio.label_error_mascota.setText("<font color='red'>MASCOTA INCORRECTA</font>")
        return
    else:
        ui_registrar_accesorio.label_error_mascota.clear()

    accesorio.accesorio = ui_registrar_accesorio.entrada_accesorios.text()
    accesorio.talla = ui_registrar_accesorio.entrada_talla_accesorio.text()
    accesorio.tipo = ui_registrar_accesorio.entrada_tipo_accesorio.text()
    accesorio.precio = ui_registrar_accesorio.entrada_precio_accesorio.text()
    
    if ui_registrar_accesorio.checkbox_ofertas.isChecked():
        accesorio.ofertas = True
    
    indice_seleccionado = ui_registrar_accesorio.combo_cliente.currentIndex()
    accesorio.cliente = ui_registrar_accesorio.combo_cliente.itemText(indice_seleccionado)
    
    if ui_registrar_accesorio.radio_standar.isChecked() :
        accesorio.envio = "standar"

    if ui_registrar_accesorio.radio_urgente.isChecked() :
        accesorio.envio = "urgente"

    if ui_registrar_accesorio.radio_recogida.isChecked():
        accesorio.envio = "recogida"

    id_generado = operaciones_bd.registro_accesorio(accesorio)
    
    ruta_imagen = "temporal/imagen.jpg"
    objeto_path = Path(ruta_imagen)
    existe = objeto_path.is_file()
    if existe:
        ruta_imagen_destino = "imagenes/" + str(id_generado) + ".jpg"
        shutil.move("temporal/imagen.jpg",ruta_imagen_destino)

    QMessageBox.about(MainWindow,"Info","Registro de Accesorio OK")

def seleccionar_imagen():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    #ancho_label_imagen = ui_registrar_accesorio.label_imagen.width()
    alto_label_imagen = ui_registrar_accesorio.label_imagen.height()
    #redimension por ancho
    #pixmap_redim = pixmap.scaledToWidth(ancho_label_imagen)
    #ui_registrar_libro.label_imagen.setPixmap(pixmap_redim)
    #redimension por alto
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_registrar_accesorio.label_imagen.setPixmap(pixmap_redim)
    #redimension por alto y ancho
    #pixmap_redim = pixmap.scaled(ancho_label_imagen,alto_label_imagen)
    #ui_registrar_libro.label_imagen.setPixmap(pixmap_redim)

def mostar_registro_accesorio():
    ui_registrar_accesorio.setupUi(MainWindow)
    ui_registrar_accesorio.boton_registrar_accesorio.clicked.connect(registrar_accesorio)
    ui_registrar_accesorio.boton_seleccionar_archivo.clicked.connect(seleccionar_imagen)
    ui_registrar_accesorio.label_error_mascota.clear()
    ui_registrar_accesorio.label_error_accesorio.clear()

def mostrar_listado_accesorios():
    ui_listar_accesorios.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_accesorios()
    texto = ""
    for l in lista_resultado:
        texto +=  "id: " + str(l[0]) + " mascota: " + l[1] + " accesorio: " + str(l[2]) + "\n"
    ui_listar_accesorios.listado_accesorios.setText(texto)

def mostrar_list_widget():
    global lista_resultado
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_accesorios()
    #voy a rellenar el list widget
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget.addItem(l[1] + " accesorio: " + str(l[2]))
    ui_ventana_list_widget.list_widget.itemClicked.connect(mostrar_registro)

def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget_accesorios.currentRow()
    texto = ""
    texto += " mascota : " + lista_resultado[indice_seleccionado][1]+"\n"
    texto += " accesorio : " + str(lista_resultado[indice_seleccionado][2]) + "\n"
    texto += " talla : " + str(lista_resultado[indice_seleccionado][3]) + "\n"
    texto += " tipo : " + str(lista_resultado[indice_seleccionado][4]) + "\n"
    texto += "precio: " + str(lista_resultado[indice_seleccionado][5])
    QMessageBox.about(MainWindow,"Info", texto)


def mostrar_table_widget():
    ui_ventana_table_widget.setupUi(MainWindow)

    accesorios = operaciones_bd.obtener_accesorios()
    fila = 0
    for l in accesorios:
        ui_ventana_table_widget.tabla_accesorios.insertRow(fila)

        columna_indice = 0
        for valor in l:

            if columna_indice == 6:
                if valor == 0:
                    valor = "NO"
                else:
                    valor = "SI"

            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.tabla_accesorios.setItem(fila,columna_indice,celda)
            columna_indice += 1

        boton_ver_detalles = QPushButton("ver detalles")
        boton_ver_detalles.clicked.connect(partial(cargar_ver_detalles,l[0]))
        ui_ventana_table_widget.tabla_accesorios.setCellWidget(fila,4,boton_ver_detalles)

        
        boton_borrar = QPushButton("borrar")
        boton_borrar.clicked.connect(partial(borrar_accesorio,l[0]))
        ui_ventana_table_widget.tabla_accesorios.setCellWidget(fila,5,boton_borrar)

        boton_editar = QPushButton("editar")
        boton_editar.clicked.connect(partial(editar_accesorio,l[0],l[1]))
        ui_ventana_table_widget.tabla_accesorios.setCellWidget(fila,6,boton_editar)


        label_miniatura = QLabel()
        ruta_imagen = "imagenes/" + str(l[0]) + ".jpg"
        objeto_path = Path(ruta_imagen)
        existe = objeto_path.is_file()
        if existe == True: #Path("imagenes/" + l[0] + ".jpg").is_file() :
            pixmap = QPixmap(ruta_imagen)
            pixmap_redim = pixmap.scaledToHeight(40)
            label_miniatura.setPixmap(pixmap_redim)
            ui_ventana_table_widget.tabla_accesorios.setCellWidget(fila,7,label_miniatura)

        fila += 1

def cargar_ver_detalles(id):
    QMessageBox.about(MainWindow,"Info","ver detalles del registro de id: " + str(id))
    ui_ventana_ver_detalles_accesorio.setupUi(MainWindow)
    accesorio = operaciones_bd.obtener_accesorio_por_id(id)

    ui_ventana_ver_detalles_accesorio.entrada_mascota_accesorio.setText(accesorio.mascota)
    ui_ventana_ver_detalles_accesorio.entrada_accesorios.setText(str(accesorio.accesorio))
    ui_ventana_ver_detalles_accesorio.entrada_talla_accesorio.setText(str(accesorio.talla))
    ui_ventana_ver_detalles_accesorio.entrada_tipo_accesorio.setText(str(accesorio.tipo))
    ui_ventana_ver_detalles_accesorio.entrada_precio_accesorio.setText(str(accesorio.precio))

    if accesorio.ofertas :
        ui_ventana_ver_detalles_accesorio.checkbox_ofertas.setChecked(True)

    ui_ventana_ver_detalles_accesorio.combo_cliente.setCurrentText(accesorio.cliente)

    if accesorio.envio == "standar":
        ui_ventana_ver_detalles_accesorio.radio_standar.setChecked(True)

    if accesorio.envio == "urgente":
        ui_ventana_ver_detalles_accesorio.radio_urgente.setChecked(True)

    if accesorio.envio == "recogida":
        ui_ventana_ver_detalles_accesorio.radio_recogida.setChecked(True)


    pixmap = QPixmap("imagenes/"+str(accesorio.id)+".jpg")
    alto_label_imagen = ui_ventana_ver_detalles_accesorio.label_imagen.height()
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_ventana_ver_detalles_accesorio.label_imagen.setPixmap(pixmap_redim)


def editar_accesorio(id,mascota):
    QMessageBox.about(MainWindow,"Info","vas a editar el registro de id: " + str(id))
    ui_ventana_editar_accesorio.setupUi(MainWindow)


    accesorio_a_editar = operaciones_bd.obtener_accesorio_por_id(id)
    ui_ventana_editar_accesorio.entrada_mascota_accesorio.setText(accesorio_a_editar.mascota)
    ui_ventana_editar_accesorio.label_error_mascota.clear()
    ui_ventana_editar_accesorio.entrada_accesorios.setText(str(accesorio_a_editar.accesorio))
    ui_ventana_editar_accesorio.label_error_accesorio.clear()
    ui_ventana_editar_accesorio.entrada_precio_accesorio.setText(str(accesorio_a_editar.precio))
    ui_ventana_editar_accesorio.entrada_talla_accesorio.setText(str(accesorio_a_editar.talla))
    ui_ventana_editar_accesorio.entrada_tipo_accesorio.setText(str(accesorio_a_editar.tipo))
    if accesorio_a_editar.ofertas :
        ui_ventana_editar_accesorio.checkbox_ofertas.setChecked(True)

    if accesorio_a_editar.cliente:
        ui_ventana_editar_accesorio.combo_cliente.setCurrentText(accesorio_a_editar.cliente)

    if accesorio_a_editar.envio == "standar":
        ui_ventana_editar_accesorio.radio_standar.setChecked(True)

    if accesorio_a_editar.envio == "urgente":
        ui_ventana_editar_accesorio.radio_urgente.setChecked(True)

    if accesorio_a_editar.envio == "recogida":
        ui_ventana_editar_accesorio.radio_recogida.setChecked(True)


    pixmap = QPixmap("imagenes/"+str(accesorio_a_editar.id)+".jpg")
    alto_label_imagen = ui_ventana_editar_accesorio.label_imagen.height()
    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_ventana_editar_accesorio.label_imagen.setPixmap(pixmap_redim)

    ui_ventana_editar_accesorio.boton_guardar_cambios_accesorio.clicked.connect(partial(guardar_cambios_accesorio,accesorio_a_editar.id))
    ui_ventana_editar_accesorio.boton_seleccionar_archivo.clicked.connect(seleccionar_imagen_editar)

def seleccionar_imagen_editar():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"/imagen.jpg")
    pixmap = QPixmap("/imagen.jpg")
    ancho_label_imagen = ui_ventana_editar_accesorio.label_imagen.width()
    alto_label_imagen = ui_ventana_editar_accesorio.label_imagen.height()

    pixmap_redim = pixmap.scaledToHeight(alto_label_imagen)
    ui_ventana_editar_accesorio.label_imagen.setPixmap(pixmap_redim)
  

def guardar_cambios_accesorio(id):
    accesorio_guardar_cambios = Accesorio()
    accesorio_guardar_cambios.mascota = ui_ventana_editar_accesorio.entrada_mascota_accesorio.text()

    resultado_validar_mascota = validadores_accesorio.validar_mascota(accesorio_guardar_cambios.mascota)
    if resultado_validar_mascota == None :
        ui_ventana_editar_accesorio.label_error_mascota.setText("<font color='red'>MASCOTA INCORRECTA</font>")
        return
    else:
        ui_ventana_editar_accesorio.label_error_mascota.clear()

    accesorio_guardar_cambios.accesorio = ui_ventana_editar_accesorio.entrada_accesorios.text()
    accesorio_guardar_cambios.talla = ui_ventana_editar_accesorio.entrada_talla_accesorio.text()
    accesorio_guardar_cambios.tipo = ui_ventana_editar_accesorio.entrada_tipo_accesorio.text()
    accesorio_guardar_cambios.precio = ui_ventana_editar_accesorio.entrada_precio_accesorio.text()

    if ui_ventana_editar_accesorio.checkbox_ofertas.isChecked():
        accesorio_guardar_cambios.ofertas = True

    accesorio_guardar_cambios.cliente = ui_ventana_editar_accesorio.combo_cliente.currentText()

    if ui_ventana_editar_accesorio.radio_standar.isChecked():
        accesorio_guardar_cambios.envio = "standar"

    if ui_ventana_editar_accesorio.radio_urgente.isChecked():
        accesorio_guardar_cambios.envio = "urgente"

    if ui_ventana_editar_accesorio.radio_recogida.isChecked():
        accesorio_guardar_cambios.envio = "recogida"

    accesorio_guardar_cambios.id = id

    QMessageBox.about(MainWindow,"Info","guardar cambios sobre el registro: " + str(id))
    operaciones_bd.guardar_cambios_accesorio(accesorio_guardar_cambios)


    ruta_imagen = "temporal/imagen.jpg"
    objeto_path = Path(ruta_imagen)
    existe = objeto_path.is_file()
    if existe:
        ruta_imagen_destino = "imagenes/" + str(id) + ".jpg"
        shutil.move("temporal/imagen.jpg",ruta_imagen_destino)


    mostrar_table_widget()

def borrar_accesorio(id):
    res = QMessageBox.question(MainWindow,"Info","Vas a borrar un registro : " + str(id))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_accesorio(id)
        mostrar_table_widget()


def mostrar_inicio():
    ui.setupUi(MainWindow)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_MainWindow()
ui_registrar_accesorio = ventana_registrar_accesorio.Ui_MainWindow()
ui_listar_accesorios = ventana_listado_accesorios.Ui_MainWindow()
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()
ui_ventana_editar_accesorio = ventana_editar_accesorio.Ui_MainWindow()
ui_ventana_ver_detalles_accesorio = ventana_ver_detalles_accesorio.Ui_MainWindow()

ui.setupUi(MainWindow)

ui.submenu_insertar_accesorio.triggered.connect(mostar_registro_accesorio)
ui.submenu_listar_accesorios.triggered.connect(mostrar_listado_accesorios)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
ui.submenu_list_widget_accesorios.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_accesorios.triggered.connect(mostrar_table_widget)

MainWindow.show()
sys.exit(app.exec_())
