#include <iostream>

int main() 
{
  using F = void(*)();
  F fn = (F)5;
  fn();
}