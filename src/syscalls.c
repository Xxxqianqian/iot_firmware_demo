#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <sys/time.h>
#include <stdlib.h>
#include <stddef.h>

typedef char* caddr_t;

int _write(int file, const char *ptr, int len) {
    return len;
}

int _read(int file, char *ptr, int len) {
    return 0;    
}

int _close(int file) {
    return -1;
}

int _fstat(int file, struct stat *st) {
    st->st_mode = S_IFCHR;
    return 0;
}

int _isatty(int file) {
    return 1;
}

int _lseek(int file, int ptr, int dir) {
    return 0;
}

void _exit(int status) {
    while(1);   
}

void _kill(int pid, int sig) {
    (void)pid;
    (void)sig;
}

int _getpid(void) {
    return 1;
}

extern char _end; // Provided by linker script

caddr_t _sbrk(int incr) {
    static char *heap_end;
    char *prev_heap_end;

    if (!heap_end) {
        heap_end = &_end;
    }
    prev_heap_end = heap_end;
    heap_end += incr;
    return (caddr_t) prev_heap_end;
}
