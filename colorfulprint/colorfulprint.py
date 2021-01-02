from datetime import datetime

class ColorfulPrint(object):
    _DATE_FORMAT = "%Y-%m-%d %H:%M:%S-%f"

    # Background is suffix B_ Foreground suffix is F_ 
    FONT_BOLD = "\x1b[1m"
    F_WHITE = "\x1b[97m"
    F_BLACK = "\x1b[30m"
    B_ERROR = "\x1b[41m"
    B_SUCCESS = "\x1b[42m"
    B_WARNING = "\x1b[43m"
    B_INFO = "\x1b[44m"
    B_DEFAULT = "\x1b[49m"
    B_CUSTOM = "\x1b[45m"
    
    
    def __init__(self):
        self.dt = datetime.now()

    @staticmethod
    def _generate_result(type: str, message: str):
        result = "{style}[{type}]{style_end}{space}{dt}{space_after_dt}{message}".format(
                style=style(),
                type=type,
                style_end=style_end(),
                space=space,
                dt=dt,
                space_after_dt=space_after_dt,
                message=message)
        return result

    @classmethod
    def success(cls, message: str):
        type = "SUCCESS"
        result = cls._generate_result(type=type, message=message)
        print(result)
    
    @classmethod
    def error(cls, message: str):
        type = "ERROR"
        result = cls._generate_result(type=type, message=message)
        print(result)

    @classmethod
    def warn(cls, message: str):
        type = "WARNING"
        result = cls._generate_result(type=type, message=message)
        print(result)

    @classmethod
    def info(cls, message: str):
        type = "INFO"
        result = cls._generate_result(type=type, message=message)
        print(result)

    
    @classmethod
    def custom(cls, type: str, message: str):
        result = cls._generate_result(type=type, message=message)
        print(result)

    @classmethod
    def _generate_result(cls, *, type:str, message: str):
        dt = datetime.now().strftime(cls._DATE_FORMAT)
        
        space_after_datetime = ' ' * 4
        style_default = f"{cls.F_WHITE}{cls.B_DEFAULT}{cls.FONT_BOLD}"
        if type == "SUCCESS":
            style = f"{cls.B_SUCCESS}{cls.F_WHITE}{cls.FONT_BOLD}"
        elif type == "ERROR":
            style = f"{cls.B_ERROR}{cls.F_WHITE}{cls.FONT_BOLD}"
        elif type == "WARNING":
            style = f"{cls.B_WARNING}{cls.F_BLACK}{cls.FONT_BOLD}"
        elif type == "INFO":
            style = f"{cls.B_INFO}{cls.F_WHITE}{cls.FONT_BOLD}"
        elif type.startswith("4"):
            style = f"{cls.B_ERROR}{cls.F_WHITE}{cls.FONT_BOLD}"
        elif type.startswith("2"):
            style = f"{cls.B_SUCCESS}{cls.F_WHITE}{cls.FONT_BOLD}"
        else:
            type = f"${type[:12]}..."
            style = f"{cls.B_CUSTOM}{cls.F_WHITE}{cls.FONT_BOLD}"
        
        space = ' ' * (20 - len(type))
        result = "{style}[{type}]{style_default}{space}{dt}{space_after_dt}{message}".format(
                style=style,
                type=type,
                style_default=style_default,
                space=space,
                dt=dt,
                space_after_dt=space_after_datetime,
                message=message)
        return result



