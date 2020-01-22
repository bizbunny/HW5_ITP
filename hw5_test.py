
>>> from hw5 import *

##### Problem 1 #####

Rock, Paper, Scissors is a two-player game in which each player chooses one of three items. 
If both players choose the same item, the game is tied. 
Otherwise, the rules that determine the winner are:
(a) Rock always beats Scissors (Rock crushes Scissors)
(b) Scissors always beats Paper (Scissors cut Paper)
(c) Paper always beats Rock (Paper covers Rock)
Implement function rps(p1Choice, p2Choice) that takes the choice ('R', 'P', or 'S') of player 1 and the choice of player 2,
and RETURNS 1 if player 1 wins, 2 if player 2 wins, or 0 if there is a tie.

>>> rps('R', 'P')
2
>>> rps('P', 'S')
2
>>> rps('R', 'R')
0
>>> rps('S', 'P')
1
>>> rps('P', 'R')
1


##### Problem 2 #####

Write a function isPrime(n) that takes in a number n and RETURNS True if n is a prime number, otherwise False.

A number is prime if it is only evenly divisible by 1 and itself. 
7 is prime because 7/1 and 7/7 are the only integer results possible.
10 is not prime becuase 10/5=2.

Hint: use the modulo (%) operator to check if n%i==0 for any i between 2 and n (including 2). 
If it is, then n is evenly divisible by i and therefore not prime

>>> isPrime(7)
True
>>> isPrime(10)
False
>>> isPrime(90823)
True
>>> isPrime(99733)
True
>>> isPrime(99735)
False


##### Problem 3 #####

Write a function that playerHasLastInitial(filename, char) that takes in a file name and a single letter as input 
and RETURNS True if a player on the roster has a last name beginning with that character, otherwise False.
We will reuse the cubsRoster.csv we used in hw3.
We want to avoid loading the whole file into memory, so use a while loop and the file readline() method, NOT the readlines() or read() methods

>>> playerHasLastInitial('cubsRoster.csv', 'A')
True
>>> playerHasLastInitial('cubsRoster.csv', 'J')
False
>>> playerHasLastInitial('cubsRoster.csv', 'V')
False
>>> playerHasLastInitial('cubsRoster.csv', 'Z')
True


##### Problem 4 #####

Write a function maxFactorial(n) that takes a number n and RETURNS the largest number whose factorial value is <= n.
For example, if n is 15, the answer is 3 because 4! is 24>15 and 3! is 6<=15

>>> maxFactorial(15)
3
>>> maxFactorial(25)
4
>>> maxFactorial(362882)
9
>>> maxFactorial(3628800)
10
>>> maxFactorial(1307674368100)
15

