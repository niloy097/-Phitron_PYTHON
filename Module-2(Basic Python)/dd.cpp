#include<bits/stdc++.h>
using namespace std;
int balance = 3000;
void change(string item, int price)
{
    cout << "Prev bal val: " << balance << endl;
    balance = balance - price;
    cout << "Balance  after bye: " << item << " " << balance << endl; 
}
int main()
{
    
    change("Sunglass", 1000);
    cout << balance << endl;
    return 0;
}