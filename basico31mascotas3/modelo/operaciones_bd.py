
import mysql.connector
from modelo import constantes_sql, clases


def conectar():
    conexion = mysql.connector.connect(
        host = "localhost", 
        user = "root",
        database = "bd_accesorios"
        
        )
    return conexion

def registro_accesorio(accesorio):

    sql = constantes_sql.SQL_INSERCION_ACCESORIO
    conexion = conectar()
   
    cursor = conexion.cursor()
    
    valores_a_insertar = (accesorio.mascota, accesorio.accesorio, accesorio.talla, accesorio.tipo, accesorio.precio, accesorio.ofertas, accesorio.cliente, accesorio.envio)
    

    try:
        cursor.execute(sql,valores_a_insertar)
    except Exception as e:
                print(e)

        
                                                  
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.disconnect()
    return id_generado

def obtener_accesorios():    
    sql = constantes_sql.SQL_SELECT_ACCESORIOS
    conexion= conectar()
    cursor=conexion.cursor()
   
    try:
        cursor.execute(sql)
    except Exception as e:
                print(e)
                
    lista_resultado= cursor.fetchall()
    conexion.disconnect()
    return lista_resultado


    
def borrar_accesorio(id_accesorio):
    sql = constantes_sql.SQL_BORRAR_ACCESORIO
    conexion = conectar()
    cursor = conexion.cursor()
     
    val = (id_accesorio,)
    #cursor.execute(sql ,val)
    try:
        cursor.execute(sql,val)
    except Exception as e:
                print(e)
    val = (id_accesorio,)
    conexion.commit()
    
    conexion.disconnect()
    
def obtener_accesorio_por_id(id):
    sql = constantes_sql.SQL_OBTENER_ACCESORIO_POR_ID
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    #cursor.execute(sql,val)
    try:
        cursor.execute(sql,val)
    except Exception as e:
                print(e)

    resultado = cursor.fetchone()
    
    print(resultado)
    conexion.disconnect()

    accesorio = clases.Accesorio()
    accesorio.id = resultado[0]
    accesorio.mascota = resultado[1]
    accesorio.accesorio = resultado[2]
    accesorio.talla = resultado[3]
    accesorio.tipo = resultado[4]
    accesorio.precio = resultado[5]

    accesorio.ofertas = resultado[6]
    accesorio.cliente = resultado[7]
    accesorio.envio = resultado[8]
    
    return accesorio


def guardar_cambios_accesorio(accesorio_a_guardar_cambios):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_ACCESORIO
    conexion = conectar()
    cursor = conexion.cursor()
    val = (accesorio_a_guardar_cambios.mascota, accesorio_a_guardar_cambios.accesorio, accesorio_a_guardar_cambios.talla, accesorio_a_guardar_cambios.tipo, accesorio_a_guardar_cambios.precio, accesorio_a_guardar_cambios.ofertas, accesorio_a_guardar_cambios.cliente,accesorio_a_guardar_cambios.envio, accesorio_a_guardar_cambios.id)
    try:
        cursor.execute(sql,val)
    except Exception as e:
        print(e)
        
    conexion.commit()
    conexion.disconnect()



    