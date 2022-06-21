# My-take-on-sorting-algorithms
Figuring out sorting algorithms without prior knowledge of their existence.

How do they work?

1. First solution is about getting the highest number and swapping its place with last number.
Next iteration loops list without it's last item, so on and so on.

2. Second solution compares each number to one on it's right. If it's bigger, then they swap places.
Process is complete if there were no changes made in one for loop iteration.

3. Third solution is about iterating every single integer from the lowest possible number on the list to the highest.
When items in list match iterates integers, they get placed in order. 
This method needs further improvements, so it stops looping sooner to be more efficient.
