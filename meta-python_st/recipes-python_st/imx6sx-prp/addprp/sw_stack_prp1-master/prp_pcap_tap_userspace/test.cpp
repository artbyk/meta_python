#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
int stat;

int main(void)
{
int fd;
char buffer[2];
if((fd=open("prp_conf.txt", O_RDONLY))==-1) {
printf("Cannot open file.\n");
exit(1);
}
int ret = read(fd, buffer, 2);
if(buffer[0] == '1'){
    printf("Y");
}
if(buffer[0] == '0'){
    printf("N");
}
// printf("%i",buffer);
// if (read(fd, buffer, 100) !=100)
// printf ("Possible read error.");
// return 0;
}

// int main(){
//     // int pid = fork();
//     unsigned int microsecond = 1000000;
//     unsigned char buffer[1558];
//     int counter = 0;
    
//     // for(int i =-1;i<10;i++){
//     while(true){
//         if(read(STDIN_FILENO,buffer,1558) != 0){
//         if (buffer[0] == 'c') {
//             stat = isatty(0);
//             // usleep(1 * microsecond);
//             printf("YES");
//             printf("%i",stat);
//         }
//         if (buffer[0] == 'e') {
//             printf("%i",counter);
//             break;

//         }
//         }
//         else{
//             counter++;
//         }
//     }
//     // }
//     // printf("%i",pid);
// }
