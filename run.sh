#!/bin/sh
#p1type="human", p2type="minimax", p1_eval_type=0, p1_prune=False, p2_eval_type=0, p2_prune=False

# arguments
# p1type, p2type,  ---- p1_eval_type, p1_prune, p2_eval_type, p2_prune, p1_depth, p2_depth
echo "--- alphabeta v alphabeta 2 - 12 depth: tiles heuristic no pruning" > bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 0 0 0 2 2 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 0 0 0 4 4 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 0 0 0 6 6 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 0 0 0 8 8 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 0 0 0 10 10 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 0 0 0 12 12 >> bookkeeping.text

echo "--- alphabeta v alphabeta 2 - 12 depth: tiles heuristic w/ pruning" >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 0 0 2 2 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 0 0 4 4 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 0 0 6 6 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 0 0 8 8 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 0 0 10 10 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 0 0 12 12 >> bookkeeping.text

echo "--- alphabeta v alphabeta 2 - 12 depth: mobile heuristic no pruning" >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 0 1 0 2 2 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 0 1 0 4 4 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 0 1 0 6 6 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 0 1 0 8 8 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 0 1 0 10 10 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 0 1 0 12 12 >> bookkeeping.text

echo "--- alphabeta v alphabeta 2 - 12 depth: mobile heuristic w/ pruning" >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 1 1 2 2 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 1 1 4 4 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 1 1 6 6 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 1 1 8 8 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 1 1 10 10 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 1 1 12 12 >> bookkeeping.text

echo "--- tiles v mobile 2 - 8 depth: w/ pruning" >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 1 1 2 2 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 1 1 4 4 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 1 1 6 6 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 0 1 1 1 8 8 >> bookkeeping.text

echo "--- mobile v tiles 2 - 8 depth: w/ pruning" >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 0 1 2 2 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 0 1 4 4 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 0 1 6 6 >> bookkeeping.text
python3 GameDriver.py alphabeta alphabeta 1 1 0 1 8 8 >> bookkeeping.text