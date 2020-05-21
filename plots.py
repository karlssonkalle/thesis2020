# !pip install brewer2mpl
#Packages:
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
from collections import Counter

#Settings for all plots:
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

#Scatterplot count

# Version
print(mpl.__version__)  #> 3.0.0
print(sns.__version__)  #> 0.9.0

#PLOT1:
# Import Data
df = pd.read_csv('NAME OF INPUTFILE.CSV')
#df=df_full.sample(3000) #Use if wanting to sample

# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
sns.stripplot(df.topics, df.mediamentions, jitter=0.3, size=8, ax=ax, linewidth=.5, hue=df.Oa_status, alpha=0.6)
# Tweaks:
plt.title('Title of plot', fontsize=22)
plt.ylim(9,369)
plt.yticks(np.arange(10, 361, 25))
plt.grid(color='grey', which='major', axis='y', linestyle='dotted', alpha=0.6)
plt.show()

#PLOT2:
# Import Data
df = pd.read_csv('NAME OF INPUTFILE.CSV')

# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
sns.stripplot(df.Oa_status, df.mediamentions, jitter=0.3, size=8, ax=ax, linewidth=.5, hue=df.Oa_status, alpha=0.6)
y= df.mediamentions
# Tweaks:
plt.yticks(np.arange(min(y), max(y)+1, 25.0))
plt.title('Title of plot', fontsize=22)
plt.ylim(9,369)
plt.yticks(np.arange(10, 361, 25))
plt.grid(color='grey', which='major', axis='y', linestyle='dotted', alpha=0.6)
plt.show()
