#CN/NAME : #30 SORIANO, MARRIANE AUDREY F.
SECTION : 9 BALINGKILAT
DATE : 08/12/2026

Computational Thinking Exercise: "Smart Vending Machine"

  Main Problem: 
The new vending machine that was installed is inefficient and has a lot of defects. It sometimes gives the wrong change, doesn't work properly when multiple students use it, gives the wrong item and can't track inventory properly.

  Possible Sub Problems:
1. The vending machine sometimes gives the wrong change.
2. The vending machine doesn't notify the buyer or anyone when an item has run out.
3. When a buyer presses a button, the vending machine gives the buyer the wrong item.
4. The vending machine becomes slow after multiple uses. 

  For each sub-problem, apply CT skills:

1. Algorithm - Running a program check and fixing errors within it can help avoid errors when the machine computes for a user’s amount of change.
2. Pattern Recognition - The machine can recognize the pattern of the item being unavailable once it has reached a quantity of 0. The machine can display an out of stock text to notify the user that the item is unavailable
3. Abstraction - Learning why the machine gives the wrong item to the buyer once can help us fix the whole thing.
4. Decomposition - The machine might be malfunctioning due to complex/unclear instructions. Decomposition would help to simplify the processes for the machine to avoid malfunctioning.


  Pseudocode : 
  
START

Check the price of the item
Check the amount of money the buyer gave
Calculate the correct amount of change to be given to the buyer
IF Given change = Correct change THEN
  Change is correct
  END
ELSE 
  Change is incorrect
  Find Problem
IF Problem is the dispenser THEN
  change dispenser
IF Problem is coin sensor THEN
  change sensor
IF Problem is program THEN
  fix program

END
