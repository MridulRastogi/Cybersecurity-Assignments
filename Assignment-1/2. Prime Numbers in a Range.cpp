/*Write a C/C++ program to check whether
a string is palindrome or not.*/
#include<iostream>
using namespace std;
int main()
{
    int a,b,c,i,j;
    cout<<"Enter the range : ";
    cin>>a>>b;
    for(i=a;i<=b;i++)
    {
        c=0;
        for(j=2;j<=i/2;j++)
            if(i%j==0)
                c=1;
        if(c==0)
            cout<<i<<" ";
    }
    return 0;
}
