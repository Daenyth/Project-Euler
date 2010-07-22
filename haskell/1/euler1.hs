module Euler1 where
import IO

problem1 :: (Integral a) => a -> a
problem1 x = sum [x | x <- [1 .. (x - 1)], x `mod` 3 == 0 || x `mod` 5 == 0 ]

main = do
    let answer = show $ problem1 1000 in putStrLn answer
