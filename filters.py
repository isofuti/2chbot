
class Filters():

    def string_preparation(ogstr: str):
        
        newstr = ''

        for char in ogstr.lower():
            
            if char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz':
                newstr = newstr + char

        return newstr

    def findbanned(text):

        falsewords = [
            'избиений', 'унижений', 'избиения', 'унижения', 'nofap', 
            'нофап', 'пофапать', 'фапаю', 'рулетка', 'пустите', 'dark',
            'где', 'накидайте', 'доставьте', 'хочу', 'тг', 'телеграм',
            'телеграмм', 'telegram', 'телег'
        ]

        for word in falsewords:

            if word in text:

                return True

        return False

    def findcategory(model, vectorizer, text):

        category = model.predict(vectorizer.transform([str(text)]))[0]

        return str(category)