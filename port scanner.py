import socket

# 1.  Definimos o IP alvo e a porta que queremos testar
alvo = "scanme.nmap.org"
porta = 80

# 2. Criamos o socket (AF_INET = IPv4) | SOCK_STREAM = TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Definimos 1 segundo como tempo limite de resposta
s.settimeout(1.0)

# 4. Tentamos a conexão com o IP e a Porta
resultado = s.connect_ex((alvo, porta))

# 5. Se o resultado for 0, a porta respondeu!
if resultado == 0:
    print(f"Porta {porta} está ABERTA!")
else:
    print(f"Porta {porta} está FECHADA.")

# 6. Fechamos a conexão
s.close()