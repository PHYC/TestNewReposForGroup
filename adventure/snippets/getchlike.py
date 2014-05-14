# this is an example for making a Getch-like
# functionality with native python modules
# note that try/finally must be used to preserve
# terminal state on exit
#
# taken from recipe at:
# http://code.activestate.com/recipes/134892/
#
# for x-platform, incorporate msvcrt.getch() try/catch

import sys, tty, termios
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
try:
  tty.setcbreak(sys.stdin)
  command=''
  diff=len(command)
  running = True
  while running:
      command+=sys.stdin.read(1)
      if diff != len(command):
        diff = len(command)
        sys.stdout.write(command[-1])
      if command[-1] == '\n':
        if command.split()[0] == 'quit':
          running = False
        command='';diff=0
finally:
  termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
