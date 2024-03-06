{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2c8e93bd",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2024-03-05T19:54:17.718723Z",
     "start_time": "2024-03-05T19:54:17.685459Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        LOB  Price\n",
      "0    Mobile  97.86\n",
      "1  Internet  53.84\n",
      "2        TV  48.00\n",
      "3  Landline  61.59\n",
      "4      VoIP  24.97\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import random\n",
    "\n",
    "# Define the lines of business\n",
    "lobs = ['Mobile', 'Internet', 'TV', 'Landline', 'VoIP']\n",
    "\n",
    "# Generate random prices for each LOB\n",
    "prices = [random.uniform(20.0, 100.0) for _ in lobs]\n",
    "\n",
    "# Create a DataFrame\n",
    "df = pd.DataFrame(list(zip(lobs, prices)), columns=['LOB', 'Price'])\n",
    "\n",
    "# Optionally, format the Price column to two decimal places\n",
    "df['Price'] = df['Price'].map('{:,.2f}'.format)\n",
    "\n",
    "# Display the DataFrame\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "41dfd3a6",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2024-03-05T19:23:37.411044Z",
     "start_time": "2024-03-05T19:23:37.391258Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>LOB</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mobile</td>\n",
       "      <td>96.90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Internet</td>\n",
       "      <td>61.37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>TV</td>\n",
       "      <td>66.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Landline</td>\n",
       "      <td>81.08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>VoIP</td>\n",
       "      <td>84.14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        LOB  Price\n",
       "0    Mobile  96.90\n",
       "1  Internet  61.37\n",
       "2        TV  66.00\n",
       "3  Landline  81.08\n",
       "4      VoIP  84.14"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc17a666",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "hide_input": false,
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
