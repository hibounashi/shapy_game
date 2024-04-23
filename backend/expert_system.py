from aima.logic import *
from aima.utils import *
import json 

# Define input data
data = [{'key': 'sides', 'answer': '0'}, {'key': 'angles', 'answer': '0'}, {'key': 'diagonals', 'answer': 'Oui'}, {'key': 'obtuseAngle', 'answer': 'Oui'}, {'key': 'acuteAngle', 'answer': 'Oui'}, {'key': 'rightAngle', 'answer': 'Oui'}, {'key': 'perpendicularSides', 'answer': 'Oui'}, {'key': 'parallelSides', 'answer': 'Oui'}, {'key': 'equalSides', 'answer': 'Oui'}, {'key': 'symmetric', 'answer': 'Oui'}]


# Function to convert features data into first-order logic statements
def convertToKBFeatures(data):
    result = []

    for item in data:
        key = item['key']
        answer = item['answer']
        print(key,answer)
        if key == "sides":
            if answer == "0":
                result.append('NbCotes(Cercle, Zero)')
            elif answer == "3":
                result.append('NbCotes(Triangle, Three)')
            elif answer == "4":
                result.append('NbCotes(Quadrant, Four)')
            elif answer == "5":
                result.append('NbCotes(Pentagone, Five)')
            elif answer == "6":
                result.append('NbCotes(Hexagone, Six)')
        elif key == "angles":
            if answer == "0":
                result.append('NbAngles(Cercle, Zero)')
            elif answer == "3":
                result.append('NbAngles(Triangle, Three)')
            elif answer == "4":
                result.append('NbAngles(Quadrant, Four)')
            elif answer == "5":
                result.append('NbAngles(Pentagone, Five)')
            elif answer == "6":
                result.append('NbAngles(Hexagone, Six)')
        elif key == "diagonals":
            if answer == "Oui":
                result.append('Feature(NbDiagonals)')
        elif key == "obtuseAngle":
            if answer == "Oui":
                result.append('Feature(ObtuseAngle)')
        elif key == "acuteAngle":
            if answer == "Oui":
                result.append('Feature(AcuteAngle)')
        elif key == "rightAngle":
            if answer == "Oui":
                result.append('Feature(RightAngle)')
        elif key == "perpendicularSides":
            if answer == "Oui":
                result.append('Feature(PerpendicularSides)')
        elif key == "parallelSides":
            if answer == "Oui":
                result.append('Feature(ParallelSides)')
        elif key == "equalSides":
            if answer == "Oui":
                result.append('Feature(EqualSides)')
        elif key == "symmetric":
            if answer == "Oui":
                result.append('Feature(Symmetry)')

    return result

def extractShapeNames(data):
    shapes_data = data['shapes']  # Extract the 'shapes' field from the data dictionary
    shape_names = shapes_data.split(', ')  # Split the string by comma and space
    return shape_names

# Function to perform forward chaining inference with given parameters
def forwardChainQuery(params ):
    KB = FolKB()
    #Database of Facts:
    '''
    #number of sides
    KB.tell(expr('NbCotes(Cercle, Zero)'))
    KB.tell(expr('NbCotes(Triangle, Three)'))
    KB.tell(expr('NbCotes(Carre, Four)'))
    KB.tell(expr('NbCotes(Rectangle, Four)'))
    KB.tell(expr('NbCotes(Pentagone, Five)'))
    KB.tell(expr('NbCotes(Hexagone, Six)'))
    #the number of Angles 
    KB.tell(expr('NbAngles(Carre, Four)'))
    KB.tell(expr('NbAngles(Triangle, Three)'))
    KB.tell(expr('NbAngles(Cercle, Zero)'))
    KB.tell(expr('NbAngles(Rectangle, Four)'))
    KB.tell(expr('NbAngles(Pentagone, Five)'))
    KB.tell(expr('NbAngles(Hexagone, Six)'))
    #Diagonals
    KB.tell(expr('NbDiagonales(Twodiag,Two)'))
    KB.tell(expr('NbDiagonales(Pentagone,Five)'))
    KB.tell(expr('NbDiagonales(Hexagone,Nine)'))
    #Other features
    KB.tell(expr('Feature(Symmetry)'))
    KB.tell(expr('Feature(ParallelSides)'))
    KB.tell(expr('Feature(PerpendicularSides)'))
    KB.tell(expr('Feature(CurvedSide)'))
    KB.tell(expr('Feature(EqualSides)'))
    KB.tell(expr('Feature(Convex)'))
    #Angles types
    KB.tell(expr('TypesOfAngles(Acute)'))
    KB.tell(expr('TypesOfAngles(Right)'))
    KB.tell(expr('TypesOfAngles(Obtuse)'))

    '''
    #add parameter into the knowledge base
    for param in params:
        KB.tell(expr(param))

    #Rule-Based System:
    KB.tell(expr('Feature(TypesOfAngles(Right)) & Feature(ParallelSides) ==> Feature(PerpendicularSides)'))
    KB.tell(expr('NbCotes(x, Three) ==> IsTriangle(x)'))
    KB.tell(expr('IsTriangle(x) & Feature(AcuteAngle) ==> IsTriangleAigu(AcuteAngle)'))
    KB.tell(expr('IsTriangle(x) & Feature(RightAngle) ==> IsTriangleRect(RightAngle)'))
    KB.tell(expr('IsTriangle(x) & Feature(ObtuseAngle) ==> IsTriangleObtus(ObtuseAngle)'))
    KB.tell(expr('NbCotes(x, Five) ==> IsPentagone(Pentagone)'))
    #KB.tell(expr('NbCotes(x, Six) ==> IsHexagone(x)'))
    #KB.tell(expr('NbDiagonales(x,Nine) ==> IsHexagone(x)'))
    KB.tell(expr('Feature(ParallelSides) & NbCotes(x, Six) ==> IsHexagone(x)'))
    KB.tell(expr('NbCotes(x, Zero) ==> IsCercle(x)'))
    #KB.tell(expr('Feature(CurvedSide) ==> IsCercle(x)'))
    KB.tell(expr('NbCotes(Quadrant, Four) ==> IsQuadrant(Quadrant)'))
    KB.tell(expr('IsQuadrant(x) & Feature(ParallelSides) & Feature(EqualSides) ==> IsCarre(Carre)'))
    KB.tell(expr('IsQuadrant(x) & Feature(PerpendicularSides) & Feature(EqualSides) ==> IsCarre(Carre)'))
    KB.tell(expr('IsQuadrant(x) & Feature(ParallelSides) & Feature(Symmetry)==> IsRectangle(Rectangle)'))
    KB.tell(expr('IsQuadrant(x) & Feature(PerpendicularSides) & Feature(Symmetry)==> IsRectangle(Rectangle)'))

    # ask using the enterd KB 
    queries = ['IsCercle(x)', 'IsTriangle(x)', 'IsQuadrant(x)', 'IsCarre(x)', 'IsRectangle(x)', 'IsHexagone(x)']
    results = []
    for query in queries:
        results.append(list(fol_fc_ask(KB, expr(query))))
    
    list_res = results # Output: [ [ {x:Cercle} ], [ {x:Triangle} ], [ {x:Quadrant} ]
    shapes = []
    for item in list_res:
        if item != []:
            shapes.append(str(item[0][x]))

    # Output: ['Quadrant,Carre']

    my_dict = {'shapes': None}
    shapes_str = ', '.join(shapes)

    # Assign the concatenated string to the 'shapes' key in the dictionary
    my_dict['shapes'] = shapes_str

    return my_dict

#print(extractShapeNames(forwardChainQuery(convertToKBFeatures(data))))