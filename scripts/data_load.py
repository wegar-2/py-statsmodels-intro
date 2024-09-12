from pathlib import Path

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd


def load_gus_monthly_inflation_data() -> pd.DataFrame:
    data = pd.read_csv(
        Path(__file__).parent.parent / "data" / "monthly_GUS_data_EoY2023.csv",
        sep=";", decimal=",", index_col=None, na_values="."
    )
    data["yearmon"] = pd.to_datetime(data["yearmon"], format="%d.%m.%Y")
    data = data.set_index("yearmon")
    data["mom"] = data["CPI_inflation_MoM"] - 100
    data["yoy"] = data["CPI_inflation_YoY"] - 100
    return data[["mom", "yoy"]]
