from ldap3 import Server, Connection, ALL

# Cambiar los detalles de estas credenciales por los correctos
ldap_server = 'localhost'  # El host del servidor LDAP
ldap_port = 389  # El puerto del servidor LDAP
ldap_user = 'cn=admin,dc=mydomain,dc=com'  # El usuario del servidor LDAP
ldap_password = 'password'  # La contraseña del servidor LDAP

server = Server(ldap_server, port=ldap_port, get_info=ALL)
conn = Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)

print(server.info)


