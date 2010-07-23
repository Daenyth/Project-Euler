{-
 -     Find the largest palindrome made from the product of two 3-digit numbers.
 -
 -     A palindromic number reads the same both ways.
 -     The largest palindrome made from the product of
 -     two 2-digit numbers is 9009 = 91 * 99.
 -}

isPalindrome :: (Show a) => a -> Bool
isPalindrome a = show a == reverse (show a)

problem4 :: Int
problem4 = maximum $ filter isPalindrome numbers
    where numbers = let numList = [100 .. 999] in [ x*y | x <- numList, y <- numList ]

main :: IO ()
main = print problem4
