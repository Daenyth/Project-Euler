module Daentools.Sequences (fib, fibs) where

fib a = fibs!!a

fibs :: (Num a) => [a]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
