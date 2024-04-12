from aima.logic import *
from aima.utils import *
import json 

# Define input data
data = {
    'features' : '4_sides, parallel_sides, equal_sides'
}

# Function to convert features data into first-order logic statements
def convertToKBFeatures(data):
    result = []
    shapes = ['Carre', 'Triangle', 'Hexagone', 'Cercle', 'Pentagone', 'Quadrant', 'Rectangle']
    features = data["features"].split(", ")
    for shape in shapes:
        for feature in features:
            if feature == "no_sides":
                result.append('NbCotes(Cercle, Zero)')
            elif feature == "3_sides":
                result.append('NbCotes(Triangle, Three)')
            elif feature == "4_sides":
                result.append('NbCotes(Quadrant, Four)')
            elif feature == "5_sides":
                result.append('NbCotes(Pentagone, Five)')
            elif feature == "6_sides":
                result.append('NbCotes(Hexagone, Six)')
            elif feature == "symmetry":
                result.append('Feature(Symmetry)')
            elif feature == "parallel_sides":
                result.append('Feature(ParallelSides)')
            #elif feature == "perpendicular_sides":
            #    result.append('Feature(PerpendicularSides)')
            elif feature == "diagonals":
                if "Rectangle" in shape:
                    result.append('Feature(NbCotes(TwoDiag, Two))')
                if "Carre" in shape:
                    result.append('Feature(NbCotes(TwoDiag, Two))')
                elif "Pentagone" in shape:
                    result.append('Feature(NbCotes(Pentagone, Five))')
                elif "Hexagone" in shape:
                    result.append('Feature(NbCotes(Hexagone, Nine))')
            elif feature == "curved_side":
                result.append('Feature(CurvedSide)')
            elif feature == "equal_sides":
                result.append('Feature(EqualSides)')
            elif feature == "acute_angle":
                result.append('Feature(TypesOfAngles(Acute))')
            elif feature == "right_angle":
                result.append('Feature(TypesOfAngles(Right))')
            elif feature == "obtuse_angle":
                result.append('Feature(TypesOfAngles(Obtuse))')
    return result


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

    KB.tell(expr('NbAngles(Carre, Four)'))
    KB.tell(expr('NbAngles(Triangle, Three)'))
    KB.tell(expr('NbAngles(Cercle, Zero)'))
    KB.tell(expr('NbAngles(Rectangle, Four)'))
    KB.tell(expr('NbAngles(Pentagone, Five)'))
    KB.tell(expr('NbAngles(Hexagone, Six)'))

    
    KB.tell(expr('NbDiagonales(Twodiag,Two)'))
    KB.tell(expr('NbDiagonales(Pentagone,Five)'))
    KB.tell(expr('NbDiagonales(Hexagone,Nine)'))

    KB.tell(expr('Feature(Symmetry)'))
    
    KB.tell(expr('Feature(ParallelSides)'))
    
    KB.tell(expr('Feature(PerpendicularSides)'))

    KB.tell(expr('Feature(CurvedSide)'))

    KB.tell(expr('Feature(EqualSides)'))

    KB.tell(expr('Feature(Convex)'))

    KB.tell(expr('Feature(TypesOfAngles(Acute)'))
    KB.tell(expr('Feature(TypesOfAngles(Right)'))
    KB.tell(expr('Feature(TypesOfAngles(Obtuse)'))

    '''
    #add parameter into the knowledge base
    for param in params:
        KB.tell(expr(param))

    #Rule-Based System:

    KB.tell(expr('Feature(TypesOfAngles(Right)) & Feature(ParallelSides) ==> Feature(PerpendicularSides)'))

    KB.tell(expr('NbCotes(x, Three) ==> IsTriangle(x)'))

    KB.tell(expr('IsTriangle(x) & Feature(AcuteAngle) ==> IsTriangleAigu(x)'))
    KB.tell(expr('IsTriangle(x) & Feature(RightAngle) ==> IsTriangleRect(x)'))
    KB.tell(expr('IsTriangle(x) & Feature(ObtuseAngle) ==> IsTriangleObtus(x)'))

    KB.tell(expr('NbCotes(x, Five) ==> IsPentagone(x)'))
    # KB.tell(expr('NbAngles(x, Five) ==> IsPentagone(x)'))

    KB.tell(expr('NbCotes(x, Six) ==> IsHexagone(x)'))
    KB.tell(expr('NbDiagonales(x,Nine) ==> IsHexagone(x)'))
    KB.tell(expr('Feature(ParallelSides) & NbCotes(x, Six) ==> IsHexagone(x)'))
    # KB.tell(expr('NbAngles(x, Six) ==> IsHexagone(x)'))

    KB.tell(expr('NbCotes(x, Zero) ==> IsCercle(x)'))
    KB.tell(expr('Feature(CurvedSide) ==> IsCercle(x)'))
    # KB.tell(expr('NbAngles(x, Zero) ==> IsCercle(x)'))

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

print(forwardChainQuery(convertToKBFeatures(data)))