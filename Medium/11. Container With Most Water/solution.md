# Problem: Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

# Solution:

Use 2-pointers to calculate the area of the water
area = (r - l) \* min(height[l], height[r])

Then move the cursor on the lower edge, because the lower edge limits the area. If you can increase the height, you can get a larger area.
