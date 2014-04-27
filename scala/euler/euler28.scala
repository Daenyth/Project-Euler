package euler

import Math.pow

object Euler28 {
  /*
   Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
    */

  def main(args: Array[String]) {
    /*
     For adding numbers in the diagonals of the spiral we can consider the
     spiral as a series of rings of numbers. Each ring will provide 4 numbers
     to the total. From the example we can observe that layer 1 (#2-9) is 3x3
     and the 4 numbers are separated by 1. For layer 2 (10-25) we see them
     spaced by 3 each. For the unshown 3rd layer, it would be 6x6 terminating
     at 36 and spaced by 5.

     We can generalize each layer of size N as providing 4 values spaced by
     2n-1, terminating at (2n+1)^2 and beginning at (2n)^2+1. Further,
     the terminating number will always be at an outside corner with this
     spiral method, so the numbers provided for layer N are:
     [ (n+2)^2, (n+2)^2 - 1*(2n), n^2 - 2*(2n), n^2 - 3*(2n) ]
     */

    val size = 1001
    /*
     if n = layer's number and
      2n-1 = size of the layer's side
      then size = 1001 means

      2n-1 = 1001
      2n = 1000
      n = 500th layer

      2n-1 = l
      2n = l - 1
      n = (l-1)/2
      */
     val n = (size - 1) / 2
     val total =
       (n to 1 by -1).flatMap { n =>
         val highest = pow(2 * n + 1, 2)
         (0 until 4).map { spacing =>
           highest - (spacing * 2*n)
         }
       } reduce { _ + _ }
     println(total.toInt + 1)
  }
}
