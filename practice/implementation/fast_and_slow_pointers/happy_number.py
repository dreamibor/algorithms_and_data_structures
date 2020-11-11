"""
Fast and slow pointers - Happy Number (medium)

Description:
Any number will be called a happy number if, after repeatedly replacing it 
with a number equal to the sum of the square of all of its digits, leads us 
to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, 
they will be stuck in a cycle of numbers which does not include ‘1’.

Example:
Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:
1. 2^​2 ​​+ 3​^​2​​ = 4 + 9 = 13
2. 1^​2 + 3^​2 = 1 + 9 = 10
3. 1^2 + 0^2​​ = 1 + 0 = 1

Notes:
1. The given number shall be positive.

Time Complexity - O(logN) - N is the total number of elements.
Space Complexity - O(1) - For two pointers.

LeetCode link: https://leetcode-cn.com/problems/happy-number/
"""

def calculate_square_sum(num: int) -> int:
    _sum = 0

    while num:
        # Python built-in function divmod (a, b) 
        # returns two numbers (a // b, a % b).
        num, digit = divmod(num, 10)
        _sum += digit * digit
    
    return _sum

def find_happy_number(num: int) -> bool:
    """ Solution - Fast and Slow Pointers
    To find a number is a happy number or not, we always end in a cycle. 
    If the number is a happy number, then the process will be stuck on 
    number 1, while if the number is not a happy number, then the process 
    will be stuck in a cycle with a set of numbers.

    We can use the same fast and slow pointers method for detecting linked 
    list cycle to find a cycle among a set of elements. We use fast and slow
    pointer to find the cycle and see if the cycle is stuck on number 1 
    (happy number) or some other number (not happy number).
    """
    slow = num
    # For fast != slow
    fast = calculate_square_sum(num)

    # Fast will reach 1 faster then slow.
    while fast != 1 and fast != slow:
        fast = calculate_square_sum(calculate_square_sum(fast))
        slow = calculate_square_sum(slow)

    return fast == 1

def find_happy_number_hash_table(num: int) -> bool:
    """ Solution - Hash Table
    When we generate the next number, we can check whether it's already 
    in the hash set, if it's not, then we add it into the hash set, if 
    it's already in the hash set, then we are in a loop.

    Time Complexity - O(logN)
    Space Complexity - O(logN)
    """
    numbers_seen = set()

    # When num == 1, then we shall terminate as 1's square sum will be 1.
    while num != 1 and num not in numbers_seen:
        numbers_seen.add(num)
        num = calculate_square_sum(num)

    return num == 1


if __name__ == "__main__":
    print(f"23 is a happy number? {find_happy_number(23)}")
    print(f"23 is a happy number? {find_happy_number_hash_table(23)}")
    print(f"12 is a happy number? {find_happy_number(12)}")
    print(f"12 is a happy number? {find_happy_number_hash_table(12)}")
    print(f"2 is a happy number? {find_happy_number(2)}")
    print(f"2 is a happy number? {find_happy_number_hash_table(2)}")
    print(f"19 is a happy number? {find_happy_number(19)}")
    print(f"19 is a happy number? {find_happy_number_hash_table(19)}")