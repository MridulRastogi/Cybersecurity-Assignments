/*Write a C/C++ program that takes n number of command line arguments
and finds the least number. In case of invalid entered value,
prompt the user to enter another value.*/
#include<iostream>
using namespace std;
int main()
{
    int n,i,least;
    cin>>n;
    int a[n];
    for(i=0;i<n;i++)
        cin>>a[i];
    least = a[0];
    for(i=0;i<n;i++)
        if(least>a[i])
            least = a[i];
    cout<<"The least value is : "<<least;
    return 0;
}
