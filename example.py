from colorfulprint import ColorfulPrint


cfprint = ColorfulPrint(log_file_path="deneme.log")

cfprint.success(message="Success")
cfprint.info(message="info message")
cfprint.warn(message="success message")
cfprint.error(message="warning message")
cfprint.error(message="error message")
cfprint.custom(type="404", message="Denemeeee")
cfprint.custom(type="200", message="Denemeeee")