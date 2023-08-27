import subprocess
from getpass import getpass

# Lista de rutas y sus correspondientes usuarios y contraseñas
rutas_usuarios_contrasenas = {
    (r"\\servidor1\carpeta", "usuario1", "contraseña1"),
    (r"\\servidor2\carpeta", "usuario2", "contraseña2"),
    # Agrega más rutas, usuarios y contraseñas según sea necesario
}

# Solicitar al usuario ingresar su nombre de usuario
usuario = input("Ingrese su nombre de usuario: ")

# Solicitar al usuario ingresar su contraseña de forma segura
contrasena = getpass("Ingrese su contraseña: ")

# Intentar mapear las unidades de red para el usuario
unidades_mapeadas = []
for ruta, usuario_ruta, contrasena_ruta in rutas_usuarios_contrasenas:
    if usuario_ruta == usuario and contrasena_ruta == contrasena:
        # Comando para mapear la unidad de red
        comando = f'net use {ruta} /user:{usuario_ruta} {contrasena_ruta}'
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if "The command completed successfully." in resultado.stdout:
            unidades_mapeadas.append(ruta)

# Mostrar unidades mapeadas
if unidades_mapeadas:
    print("Unidades de red mapeadas:")
    for unidad in unidades_mapeadas:
        print(unidad)
else:
    print("No se encontraron unidades de red mapeadas para el usuario y contraseña proporcionados.")

# Esperar a que el usuario presione Enter para continuar
input("Presione Enter para cerrar el programa...")

# Eliminar las unidades mapeadas y las credenciales
for unidad in unidades_mapeadas:
    subprocess.run(f'net use {unidad} /delete', shell=True, capture_output=True)
