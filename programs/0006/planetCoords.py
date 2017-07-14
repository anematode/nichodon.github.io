import telnetlib,sys,time

import os
os.system('cls' if os.name == 'nt' else 'clear')

print "Logging into horizons.jpl.nasa.gov:6775..."
try:
    horizons = telnetlib.Telnet("horizons.jpl.nasa.gov",6775)
except:
    print "An unknown error occurred while connecting."
    sys.exit(-1)

print "Provide updates? (Y if yes, N if no)"
updates = raw_input("> ")

updates = (updates.upper() == "Y")

horizons.read_until('Horizons> ')

objs = ["Mercury","Venus","Earth","Moon","Mars","Jupiter"]
objids = [199, 299, 399, 301, 499, 599]

isfirstrun = True

currenttime = time.strftime("%Y-%B-%d %H:%M")
if updates:
    print "\nCurrent Ephemeris Time: " + currenttime + ".\n"

command = "var bodyPositions = {"

for i,obj in enumerate(objs):
    if updates:
        print "Collecting data for " + obj + "..."
    
    horizons.write(str(objids[i])+'\n')
    
    horizons.read_until('<cr>: ')
    horizons.write('E\n')
    
    horizons.read_until(' : ')
    horizons.write('v\n')
    
    horizons.read_until(' : ')
    horizons.write('@sun\n' if isfirstrun else 'y\n')
    
    horizons.read_until(' : ')
    horizons.write('eclip\n')
    
    horizons.read_until(' : ')
    horizons.write(currenttime + '\n')
    
    horizons.read_until(' : ')
    horizons.write('\n')
    
    horizons.read_until(' : ')
    horizons.write('14d\n')
    
    horizons.read_until(' : ')
    horizons.write('y\n')
    
    horizons.read_until('$$SOE')
    contents = horizons.read_until('$$EOE')
    
    horizons.read_until('[R]edisplay, ? : ')
    horizons.write('N\n')
    horizons.read_until('Horizons> ')
    
    coords = [(k+" " if k != '' else '') for k in (contents.split('\n')[2]
                                                           .replace('Y',"")
                                                           .replace('X',"")
                                                           .replace('Z',"")
                                                           .replace('=',""))
                      .split(' ')]
    newcoords = []
    
    for coord in coords:
        if (coord != ''):
            newcoords.append(str(float(coord.replace(' ','').replace('\r','')) * 100))

    newcoords[1],newcoords[2] = newcoords[2],newcoords[1]

    if updates:
        print "Collected data for " + obj + ". (%s%% done)\n" \
              % (round(100 * i/float(len(objs)),3))

    command = command + obj + ":[" + ','.join(newcoords) + '],'
    
    isfirstrun = False

horizons.close()

command = command[:-1] + "};"

print "Completed query of " + str(len(objs)) + " bodies! Paste the following into the JS:\n\n"

print command

print "\n"
sys.exit(0)
