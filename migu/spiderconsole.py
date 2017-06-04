#-*- coding:utf-8 -*-
"""
This is a video spider

Usage:
    spiderconsole.py  [-i start programa]
    spiderconsole.py  [-h get help]
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys,colorful
import cmd
from video import search,mgvideo
from docopt import docopt, DocoptExit
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = colorful.green('Welcome come to my world!')+colorful.red("Now,Let's start")+'\n'+'''
       fa              fafafa              fafafa
     fa  fa          fa                  fa
    fafafafa        fa                  fa    fafa
   fa      fa        fa                  fa     fa
  fa        fa         fafafa              fafafaf
'''+'\n'+colorful.green('''you could use
-help (get help)
-quit  (exit program)
-search  (migu video search)
-mgvideo (migu video channel)
''')
    prompt = colorful.red('bf>')
    file = None

    @docopt_cmd
    def do_mgvideo(self, arg):
        """Usage: mgvideo"""
        video_channel=mgvideo.Miguvideo()
        video_channel.run()

    @docopt_cmd
    def do_search(self,arg):
        """Usage: search

Options:
    --search=<n>
        """
        new=search.migu_go()
        new.run()
    @docopt_cmd
    def do_serial(self, arg):
        """Usage: serial <port> [--baud=<n>] [--timeout=<seconds>]

Options:
    --baud=<n>  Baudrate [default: 9600]
        """

        print(arg)
    @docopt_cmd
    def do_wait(self,arg):
        """Usage: wait <port> [--baud=<n>] [--timeout=<seconds>]

Options:
    --baud=<n>  Baudrate [default: 9600]
        """
        print(arg)
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
