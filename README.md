# muh language

## Language Spec

Basic syntax
  - Semicolons and braces.
  - Comments

Primitives:
  - integer number type
  - floating point number type
  - Booleans
  - Arraylist
  - string
  - Tuple


Control Flow:
  - do {...} unless(p);
  - do {...} unless(p) { (happens when p is true) ... }
  - maybe do, please (default 50% chance of execution, each please increases likelihood by a factor of 5%, capped at 99%)
  - while loop
  - functions
  - if-else (hidden easter egg)
  - goto-labels


Module System:
  - Every file is a "module". [file].[identifier] to access value
  - Imperative code is only allowed in functions. At the top level only declarations such as variable, struct, functions are allowed.
  - Entry point must have a main function.
    
## Language syntax

### Basic syntax

#### Comments
Comments will be marked with `//`, the entire rest of the line will be marked as a comment.

#### Block comments
Block comments will be demarcated by `/*` `*/`


#### Semicolon terminated statements

By default all single line statements must be terminated with a semicolon

```
<statement>;
```


### keywords

- 'int'
- 'float'
- 'string'
- 'bool'
- 'true'
- 'false'
- 'do'
- 'unless'
- 'please'
- 'maybe'
- 'while'
- '->'
- 'fn'
- 'ret'
- 'struct'
- 'goto'
- 'loop'
### primitives

ints:
```
1
100
100_000_103
0x932423
chinese character integer constants

四百八十五 -> 485

```
Base Chinese Numbers:
    零一二三四五六七八九十百千万亿

Array literal:

```
[]
[1, 2]
["a" * 5] => ["a", "a", "a", "a", "a"]
```

String literal:

strings are utf-8 by default

```
"asdf"
"\n\t"
"一二三四五六七八九十"
```

Tuple:

```
// () empty tuple disallowed b/c alan said so
(1, 2)
("a", 2, [1, 2]) // heterogenous bby
```


boolean:

```
bool x = true;
bool f = false;
```


### identifiers

All identfiers must be alphanumeric or underscore, cant start with number `[a-zA-Z][0-9]`

```
a
abc1
a2b3
```


### variable decl


```
<type> <typename>

int my_number;
float my_float;
```

### compound decl + assignment

int my_number = 3;
float my_float = 4.5;

### function decl

```
fn <func_name>(<type_name> <name>, <type_name> <name>, ...) -> <ret_type> {
    <code block>
}

fn name(int a, string b) -> bool {

}

```

### struct decl

```
struct My_struct {
    int i;
    int b;
}

My_struct name = {0, 1};
My_struct name = {i = 0, b = 1};
```

### probabilistic structures
```
maybe do {
    <statements>
}

maybe do {
    <statements>
} please, please, please, ...;
```


### control flow

#### branches
```
do {
// executes if p is false
<statements>
} unless(p) {
// executes if p is true
<statements>
}
```

#### unconditional jump
The following demarcates a section of code.
<label_name> :

goto <label_name>;
will unconditionally jump code execution toward the label name.

#### loop
```
while (p) {
    <statements>
}
loop {
    <statements>
}
```