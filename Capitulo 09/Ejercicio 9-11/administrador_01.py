# 9-11. Imported Admin:
#           Start with your work from Exercise 9-8 (page 173).
#           Store the classes User, Privileges, and Admin in one module.
#           Create a separate file, make an Admin instance, and call show_privileges() to show that
#           everything is working correctly.

"""Archivo separado creando instancia y llamando metodo para comprobar funcionamiento"""

import administrador

super_admin = administrador.Admin("edwin", "chica", "palo", "098987876", "amo de casa",
                                  ["puede navegar en internet", "puede beber"])
super_admin.describir_usuario()
super_admin.privilegios.mostrar_privilegios()



