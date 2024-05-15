# To run this software:
# 1: open a terminal in a second window
# 2: open safari full screen in a macbook main monitor window
# 3: navigate to https://neuralink.com/webgrid/
# 4: in the terminal window run the following commands or type '. ./start.sh':

source pyvenv/bin/activate
python -c 'import main; main.playWebgrid()'
source deactivate