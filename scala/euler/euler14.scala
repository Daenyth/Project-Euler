package euler
import scala.collection.mutable
import Stream.cons

object Euler14 {
  val cache = mutable.Map[Long, Long]()

  def nextCollatz(n: Long): Long ={
    n % 2 match {
      case 0 => n / 2
      case 1 => 3 * n + 1
    }
  }

  def memoCollatz(n: Long): Long =
    cache.get(n) match {
      case Some(next) => next
      case None =>
        val next = nextCollatz(n)
        cache += (n -> next)
        next
    }

  def collatzChain(start: Long): Stream.Cons[Long] =
    cons(
      start,
      {
        val next = memoCollatz(start)
        if(next == 1)
          Stream.empty
        else
          cons(next, collatzChain(next))
      }
    )

  def chainLength(n: Long) = collatzChain(n).length

  def main(args: Array[String]) {
    val max = (1000000 to 2 by -1).flatMap { n =>
      print("\r" + n)
      if(cache.contains(n)) None
      else Some(n -> chainLength(n))
    }.maxBy(_._2)
    println()
    println(max)
  }
}
