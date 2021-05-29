# 2D-deadfish
2D version of Deadfish~ esolang made by Wasif

# Introduction

It just adds some fancy 2D language features on top of traditional Deadfish~.

Imagine a normal program `io`. It increments accumulator, outputs it and terminates. Here's an elaboration how the interpreter reads the program.

The program is surrounded by EOF tokens.

```
EOF EOF EOF EOF
EOF  i   o  EOF
EOF EOF EOF EOF
```
The default direction of IP is set to right, and position is (1,1) meaning first token `i`. (`[]` denotes current position of IP)

```
EOF EOF EOF EOF
EOF [i]  o  EOF
EOF EOF EOF EOF
```

Then after executing first command, IP moves 1 step right,

```
EOF EOF EOF EOF
EOF  i  [o] EOF
EOF EOF EOF EOF
```
Then again executes current instruction and moves on,
```
EOF EOF EOF EOF
EOF  i   o  [EOF]
EOF EOF EOF EOF
```
But sadly IP has hit the EOF token. So the program terminates. Using the commands below we can manipulate the accumulator and direction of IP variously.

# Commands

- `i`: Increment accumulator
- `o`: Print accumulator as digit without trailing newline
- `d`: Decrement accumulator
- `c`: Square accumulator
- `w`: Print 'Hello, World!' without traling newline
- `h`: Terminate
- `<`: Change IP direction to left
- `>`: Change IP direction to right
- `v`: Change IP direction to down
- `^`: Change IP direction to up
- `~`: Reset accumulator to 0
- `{`: Execute commands inside brace block 10 times
- `}`: End the brace block
- `(`: Execute commands inside the parentheses block if accumulator is 0, and if not push the IP to the end of the parentheses block
- `)`: End the parentheses block
- `!`: Move IP to random position in current line

It can recieve integer input which is automatically set to the accumulator. If no input or invalid input is given accumulator defaults to 0.

# Examples
**Hello, World!**
```
w
```
**Truth machine**
```
(o^)>o<
```

*It is still remaining some development. Core interpreter is ready. Online interpreter and Debugger features are coming soon!**
