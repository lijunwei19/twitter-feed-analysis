#include <vector>
#include <string>
#include <stdio.h>     
#include <iostream> 
using std::vector;
using std::string;

// function 1:   int sum_square_digitals(int x)   -- give abc integer return a*a+b*b+c*c
// function 2:   int count(int*p, int x)        ---- give array address and x, if x is already in array return 0, else return 1 
// function 3:   void print_lib(int *p, int x)  ---- give array address and length print out array elements
// function 4:   bool is_happy(int x)          ----- give a digital to judge if it is happy number
int sum_square_digitals(int x)
{   
  //printf("x is %d\n",x );
  int quotient=1;
  int sum=0;
  int remain[10]={0}; // must be static int//
  int i =1;
  while (quotient!=0){
    remain[i-1]=x%10;
    quotient=x/10;
    x=quotient;
    //printf("i is %d, quotient is %d,remain is %d\n",i ,quotient,remain[i-1]);
    i++;
  }
  for (int i=0; i<=9; ++i){
    sum=sum+remain[i]*remain[i];
  }
  return sum;
}
//##################################################################################
int count(int*p, int x){
  for (int i=0; *(p+i)!=0; ++i){
    if (*(p+i)==x){
      return 0;
    }
  }
  return 1;
}
//##################################################################################
void print_lib(int *p, int x){

  printf("this is lib :\n");

  for (int i=0;i<=x;++i){
  //  printf("%d  ", *(p+i) );
  }

}
//##################################################################################
bool is_happy(int x){
    int sum_digital;
    int lib[50]={0};  // 0 is flag  checking the end of library. no sum of power equal to zero except zero.
    sum_digital=sum_square_digitals(x);
    int i=0;
    int m=count(lib,sum_digital);
    while(m){
      lib[i]=sum_digital;
      i++;
      sum_digital=sum_square_digitals(sum_digital);
      m=count(lib,sum_digital);
    }
    //printf("repeat number is %d\n",sum_digital);
    if (sum_digital==1){
      return true; 
    }
    return false;
}
//##################################################################################

double product_of_positives(vector<double>) {

}

int product_of_positives(vector<int>) {

}

vector<int> proper_divisors(int n) {

}

string add(const string& num1, const string& num2) {
  
}

// delete main before submit code
int main(){
 // put code here
bool x = is_happy(13);
 std::cout << x << std::endl;
  return 0;
}