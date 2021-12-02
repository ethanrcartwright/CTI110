#PYT Final Project
#CTI-110
#Ethan Cartwright
#12/2/21
#

print(""" This python program is designed to find a user entered number, and find it in a list using binary search.
-------------------------------------------------------------
Binary Search is a search method that is intergral to many algorithims and is used today in other technologies. Binary search works by searching for a value by first getting the value and comparing it to the halfway point of the list. If the value is higher than the halfway point, the lower half of the list is discarded in the search and vice-versa. The program continues this until there is no values to the left or right of the value and returns the value to the user.
""")

def binary_search(sequence, item):
  begin_index = 0 #beginning of the index
  end_index = len(sequence) - 1 #userdefined end of the index

  while begin_index <= end_index:
    midpoint = begin_index + (end_index - begin_index) // 2
    #this line of code finds the midpoint by adding the beginning index and the remaining items in the sequence and then dividing it by two. 
    midpoint_value = sequence[midpoint]
    #this finds the midpoint in the sequence

    if midpoint_value == item:
      return midpoint # if the midpoint equals the item we are trying to find, return the midpoint

    elif item < midpoint_value:
      end_index = midpoint - 1
    

    else:
      begin_index = midpoint + 1

  return None

def main():
  sequence = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22]
  print("Choose an item between 0 and 22: ", end = '')
  item = int(input(" "))
  print("If returned 'None', that means the item was not in the sequence. If a number is returned, that number indicates where it is located in the list.")
  print(binary_search(sequence, item))
  print(sequence)



if __name__ ==  "__main__":
  main()