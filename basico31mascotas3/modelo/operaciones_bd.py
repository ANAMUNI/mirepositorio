'''procedimmiennto con base de datos es:
1. conectr
2.  operar
3. desconectr
'''
#EL PROCEDIMIENTO CON BASES DE DATOS ES:
#1.CONECTAR  -- 2. OPERAR --- 3.DESCONECTAR

import mysql.connector
from modelo import constantes_sql
from mysql.connector import cursor

#para conectar con nuestra base de datos:

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost", #nos vamos a conectar con la bd q esta instalada en nuesstro equipo
        user = "root",
        database = "bd_accesorios"
        
        )
    return conexion

def registrar_accesorios(accesorio):

    sql = constantes_sql.SQL_INSERCION_ACCESORIOS
    conexion = conectar()
   
    cursor = conexion.cursor()
    
    valores_a_insertar = (accesorio.mascota, accesorio.accesorio, accesorio.talla, accesorio.tipo, accesorio.precio)
    
    cursor.execute(sql, valores_a_insertar)
    conexion.commit()
    conexion.disconnect()
    
def obtener_accesorios():    
    sql = constantes_sql.SQL_SELECT_ACCESORIOS
    conexion= conectar()
    cursor=conexion.cursor()
    cursor.execute(sql)
    lista_resultado= cursor.fetchall()
    conexion.disconnect()
    return lista_resultado


    
def borrar_accesorio(id_accesorio):
    sql = constantes_sql.SQL_BORRAR_ACCESORIOS
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_borrar = (id_accesorio,)
    cursor.execute(sql ,valores_a_borrar)
    conexion.commit()
    conexion.disconnect()