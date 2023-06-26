from ldap3 import Server, Connection, ALL, Tls
import ssl

# Cambiar los detalles de estas credenciales por los correctos
ldap_server = 'localhost'  # El host del servidor LDAP
ldap_port = 389  # El puerto del servidor LDAP
ldap_user = 'cn=admin,dc=mydomain,dc=com'  # El usuario del servidor LDAP
ldap_password = 'password'  # La contraseña del servidor LDAP

# Añadir protocolo seguro
tls = Tls(validate=ssl.CERT_NONE)
server = Server(ldap_server, port=ldap_port, use_ssl=True, tls=tls)

conn = Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)

print(server.info)