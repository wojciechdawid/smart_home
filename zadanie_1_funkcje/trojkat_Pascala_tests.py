from trojkat_Pascala import pascal_triangle


def test_pascal_traiangle():
    actual = pascal_triangle(6)
    assert actual == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1]
    ]

def test_pascal_triangle_to_str():
    actual = pascal_triangle(7, to_str=True)
    assert actual == """       1       
      1 1      
     1 2 1     
    1 3 3 1    
   1 4 6 4 1   
  1 5 10 10 5 1  
 1 6 15 20 15 6 1 
"""
