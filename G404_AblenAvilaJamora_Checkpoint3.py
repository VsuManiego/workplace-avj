#Checkpoint no. 3
#Ablen,Avila,Jamora

#So this is our 90% of our project. This Checklists help be more efficient, and save time. 
#This in turn allows us to focus on more creative activities. It helps us be more specific of what equipment to be used of what type of Hazard may occur in your Workplace.
#To complete this project, our goal is to store the csv file which helps you to identify the meaning and uses of each specific gears equipment.

from tkinter import *
from tkinter.ttk import Combobox

window=Tk()
window.geometry('500x400')

#creating a list
hazard = [
    "Safety Hazard",
    "Biological Hazard",
    "Chemical Hazard",
    "Physical Hazard",
    "Ergonomic Hazard"]
    
#creating classifications of hazard
biological = [
    "Head Protection", 
    "Eye Protection", 
    "Foot Protection", 
    "Hand Protection",
    "Respiratory Protection",
    "Protective Clothing"]
chemical = [
    "Head Protection", 
    "Eye Protection", 
    "Foot Protection", 
    "Hand Protection",
    "Respiratory Protection",
    "Protective Clothing"]
physical = [
    "Ear Protection",
    "Head Protection", 
    "Eye Protection", 
    "Foot Protection", 
    "Hand Protection",
    "Respiratory Protection",
    "Protective Clothing"]
ergonomic = [ 
    "Foot Protection", 
    "Hand Protection",
    "Protective Clothing",]
safety = [
    "Head Protection", 
    "Eye Protection", 
    "Foot Protection",
    "Ear Protection",
    "Hand Protection",
    "Respiratory Protection",
    "Protective Clothing"]

#create the dropbox
l0=Label(window,text='Choose What type of Hazard is Present in your Workplace?')
l0.pack()
my_combo = Combobox(window, value=hazard)
my_combo.current(0)
my_combo.pack(pady=10)

def pick_hazard(e):
        if my_combo.get() == "Biological Hazard":
            hazard_combo.config(value=biological)
            hazard_combo.current(0)
        if my_combo.get() == "Chemical Hazard":
            hazard_combo.config(value=chemical)
            hazard_combo.current(0)
        if my_combo.get() == "Physical Hazard":
            hazard_combo.config(value=physical)
            hazard_combo.current(0)  
        if my_combo.get() == "Safety Hazard":
            hazard_combo.config(value=safety)
            hazard_combo.current(0)
        if my_combo.get() == "Ergonomic Hazard":
            hazard_combo.config(value=ergonomic)
            hazard_combo.current(0)
my_combo.bind("<<ComboboxSelected>>", pick_hazard)
l1=Label(window,text='Personal Protective Equipment Selection will be:')
l1.pack()
hazard_combo = Combobox(window, values=[" "])
hazard_combo.current(0)
hazard_combo.pack(pady=10)

#create a listbox
l2=Label(window,text='Continue Clicking Here to Choose: The Personal Protective Equipment for Specific Gears')
l2.pack()
frame = Frame(window)
frame.pack(pady=10,)

#craeting a list
ppeselection = [
    "Ear Protection",
    "Head Protection",
    "Eye Protection",
    "Foot Protection",
    "Hand Protection",
    "Protective Clothing",
    "Respiratory Protection"]
Ear_Protection = [
    "Ear Muffs",
    "Ear Plugs",
	"Canal Caps"]
Head_Protection = [
    "Hard Hats",
	"Bump caps",
	"Flame resistant Balaclava",
    "Welder's Helmet"]
Eye_Protection = [
	"Goggles",
	"Safety Glasses",
	"Laser eyewear"]
Foot_Protection = [
	"Safety Shoes",
	"Slip resistant shoes",
	"Foot/Shin guards"]
Hand_Protection = [
	"Leather gloves",
	"Cut-resistant gloves",
	"Electric safety gloves"]
Protective_Clothing = [
	"Coveralls",
	"Leather clothing",
	"Safety visibility vest",
	"Flame Resistant Aprons",]
Respiratory_Protection = [
	"Dust Mask",
	"Power air- purifying respirator/PAPR",
	"Cartridge respirator",
	"Self-contained breathing apparatus/SCBA",]
    
def list_ppe(e):
    my_list2.delete(0, END)
    if my_list1.get(ANCHOR) == "Ear Protection":
        for item in Ear_Protection:
            my_list2.insert(END, item)
    if my_list1.get(ANCHOR) == "Head Protection":
        for item in Head_Protection:
            my_list2.insert(END, item)
    if my_list1.get(ANCHOR) == "Eye Protection":
        for item in Eye_Protection:
            my_list2.insert(END, item)
    if my_list1.get(ANCHOR) == "Hand Protection":
        for item in Hand_Protection:
            my_list2.insert(END, item)
    if my_list1.get(ANCHOR) == "Foot Protection":
        for item in Foot_Protection:
            my_list2.insert(END, item)
    if my_list1.get(ANCHOR) == "Protective Clothing":
        for item in Protective_Clothing:
            my_list2.insert(END, item)
    if my_list1.get(ANCHOR) == "Respiratory Protection":
        for item in Respiratory_Protection:
            my_list2.insert(END, item)   

my_list1 = Listbox(frame)
my_list1.grid(row=0, column=0)          
my_list2 = Listbox(frame)
my_list2.grid(row=0, column=1, padx=20, ipadx=50)

for item in ppeselection:
    my_list1.insert(END, item)
my_list1.bind("<<ListboxSelect>>", list_ppe)    
    






window.mainloop()
