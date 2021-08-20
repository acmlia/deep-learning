import os
import settings
import logging


class Loader:
    """
    Image training and validation loader

    Source:
        - https://keras.io/examples/vision/oxford_pets_image_segmentation/
    """

    def __init__(self, directory):
        self.list_image = self.list_entries(directory)

    def list_entries(self, directory):
        """
        Image training and validation loader. List the entries
        
        :param directory: 
        :return input_img_paths: list
        """
        input_img_paths = sorted(
            [
                os.path.join(directory, fname)
                for fname in os.listdir(directory)
                if (fname.endswith(settings.GEOGRAPHIC_ACCEPT_EXTENSION)
                    or fname.endswith(settings.NON_GEOGRAPHIC_ACCEPT_EXTENSION))
                   and not fname.startswith(".")
            ]
        )

        logging.info(">>>> Number of samples: {}".format(len(input_img_paths)))
        return input_img_paths

    def get_list_images(self):
        """
        :return list_image: return the list of absolute path to the images
        """
        return self.list_image
