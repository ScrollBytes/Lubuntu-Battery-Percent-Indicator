# Lubuntu Battery Percent Indicator
This is a python script that shows a battery percent indicator applet for **Lubuntu 20.04**

![Screenshot](/screenshot.png)

### ⭐ Before you run the script:
This script requires the python module **[psutil](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst)** - run these commands to install it:
    
    sudo apt install python3-pip
    sudo pip3 install psutil


### ⭐ How to make the icon show correctly
It seems the lxqt-panel will only show icons from your current icon theme's folder located in "/usr/share/icons". Directly linking to an icon outside of this folder did not work.

![Screenshot2](/before-after.png)

The **icons.zip** file in this project contains a 24x24 svg image file for the numbers 1 to 100. 

**You must extract these images into your current icon theme's folder (inside the 24x24 directory).**

I use the *Numix Circle* icon theme. I used this command to open the file manager in root mode then pasted my icons inside.

    sudo pcmanfm-qt /usr/share/icons/Numix-Circle/24/panel

After moving the icons to that folder - reload the icon cache

    sudo update-icon-caches /usr/share/icons/*

Now lxqt-panel should see the icons and show them correctly.


### ⭐ Running the script on startup:

Make the script executable

    chmod +x /path/to/script/battery-percent-indicator.py
    
Test it in your terminal

    /path/to/script/battery-percent-indicator.py
    
Make it run on startup (Lubuntu 20.04)
1. Start Menu -> Preferences -> LXQt settings -> Session Settings
2. Click "Autostart" on left
3. Click "Add" button on right
4. Paste */path/to/script/battery-percent-indicator.py* in the "command" box
5. Type a name in the "name" box
5. Click OK
6. Reboot
