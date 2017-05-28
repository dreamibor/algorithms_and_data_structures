#include <iostream>
#include <array>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <algorithm>


using namespace std;

void hi_array(const array<int, 5> &array) {
  cout << "The array size is: " << array.size() << endl;
}
int main(int argc, char const *argv[]) {
  // Vector
  vector<double> myvector;
  myvector = {9, 7, 3, 78};
  myvector.push_back(90);
  cout << "Element at index 0: " << myvector.at(0) << endl;
  cout << "Vector Size: " << myvector.size() << endl;
  sort(myvector.rbegin(), myvector.rend());
  for (const auto &element: myvector)
    cout << element << " ";
  cout << endl;
  cout << "Vector stack top: " << myvector.back() << endl;

  // Array
  array<int, 5> myarray;
  myarray = {1, 3, 5, 7, 9};
  cout << "Element at index 2: " << myarray.at(2) << endl;
  hi_array(myarray);

  // Stack
  stack<int> mystack;
  mystack.push(67);
  mystack.push(68);
  mystack.pop();
  cout << "Poped Element: " << mystack.top() << endl;
  cout << mystack.empty() << endl;

  // Queue
  queue<double> myqueue;
  myqueue.emplace(90.8);
  myqueue.push(78.65);
  myqueue.push(56.34);
  cout << "Front: " << myqueue.front() << " ";
  cout << "Back: " << myqueue.back() << " ";
  cout << endl;
  myqueue.pop();
  cout << "Front: " << myqueue.front() << " ";
  cout << "Back: " << myqueue.back() << " ";
  cout << endl;

  //Map
  map<int, string> my_map;
  my_map[1] = "one";
  my_map[2] = "two";
  my_map.insert(pair<int, string> (5, "five") );
  //my_map.insert(pair<int, string> (5, "six") );
  my_map[5] += "six";
  if(my_map.find(5) != my_map.end()) {
    cout << my_map.at(5);
  }
  cout << endl;

  // Unordered Map
  unordered_map<string, int> hello;
  hello.insert( {{"ORCL",100},{"GOOG",100}});
  cout << hello.at("ORCL") << endl;
  hello.hash_function();

  // Unordered Multimap
  unordered_multimap<string, int> multi_dict;
  multi_dict.insert( {{"ORCL",100},{"GOOG",100}});
  multi_dict.insert( {{"ORCL",200},{"GOOG",300}});
  for (auto &x:multi_dict){
    cout << "Multimap Keys:" << x.first << endl;
  }
  auto range = multi_dict.equal_range("GOOG");
  for (auto i = range.first; i != range.second; ++i)
  {
      std::cout << i->first << ": " << i->second << '\n';
  }


  // Set
  set<int> myset;
  int set_list[] = {10, 20, 30, 40};
  myset.insert(50);
  myset.insert(set_list, set_list + 4);
  set<int>::iterator it;
  for(it = myset.begin(); it != myset.end(); it++)
    cout << *it << " ";
  cout << endl;

  // Unordered_set
  unordered_set<string> colours = {"blue", "red", "green"};
  if (colours.find("red") != colours.end())
  {
    cout << "red finded!";
  }
  cout << endl;



  return 0;
}
