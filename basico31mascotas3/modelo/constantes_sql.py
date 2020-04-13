'''
las constantes se ponen en mayúsculas
ALGO QUE NO PUEDE CAMBIAR, SE COJE  PERO NO SE MODIFIICA
SE  COPI LA  LINEA DE INSERT DE  SQL y se pone %s para dar luego los valores
'''

SQL_INSERCION_ACCESORIOS = "INSERT INTO tabla_accesorios (id, mascota, accesorio, talla, tipo, precio) VALUES (NULL, %s, %s, %s, %s, %s);"  

SQL_SELECT_ACCESORIOS ="SELECT * FROM tabla_accesorios"

SQL_BORRAR_ACCESORIOS = "DELETE FROM tabla_accesorios WHERE id = %s;"