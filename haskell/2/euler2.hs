{-
 - Find the sum of all the even-valued terms in the sequence which do not exceed four million.
 -}

fib a = fibs!!a

fibs :: (Num a) => [a]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

problem2 :: (Integral a) => a -> a
problem2 lim = sum $ filter even $ takeWhile (<lim) fibs

main :: IO ()
main = print $ problem2 4000000
