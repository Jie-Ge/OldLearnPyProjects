import pandas as pd
import numpy as np

target_list = pd.DataFrame([[123, '12:00:10', 4],
                            [456, '15:52:12', 5],
                            [252, '32:45:69', 6]], columns=['id', 'appl_sbm_tm', 'shu'])

order_info = pd.DataFrame([[123, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]], columns=['id', 'time_order', 'ss'])

target_list = target_list[['id', 'appl_sbm_tm']].merge(order_info[['id', 'time_order']], on='id', how='left')

print(target_list)







