import os
import shutil
import sys

import click
from django.core import management

def write_ignore (directory):
  gitignore = os.path.join(directory, '.gitignore')
  
  with open(gitignore, 'a') as fh:
    fh.write('\n# Added by djzen\n')
    fh.write('.env\n')
    fh.write('db.sqlite3\n')
    fh.write('static-compiled\n')
    fh.write('# End djzen\n\n')
    
@click.group()
def zen_commands ():
  pass

@zen_commands.command()
@click.argument('name')
@click.argument('directory', required=False)
def startproject (name, directory):
  """
  Creates a Django project directory structure for the given project name in
  the current directory or optionally in the given directory.
  """
  
  
  exe = shutil.which('django-admin.py')
  if exe is None:
    print("Could not find django-admin.py. Is Django installed?")
    sys.exit(1)
    
  args = [exe, 'startproject', name]
  if directory:
    args.append(directory)
    
  else:
    while 1:
      print('Install to:')
      print('  [1] Current directory (recommended)')
      print('  [2] {}'.format(name))
      ans = click.prompt('Directory?', default='1')
      if ans == '1':
        directory = os.getcwd()
        args.append(directory)
        break
        
      elif ans == '2':
        directory = name
        break
        
  args.append('--template')
  basedir = os.path.dirname(os.path.abspath(__file__))
  tpl = os.path.join(basedir, 'project_template')
  args.append(tpl)
  args.extend(['-n', '.env'])
  
  management.execute_from_command_line(args)
  
  if os.path.exists(directory):
    if click.confirm('Setup .gitignore?', default=True):
      write_ignore(directory)
      
if __name__ == '__main__':
  zen_commands()
  