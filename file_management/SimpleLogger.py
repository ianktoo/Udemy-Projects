import os
from datetime import datetime
from zoneinfo import ZoneInfo

class SimpleLogger(object):
    """
    Description:
        Simple logger class.

    Examples:
        >>> sl = SimpleLogger()
        >>> sl.log("INFO", "This is a message")
        >>> sl.debug("The code is not working here.")

        >>> sl2 = SimpleLogger(level="DEBUG", log_file="log-files/collect.log")
        >>> sl2.debug("The code is not working here. Working to resolve it!")

    """

    def __init__(self, log_file="app.log", level="INFO"):
        """
        Description: Constructor
        :param log_file: Optional log file name
        :param level: optional logging level. Default is INFO
        """
        self.log_file = log_file # save the log file defined
        self.level = level.upper() # make the level upper case.
        self.levels = [
            "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
        ]

        os.makedirs(os.path.dirname(log_file), exist_ok=True) if os.path.dirname(log_file) else False

    def _should_log(self, level):
        return self.levels.index(level) >= self.levels.index(self.level)

    def _format_message(self, level, message):
        # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        local_time = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d %H:%M:%S %Z")
        return "[%s]:\t[%s]:\t\'%s\'\n" % (local_time, level, message)

    def log(self, level, message):
        level = level.upper()

        if level not in self.levels:
            raise Exception("Invalid log level: %s" % level)

        if self._should_log(level):
            with open(self.log_file, "a", encoding="utf-8") as log:
                log.write(self._format_message(level, message))

    def debug(self, message):
        self.log("DEBUG", message)

    def info(self, message):
        self.log("INFO", message)

    def warning(self, message):
        self.log("WARNING", message)

    def error(self, message):
        self.log("ERROR", message)

    def critical(self, message):
        self.log("CRITICAL", message)