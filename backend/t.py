def convert_to_kb_features(data):
    result = []
    shapes = ['Carre', 'Triangle', 'Hexagone', 'Cercle', 'Pentagone', 'Quadrant', 'Rectangle']
    
    for item in data:
        key = item['key']
        answer = item['answer']
        
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
                result.append('Feature(Symmetric)')
                
    return result

# Example usage:
