from water import daily_demand

def test_daily_demand_values():
  assert daily_demand(5000,100) == 500000

