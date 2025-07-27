## 🖼️ Picture Filtering for Charlie's Patience 🖼️

Alice and Bob are on a holiday, capturing many memories, but Charlie has a rule: he doesn't want to see the same motif repeated endlessly! He'll only sit through their photo session if each motif appears **at most N times**.

Luckily, they've encoded their motifs as numbers. Your task is to help them filter their list of motifs so that no number appears more than N times, all while **preserving the original order** of the motifs.

### The Challenge

Given a list of numbers and a maximum count `N`, create a new list containing each number from the input list at most `N` times, without changing the order of the elements.

### Examples

* If `N = 2` and the input list is `[1, 2, 3, 1, 2, 1, 2, 3]`:
    * You take `[1, 2, 3, 1, 2]` (at this point, 1 and 2 have appeared twice).
    * You drop the next `[1, 2]` because this would make 1 and 2 appear 3 times.
    * Then you take `3`.
    * The final result is `[1, 2, 3, 1, 2, 3]`.

* If `N = 1` and the input list is `[20, 37, 20, 21]`:
    * The result would be `[20, 37, 21]`.