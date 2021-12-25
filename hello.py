from flask import Flask, Blueprint
from flask import request as flaskreq, jsonify
import json
import requests

hello = Blueprint('hello', __name__)


def returnStr(cat):
    request = requests.get('https://intelli-mall.herokuapp.com/product')
    request.raise_for_status()
    jsonResponse=request.json()
    jsonStr=''
    for k in range(len(cat)):
        idArr=[]
        titleArr=[]
        descriptionArr=[]
        imageUrlArr=[]
        priceArr=[]
        numOfOrdersArr=[]
        lastUpdatedArr=[]
        str = cat[k]
        for i in range(len(jsonResponse)):
            if(jsonResponse[i]['category'].strip() == str):
                idArr.append(jsonResponse[i]['id'])
                titleArr.append(jsonResponse[i]['title'])
                descriptionArr.append(jsonResponse[i]['description'])
                imageUrlArr.append(jsonResponse[i]['image_url'])
                priceArr.append(jsonResponse[i]['price'])
                lastUpdatedArr.append(jsonResponse[i]['last_updated_at'])
                numOfOrdersArr.append(jsonResponse[i]['count'])

        sortedNumOfOrdersIndexArr=sorted(range(len(numOfOrdersArr)), key=lambda k: numOfOrdersArr[k], reverse=True)
        sortedNumOfOrdersArr=sorted(numOfOrdersArr, reverse=True)
        
        for i in range(len(sortedNumOfOrdersArr)):
            if i<len(sortedNumOfOrdersArr)-1 or k<len(cat)-1:
                data = {}
                data['id'] = idArr[sortedNumOfOrdersIndexArr[i]]
                #data['title'] = titleArr[sortedNumOfOrdersIndexArr[i]]
                #data['description'] = descriptionArr[sortedNumOfOrdersIndexArr[i]]
                #data['image_url'] = imageUrlArr[sortedNumOfOrdersIndexArr[i]]
                #data['price'] = priceArr[sortedNumOfOrdersIndexArr[i]]
                #data['category'] = str
                data['last_updated_at'] = lastUpdatedArr[sortedNumOfOrdersIndexArr[i]]
                #data['count'] = numOfOrdersArr[sortedNumOfOrdersIndexArr[i]]
                jsonStr +=json.dumps(data)+","
            else:
                data = {}
                data['id'] = idArr[sortedNumOfOrdersIndexArr[i]]
                #data['title'] = titleArr[sortedNumOfOrdersIndexArr[i]]
                #data['description'] = descriptionArr[sortedNumOfOrdersIndexArr[i]]
                #data['image_url'] = imageUrlArr[sortedNumOfOrdersIndexArr[i]]
                #data['price'] = priceArr[sortedNumOfOrdersIndexArr[i]]
                #data['category'] = str
                data['last_updated_at'] = lastUpdatedArr[sortedNumOfOrdersIndexArr[i]]
                #data['count'] = numOfOrdersArr[sortedNumOfOrdersIndexArr[i]]
                jsonStr +=json.dumps(data)

    return jsonStr


@hello.route('/recomendation', methods=['GET', 'POST'])
def hello_world():
    cat = flaskreq.args.getlist('category')
    print(cat)
    #for i in cat[0][0]:
        #print(i)
    '''
    response = app.response_class(
        #response='['+returnStr(cat)+']',
        response=returnStr(cat),
        status=200,
        mimetype='application/json'
    )
    '''
    print('ahmed')
    return 'ahmed'
    
    #return ''

if __name__ == '__main__':
   app = Flask(__name__)
app.register_blueprint(hello, url_prefix = '/')

app.run()