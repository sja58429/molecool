import molecool
import numpy as np 

def test_calculate_distance():
    
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])
    
    expected_distance = 2
    
    calculate_distance = molecool.calculate_distance(r1,r2)
    
    assert expected_distance == calculate_distance