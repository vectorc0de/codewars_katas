## 🎯 Finding the Longest Consecutive Strings 🎯

You're given an **array (list) of strings**, `strarr`, and an **integer**, `k`. Your mission is to find and return the **first longest string** that's formed by concatenating `k` consecutive strings from `strarr`.

### Example Scenario

Let's look at an example to make this clear:

`strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]`, `k = 2`

We'll concatenate `k` (2) consecutive strings from the array:

* **"tree" + "foling"** = "treefoling" (length: 10)
* **"foling" + "trashy"** = "folingtrashy" (length: 12)
* **"trashy" + "blue"** = "trashyblue" (length: 10)
* **"blue" + "abcdef"** = "blueabcdef" (length: 10)
* **"abcdef" + "uvwxyz"** = "abcdefuvwxyz" (length: 12)

In this case, two concatenated strings are the longest with a length of 12: "folingtrashy" and "abcdefuvwxyz". Since "folingtrashy" appeared first in the original sequence, that's our answer.

Therefore, `longest_consec(strarr, 2)` should return **"folingtrashy"**.

### Another Example

`longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)` should return **"abigailtheta"**.

### Important Considerations

* Let `n` be the length of the input string array.
* If `n` is `0` (the array is empty), or if `k` is greater than `n` (`k > n`), or if `k` is less than or equal to `0` (`k <= 0`), your function should return an **empty string (`""`)**.

*Note: **Consecutive strings** means they follow one after another in the array without any interruption.*