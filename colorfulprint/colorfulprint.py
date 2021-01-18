import dotenv
from datetime import datetime
from pathlib import Path
class ColorfulPrint(object):
    _DEFAULT_CONFIG_PATH = Path("colorfulprint/cfprint.env")
    _DATE_FORMAT = "%Y-%m-%d %H:%M:%S-%f"

    # Background is suffix B_ Foreground suffix is F_ 
    FONT_BOLD = "\x1b[1m"
    F_WHITE = "\x1b[97m"

    B_ERROR = "\x1b[41m"
    B_SUCCESS = "\x1b[42m"
    B_WARNING = "\x1b[43m"
    B_INFO = "\x1b[44m"
    B_DEFAULT = "\x1b[49m"
    B_CUSTOM = "\x1b[45m"
    
    def __init__(self, *, log_file_path: bool = None):
        self._config = dotenv.dotenv_values(self._DEFAULT_CONFIG_PATH)
        self._log_file_path = log_file_path
    

    def success(self, message: str):
        type = "SUCCESS"
        result = self._generate_result(type=type, message=message)
        print(result)
    
    def error(self, message: str):
        type = "ERROR"
        result = self._generate_result(type=type, message=message)
        print(result)

    def warn(self, message: str):
        type = "WARNING"
        result = self._generate_result(type=type, message=message)
        print(result)

    def info(self, message: str):
        type = "INFO"
        result = self._generate_result(type=type, message=message)
        print(result)

    def custom(self, type: str, message: str):
        result = self._generate_result(type=type, message=message)
        print(result)

    
    def _generate_result(self, *, type: str, message: str):
        dt = datetime.now().strftime(self._DATE_FORMAT)
        
        default_space = ' ' * 10
        style_default = f"{self.F_WHITE}{self.B_DEFAULT}{self.FONT_BOLD}"
        if type == "SUCCESS":
            style = f"{self.B_SUCCESS}{self.F_WHITE}{self.FONT_BOLD}"
        elif type == "ERROR":
            style = f"{self.B_ERROR}{self.F_WHITE}{self.FONT_BOLD}"
        elif type == "WARNING":
            style = f"{self.B_WARNING}{self.F_WHITE}{self.FONT_BOLD}"
        elif type == "INFO":
            style = f"{self.B_INFO}{self.F_WHITE}{self.FONT_BOLD}"
        elif type.startswith("4"):
            style = f"{self.B_ERROR}{self.F_WHITE}{self.FONT_BOLD}"
        elif type.startswith("2"):
            style = f"{self.B_SUCCESS}{self.F_WHITE}{self.FONT_BOLD}"
        else:
            type = f"${type[:12]}..."
            style = f"{self.B_CUSTOM}{self.F_WHITE}{self.FONT_BOLD}"
        
        space = ' ' * (20 - len(type))
        
        result = "{style}[{type}]{style_default}{space}{dt}{space_default}{message}".format(
                style=style,
                type=type,
                style_default=style_default,
                space=space,
                dt=dt,
                space_default=default_space,
                message=message)

        log_result = "[{type}]{space}{dt}{space_default}{message}".format(
                type=type,
                space=space,
                dt=dt,
                space_default=default_space,
                message=message)
        
        if self._log_file_path:
            with open(self._log_file_path, mode="a") as file:
                file.write(log_result)
                file.write("\n")
        
        return result



cfprint = ColorfulPrint()