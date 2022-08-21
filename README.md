# -kriyadocsSaasAcademy-Codeathon2022

## PDF validator 
 
##*Problem statement:*
 
An application that takes a pdf (generated from an application) as input and certifies if the pdf is valid. To certify that the pdf is valid, it should satisfy the rules given below. 
Rule 1: Font Style The font style of the PDF should be one among the following: 
● ClassGarmond
● Frutiger LT Pro 
● Frutiger LT Std 
● Symbol 
● Times New Roman
● Arial 
If there is a font style in any page of the PDF that doesn’t fall in the above list, mark it as an error 
Rule 2: Minimum lines The minimum number of lines on any page of the PDF is 5. If the PDF has any page with less than 5 lines, mark it as an error 
Rule 3: Missing header or footer Every PDF that we generate has a header and footer, If the input PDF does not have a header or a footer, mark it as an error 
Rule 4: Blank page If the PDF has a blank page, with just the header and footer and with no content in the text area (the area between the header and footer), mark it as an error 
Rule 5: Short column Every page of the PDF will have two columns. The margin of each column should be 8.504 pt on all sides. Check if any page of the PDF has a short column (ie., if the bottom margin is greater than 8.504 ± 0.5). 
Rule 6: Text exceeds margin Check if the content in the text area exceeds the margin on the left or right. 
Rule 7: Missing Entity Certain fonts don't support a few entities. For example, ⅀ may not be present in a few fonts. In case there is a missing entity, it will be displayed as shown below. Check if the PDF has any missing entities
 Output In case the PDF fails one or more of the above rules, mark it as an error. You can either annotate the error in the PDF or return it as a JSON as shown below 
Eg: { Missing_Entity: { Page: 2 Line : 4 } Short_column: { Page: 4 } } 
You can change the structure of JSON if needed. User Interface You can create a simple UI where you can upload a PDF 
 
My solution: 
 
Rule1:
         
Using the [Fitz](https://pymupdf.readthedocs.io/en/latest/module.html) python module, the font style of each line is extracted and stored in a list data type. Further, the list is compared with the valid font style list and the output is returned as True or False
 
Rule2:
         
Using the [borb](https://github.com/jorisschellekens/borb-examples) python module, the pdf document is read by each page and each line is counted. After counting using the if statement the condition is checked, ie whether the no.of lines is greater than 5 is True or False.
 
OUTPUT:
           
The output is written using the JSON module and it is fetched into the result webpage.


##Acknowledgements

-[Flask module](https://pypi.org/project/Flask/)

-[Real-python](https://realpython.com/)

-[borb](https://github.com/jorisschellekens/borb-examples)

-[Fitz](https://pymupdf.readthedocs.io/en/latest/module.html)


