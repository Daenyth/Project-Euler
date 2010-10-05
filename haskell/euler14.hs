{-
 - Which starting number, under one million, produces the longest collatz chain?
 -}

import Control.Arrow

collatz :: (Integral a) => a -> a
collatz 1 = 1
collatz x = if (odd x)
            then (3 * x + 1)
            else (x `div` 2)

collatzChain :: Int -> [Int]
collatzChain = terminate . iterate collatz
    where
        terminate (1:_) = [1]
        terminate (x:xs) = x:terminate xs

problem14 x = snd . maximum $ map (length . collatzChain &&& id) [1..x]

main = print $ problem14 1000000
