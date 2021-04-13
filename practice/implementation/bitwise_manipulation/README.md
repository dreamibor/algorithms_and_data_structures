# Bit Manipulation

Data in a computer is stored using binary format (0 or 1), so bit manipulation is operating on the binary data in the memory directly, since we don't need to convert the numbers to decimal numeral system back and forth, so we can accelerate the processing time.

## Bitwise Opertors

Basic bitwise operators:
|      Name     | Python operator |   Example   |
| :-----------: |:---------------:|:-----------:|
|      AND      |        &        |  1 & 0 = 0  |
|      OR       |        \|       |  1 \| 0 = 1 |
|      NOT      |        ~        |  ~1 = 0    |
|      XOR      |        ^        |  1 ^ 0 = 1  |
|   Left Shift  |        <<       |  1 << 1 = 2 |
|  Right Shift  |        >>       |  2 >> 1 = 1 |

XOR means Exclusive OR.

We can build compound operator with those bitwise operators, for example:

1. a &= b meaning a = a & b
2. a <<= n meaning a = a << n

Properties of XOR:
1. a ^ 0 = a
2. a ^ a = 0
3. a ^ b ^ a = b

High-level bit manipulation:
1. a & (a - 1) - removes the last 1-bit in a.

## Binary System
A number can be represented using **positional notation (进位制)**, and in a positional system, we need to know the **base**, which is the number of digits available to represent the number.
Human beings are more used to **base-ten numeral system**, which is also known as **decimal system**. Computers use **base-two numeral system**, or called **binary system**.

Check the bit-length of any integer number in Python:

``` Python
>>> (42).bit_length()
6
```

A byte or octet, comprises 8 bits, can store 256 distinct values. 

### Unsigned and Singed Integers
Integers in Python can have an infinite number of bits, the sign bit doesn’t have a fixed position. In fact, there’s no sign bit at all in Python!

For the bitwise NOT (~), it performs logical negation, which flips all the bits in the number.
For each bit of bitwise, it works as follows:
```
~a = 1 - a
```
For example, ~1 = 1 - 1 = 0.

However, we need to be careful about bitwise NOT in Python, since Python doesn't have sign bit natively. That means all numbers in Python have an implicit sign attached to them whether you specify one or not. 

For example:
| a          | ~a        |
| :--------: |:---------:| 
| 10011100_2 | 1100011_2 |
| 156_10     | 99_10     |

But in Python:
``` Python
>>> ~ 156
-157
```
Instead of the expected 99_10, you get a negative value.

### Binary Number Representations
#### Unsigned Integers
Python natively doesn't support unsigned numbers. To experiment with unsigned integers in Python, we can use `ctypes`:
``` Python
>>> from ctyptes import c_uint8 as unsigned_byte
>>> unsigned_byte(-42).value
214
```
#### Signed Integers
We can use a sign-magnitude to represent a signed integers, the other bits work the same as unsigned integers.
For example:

| Binary Sequence | Sign-Magnitude Value | Unsigned Value |
|:---------------:|:--------------------:|:--------------:|
| 00101010_2      | 42_10                | 42_10          |
| 10101010_2      | -42_10               | 170_10         | 

A zero on the leftmost indicates a positive (+) number while a one indicates a negative (-) number.

Binary representations of signed integers only make sense on fixed-length bit sequences. Otherwise, you couldn’t tell where the sign bit was. In Python, however, you can represent integers with as many bits as you like:

``` Python
>>> f"{-5 & 0b1111:04b}"
'1011'
>>> f"{-5 & 0b11111111:08b}"
'11111011'
```

Whether it’s four bits or eight, the sign bit will always be found in the leftmost position.

When you apply standard binary arithmetic to numbers stored in sign-magnitude, it may not give you the expected results
For example, adding two numbers with the same magnitude but opposite signs won’t make them cancel out:

| Expression | Binary Sequence | Sign-Magnitude Value |
|:----------:|:---------------:|:--------------------:|
| a          | 001010102       | 42_10                |
| b          | 101010102 	   | -42_10               | 
| a+b        | 110101002       | -84_10               | 

As we can see, the sum of 42 and -42 doesn’t produce zero. 
Also, the carryover bit can sometimes propagate from magnitude to the sign bit, inverting the sign and yielding an unexpected result.

#### Two's Complement
Two's complement - When finding bit sequences of negative values in two’s complement, the trick is to **add one to the result after negating the bits(取反加一)**.
For example:
00000001_2, we first negate the number to 11111110_2 (which is also called One's Complement), and then +1, resulting 11111111_2.

**This pushes the bit sequences of negative numbers down by one place**. As a side effect, the range of available values in two’s complement becomes asymmetrical, with a lower bound that’s a power of two and an odd upper bound. For example, an 8-bit signed integer will let you store numbers from -128_10 to 127_10 in two’s complement.

#### Big-Endian vs Little-Endian
Endianness (字节序) is the order or sequence of bytes of a word of digital data in computer memory. 

For example, for a 32-bit unsigned integer corresponding to 1969_10, it could be represented in binary format 00000000000000000000011110110001_2.

We can imagine memory as a one-dimensional tape consisting of bytes, then you’d need to break that data down into individual bytes and arrange them in a contiguous block. Some find it natural to start from the left end because that’s how they read, while others prefer starting at the right end:

| Byte Order    | Address N  | Address N+1 | Address N+2 | Address N+3 |
|:-------------:|:----------:|:-----------:|:-----------:|:-----------:|
| Big-Endian    | 00000000_2 | 00000000_2  | 00000111_2  | 10110001_2  |
| Little-Endian | 10110001_2 | 00000111_2  | 00000000_2  | 00000000_2  |

When bytes are placed from left to right, the most-significant byte is assigned to the lowest memory address. This is known as the **big-endian order**. Conversely, when bytes are stored from right to left, the least-significant byte comes first. That’s called little-endian order.

Check the system's endianness:
``` Python
>>> import sys
>>> sys.byteorder
'little'
```

You can’t change endianness, though, because it’s an intrinsic feature of your CPU architecture.
1. x86 (Intel and AMD) - little endian
2. Arm - big endian

Reference:
1. [Bitwise Operators in Python](https://realpython.com/python-bitwise-operators/#binary-number-representations)