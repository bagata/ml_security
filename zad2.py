"""
        "Zrób `dataframe`, który na początek zawiera dwie kolumny:\n",
        "- **age** (losowe wartości od 15 do 50)\n",
        "- **weight** (losowe wartości od 50 do 80)"
"""

import pandas as pd
import random

a = {"age": pd.Series([random.randint(15,51)]) , "weight": pd.Series([random.randint(50, 81)])}
dframe= pd.DataFrame(a)
print(dframe)
