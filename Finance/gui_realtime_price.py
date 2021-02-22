import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import GridSpec
import matplotlib.ticker as mticker
from mplfinance.original_flavor import candlestick_ohlc
import datetime
import math
from realtime_stock_price import COMPANY

def main():
    fig = plt.figure()
    fig.patch.set_facecolor('#121416')
    gs = fig.add_gridspec(6,6)
    ax1 = fig.add_subplot(gs[0:4, 0:4])
    ax2 = fig.add_subplot(gs[0, 4:6])
    ax3 = fig.add_subplot(gs[1, 4:6])
    ax4 = fig.add_subplot(gs[2, 4:6])
    ax5 = fig.add_subplot(gs[3, 4:6])
    ax6 = fig.add_subplot(gs[4, 4:6])
    ax7 = fig.add_subplot(gs[5, 4:6])
    ax8 = fig.add_subplot(gs[4, 0:4])
    ax9 = fig.add_subplot(gs[5, 0:4])

    figure_design(ax1)
    plt.show()

def figure_design(ax):
    ax.set_facecolor('#091217')
    ax.tick_params(axis='both', labelsize=7, colors='white')
    ax.ticklabel_format(useOffset=False)
    ax.spines['bottom'].set_color('#808080')
    ax.spines['top'].set_color('#808080')
    ax.spines['left'].set_color('#808080')
    ax.spines['right'].set_color('#808080')

if __name__ == '__main__':
    main()