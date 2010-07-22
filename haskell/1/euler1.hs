module Euler1 where
import IO

multOf x y = x `mod` y == 0

problem1 :: (Integral a) => a -> a
problem1 x = sum [x | x <- [1 .. (x - 1)], x `multOf` 3 || x `multOf` 5 ]

main = do
    let answer = show $ problem1 1000 in putStrLn answer
