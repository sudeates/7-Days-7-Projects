import socket
import os

def start_server():
    HOST, PORT = '127.0.0.1', 8080
    
    server_socket = socket.socket(socket.AF_INET, socket.socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    
    print(f"Gelişmiş Sunucu hazır: http://{HOST}:{PORT}")

    while True:
        client_conn, addr = server_socket.accept()
        request = client_conn.recv(1024).decode()
        
        if not request:
            continue

        # İstek satırını parçala (Örn: GET /index.html HTTP/1.1)
        header = request.split('\n')[0]
        filename = header.split()[1]

        # Ana dizin isteğini index.html'e yönlendir
        if filename == '/':
            filename = '/index.html'

        filepath = f"./public{filename}"

        try:
            # Dosyayı binary modda oku (resimler için önemli)
            with open(filepath, 'rb') as f:
                content = f.read()
            
            response = "HTTP/1.1 200 OK\r\n"
            # Basit bir MIME type kontrolü
            if filename.endswith(".html"): response += "Content-Type: text/html\r\n"
            elif filename.endswith(".css"): response += "Content-Type: text/css\r\n"
            elif filename.endswith(".jpg"): response += "Content-Type: image/jpeg\r\n"
            
            response += f"Content-Length: {len(content)}\r\n\r\n"
            
            client_conn.sendall(response.encode() + content)
        except FileNotFoundError:
            # Dosya yoksa 404 gönder
            response = "HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>404 Sayfa Bulunamadi</h1>"
            client_conn.sendall(response.encode())

        client_conn.close()

if __name__ == "__main__":
    start_server()