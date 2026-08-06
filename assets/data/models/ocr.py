import easyocr
import cv2
import os


class OCRReader:

    def __init__(self, languages=["en"]):
        """
        Initialize EasyOCR reader.

        Example:
        OCRReader(["en"])
        OCRReader(["en", "hi"])
        """
        self.reader = easyocr.Reader(languages)

    def image_to_text(self, image_path):
        """
        Extract text from an image.
        """

        if not os.path.exists(image_path):
            return {
                "success": False,
                "error": "Image file not found."
            }

        try:

            result = self.reader.readtext(image_path)

            extracted_text = ""

            for item in result:
                extracted_text += item[1] + "\n"

            return {
                "success": True,
                "text": extracted_text.strip()
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def image_with_boxes(self, image_path):

        image = cv2.imread(image_path)

        result = self.reader.readtext(image_path)

        for detection in result:

            bbox, text, confidence = detection

            top_left = tuple(map(int, bbox[0]))
            bottom_right = tuple(map(int, bbox[2]))

            cv2.rectangle(
                image,
                top_left,
                bottom_right,
                (0,255,0),
                2
            )

            cv2.putText(
                image,
                text,
                (top_left[0], top_left[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,0,0),
                2
            )

        output = "ocr_output.jpg"

        cv2.imwrite(output, image)

        return output


if __name__ == "__main__":

    ocr = OCRReader(["en"])

    path = input("Enter image path : ")

    result = ocr.image_to_text(path)

    if result["success"]:

        print("\nExtracted Text:\n")
        print(result["text"])

        image = ocr.image_with_boxes(path)

        print("\nSaved Output Image :", image)

    else:

        print(result["error"])