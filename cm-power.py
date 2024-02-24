#!/usr/bin/python3

import hostlist
import sys
import argparse
import getopt

#Add menu items here

def mainMenu():

    print('''
================================
<NAME> CLUSTER MANAGER
================================
1 - Power on nodes
2 - Power off nodes
3 - Illuminate server UID
4 - List nodes
5 - XXX
6 - Exit
================================
''')

def helpMenu():

    print('''
Usage: cm-power.py [NODES]

NODES in hostname format as follows:

node1,node2,node9,node10; or
node[1-2,9-10]

''')
    sys.exit()

def pwrOn(nodeList = [], *args):
    print("\nPowering on nodes\n")
    sys.exit()

def pwrOff(nodeList = [], *args):
    listNodes(nodeList)
    print("**************************************************")
    print("WARNING: ABOUT TO POWER OFF THE NODES LISTED ABOVE")
    print("**************************************************")
    print(userConfirm())
    #do ilo redfish stuff here
    sys.exit()

def uidOn(nodeList = [], *args):
    print("\nIlluminating UIDs\n")
    sys.exit()

def listNodes(nodeList = [], *args):
    print("\n*********")
    print("Node List")
    print("*********")
    for i in nodeList:
        print(i)
    print("\n")

def reserved(*_):
    print("No functionality here")
    sys.exit()

def cmClose(*_):
    print("Exiting...")
    sys.exit()

def userConfirm():
    check = str(input("Are you sure you want to proceed? (y/n): ")).lower().strip()
    if check == 'y' or check == 'yes':
        return True
    elif check == 'n' or check == 'no':
        return False
    else:
        print('Invalid Input')
        return userConfirm()

def menu():

    nodes = hostlist.expand_hostlist(sys.argv[1])
    mainMenu()
    userChoice = 0
    while userChoice != 6:
        #Add menu items to dictionary "menuOpt", menu number then function name
        userChoice = input("Select a number: ")
        menuOpt = { '1': pwrOn,  '2': pwrOff, '3': uidOn, '4': listNodes, '5': reserved, '6': cmClose }
        if userChoice in menuOpt:
            cmFunct = menuOpt.get(userChoice)
            cmFunct(nodes)
        else:
            print("That is not a vaild option, try again")
            userChoice = 0
            continue
        mainMenu()

if len(sys.argv) != 2:
    helpMenu()

menu()
