# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:10:56 2020

@author: m58527
"""

import tkinter as tk
from tkinter import ttk
from functools import partial
import numpy as np
import pandas as pd
from addMenuBar import CreateMenuBar
import tkinter.filedialog as fd


#%% CREATE CLASS
class movieRatings:
    
    numberOfMovies = 1
    numberOfRateCriteria = 1
    maxNumMovies = 6
    maxNumRateCrit = 2
    
    global listOfPeople
    listOfPeople = ['Default']
    
    cellWidth = 15
    cellHeight = 5
    cellFontSize = 15
    
    windowWidth = 1200
    windowHeight = 800


    def __init__(self,root):
        
        global masterEntryArray
        masterEntryArray = [[None for i in range(self.maxNumRateCrit+2)] for j in range(self.maxNumMovies)]
        global masterValueArray
        masterValueArray = [[None for i in range(self.maxNumRateCrit+2)] for j in range(self.maxNumMovies)]
        masterValueArray[0][0] = 'Movies'
        masterValueArray[0][1] = 'Rating'
        
        self.root=root
                
        def setWindowStuff(self):
            # Title of the window
            self.root.title("Movie Rater")
            self.root.config(bg='red')
            # Set icon
            self.root.geometry(str(self.windowWidth)+'x'+str(self.windowHeight))
            
        setWindowStuff(self)
    
        #%% MENU BAR 
        
        CreateMenuBar(self,root)

                
        #%% CREATE FRAMES
        
        def createHeaderFrame(self):
            self.headerFrame = tk.Frame(root)
            self.headerFrame.pack(fill=tk.X,side=tk.TOP)
            self.headerFrame.config(bg='SkyBlue1',
                                    height = self.windowHeight/4)
        
        def createProfileFrame(self):
            self.profileFrame = tk.Frame(self.headerFrame)
            self.profileFrame.pack(side=tk.LEFT,fill=tk.Y)
            self.profileFrame.config(bg='Plum2',
                                     width=self.windowWidth/5)
        
        def createOptionsFrame(self):
            
            self.optionsFrame = tk.Frame(root)
            self.optionsFrame.pack(fill=tk.X,side=tk.TOP)
            self.optionsFrame.config(bg='blue',
                                    height = self.windowHeight/10)
        
        def createContentFrame(self):
            self.contentLabelFrame = tk.Frame(root)
            self.contentLabelFrame.pack(fill=tk.BOTH,side=tk.TOP)
            self.contentLabelFrame.config(bg='green',
                                          height=30)
            
            self.contentFrame = tk.Frame(root)
            self.contentFrame.pack(fill=tk.BOTH,side=tk.TOP,expand=tk.TRUE)
            self.contentFrame.config(bg='pink')
  
        def createAllFrames(self):
            
            createHeaderFrame(self)
            createProfileFrame(self)
            createOptionsFrame(self)
            createContentFrame(self)
            
        createAllFrames(self)


        #%% CONTENT FOR PROFILE FRAME
        
        self.addPersonLabel = tk.Label(self.profileFrame)
        self.addPersonLabel.pack(sid=tk.TOP,fill=tk.X)
        self.addPersonLabel.config(text='Logged in as:',bg='Skyblue1',relief='groove')

        self.choosePersonBox = ttk.Combobox(self.profileFrame)
        self.choosePersonBox.pack(side=tk.TOP,fill=tk.X)
        self.choosePersonBox.config(values=listOfPeople)
        
        self.addPersonButton = tk.Button(self.profileFrame)
        self.addPersonButton.pack(side=tk.TOP)
        self.addPersonButton.config(text='Add Person',command=self.addPersonFunction)

        #%% CONTENT FOR HEADER FRAME
        
        def headerFrameLabels(self):
            
            #welcome label
            self.welcomeLabel = tk.Label(self.headerFrame)
            self.welcomeLabel.pack(side=tk.TOP,fill=tk.X)
            self.welcomeLabel.config(text = 'Welcome to your own personl movie rater!')
            
            #instructions
            self.instructionsLabel = tk.Label(self.headerFrame)
            self.instructionsLabel.pack(fill=tk.X,side=tk.TOP)
            self.instructionsLabel.config(bg='SkyBlue1',
                                          text = ''''This GUI is a practice GUI made my James Gessel. It is built in python \
                                          and utilizes python libraries including pandas, tkinter, numpy, and scikit-learn. \
                                          It is mean to take in a list of movies and your personal rating system, and it will \
                                          output a list of recommended movies, and their predicted results, using your rating system.''',
                                          justify=tk.CENTER,
                                          font=('Arial',24,'bold'),
                                          wraplength=750)
            
        headerFrameLabels(self)

                
        #%% CONTENT FOR OPTIONS FRAME 
        
        def addOptionsContent(self):
                        
            self.addMovieButton = tk.Button(self.optionsFrame)
            self.addMovieButton.pack(expand=tk.TRUE,fill=tk.BOTH,side=tk.LEFT)
            self.addMovieButton.config(text='Add Movie', 
                                       command=self.addMovieFunction,
                                       bg='SeaGreen1')
            
            self.addRatingButton = tk.Button(self.optionsFrame)
            self.addRatingButton.pack(expand=tk.TRUE,fill=tk.BOTH,side=tk.LEFT)
            self.addRatingButton.config(text='Add Rating Criteria', command=self.addRatingFunction,
                                        bg='SeaGreen1')
            
            self.resetTableButton = tk.Button(self.optionsFrame)
            self.resetTableButton.pack(expand=tk.TRUE,fill=tk.BOTH,side=tk.LEFT)
            self.resetTableButton.config(text='Reset Table', command=self.resetTableFunction)
            
            self.saveDataButton = tk.Button(self.optionsFrame)
            self.saveDataButton.pack(expand=tk.TRUE,fill=tk.BOTH,side=tk.LEFT)
            self.saveDataButton.config(text='Save Data', command=self.saveTableFunction)
            
            self.saveFileButton = tk.Button(self.optionsFrame)
            self.saveFileButton.pack(expand=tk.TRUE,fill=tk.BOTH,side=tk.LEFT)
            self.saveFileButton.config(text='Save to file', command=self.saveFileFunction)
            
            self.runPredictionButton = tk.Button(self.optionsFrame)
            self.runPredictionButton.pack(expand=tk.TRUE,fill=tk.BOTH,side=tk.LEFT)
            self.runPredictionButton.config(text='Run Prediction', command=self.runPredictionFunction)   
            
            self.editExcelButton = tk.Button(self.optionsFrame)
            self.editExcelButton.pack(expand=tk.TRUE,fill=tk.BOTH,side=tk.LEFT)
            self.editExcelButton.config(text='Edit In Excel', command=self.editExcelFunction)
            
            self.loadExcelButton = tk.Button(self.optionsFrame)
            self.loadExcelButton.pack(expand=tk.TRUE,fill=tk.BOTH,side=tk.LEFT)
            self.loadExcelButton.config(text='Load from Excel', command=self.loadExcelFunction)
            
        addOptionsContent(self)

        
        #%% CONTENT FOR CONTENT FRAME
        
        def addContentContent(self):
            
            self.contentFrameLabel = tk.Label(self.contentLabelFrame)
            self.contentFrameLabel.pack(fill=tk.BOTH,expand=tk.TRUE,side=tk.TOP)
            self.contentFrameLabel.config(text='Please fill out the table below, then press save data',
                                          bg='DarkSlateGray1',
                                          relief='ridge')
            
            self.movieNameLabel = tk.Label(self.contentFrame)
            self.movieNameLabel.grid(row=0,column=0)
            self.movieNameLabel.config(text='Movie Name')
    
            self.movieRateCriteriaLabel = tk.Label(self.contentFrame)
            self.movieRateCriteriaLabel.grid(row=0,column=1)
            self.movieRateCriteriaLabel.config(text='Rating')
            
            # self.initialMovieEntry = tk.Entry(self.contentFrame,width=self.cellWidth,fg='blue',font=('Arial',self.cellFontSize,))
            # self.initialMovieEntry.grid(row=1,column=0)
            # masterEntryArray[1][0] = self.initialMovieEntry
            
            # self.initialRatingEntry = tk.Entry(self.contentFrame,width=self.cellWidth,fg='blue',font=('Arial',self.cellFontSize,))
            # self.initialRatingEntry.grid(row=1,column=1)
            # masterEntryArray[1][1] = self.initialRatingEntry

        addContentContent(self)
                           
    #%% MENU BAR FUNCTIONS, ETC
      
    def exit(self,*args):
        op = tk.messagebox.askyesno("WARNING","Your Unsaved Data May Be Lost!! \nWant to Exit?")
        if op>0:
            self.root.destroy()
        else:
            return
        
    def adjustMaxMovies(self):
        newMaxMovies = tk.simpledialog.askinteger('CHANGE MAX MOVIES','New maximum number of movies:')
        self.maxNumMovies = newMaxMovies-1
        
    def adjustMaxRateCriteria(self):
        newMaxRateCrit = tk.simpledialog.askinteger('CHANGE MAX RATING CRITERIA','New maximum number of rating criteria columns:')
        self.maxNumRateCrit = newMaxRateCrit-1
        
    #%% FUNCTIONS FOR PROFILE FRAME
    
    def addPersonFunction(self):
        self.nameToAdd = tk.simpledialog.askstring('Add New User','Please enter the name of the new user.')
        listOfPeople.append(self.nameToAdd)
        self.choosePersonBox.config(values=listOfPeople)

    #%% FUNCTIONS FOR HEADER FRAME
    
    #%% FUNCTIONS FOR OPTIONS FRAME
    
    #add movie row
    def addMovieFunction(self):
        if self.numberOfMovies+1>self.maxNumMovies:
            print('max number of movies reached')
            self.contentFrameLabel.config(text='Maximum number of movies reached.')
        else:
            #add new entry row
            self.contentFrameLabel.config(text='Added row.')
            for eachCol in np.arange(self.numberOfRateCriteria+1):
                _newEntry = tk.Entry(self.contentFrame)
                _newEntry.grid(row=self.numberOfMovies,column=eachCol)
                _newEntry.config(width=self.cellWidth,fg='blue',font=('Arial',self.cellFontSize,))
                masterEntryArray[self.numberOfMovies][eachCol] = _newEntry
            self.numberOfMovies += 1

    #add rate column
    def addRatingFunction(self):
        if self.numberOfRateCriteria>self.maxNumRateCrit:
            print('max number of rate cols reached')
            self.contentFrameLabel.config(text='Maximum number of rating criteria reached.')
        else:
            #add new entry cols
            self.contentFrameLabel.config(text='Added column.')
            for eachRow in range(self.numberOfMovies):
                _newEntry = tk.Entry(self.contentFrame)
                _newEntry.grid(row=eachRow,column=self.numberOfRateCriteria+1)
                _newEntry.config(width=self.cellWidth,fg='blue',font=('Arial',self.cellFontSize,))
                masterEntryArray[eachRow][self.numberOfRateCriteria+1] = _newEntry
            self.numberOfRateCriteria += 1


    def resetTableFunction(self):
        self.contentFrameLabel.config(text='Reset table.')
        self.contentFrame.destroy()
        self.contentFrame = tk.Frame(self.root)
        self.contentFrame.pack(fill=tk.BOTH,side=tk.TOP,expand=tk.TRUE)
        self.contentFrame.config(bg='pink',
                                 height = 50)
        
        self.movieNameLabel = tk.Label(self.contentFrame)
        self.movieNameLabel.grid(row=0,column=0)
        self.movieNameLabel.config(text='Movie Name')

        
        self.movieRateCriteriaLabel = tk.Label(self.contentFrame)
        self.movieRateCriteriaLabel.grid(row=0,column=1)
        self.movieRateCriteriaLabel.config(text='Rating')
        
        self.numberOfMovies = 1
        self.numberOfRateCriteria = 1
        
    def saveTableFunction(self):
        self.contentFrameLabel.config(text='Saving Table.')
        #read table
        for row in range(len(masterEntryArray)):
            for col in range(len(masterEntryArray[0])):
                print('Row',row,'Col',col,'entry',masterEntryArray[row][col])
                if masterEntryArray[row][col] is not None:
                    masterValueArray[row][col] = masterEntryArray[row][col].get()
        self.contentFrameLabel.config(text='Saved Table.')
        print(masterEntryArray)
        
    def saveFileFunction(self):
        self.contentFrameLabel.config(text='Saving to file.')
        saveAsFilePath = fd.asksaveasfile(filetypes=(('csv files','.csv')), defaultextension=(('.csv')))
        print(saveAsFilePath)
        # masterValueDF = pd.DataFrame(masterValueArray)
        # saveFilename = str(self.choosePersonBox.get())+'MovieFile.csv'
        # masterValueDF.to_csv(saveFilename)
        # self.contentFrameLabel.config(text='Saved to file.')
        
    def runPredictionFunction(self):
        self.saveTableFunction()
        print('run prediction')
        self.contentFrameLabel.config(text='Saved table, running prediction.')
        
    def editExcelFunction(self):
        self.saveTableFunction()
        self.contentFrameLabel.config(text='Opening in excel.')
        
    def loadExcelFunction(self):
        self.contentFrameLabel.config(text='Select a file to load.')
        self.getFilePath= fd.askopenfilename()
        print(self.getFilePath)
        if self.getFilePath.endswith('.csv'):
            loadedFileDF = pd.read_csv(self.getFilePath)
            masterValueArray = list(loadedFileDF)
            for row in range(len(masterEntryArray)):
                for col in range(len(masterEntryArray[0])):
                    if masterEntryArray[row][col] is not None:
                        masterEntryArray[row][col].delete(0,tk.END)
                        masterEntryArray[row][col].insert(0,masterValueArray[row][col])
                
            self.contentFrameLabel.config(text='Loaded values from excel.')
        else:
            fileTypeErrorMessage = tk.messagebox.showerror('File Type Error','File type is not .csv, please select different file')
            self.contentFrameLabel.config(text='Please select a csv file.')

    #%% FUNCTIONS FOR CONTENT FRAME
        
#%% MAIN FUNCTION

def main():
    #create parent window
    root = tk.Tk()
    app = movieRatings(root)
    root.mainloop()
  
#%% CALL MAIN

if __name__ == "__main__": main()