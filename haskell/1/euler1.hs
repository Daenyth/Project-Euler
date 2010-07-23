multOf x y = x `mod` y == 0

-- Find the sum of all the multiples of 3 or 5 below 1000.
problem1 :: (Integral a) => a -> a
problem1 lim = sum [x | x <- [1 .. (lim - 1)], x `multOf` 3 || x `multOf` 5 ]

main = print $ problem1 1000
