# 9-12. Multiple Modules:
#           Store the User class in one module, and store the Privileges and Admin classes in a separate module.
#           In a separate file, create an Admin instance and call show_privileges() to show that everything is still
#           working correctly.

from modulos2 import Admin

mi_admin = Admin("andres", "botero", "palocabildo", "234234234", "futbolista", ["puede crear jugadores",
                                                                                "puede borrar jugadores",
                                                                                "puede crear equipos"])
mi_admin.describir_usuario()
mi_admin.privilegios.mostrar_privilegios()