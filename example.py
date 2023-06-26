# ldap_example.py
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPException

def connect_to_ldap_server(host, port, user, password):
    try:
        # Crear una instancia del objeto `Server`
        s = Server(host, port=port, get_info=ALL)

        # Crear una instancia del objeto `Connection`
        c = Connection(s, 
                       auto_bind=True, 
                       user=user, 
                       password=password)
        
        # Imprimir información sobre el servidor LDAP
        print(s.info)

    except LDAPException as e:
        print(f"Error while connecting to LDAP server: {e}")
        return None

# Actualizar estos valores con los valores correctos para tu servidor y credenciales LDAP
host = 'localhost'
port = 389
user = 'cn=admin,dc=mydomain,dc=com'
password = 'password'

connect_to_ldap_server(host, port, user, password)
