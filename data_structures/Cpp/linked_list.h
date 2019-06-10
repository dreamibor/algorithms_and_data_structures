//
// Created by ZhangZhaoyu on 23/05/2017.
//

#include <iostream>
using namespace std;


template <class T>
struct node{
  T data;
  node<T>* next;
};

template <class T>
class LinkedList{
private:
  node<T> * head;
  int length;

public:
  LinkedList();
  bool delete_element(int index);
  bool insert_element(node<T> *new_node, int position);
  void print_list();
  ~LinkedList() { cout << "Destroyed!" << endl; };
};
