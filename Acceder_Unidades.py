import string
import subprocess
from tkinter import messagebox
import tkinter as tk
import psutil

# Arreglo de unidades mapeadas
unidades_mapeadas = []

# Constantes de rutas de las unidades
ruta_scanner = r"\\192.168.233.9\scanner"
ruta_gerencia = r"\\192.168.233.9\Gerencia"
ruta_admin = r"\\192.168.233.9\Admin"
ruta_capacitaciones = r"\\192.168.233.9\Capacitaciones"
ruta_procesales = r"\\192.168.233.9\Op-Procesales"
ruta_bogota = r"\\192.168.233.9\A-Bogota"
ruta_colpatria = r"\\192.168.233.9\A-Colpatria"
ruta_popular = r"\\192.168.233.9\A-Popular"
ruta_serfinanza = r"\\192.168.233.9\A-Serfinanza"
ruta_comercial = r"\\192.168.233.9\Comercial"
ruta_juridico = r"\\192.168.233.9\juridico"
ruta_manuales = r"\\192.168.233.9\Manual_Y_Politicas"

# Constantes de usuarios y contraseñas
usuario_admon = "admon"
contra_admon = "admon"
usuario_cbogota = "cbogota"
contra_cbogota = "cbogota"
usuario_jbogota = "jbogota"
contra_jbogota = "jbogota"
usuario_ccolpatria = "ccolpatr"
contra_ccolpatria = "ccolpatr"
usuario_jcolpatria = "jcolpatr"
contra_jcolpatria = "jcolpatr"
usuario_cpopular = "cpopular"
contra_cpopular = "cpopular"
usuario_jpopular = "jpopular"
contra_jpopular = "jpopular"
usuario_cserfinanza = "cserfina"
contra_cserfinanza = "cserfina"
usuario_jserfinanza = "jserfina"
contra_jserfinanza = "jserfina"
usuario_gerencia = "gerencia"
contra_gerencia = "gerencia"

# Lista de rutas y sus correspondientes usuarios y contraseñas
unidades_red = {
    # Usuario Administrativo
    "A:": {"ruta": ruta_scanner, "usuario": usuario_admon, "contrasena": contra_admon},
    "B:": {"ruta": ruta_capacitaciones, "usuario": usuario_admon, "contrasena": contra_admon},
    "C:": {"ruta": ruta_admin, "usuario": usuario_admon, "contrasena": contra_admon},
    "D:": {"ruta": ruta_procesales, "usuario": usuario_admon, "contrasena": contra_admon},
    "E:": {"ruta": ruta_gerencia, "usuario": usuario_admon, "contrasena": contra_admon},
    "AAE:": {"ruta": ruta_manuales, "usuario": usuario_admon, "contrasena": contra_admon},
    # Usuario Comercial Bogota
    "F:": {"ruta": ruta_scanner, "usuario": usuario_cbogota, "contrasena": contra_cbogota},
    "G:": {"ruta": ruta_comercial, "usuario": usuario_cbogota, "contrasena": contra_cbogota},
    "H:": {"ruta": ruta_capacitaciones, "usuario": usuario_cbogota, "contrasena": contra_cbogota},
    "I:": {"ruta": ruta_procesales, "usuario": usuario_cbogota, "contrasena": contra_cbogota},
    "J:": {"ruta": ruta_bogota, "usuario": usuario_cbogota, "contrasena": contra_cbogota},
    "AAF:": {"ruta": ruta_manuales, "usuario": usuario_cbogota, "contrasena": contra_cbogota},
    # Usuario Comercial Colpatria
    "K:": {"ruta": ruta_scanner, "usuario": usuario_ccolpatria, "contrasena": contra_ccolpatria},
    "L:": {"ruta": ruta_comercial, "usuario": usuario_ccolpatria, "contrasena": contra_ccolpatria},
    "M:": {"ruta": ruta_capacitaciones, "usuario": usuario_ccolpatria, "contrasena": contra_ccolpatria},
    "N:": {"ruta": ruta_procesales, "usuario": usuario_ccolpatria, "contrasena": contra_ccolpatria},
    "O:": {"ruta": ruta_colpatria, "usuario": usuario_ccolpatria, "contrasena": contra_ccolpatria},
    "AAG:": {"ruta": ruta_manuales, "usuario": usuario_ccolpatria, "contrasena": contra_ccolpatria},
    # Usuario Comercial Popular
    "P:": {"ruta": ruta_scanner, "usuario": usuario_cpopular, "contrasena": contra_cpopular},
    "Q:": {"ruta": ruta_comercial, "usuario": usuario_cpopular, "contrasena": contra_cpopular},
    "R:": {"ruta": ruta_capacitaciones, "usuario": usuario_cpopular, "contrasena": contra_cpopular},
    "S:": {"ruta": ruta_procesales, "usuario": usuario_cpopular, "contrasena": contra_cpopular},
    "T:": {"ruta": ruta_popular, "usuario": usuario_cpopular, "contrasena": contra_cpopular},
    "AAH:": {"ruta": ruta_manuales, "usuario": usuario_cpopular, "contrasena": contra_cpopular},
    # Usuario Comercial Serfinanza
    "U:": {"ruta": ruta_scanner, "usuario": usuario_cserfinanza, "contrasena": contra_cserfinanza},
    "V:": {"ruta": ruta_comercial, "usuario": usuario_cserfinanza, "contrasena": contra_cserfinanza},
    "W:": {"ruta": ruta_capacitaciones, "usuario": usuario_cserfinanza, "contrasena": contra_cserfinanza},
    "X:": {"ruta": ruta_procesales, "usuario": usuario_cserfinanza, "contrasena": contra_cserfinanza},
    "Y:": {"ruta": ruta_serfinanza, "usuario": usuario_cserfinanza, "contrasena": contra_cserfinanza},
    "AAI:": {"ruta": ruta_manuales, "usuario": usuario_cserfinanza, "contrasena": contra_cserfinanza},
    # Usuario Jurídico Bogota
    "Z:": {"ruta": ruta_scanner, "usuario": usuario_jbogota, "contrasena": contra_jbogota},
    "AAB:": {"ruta": ruta_juridico, "usuario": usuario_jbogota, "contrasena": contra_jbogota},
    "AA:": {"ruta": ruta_capacitaciones, "usuario": usuario_jbogota, "contrasena": contra_jbogota},
    "AB:": {"ruta": ruta_procesales, "usuario": usuario_jbogota, "contrasena": contra_jbogota},
    "AC:": {"ruta": ruta_bogota, "usuario": usuario_jbogota, "contrasena": contra_jbogota},
    "AAJ:": {"ruta": ruta_manuales, "usuario": usuario_jbogota, "contrasena": contra_jbogota},
    # Usuario Jurídico Colpatria
    "AD:": {"ruta": ruta_scanner, "usuario": usuario_jcolpatria, "contrasena": contra_jcolpatria},
    "AE:": {"ruta": ruta_juridico, "usuario": usuario_jcolpatria, "contrasena": contra_jcolpatria},
    "AF:": {"ruta": ruta_capacitaciones, "usuario": usuario_jcolpatria, "contrasena": contra_jcolpatria},
    "AG:": {"ruta": ruta_procesales, "usuario": usuario_jcolpatria, "contrasena": contra_jcolpatria},
    "AH:": {"ruta": ruta_colpatria, "usuario": usuario_jcolpatria, "contrasena": contra_jcolpatria},
    "AAK:": {"ruta": ruta_manuales, "usuario": usuario_jcolpatria, "contrasena": contra_jcolpatria},
    # Usuario Jurídico Popular
    "AI:": {"ruta": ruta_scanner, "usuario": usuario_jpopular, "contrasena": contra_jpopular},
    "AJ:": {"ruta": ruta_juridico, "usuario": usuario_jpopular, "contrasena": contra_jpopular},
    "AK:": {"ruta": ruta_capacitaciones, "usuario": usuario_jpopular, "contrasena": contra_jpopular},
    "AL:": {"ruta": ruta_procesales, "usuario": usuario_jpopular, "contrasena": contra_jpopular},
    "AM:": {"ruta": ruta_popular, "usuario": usuario_jpopular, "contrasena": contra_jpopular},
    "AAL:": {"ruta": ruta_manuales, "usuario": usuario_jpopular, "contrasena": contra_jpopular},
    # Usuario Jurídico Serfinanza
    "AN:": {"ruta": ruta_scanner, "usuario": usuario_jserfinanza, "contrasena": contra_jserfinanza},
    "AO:": {"ruta": ruta_juridico, "usuario": usuario_jserfinanza, "contrasena": contra_jserfinanza},
    "AP:": {"ruta": ruta_capacitaciones, "usuario": usuario_jserfinanza, "contrasena": contra_jserfinanza},
    "AQ:": {"ruta": ruta_procesales, "usuario": usuario_jserfinanza, "contrasena": contra_jserfinanza},
    "AR:": {"ruta": ruta_serfinanza, "usuario": usuario_jserfinanza, "contrasena": contra_jserfinanza},
    "AAM:": {"ruta": ruta_manuales, "usuario": usuario_jserfinanza, "contrasena": contra_jserfinanza},
    # Usuario Gerencia
    "AS:": {"ruta": ruta_scanner, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AT:": {"ruta": ruta_gerencia, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AU:": {"ruta": ruta_admin, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AV:": {"ruta": ruta_capacitaciones, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AW:": {"ruta": ruta_procesales, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AX:": {"ruta": ruta_bogota, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AY:": {"ruta": ruta_colpatria, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AZ:": {"ruta": ruta_popular, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AAA:": {"ruta": ruta_serfinanza, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AAC:": {"ruta": ruta_comercial, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AAD:": {"ruta": ruta_juridico, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
    "AAN:": {"ruta": ruta_manuales, "usuario": usuario_gerencia, "contrasena": contra_gerencia},
}


# Función para buscar una letra de unidad disponible
def buscar_letra_disponible():
    letras_usadas = set()
    for unidad in string.ascii_uppercase:  # Letras de A a Z
        try:
            resultado = subprocess.run(f'net use {unidad}:', shell=True, capture_output=True, text=True)
            if "Nombre local" in resultado.stdout:
                letras_usadas.add(unidad)
        except subprocess.CalledProcessError:
            pass  # La letra no está en uso

    letras_disponibles = [letra for letra in reversed(string.ascii_uppercase) if letra not in letras_usadas]
    return letras_disponibles[0] if letras_disponibles else None


# Función para cerrar los procesos específicos
# def cerrar_procesos():
#     # Obtener una lista de todos los procesos en ejecución
#     for proc in psutil.process_iter():
#         try:
#             pinfo = proc.as_dict(attrs=['pid', 'name'])
#             if any(programa.lower() in pinfo['name'].lower() for programa in ['winword', 'excel', 'powerpnt', 'acrobat', 'explorer']):
#                 proc.terminate()  # Terminar el proceso de manera amigable
#                 print(f"Proceso {pinfo['name']} terminado.")
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass


# Función para manejar el cierre de la ventana
def cerrar_ventana():
    if messagebox.askokcancel("Cerrar", "¿Estás seguro de que deseas cerrar el programa?"):
        # cerrar_procesos()
        eliminar_unidades_mapeadas()
        ventana.destroy()

def cerrar_sesion():
    if messagebox.askokcancel("Cerrar Sesión", "¿Estás seguro de que deseas cerrar la sesión?"):
        # cerrar_procesos()
        eliminar_unidades_mapeadas()
        entry_usuario.config(state="normal")
        entry_contrasena.config(state="normal")
        boton_ejecutar.config(state="active")
        boton_sesion.config(state="disabled")
        entry_usuario.delete(0, tk.END)
        entry_contrasena.delete(0, tk.END)


# Función para eliminar unidades mapeadas al finalizar
def eliminar_unidades_mapeadas():
    for unidad in unidades_mapeadas:
        subprocess.run(f'net use {unidad}: /delete', shell=True, capture_output=True)
    unidades_mapeadas.clear()

def ejecutar_programa():
    # Solicitar al usuario ingresar su nombre de usuario
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Desactivar campos de entrada
    entry_usuario.config(state="disabled")
    entry_contrasena.config(state="disabled")
    boton_ejecutar.config(state="disabled")
    boton_sesion.config(state="active")

    # Antes de mapear nuevas unidades, desconecta las conexiones previas al mismo servidor
    for unidad, datos in unidades_red.items():
        servidor = datos["ruta"].split("\\")[2]  # Obtén el nombre del servidor
        subprocess.run(f'net use /delete /y \\\\{servidor}', shell=True, capture_output=True, text=True)

    # Conectar a unidades del usuario
    for unidad, datos in unidades_red.items():
        ruta = datos["ruta"]
        usuario_ruta = datos["usuario"]
        contrasena_ruta = datos["contrasena"]

        if usuario_ruta == usuario and contrasena_ruta == contrasena:
            letra_disponible = buscar_letra_disponible()
            # Comando para mapear la unidad de red
            if letra_disponible:
                comando = f'net use {letra_disponible}: {ruta} /user:{usuario_ruta} {contrasena_ruta}'
                resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
                if "Se ha completado el comando correctamente." in resultado.stdout:
                    unidades_mapeadas.append(letra_disponible)

    # Mostrar mensaje de éxito
    if unidades_mapeadas:
        unidades_mapeadas_str = ", ".join(unidades_mapeadas)
        messagebox.showinfo("Éxito", f"Unidades mapeadas correctamente: {unidades_mapeadas_str}")
    else:
        messagebox.showwarning("Advertencia",
                               "No se encontraron unidades de red mapeadas para el usuario y contraseña proporcionados.")
        # cerrar_ventana()

#Creación interfaz de usuario
# Crear ventana
ventana = tk.Tk()
ventana.title("Mapeo de Unidades de Red")

# Establecer el tamaño inicial de la ventana (ancho x alto)
ventana.geometry("400x150")

# Deshabilitar el redimensionamiento horizontal y vertical
ventana.resizable(False, False)

# Campos de entrada para usuario y contraseña
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

label_contrasena = tk.Label(ventana, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.pack()

# Crear un contenedor para los botones dentro del contenedor principal
contenedor_botones = tk.Frame(ventana)
contenedor_botones.pack(side=tk.TOP, pady=10)

# Botón para ejecutar el programa
boton_ejecutar = tk.Button(contenedor_botones, text="Ejecutar", command=ejecutar_programa)
boton_ejecutar.pack(side=tk.LEFT, padx=5, pady=10)

# Botón para cerrar la sesión
boton_sesion = tk.Button(contenedor_botones, text="Cerrar Sesión", command=cerrar_sesion)
boton_sesion.pack(side=tk.LEFT, padx=5, pady=10)
boton_sesion.config(state=tk.DISABLED)

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Iniciar el ciclo de la ventana
ventana.mainloop()
