from datetime import datetime

class ColorfulPrint(object):
    _DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    # Background is suffix B_ Foreground suffix is F_ 
    FONT_BOLD = "\x1b[1m"
    F_WHITE = "\x1b[97m"
    
    B_ERROR = "\x1b[41m"
    B_SUCCESS = "\x1b[42m"
    B_WARNING = "\x1b[43m"
    B_INFO = "\x1b[44m"
    B_DEFAULT = "\x1b[49m"
    

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
    def print(cls, *, type:str, message: str):
        dt = datetime.now().strftime(cls._DATE_FORMAT)
        space_after_datetime = ' ' * 4
        style_default = f"{cls.F_WHITE}{cls.B_DEFAULT}{cls.FONT_BOLD}"
        if type == "SUCCESS":
            space = ' ' * 2
            style = f"{cls.B_SUCCESS}{cls.F_WHITE}{cls.FONT_BOLD}"
        elif type == "ERROR":
            space = ' ' * 4
            style = f"{cls.B_ERROR}{cls.F_WHITE}{cls.FONT_BOLD}"
        elif type == "WARNING":
            space = ' ' * 2
            style = f"{cls.B_WARNING}{cls.F_WHITE}{cls.FONT_BOLD}"
        elif type == "INFO":
            space = ' ' * 5
            style = f"{cls.B_INFO}{cls.F_WHITE}{cls.FONT_BOLD}"

        result = "{style}[{type}]{style_default}{space}{dt}{space_after_dt}{message}".format(
                style=style,
                type=type,
                style_default=style_default,
                space=space,
                dt=dt,
                space_after_dt=space_after_datetime,
                message=message)

        print(result)



