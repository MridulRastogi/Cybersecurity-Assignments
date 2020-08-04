/*You are given a string (you need to take it input from user),
the task is to encrypt this string using # and $ symbols, alternatively.
While encrypting the message the encrypted format must repeat
the symbol as many times as the letter position in alphabetical order
(consider the string as case insensitive).*/
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int i,val;
    string s;
    char ch;
    cout<<"Enter a string : ";
    getline(cin,s);
    for(i=0;i<s.length();i++)
        s[i]=toupper(s[i]);
    for(i=0;i<s.length();i++)
    {
        val = int(s[i])-64;
        if(i%2==0 && s[i]>=65 && s[i]<=90)
            while(val--)
                cout<<"#";
        else if(i%2==1 && s[i]>=65 && s[i]<=90)
            while(val--)
                cout<<"$";
    }
    return 0;
}
