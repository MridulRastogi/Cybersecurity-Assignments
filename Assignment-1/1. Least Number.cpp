/*Write a C/C++ program that takes n number of command line arguments
and finds the least number. In case of invalid entered value,
which contains characters other than digits then
prompt the user to enter another value.*/
#include<iostream>
#include<sstream>
#include<string>
using namespace std;
int main()
{
    int n,i,j,c,least;
    cin>>n;
    int a[n];
    string s[n];

    for(i=0;i<n;i++)
    {
        cin>>s[i];
        do
        {
            c=0;
            for(j=0;j<s[i].length();j++)
            {
                if(s[i][j]<48 || s[i][j]>57)
                    c=1;
            }
            if(c==1)
            {
                s[i] = "";
                cout<<"Enter again : ";
                cin>>s[i];
            }
        }
        while(c==1);
        a[i]=stoi(s[i]);
        //sscanf(s[i],"%d",&a[i]);
    }
    least = a[0];
    for(i=0;i<n;i++)
        if(least>a[i])
            least = a[i];
    cout<<"The least value is : "<<least;
    return 0;
}
