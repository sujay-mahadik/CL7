#include<stdio.h>
#include<math.h>

int gcd(int a, int b){
    if(b == 0)
        return a;
    return gcd(b, a % b);
}
int main(){

    double msg, p, q, n, phi, e, d, k;
    double eMsg, dMsg;

    //default p q
    
    p = 3;
    q = 7;

    //user defined p q
    
    // printf("Enter prime numbers: \n");
    // scanf("%d %d", &p, &q);

    n = p * q;
    phi = (p-1)*(q-1);

    //base e to start
    //e is public key for encryption
    e = 2;

    // co-prime e for phi
    while(e<phi){
        if(gcd(e, phi)==1)
            break;
        else
            e++;
    }
    printf("E is %lf\n", e);

    //k is any constant value which satisfies d * e = 1 + (k * phi)
    k = 2;

    //d is private key for decryption
    d = (1 + (k * phi)) / e;

    printf("Public Key (n, e) = (%lf, %lf)\n", n, e);
    printf("Private Key (n, d) = (%lf, %lf)\n", n, d);

    printf("Enter msg(int) to be encrypted: \n");
    scanf("%lf", &msg);

    //encryption
    eMsg = pow(msg, e);
    eMsg = fmod(eMsg, n);

    printf("Encrypted msg is: %lf\n", eMsg);

    //decryption
    dMsg = pow(eMsg, d);
    dMsg = fmod(dMsg, n);

    printf("Original msg is: %lf\n", dMsg);
    
return 0;
}