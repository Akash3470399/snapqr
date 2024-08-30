from abc import ABC, abstractmethod

class Detector(ABC):
    
    @abstractmethod
    def inputImage(self, image):
        """
            Accept the image if image is in valid format (image have qr code in it)
            input parameters:
                image : image pixcels (numpy) matrix 
            output:
                True/False determining the input was valid or not.
        """
        pass
    
    @abstractmethod
    def process(self):
        """
            Procees the image for qr code detection & produce the extracted data.

            process include:
                extract the data from the qr code 
                
            output:
                returns the extracted data in bytes array formate

        """
        pass