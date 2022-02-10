# Below is a dictionary that shows the details of leaders that govern country ABC
# From 2000 to 2020
Leaders_ABC = {
    "id":["0011A","020Z","222F","876F"],
    "FirstName":["Gavin","Aminat","Adeleke","Bigjara"],
    "LastName":["Goved","Mustapha","Bright","Bonenus"],
    "Age":["56","44","67","35"],
    "Hobbies":[["singing","comedy","rap"],["Swiming","Cyclin"],["coding","cooking","Sleeping"],["Teaching","Talking","Coding","Singin"]],
    "Spouse":["Shade","Mustapha","JiriJiri","Finejara"],
    "Reign":[[2000,2001,2002,2003,2004,2005],[2005,2006,2007,2008,2009,2010],[2011,2012,2013,2014,2015],[2015,2016,2017,2018,2019,2020]]
}
#who was elected leader in 2005
#use a condition
#print(Leaders_ABC["Reign"][0][0])
if (Leaders_ABC["Reign"][0][0]) == 2005:
     print(Leaders_ABC["FirstName"][0]+ " " + Leaders_ABC["LastName"][0]," Was the elected leader year 2005")
elif(Leaders_ABC["Reign"][1][0]) == 2005:
    print(Leaders_ABC["FirstName"][1]+ " " + Leaders_ABC["LastName"][1]," Was the elected leader year 2005")
elif(Leaders_ABC["Reign"][2][0]):
     print(Leaders_ABC["FirstName"][2]+ " "+Leaders_ABC["LastName"][2]," Was the elected leader year 2005")
elif(Leaders_ABC["Reign"][3][0]):
     print(Leaders_ABC["FirstName"][3]+ " "+Leaders_ABC["LastName"][3]," Was the elected leader year 2005")
print()
#find the leaders with the highest hobbies
hobbies_1_no = (len(Leaders_ABC["Hobbies"][0]))
hobbies_2_no = (len(Leaders_ABC["Hobbies"][1]))
hobbies_3_no = (len(Leaders_ABC["Hobbies"][2]))
hobbies_4_no = (len(Leaders_ABC["Hobbies"][3]))
maximum_hob = max(hobbies_1_no,hobbies_2_no,hobbies_3_no,hobbies_4_no)
if (maximum_hob == hobbies_1_no):
    print("Gavin Goved has the highest hobby: singing, comedy and rap]")
elif(maximum_hob == hobbies_2_no):
     print("Aminat Mustapha has the highest hobby: Swiming and Cycling.")
elif(maximum_hob == hobbies_3_no):
     print("Adeleke Bright has the highest hobby: coding, cooking and Sleeping")
elif(maximum_hob == hobbies_4_no):
     print("Bigjara Bonenus has the highest hobby: Teaching, Talking, Coding and Singing")
print()
#To change the last name of Bigjara
print()
print(Leaders_ABC)
Leaders_ABC["LastName"][3] = "AIC"
print()
print(Leaders_ABC)
print()
# listing the hobbies of leaders of year 2011 to 2020
print(Leaders_ABC["Hobbies"][2] + Leaders_ABC["Hobbies"][2])

