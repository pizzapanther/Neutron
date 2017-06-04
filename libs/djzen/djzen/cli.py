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
    fh.write('# End djzen\n\n')
    
def write_requirements (directory):
  from pip._vendor import pkg_resources
  from pip._vendor.packaging.utils import canonicalize_name
  
  requirements = os.path.join(directory, 'requirements.txt')
  lines = []
  
  for p in pkg_resources.working_set:
    pname = canonicalize_name(p.project_name)
    write = False
    if pname.lower() in ['djzen', 'uwsgi', 'whitenoise']:
      write = True
      
    elif pname.lower().startswith('django'):
      write = True
      
    if write:
      lines.append('{}=={}'.format(pname, p.version))
      
  if lines:
    lines.sort()
    with open(requirements, 'a') as fh:
      fh.write('\n# Added by djzen\n')
      for line in lines:
        fh.write(line + '\n')
        
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
    
  args.append('--template')
  basedir = os.path.dirname(os.path.abspath(__file__))
  args.append(os.path.join(basedir, 'project_template'))
  args.extend(['-n', '.env'])
  
  management.execute_from_command_line(args)
  
  if not directory:
    directory = os.path.join(os.getcwd(), name)
    
  if os.path.exists(directory):
    if click.confirm('Setup .gitignore?', default=True):
      write_ignore(directory)
      
    if click.confirm('Setup requirements.txt?', default=True):
      write_requirements(directory)
      
if __name__ == '__main__':
  zen_commands()
  