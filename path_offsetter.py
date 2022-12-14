# -*- coding: utf-8 -*-

from inspect import getfile
from re import T
import numpy as np
import json
import tkinter
from tkinter import * 
from tkinter.filedialog import askopenfilename

edit_or_combine_test = 1
cam_to_edit = None 
consecutive = None
x_offset = None
y_offset = None
z_offset = None
edit_pan_tilt = None
pan = None
tilt = None
name = None
series_num =None
start = None
end = None
number_of_paths = None
filename = None


def set_value(value):
  global edit_or_combine_test
  edit_or_combine_test = value
  root.destroy()
  
def set_value_cams():
  global cam_to_edit
  cam_to_edit = cam.get()
  root.destroy()

def set_consecutive(value):
  global consecutive
  consecutive = value
  root.destroy()

def getXYZ():
  global x_offset ,y_offset, z_offset
  x_offset = float(x.get())
  y_offset = float(y.get())
  z_offset = float(z.get())
  root.destroy()

def pan_tilt_ask(value):
  global edit_pan_tilt
  edit_pan_tilt = value
  root.destroy()

def getPT():
  global pan, tilt
  pan = float(p.get())
  tilt = float(t.get())
  root.destroy()
  
def getFilename():
  global name
  name = file.get()
  root.destroy()

def getSections():
  global series_num
  series_num = int(sections.get())
  root.destroy()

def getStartEnd():
  global start, end
  start = int(st.get())
  end = int(en.get())
  root.destroy()

def getPaths():
  global number_of_paths
  number_of_paths = int(path_num.get())
  root.destroy()

def Close():
  root.destroy()


root = Tk()
root.eval('tk::PlaceWindow . center')
f = Frame(root)
Button(f, text='Edit a path',command=lambda *args: set_value("a")).pack(side = LEFT, padx = 10, pady = 5)
Button(f, text='Combine paths',command=lambda *args: set_value("b")).pack(side = LEFT, padx= 10, pady = 5)
Button(f, text='Invert a path',command=lambda *args: set_value("c")).pack(side = LEFT, padx= 10, pady = 5)
label = Label(root, text = "Choose what you would like to do!")
label.pack()
f.pack()
root.mainloop()

  
#EDITING PATHS
if edit_or_combine_test == "a":

  root = Tk()
  root.withdraw()
  filename = askopenfilename()
  root.destroy()


  #Check valid .cproj file
  while True:
    if filename.endswith('.cproj'):
      break
    else:
      print("Sorry, that file is not a COPIS path, please choose another file\n")
      root = Tk()
      root.withdraw()
      filename = askopenfilename()
      root.destroy()

  

  # reading the data from the file
  with open(filename) as f:
    path_file = f.read()

  # reconstructing the data as a dictionary
  path = json.loads(path_file)

  #get the length of the imaging path (in pose sets)
  poses = (len(path['imaging_path']))


  root = Tk()
  
  root.attributes('-topmost',True)
  f=Frame(root)
  label = Label(root, text = "If you would like to edit only a single camera \n enter its index, if not leave blank.").pack(side = TOP, pady = 5)
  cam = Entry(root)
  cam.pack(pady = 5)
  Button(root, text = "Continue", command=lambda *args: set_value_cams()).pack(side = BOTTOM, pady = 5)
  root.eval('tk::PlaceWindow . center')
  root.mainloop()

  #cam_to_edit = input("If you would like to edit only a single camera enter its index, if not enter 'n'.\n")
  
  #check the camera index or n value from input
  while True:
    if cam_to_edit == "0" or cam_to_edit == "1" or cam_to_edit == "2" or cam_to_edit == "3" or cam_to_edit == "4" or cam_to_edit == "5" or cam_to_edit == "":
      break
    else:
      root = Tk()
      f=Frame(root)
      label = Label(root, text = "Sorry, your input was not valid, enter a camera index (0-5) or n").pack(side = TOP, pady = 20)
      cam = Entry(root)
      cam.pack(pady = 20)
      Button(root, text = "Continue", command=lambda *args: set_value_cams()).pack(side = BOTTOM, pady = 20)
      root.eval('tk::PlaceWindow . center')
      root.mainloop()

  if cam_to_edit != "":

    root = Tk()
    f= Frame(root)
    label = Label(root, text = "Do you wish to edit...")
    Button(f, text = "All poses for this camera?", command=lambda *args: set_consecutive("a")).pack(side = LEFT, padx = 10, pady =10)
    Button(f, text = "Certain sections of poses?", command=lambda *args: set_consecutive("b")).pack(side = RIGHT, padx = 10, pady = 10)
    label.pack(pady = 10)
    f.pack()
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

    #editing all for this cam
    if consecutive == "a":
      cam_to_edit = int(cam_to_edit)

      root = Tk()
      Label(root, text = "Enter your X, Y, and Z Offsets and press Submit").grid(row = 0, sticky= N)
      Label(root, text = "X Offset").grid(row = 1, sticky = W)
      Label(root, text = "Y Offset").grid(row = 2, sticky = W)
      Label(root, text = "Z Offset").grid(row = 3, sticky = W)
      x=Entry(root)
      y=Entry(root)
      z=Entry(root)
      x.grid(row = 1, column = 0)
      y.grid(row = 2, column = 0)
      z.grid(row = 3, column = 0)
      Button(root, text = "Submit", command=lambda *args: getXYZ()).grid(row = 5, column = 0)
      root.eval('tk::PlaceWindow . center')
      root.mainloop()

      root = Tk()
      f= Frame(root)
      label = Label(root, text = "Do you wish to fix pan and tilt?")
      Button(f, text = "Yes", command=lambda *args: pan_tilt_ask("y")).pack(side = LEFT, padx = 10, pady =10)
      Button(f, text = "No", command=lambda *args: pan_tilt_ask("n")).pack(side = RIGHT, padx = 10, pady = 10)
      label.pack(pady = 10)
      f.pack()
      root.eval('tk::PlaceWindow . center')
      root.mainloop()

      #edit_pan_tilt = input("Would you like to fix pan and tilt? y/n\n")

      if edit_pan_tilt == "y":
        root = Tk()
        Label(root, text = "Enter your pan and tilt values and press Submit").grid(row = 0, sticky= N)
        Label(root, text = "Pan").grid(row = 1, sticky = W)
        Label(root, text = "Tilt").grid(row = 2, sticky = W)
        p=Entry(root)
        t=Entry(root)
        p.grid(row = 1, column = 0)
        t.grid(row = 2, column = 0)
        Button(root, text = "Submit", command=lambda *args: getPT()).grid(row = 5, column = 0)
        root.eval('tk::PlaceWindow . center')
        root.mainloop()

      for i in range(0,poses):

        cams = len(path['imaging_path'][i])

        for j in range(0, cams):

          if path['imaging_path'][i][j][0]['device'] == cam_to_edit:

            new_x = float(path['imaging_path'][i][j][0]['args'][0][1]) + x_offset
            new_y = float(path['imaging_path'][i][j][0]['args'][1][1]) + y_offset
            new_z = float(path['imaging_path'][i][j][0]['args'][2][1]) + z_offset

            path['imaging_path'][i][j][0]['args'][0][1] = str(new_x)
            path['imaging_path'][i][j][0]['args'][1][1] = str(new_y)
            path['imaging_path'][i][j][0]['args'][2][1] = str(new_z)

            if edit_pan_tilt == "y":
              path['imaging_path'][i][j][0]['args'][3][1] = str(pan)
              path['imaging_path'][i][j][0]['args'][4][1] = str(tilt)

    #editing sections
    else: 

      root = Tk()
      Label(root, text = "How many sections would you like to adjust?").grid(row = 0, sticky= N)
      Label(root, text = "Number of Sections").grid(row = 1, sticky = W)
      sections=Entry(root)
      sections.grid(row = 1, column = 0)
      Button(root, text = "Submit", command=lambda *args: getSections()).grid(row = 2, column = 0)
      root.eval('tk::PlaceWindow . center')
      root.mainloop()

      series_dct = {}

      for i in range(0,series_num):

            series_dct[i] = []

            root = Tk()
            Label(root, text = ("Enter the starting and ending poses for Section %s" % str(i+1))).grid(row = 0, sticky= N)
            Label(root, text = "Start").grid(row = 1, sticky = W)
            Label(root, text = "End").grid(row = 2, sticky = W)
            st=Entry(root)
            en=Entry(root)
            st.grid(row = 1, column = 0)
            en.grid(row = 2, column = 0)
            Button(root, text = "Submit", command=lambda *args: getStartEnd()).grid(row = 5, column = 0)
            root.eval('tk::PlaceWindow . center')
            root.mainloop()

            for p in range(start, end+1):
                series_dct[i].append(p)

      root = Tk()
      Label(root, text = "Enter your X, Y, and Z Offsets and press Submit").grid(row = 0, sticky= N)
      Label(root, text = "X Offset").grid(row = 1, sticky = W)
      Label(root, text = "Y Offset").grid(row = 2, sticky = W)
      Label(root, text = "Z Offset").grid(row = 3, sticky = W)
      x=Entry(root)
      y=Entry(root)
      z=Entry(root)
      x.grid(row = 1, column = 0)
      y.grid(row = 2, column = 0)
      z.grid(row = 3, column = 0)
      Button(root, text = "Submit", command=lambda *args: getXYZ()).grid(row = 5, column = 0)
      root.eval('tk::PlaceWindow . center')
      root.mainloop()

      root = Tk()
      f= Frame(root)
      label = Label(root, text = "Do you wish to fix pan and tilt?")
      Button(f, text = "Yes", command=lambda *args: pan_tilt_ask("y")).pack(side = LEFT, padx = 10, pady =10)
      Button(f, text = "No", command=lambda *args: pan_tilt_ask("n")).pack(side = RIGHT, padx = 10, pady = 10)
      label.pack(pady = 10)
      f.pack()
      root.eval('tk::PlaceWindow . center')
      root.mainloop()

      if edit_pan_tilt == "y":
        root = Tk()
        Label(root, text = "Enter your pan and tilt values and press Submit").grid(row = 0, sticky= N)
        Label(root, text = "Pan").grid(row = 1, sticky = W)
        Label(root, text = "Tilt").grid(row = 2, sticky = W)
        p=Entry(root)
        t=Entry(root)
        p.grid(row = 1, column = 0)
        t.grid(row = 2, column = 0)
        Button(root, text = "Submit", command=lambda *args: getPT()).grid(row = 5, column = 0)
        root.eval('tk::PlaceWindow . center')
        root.mainloop()

      for i in range((len(series_dct))):
        for j in range(len(series_dct[i])): 
          cams = len(path['imaging_path'][series_dct[i][j]])

          for k in range(0, cams):
            if path['imaging_path'][series_dct[i][j]][k][0]['device'] == cam_to_edit:
              new_x = float(path['imaging_path'][series_dct[i][j]][k][0]['args'][0][1]) + x_offset
              new_y = float(path['imaging_path'][series_dct[i][j]][k][0]['args'][1][1]) + y_offset
              new_z = float(path['imaging_path'][series_dct[i][j]][k][0]['args'][2][1]) + z_offset

              path['imaging_path'][series_dct[i][j]][k][0]['args'][0][1] = str(new_x)
              path['imaging_path'][series_dct[i][j]][k][0]['args'][1][1] = str(new_y)
              path['imaging_path'][series_dct[i][j]][k][0]['args'][2][1] = str(new_z)

              if edit_pan_tilt == "y":
                path['imaging_path'][series_dct[i][j]][k][0]['args'][3][1] = str(pan)
                path['imaging_path'][series_dct[i][j]][k][0]['args'][4][1] = str(tilt)    

  #editing all cameras          
  else:
    root = Tk()
    Label(root, text = "Enter your X, Y, and Z Offsets and press Submit").grid(row = 0, sticky= N)
    Label(root, text = "X Offset").grid(row = 1, sticky = W)
    Label(root, text = "Y Offset").grid(row = 2, sticky = W)
    Label(root, text = "Z Offset").grid(row = 3, sticky = W)
    x=Entry(root)
    y=Entry(root)
    z=Entry(root)
    x.grid(row = 1, column = 0)
    y.grid(row = 2, column = 0)
    z.grid(row = 3, column = 0)
    Button(root, text = "Submit", command=lambda *args: getXYZ()).grid(row = 5, column = 0)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

    root = Tk()
    f= Frame(root)
    label = Label(root, text = "Would you like to fix pan and tilt?")
    Button(f, text = "Yes", command=lambda *args: pan_tilt_ask("y")).pack(side = LEFT, padx = 10, pady =10)
    Button(f, text = "No", command=lambda *args: pan_tilt_ask("n")).pack(side = RIGHT, padx = 10, pady = 10)
    label.pack(pady = 10)
    f.pack()
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

    if edit_pan_tilt == "y":
      root = Tk()
      Label(root, text = "Enter your pan and tilt values and press Submit").grid(row = 0, sticky= N)
      Label(root, text = "Pan").grid(row = 1, sticky = W)
      Label(root, text = "Tilt").grid(row = 2, sticky = W)
      p=Entry(root)
      t=Entry(root)
      p.grid(row = 1, column = 0)
      t.grid(row = 2, column = 0)
      Button(root, text = "Submit", command=lambda *args: getPT()).grid(row = 5, column = 0)
      root.eval('tk::PlaceWindow . center')
      root.mainloop()
    
    for i in range(0,poses):

      cams = len(path['imaging_path'][i])

      for j in range(0, cams):
        new_x = float(path['imaging_path'][i][j][0]['args'][0][1]) + x_offset
        new_y = float(path['imaging_path'][i][j][0]['args'][1][1]) + y_offset
        new_z = float(path['imaging_path'][i][j][0]['args'][2][1]) + z_offset

        path['imaging_path'][i][j][0]['args'][0][1] = str(new_x)
        path['imaging_path'][i][j][0]['args'][1][1] = str(new_y)
        path['imaging_path'][i][j][0]['args'][2][1] = str(new_z)

        if edit_pan_tilt == "y":
          path['imaging_path'][i][j][0]['args'][3][1] = str(pan)
          path['imaging_path'][i][j][0]['args'][4][1] = str(tilt)

  #getting filename settings
  root = Tk()
  Label(root, text = "Enter 'NewFilename' or leave blank to generate automatically").grid(row = 0, sticky= N)
  Label(root, text = "Filename").grid(row = 1, sticky = W)
  file=Entry(root)
  file.grid(row = 1, column = 0)
  Button(root, text = "Submit and Save", command=lambda *args: getFilename()).grid(row = 2, column = 0)
  root.eval('tk::PlaceWindow . center')
  root.mainloop()

  #automatic file naming  
  if name == "":
      new_filename = filename[:len(filename)-6] + "_edited" + ".cproj"
      print(new_filename)

      with open(new_filename, 'w') as convert_file:
        convert_file.write(json.dumps(path))

  #setting user inputed filename
  else:
    
    new_filename = filename.rsplit("/", 1)[0] + "/" + name + ".cproj"
    with open(new_filename, 'w') as convert_file:
      convert_file.write(json.dumps(path))


#COMBINING PATHS
elif edit_or_combine_test == "b":

  root = Tk()
  root.attributes('-topmost',True)
  f=Frame(root)
  label = Label(root, text = "How many paths would you like to combine? All settings besides \n poses (proxies, profiles  etc.) will be taken from the first path chosen").pack(side = TOP, pady = 5)
  path_num = Entry(root)
  path_num.pack(pady = 5)
  Button(root, text = "Submit", command=lambda *args: getPaths()).pack(side = BOTTOM, pady = 5)
  root.eval('tk::PlaceWindow . center')
  root.mainloop()

  # number_of_paths = int(input("How many paths would you like to combine? All settings besides camera poses (proxies, device profiles, etc.) will be taken from the first path chosen\n"))
  paths = {}
  combined_path = {"imaging_path" : [] , "profile": {}, "proxies":{}}

  for i in range(number_of_paths):
    paths[i] = {}
   
    root = Tk()
    root.withdraw()
    filename = askopenfilename()
    root.destroy()

    while True:
      if filename.endswith('.cproj'):
        break
      else:
        root = Tk()
        root.attributes('-topmost',True)
        label = Label(text = "Sorry, that file is not a COPIS path, please choose another file").pack(side = TOP, pady = 10)
        Button(root, text = "Try again", command=Close).pack(side = BOTTOM, pady = 10)
        root.eval('tk::PlaceWindow . center')
        root.mainloop()

        root = Tk()
        root.withdraw()
        filename = askopenfilename()
        root.destroy()
        
    if i == 0:
      path1name = filename

    # reading the data from the file
    with open(filename) as f:
      path = f.read()

    # reconstructing the data as a dictionary
    path_i= json.loads(path)

    paths[i] = path_i

  combined_path['profile'] = paths[0]['profile']
  combined_path['proxies'] = paths[0]['proxies']

  #getting filename settings
  root = Tk()
  root.eval('tk::PlaceWindow . center')
  root.attributes('-topmost',True)
  Label(root, text = "Enter 'NewFilename' or leave blank to generate automatically").grid(row = 0, sticky= N)
  Label(root, text = "Filename").grid(row = 1, sticky = W)
  file=Entry(root)
  file.grid(row = 1, column = 0)
  Button(root, text = "Submit and Save", command=lambda *args: getFilename()).grid(row = 2, column = 0)
  root.mainloop()

  for i in range(len(paths)):
    for j in range(len(paths[i]['imaging_path'])):

      combined_path['imaging_path'].append(paths[i]['imaging_path'][j])

  if name == "":
    new_filename = path1name[:len(path1name)-6] + "_combined" + ".cproj"
    print(new_filename)

    with open(new_filename, 'w') as convert_file:
      convert_file.write(json.dumps(combined_path))

  else:
    new_filename = path1name.rsplit("/", 1)[0] + "/" + name + ".cproj"
    print(new_filename)
    with open(new_filename, 'w') as convert_file:
      convert_file.write(json.dumps(combined_path))
      print(new_filename)


else:
  
  root = Tk()
  root.withdraw()
  filename = askopenfilename()
  root.destroy()

  #Check valid .cproj file
  while True:
    if filename.endswith('.cproj'):
      break
    else:
      print("Sorry, that file is not a COPIS path, please choose another file\n")
      root = Tk()
      root.withdraw()
      filename = askopenfilename()
      root.destroy()

  # reading the data from the file
  with open(filename) as f:
    path_file = f.read()

  # reconstructing the data as a dictionary
  path = json.loads(path_file)

  #get the length of the imaging path (in pose sets)
  poses = (len(path['imaging_path']))

  inverted_path = {"imaging_path" : [] , "profile": {}, "proxies":{}}

  inverted_path['profile'] = path['profile']
  inverted_path['proxies'] = path['proxies']

  #getting filename settings
  root = Tk()
  Label(root, text = "Enter 'NewFilename' or leave blank to generate automatically").grid(row = 0, sticky= N)
  Label(root, text = "Filename").grid(row = 1, sticky = W)
  file=Entry(root)
  file.grid(row = 1, column = 0)
  Button(root, text = "Submit and Save", command=lambda *args: getFilename()).grid(row = 2, column = 0)
  root.eval('tk::PlaceWindow . center')
  root.mainloop()

  #inverting the path
  for i in range(0,poses): 
    cams = len(path['imaging_path'][i])
    for j in range(0,cams):

      inverted_path['imaging_path'].append(path['imaging_path'][i][j])

      if path['imaging_path'][i][j][0]['device'] == 0:
        path['imaging_path'][i][j][0]['device'] = 3
        path['imaging_path'][i][j][1][0]['device'] = 3

      elif path['imaging_path'][i][j][0]['device'] == 1:
        path['imaging_path'][i][j][0]['device'] = 4
        path['imaging_path'][i][j][1][0]['device'] = 4
      
      elif path['imaging_path'][i][j][0]['device'] == 2:
        path['imaging_path'][i][j][0]['device'] = 5
        path['imaging_path'][i][j][1][0]['device'] = 5
      
      elif path['imaging_path'][i][j][0]['device'] == 3:
        path['imaging_path'][i][j][0]['device'] = 0
        path['imaging_path'][i][j][1][0]['device'] = 0
      
      elif path['imaging_path'][i][j][0]['device'] == 4:
        path['imaging_path'][i][j][0]['device'] = 1 
        path['imaging_path'][i][j][1][0]['device'] = 1 
      
      else:
        path['imaging_path'][i][j][0]['device'] = 2 
        path['imaging_path'][i][j][1][0]['device'] = 2

      inverted_z = -1 * float(path['imaging_path'][i][j][0]['args'][2][1])
      path['imaging_path'][i][j][0]['args'][2][1] = str(inverted_z)

      inverted_path['imaging_path'].append(path['imaging_path'][i][j])

  #automatic file naming  
  if name == "":
      new_filename = filename[:len(filename)-6] + "_inverted" + ".cproj"
      print(new_filename)

      with open(new_filename, 'w') as convert_file:
        convert_file.write(json.dumps(inverted_path))

  #setting user inputed filename
  else:
    new_filename = filename.rsplit("/", 1)[0] + "/" + name + ".cproj"
    with open(new_filename, 'w') as convert_file:
      convert_file.write(json.dumps(inverted_path))