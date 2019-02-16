#include <iostream>

int main() 
{
  using F = void(*)();
  F fn = (F)-1;
  fn();
}