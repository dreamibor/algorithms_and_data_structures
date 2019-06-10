#include <iostream>
#include <array>
using namespace std;

void bubble_sorting(int myarray[], int len)
{
  for (int i=len-1; i>0; i--)
  {
    for (int j=0; j<i; j++)
    {
      if (myarray[j] > myarray[j+1]) {
        int temp = myarray[j];
        myarray[j] = myarray[j+1];
        myarray[j+1] = temp;
      }
    }
  }
}

int main() {
  int myarray[] = {1, 5, 2, 7, 4};
  for(int i=0;i<5;i++){
    cout << myarray[i] << " ";
  }
  cout << endl;
  bubble_sorting(myarray, 5);
  // for(const auto &ele: myarray)
  //   cout << ele << "\n";
  for(int i=0;i<5;i++){
    cout << myarray[i] << " ";
  }
  cout << endl;
  return 0;
}
