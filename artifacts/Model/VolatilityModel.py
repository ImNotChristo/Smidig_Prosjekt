import subprocess
import os

class VolatilityModel:
    def __init__(self):
        self.command = ""
        self.file_path = ""

    def set_command(self, command):
        self.command = command

    def set_file_path(self, file_path):
        self.file_path = file_path

    def execute_volatility_command(self):
        if not self.file_path or not self.command:
            return "File path or command not specified."

        script_dir = os.path.dirname(os.path.abspath(__file__))
        vol_path = os.path.join(script_dir, '..', '..', 'volatility3', 'vol.py')
        
        vol_command = ['python', vol_path, '-f', self.file_path]

        if self.command in ['windows.dumpfiles', 'windows.memmap', 'windows.handles', 'windows.dlllist']:
            pid = self.ask_for_pid()
            if not pid:
                return "PID not provided."
            if self.command == 'windows.dumpfiles':
                output_dir = self.ask_for_output_dir()
                if not output_dir:
                    return "Output directory not provided."
                vol_command.extend(['-o', output_dir, self.command, '--pid', pid])
            elif self.command == 'windows.memmap':
                output_dir = self.ask_for_output_dir()
                if not output_dir:
                    return "Output directory not provided."
                vol_command.extend(['-o', output_dir, self.command, '--dump', '--pid', pid])
            else:
                vol_command.extend([self.command, '--pid', pid])
        elif self.command == 'windows.vadyarascan':
            yara_rules = self.ask_for_yara_rules()
            if not yara_rules:
                return "YARA rules not provided."
            vol_command.extend([self.command, '--yara-rules', yara_rules])
        else:
            vol_command.append(self.command)
        
        try:
            result = subprocess.run(vol_command, capture_output=True, text=True)
            return result.stdout + "\n" + result.stderr
        except Exception as e:
            return f"Error running Volatility command: {e}"

    def ask_for_pid(self):
        return "1234"

    def ask_for_output_dir(self):
        return "/path/to/dir"

    def ask_for_yara_rules(self):
        return "rules"
