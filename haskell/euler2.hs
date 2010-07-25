{-
 - Find the sum of all the even-valued terms in the sequence which do not exceed four million.
 -}

import Daentools.Sequences (fibs)

problem2 :: (Integral a) => a -> a
problem2 lim = sum $ filter even $ takeWhile (<lim) fibs

main :: IO ()
main = print $ problem2 4000000
