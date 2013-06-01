#!/usr/bin/env python2
# coding: utf-8
from __future__ import unicode_literals, division, print_function

import sys
from datetime import datetime

import pandas
import pandas.io.sql as psql
import sqlite3

import matplotlib
import matplotlib.pyplot as plt
import numpy

if len(sys.argv) != 2:
	print('Usage: ' + sys.argv[0] + ' /path/to/firefox/profile')
	print('Plot tab counts from a Firefox profile with the Tab Count Logger extension installed.')
	sys.exit(1)
profiledir = sys.argv[1]


def plot(log, xlabel):
	fig = plt.figure()
	tabaxes = fig.add_subplot(1, 1, 1)
	tabaxes.set_xlabel(xlabel)
	tabaxes.set_ylabel('Tabs')
	winaxes = tabaxes.twinx()
	winaxes.set_ylabel('Windows')
	
	tabplot, = tabaxes.plot(log.index, log['tabs'], label='Tabs', color='blue',
		marker=',', linestyle='None'
	)
	tabaxes.get_yaxis().label.set_color(tabplot.get_color())
	winplot, = winaxes.plot(log.index, log['windows'], label='Windows', color='red',
		marker=',', linestyle='None'
	)
	winaxes.get_yaxis().label.set_color(winplot.get_color())
	
	tablines, tablabels = tabaxes.get_legend_handles_labels()
	winlines, winlabels = winaxes.get_legend_handles_labels()
	tabaxes.legend(tablines + winlines, tablabels + winlabels, loc=0)
	fig.tight_layout()
	return fig


with sqlite3.connect(profiledir + "/tabCountLog.sqlite", detect_types=sqlite3.PARSE_DECLTYPES) as con:
	log = psql.read_frame('SELECT * FROM tabCountLog', con, index_col='timestamp')
	log_notime = psql.read_frame('SELECT * FROM tabCountLog', con)
	
	print('Found {0} data points'.format(log.shape[0]))
	print(log)
	print(log.head())
	print('...')
	print(log.tail())
	
	plot(log, 'Time')
	plot(log_notime, 'Observation number')
	plt.show()