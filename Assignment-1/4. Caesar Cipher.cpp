/*Write a C/C++ program to encrypt and decrypt the string using Caesar Cypher Algorithm. While
encrypting the given string, 5 is added to the ASCII value of the characters.
Similarly, for decrypting the string, 5 is subtracted from the ASCII value of the characters
to print an original string. Example - Input String - hello, Encrypted String - mjqqt*/
#include<iostream>
#include<string>
using namespace std;
int main()
{
    int i;
    char ch;
    string s,s2="";
    cout<<"Enter a string : ";
    getline(cin,s);
    cout<<"Choose the Operation : "<<endl<<"E for Encryption"<<endl<<"D for Decryption"<<endl<<"Q to Quit"<<endl;
    cin>>ch;
    switch(ch)
    {
        case 'E'|'e':   for(i=0;i<s.length();i++)
                        {
                            if((s[i]>=65 && s[i]<=85) || (s[i]>=97 && s[i]<=117))
                                s2.push_back(char(int(s[i])+5));
                            else if((s[i]>=86 && s[i]<=90)||(s[i]>=118 && s[i]<=122))
                                s2.push_back(char(int(s[i])-21));
                            else
                                s2.push_back(s[i]);
                        }
                        cout<<"Original String  : "<<s<<endl<<"Encrypted String : "<<s2;
        break;
        case 'D'|'d':   for(i=0;i<s.length();i++)
                    {
                        if((s[i]>=65 && s[i]<=69) || (s[i]>=97 && s[i]<=101))
                            s2.push_back(char(int(s[i])+21));
                        else if((s[i]>=70 && s[i]<=90)||(s[i]>=102 && s[i]<=122))
                            s2.push_back(char(int(s[i])-5));
                        else
                            s2.push_back(s[i]);
                    }
                    cout<<"Original String  : "<<s<<endl<<"Decrypted String : "<<s2;
        break;
        case 'Q'|'q': i = NULL;
        break;
        default:    cout<<"Enter a Valid Input";
    }
    return 0;
}
