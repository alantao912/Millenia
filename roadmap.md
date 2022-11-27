# Roadmap


**Notes**

A rough roadmap.

Since it's much easier to implement a parse rule than the language implementation for it, the general heuristic we use is that **it is okay for the backend to implement a much smaller subset of what the parser can handle**.


Another principle: generally speaking, we should be fine with playing fast and loose with the type system's soundness (just crashing when something bad happens) w.r.t. the implementation. So for a while the language will be quite possible the first instance of an *ostensibly strongly-typed* language, one which claims to be strongly typed but is rather lax in practice.



## Milestone 1 - Basic Parsing

- [ ] parse rule for keywords
- [ ] parse rule for comments
- [ ] parse rules for primitives
    - [ ] integers
    - [ ] bools
    - [ ] floats
    - [ ] lists
    - [ ] strings
    - [ ] chinese numeral integers (optional) 


## Milestone 2 - Parse minimal featureset

- [ ] rule for variable declaration
- [ ] rule for assignment/update
- [ ] rule for if/then
- [ ] rule for func declaration
- [ ] (temporary) parse a built-in `print()` function


## Milestone 3 - Barebones implementation of Milestone 2

- [ ] PoC AST interpreter written in python
  - [ ] rudimentary type system (can be much more restricted compared to what we can parse)
  - [ ] impl. for built-in `print()`
  - [ ] impl. for bool/int/float/string




## Milestone 4 - Enhanced control flow parsing

- [ ] rule for `goto`
- [ ] rule for `while` and `loop`
- [ ] rule for `maybe do {} [...please]`
- [ ] rule for `do unless`


## Milestone 5 - Rich data structures implementation

We will be enhancing the PoC AST interpreter with the following 

- [ ] impl. tuples
- [ ] impl. lists
- [ ] impl. structs



## Milestone 6 - Perfomance Update

- [ ] rudimentary backend that outputs c code from generated AST




## Misc/Unassigned


- [ ] functions as values (closures right?), and representing them as types (i.e `fn[Point -> float]`)
- [ ] potentially doing something with exceptions/crashes/error handling
- [ ] implementing chinese to decimal conversion




