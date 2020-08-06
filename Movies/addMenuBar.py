# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:20:34 2020

@author: m58527
"""
from tkinter import * 

#%% MENU BAR 
def CreateMenuBar(self,root):
        # CREATE MENU BAR
        self.menubar = Menu(root,font=("times new roman",15),activebackground="skyblue")
        # PUT MENU BAR ON ROOT WINDOW
        root.config(menu=self.menubar)
        
        # CREATE FILE MENU
        self.filemenu = Menu(self.menubar,font=("times new roman",12),activebackground="skyblue",tearoff=0)
        # ADD A 'RESET' COMMAND
        self.filemenu.add_command(label="Reset fields",accelerator="Ctrl+R",command=self.resetTableFunction)
        # ADD A SEPARATOR BETWEEN EXIT AND THE REST
        self.filemenu.add_separator()
        # ADD EXIT COMMAND
        self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
        # CREATE EDIT MENU
        self.editmenu = Menu(self.menubar,font=("times new roman",12),activebackground="skyblue",tearoff=0)
        # ADD A 'EXAMPLE' COMMAND
        self.editmenu.add_command(label="Example",accelerator="Ctrl+E")
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        
        # CREATE VIEW MENU
        self.viewmenu = Menu(self.menubar,font=("times new roman",12),activebackground="skyblue",tearoff=0)
        # ADD A 'EXAMPLE' COMMAND
        self.viewmenu.add_command(label="Example",accelerator="Ctrl+E")
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        
        # CREATE USERS WINDOW
        self.usermenu = Menu(self.menubar,font=("times new roman",12),activebackground="skyblue",tearoff=0)
        # ADD A 'EXAMPLE' COMMAND
        self.usermenu.add_command(label="Add User",accelerator="Ctrl+E")
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="Users", menu=self.usermenu)
        
        # CREATE SETTINGS WINDOW
        self.settingsmenu = Menu(self.menubar,font=("times new roman",12),activebackground="skyblue",tearoff=0)
        # ADD A 'Adjust max movies' COMMAND
        self.settingsmenu.add_command(label="Adjust Max Movies",accelerator="Ctrl+E",command=self.adjustMaxMovies)
        # ADD A 'Adjust max rate crit' COMMAND
        self.settingsmenu.add_command(label="Adjust Max Rating Criteria",accelerator="Ctrl+E",command=self.adjustMaxRateCriteria)
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="Settings", menu=self.settingsmenu)