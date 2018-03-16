#!/bin/bash

# Remove previous message queues
#ipcrm --all=msg

#make

#echo "Starting packet_sender process"
#gnome-terminal -x bash -c "./packet_sender 3; echo \"Press any key to close terminal\";read -n1"

#echo "Starting packet_receiver process"
#gnome-terminal -x bash -c "./packet_receiver 3; echo \"Press any key to close terminal\";read -n1"

#make clean

#sh -c 'cd PART_A && exec pwd && exec python Kruskal.py'
cd PART_A
echo ""
echo "''''''Running Kruskal.py''''''"
echo ""
echo ""
gnome-terminal -x bash -c "python Kruskal.py; echo \"Press any key to close terminal\";read -n1"

echo ""
echo ""
echo "''''''Running Prim.py''''''''"
echo ""
echo ""
gnome-terminal -x bash -c "python Prim.py; echo \"Press any key to close terminal\";read -n1"


cd ..

cd PART_B
echo ""
echo "''''''Running Floydw.py''''''"
echo ""
echo ""
gnome-terminal -x bash -c "python Floydw.py; echo \"Press any key to close terminal\";read -n1"

echo ""

cd ..

cd PART_C
echo ""
echo "''''''BCon.py''''''"
echo ""
echo ""
gnome-terminal -x bash -c "python BCon.py; echo \"Press any key to close terminal\";read -n1"

echo ""
