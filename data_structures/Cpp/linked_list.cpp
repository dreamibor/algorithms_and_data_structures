//
// Created by ZhangZhaoyu on 23/03/2017.
//
#include <iostream>
#include "linked_list.h"
using namespace std;

template <class T>
LinkedList<T>::LinkedList() {
  //head -> data = NULL;
  head -> next = NULL;
  length = 0;
}

template <class T>
void LinkedList<T>::print_list() {
  cout << length << endl;
}

int main() {
  LinkedList<int> my_linkedlist;
  my_linkedlist.print_list();
}
