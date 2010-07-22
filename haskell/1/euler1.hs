module Euler1 (wanted, problem1, main) where
import IO

wanted :: (Integral a) => a -> Bool
wanted x
    | x `mod` 3 == 0 = True
    | x `mod` 5 == 0 = True
    | otherwise = False

problem1 :: (Integral a) => a -> a
problem1 x = sum $ filter wanted [1 .. (x - 1)]

main = do
    let answer = show $ problem1 1000 in putStrLn answer
