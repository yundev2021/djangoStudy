import os
import sys

class ManagementUtility:
    def __init__(self, argv=None):
        #sys.argv[:] 이렇게 해야 리스트를 복사해서 쓴다. 아니면 원본 sys.argv를 수정해 버린다.
        self.argv = argv or sys.argv[:] 
        self.prog_name = os.path.basename(self.argv[0])
        print(self.prog_name)
        if self.prog_name == '__main__.py': #/django/__main__.py 에서도 호출한다.
            self.prog_name = 'python -m django'
        self.settings_exception = None
        
    def execute(self):
        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = 'help'
            
            

def execute_from_command_line(argv=None):
    utility = ManagementUtility(argv)
    utility.execute()
