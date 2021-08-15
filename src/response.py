"""
## This module's purpose is to handle botApi responses
"""
import json


class BotAPIResponse:
    """
    Parses the right object for the response
    """

    def __init__(self, raw_json, expected_object=None):
        """Creates a BotAPIResponse object and sets variables for errors

        This object can handle errors and is passed as second variable by functions
        - - - - -
        **Args**:

        - `raw_json` (string): JSON string of the response
        - `expected_object` (any type, optional): Can be any expected result by botApi like types.Message or bool, to generate the object. Defaults to None.
        """
        self.raw = raw_json
        """JSON String given by APIs"""
        self.decoded = json.loads(raw_json)
        """JSON dictionary decoded with `json.loads`"""
        self.ok = self.decoded["ok"]
        """`True` if the request was executed with success, `False` if not"""
        self.error_code = None
        """Error code given by botAPI, if there is no error it is set to `None`"""
        self.description = None
        """Error description given by botAPI, if there is no error it is set to `None`"""
        self.connection_error = None
        """bool, True if there was a connection error, False if not"""
        if (not self.decoded["ok"]) and "result" in self.decoded:
            if "error_code" in self.decoded:
                self.error_code = self.decoded["error_code"]
            if "description" in self.decoded:
                self.description = self.decoded["description"]
            if "connection_error" in self.decoded:
                self.connection_error = self.decoded["connection_error"]
            else:
                self.connection_error = False
        else:
            self.expected_object = expected_object

    def getObject(self):
        """Get the best object for the response

        **Returns:**

        - `None`: if there was an error
        - Object specified in the init: if the request was a success
        """
        if "result" in self.decoded and (
                self.expected_object is None or self.expected_object.__module__ != "silbot.types" or (
                type(self.decoded["result"]) != dict and type(self.decoded["result"]) != list)):
            return self.decoded["result"]
        if self.decoded["ok"]:
            return self.expected_object(self.decoded["result"])
        else:
            return None

    def setObject(self, func):
        """Parse the response as a given object, returns None if there is an error

        **Args**:

        - `func` (class): A Class from `silbot.types` to encode the result

        **Returns**:

        - The specified `silbot.types` object in `func`
        """
        if "result" in self.decoded:
            return func(self.decoded["result"])
        else:
            return None
