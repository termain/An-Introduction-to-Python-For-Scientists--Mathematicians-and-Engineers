class MyVector(object):
  """A vector class that can contain any numeric type with addition and multiplication defined"""
  def __init__(self, input_list): #we make sure that our two addends, self and other are the same length. 
    """Initialize a MyVector from a list. Sets the length attribute and copies the list into the MyVector"""
    self.elements = input_list[:] #Using list slices to copy the input list
    self.length = len( self.elements )

  def __len__(self):
    """Return the length of the vector"""
    return( self.length )

  def __getitem__(self, index):
    """Return the vector element at index"""
    return( self.elements[index] )

  def __setitem__(self, index, value):
    """Set element index to value"""
    #notice that __setitem__() doesn't return anything. Instead, it alters the MyVector object
    self.elements[index] = value

  def __add__(self,other):
    """Addition for vectors"""
    if (len(self) != len(other) ):
      raise ArithmeticError, "Vector addends must be the same length"

    vector_sum = MyVector( [0]*len( self ) ) #allocate new vector that will hold the sum

    for index in range( len(self) ): #range returns a list of integers from zero to it's argument minus one
      vector_sum[index] = self[index]+other[index]

    return(vector_sum)

  def __radd__(self, other):
    """Addition for vectors with other sequence types when the vector is the right operand"""
    return( self + other )

  def __str__(self):
    """Return a string representation of the MyVector"""
    output_string = "["
    for index in range(len(self) - 1 ): #we don't want to print the last element just yet
        output_string = output_string + str( self[index] ) + "," #'+' concatenates strings
    #[-1] accesses the last elemetn of a sequence type. [-2] the second to last, and so on.
    output_string = output_string + str(self[-1]) + "]" #this way, we don't print a comma after the last element

    return output_string

  def __repr__(self):
    """Return a string that the interpreter uses to represent MyVector"""
    return str(self)
