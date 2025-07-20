def max_list(lst):
  max_element = lst[0]
  l = len(lst)
  iterate_limit = l//2 if l%2==0 else (l//2)+1
  if all(isinstance(x,int) for x in lst):
    # return max(lst)
    for i in range(iterate_limit):
      if lst[i] > max_element:
        max_element = lst[i]
      if lst[l-i-1] > max_element:
        max_element = lst[l-i-1]
    print(max_element)
      
  else:
    print("This list contains non numberic numbers")

def min_list(lst):
  min_element = lst[0]
  l = len(lst)
  iterate_limit = l//2 if l%2==0 else (l//2)+1
  if all(isinstance(x,int) for x in lst):
    # return max(lst)
    for i in range(iterate_limit):
      if lst[i] < min_element:
        min_element = lst[i]
      if lst[l-i-1] < min_element:
        min_element = lst[l-i-1]
    print(min_element)
      
  else:
    print("This list contains non numberic numbers")

def reverse_dict(dic):
  print({v:k for k,v in dic.items()})

def freq_count(lst):
  d=dict()
  for i in lst:
    d[i] =d.get(i,0)+1
  print(d)

max_list([1,3,5,4,2])
min_list([5,3,1,4,2])
reverse_dict({1:True,2:False})
freq_count([1,1,1,1,1,2,2,2,2,22,2,3,3,3,3,3,3,4,4,4,4,4,4,55,23432,6575,3143])