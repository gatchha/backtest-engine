from engine import engine


prix = [100,102]
positions = [1,1]
def test_basic():
    assert abs(engine([1,1], [100,102], 0, 0)[0].iloc[1] - 0.02) < 1e-6
   
 

