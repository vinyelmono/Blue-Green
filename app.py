import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler

def crear_Servidor(version, puerto):

    class Manejador(BaseHTTPRequestHandler):

        def do_GET(self):

            if self.path == '/health':
                respuesta = f"OK - Version: {version}"
                codigo = 200
            else:
                respuesta = f"Aplicacion ejecutandose - version {version}"
                codigo = 200

            self.send_response(codigo)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(respuesta.encode())

        def log_message(self, formato, *argumentos):
            return  # Desactivar el registro de solicitudes en consola

    return HTTPServer(('127.0.0.1', puerto), Manejador)


# Funcion Principal
def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--version', required=True)
    parser.add_argument('--puerto', type=int, required=True)

    argumentos = parser.parse_args()

    servidor = crear_Servidor(argumentos.version, argumentos.puerto)

    print(f"Servidor {argumentos.version} en el puerto {argumentos.puerto}")

    servidor.serve_forever()


if __name__ == '__main__':
    main()