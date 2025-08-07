### The Fibonacci Sequence

The Fibonacci numbers are the numbers in the following integer sequence ($F_n$):
$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...$

The sequence is defined by the following recurrence relation:
$F_0 = 0$
$F_1 = 1$
$F_n = F_{n-1} + F_{n-2}$


### The Problem

Given a number, `prod`, we search for two consecutive Fibonacci numbers, $F_n$ and $F_{n+1}$, that satisfy the following condition:
$F_n * F_{n+1} = \text{prod}$

Your function should take an integer (`prod`) and return an array/tuple (check the function signature for your language) in the following format:

* If $F_n * F_{n+1} = \text{prod}$: `(F(n), F(n+1), true)`
* If no two consecutive Fibonacci numbers are found that satisfy the condition: `(F(n), F(n+1), false)`
    * Where $F_n$ is the smallest Fibonacci number such that $F_n * F_{n+1} > \text{prod}$.



### Examples

* **714** `> (21, 34, true)`
    (since $F_8 = 21$, $F_9 = 34$, and $21 * 34 = 714$)

* **800** `> (34, 55, false)`
    (since $F_8 = 21$, $F_9 = 34$, $F_{10} = 55$, and $21 * 34 < 800 < 34 * 55$)