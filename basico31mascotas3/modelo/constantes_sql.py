

SQL_INSERCION_ACCESORIO = "INSERT INTO tabla_accesorios (id, mascota, accesorio, talla, tipo, precio, ofertas, cliente, envio) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);" 

SQL_SELECT_ACCESORIOS ="SELECT  id, mascota, accesorio, tipo  FROM tabla_accesorios"

SQL_BORRAR_ACCESORIO = "DELETE FROM tabla_accesorios WHERE id = %s;"

SQL_OBTENER_ACCESORIO_POR_ID = "SELECT * FROM tabla_accesorios WHERE id = %s;"

SQL_GUARDAR_CAMBIOS_ACCESORIO = "UPDATE tabla_accesorios SET mascota = %s, accesorio = %s, talla= %s, tipo = %s, precio = %s, ofertas= %s, cliente = %s, envio = %s WHERE id  = %s;"