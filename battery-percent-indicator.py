#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

import signal ## needed for indicator

from gi.repository import GLib ## used to run code every x seconds

import psutil ## to get battery level

import math ## for rounding battery percent


## GLOBAL VARIABLES - these variables can be used inside ALL functions below -----

APPINDICATOR_ID = 'myappindicator'

## creates the indicator
indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'bpi-white-1', appindicator.IndicatorCategory.SYSTEM_SERVICES)

## END - GLOBAL VARIABLES -----





## main function
def main():
	
    ## indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'icon-name-here', appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu())
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	
	## get initial battery percent and show
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)
	
	percentCONVERTED = int(float(percent));

	## indicator.set_label(str(percentCONVERTED) + '%', '----')
	indicator.set_icon_full('bpi-white-' + str(percentCONVERTED) + '','')
	
	## indicator.set_label(str(percentCONVERTED) + '%', '----')
	
	## this is the timer that runs function below every x seconds
	GLib.timeout_add(60000, change_label, indicator)
    
	gtk.main()
	
	## END main function
	



## build function    
def build_menu():
    menu = gtk.Menu()
    
    ## menu item 1
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    ## end - menu item 1
    
    menu.show_all()
    return menu
	
	## END build function
	
	


## quit function - called from menu item click
def quit(source):
    gtk.main_quit()  
    
    ## END quit function
    
    
    

## change_label function - called at the beginning and repeats every x seconds
def change_label(ind_app):
	
	## get battery level
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)
	
	percentCONVERTED = int(float(percent));

	## indicator.set_label(str(percentCONVERTED) + '%', '----')
	indicator.set_icon_full('bpi-white-' + str(percentCONVERTED) + '','')
	
	## print('Percent Updated - ' + str(percentCONVERTED) + '')
	
	return True ## important - timer will stop if this is not here
	
	## END change label function
	
    


## linked to main function - IMPORTANT
if __name__ == "__main__":
    main()
