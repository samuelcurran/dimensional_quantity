from hypothesis import strategies as st
from dimnum import DimensionalQuantity as dq

DQ_strategy = st.builds(dq, st.integers(),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5))

for _ in range(10):
    print(DQ_strategy.example())
