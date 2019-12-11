""" bardcode.py: This is the python module for functions relating to the barcode scanner

This python module is used to interface with the barcode scanner and to provide a class
interaction to get reading, parse task, determine next action, load job, etc.
"""

class BarcodeScanner: 

    def __init__(self): 
        """ Init function for barcode scanner """

        # Status - determines if scanner is ready or busy
        self.status = "Ready" 

        # Store Last Read Message
        self.last_read_scan = None

    def load_job(self):
        job_id = input()

        return job_id


if __name__ == "__main__":
    barcode_scanner = BarcodeScanner()

    job = barcode_scanner.load_job()
