/*Write a C/C++ program that lists down all the
prime numbers in a range between a and b,
where a and b are two whole numbers.*/
#include<iostream>
#include<string>
using namespace std;
int main()
{
    int i,c=0;
    string s;
    cout<<"Enter a string : ";
    cin>>s;
    for(i=0;i<=s.length()/2;i++)
    {
        if(s[i]!=s[s.length()-i-1])
            c=1;
    }
    if(c==1)
        cout<<"Not a Palindrome String";
    else
        cout<<"Palindrome String";
    return 0;
}
